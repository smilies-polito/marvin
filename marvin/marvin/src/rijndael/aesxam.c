
 /*
   -----------------------------------------------------------------------
   Copyright (c) 2001 Dr Brian Gladman <brg@gladman.uk.net>, Worcester, UK
   
   TERMS

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions
   are met:
   1. Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
   2. Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

   This software is provided 'as is' with no guarantees of correctness or
   fitness for purpose.
   -----------------------------------------------------------------------
 */

/* Example of the use of the AES (Rijndael) algorithm for file  */
/* encryption.  Note that this is an example application, it is */
/* not intended for real operational use.  The Command line is: */
/*                                                              */
/* aesxam input_file_name output_file_name [D|E] hexadecimalkey */
/*                                                              */
/* where E gives encryption and D decryption of the input file  */
/* into the output file using the given hexadecimal key string  */
/* The later is a hexadecimal sequence of 32, 48 or 64 digits   */
/* Examples to encrypt or decrypt aes.c into aes.enc are:       */
/*                                                              */
/* aesxam file.c file.enc E 0123456789abcdeffedcba9876543210    */
/*                                                              */
/* aesxam file.enc file2.c D 0123456789abcdeffedcba9876543210   */
/*                                                              */
/* which should return a file 'file2.c' identical to 'file.c'   */

#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <ctype.h>
#include "rijndeal.h"
#include "xil_printf.h"
#include "aes.h"

/* A Pseudo Random Number Generator (PRNG) used for the     */
/* Initialisation Vector. The PRNG is George Marsaglia's    */
/* Multiply-With-Carry (MWC) PRNG that concatenates two     */
/* 16-bit MWC generators:                                   */
/*     x(n)=36969 * x(n-1) + carry mod 2^16                 */ 
/*     y(n)=18000 * y(n-1) + carry mod 2^16                 */
/* to produce a combined PRNG with a period of about 2^60.  */  
/* The Pentium cycle counter is used to initialise it. This */
/* is crude but the IV does not need to be secret.          */
 
/* void cycles(unsigned long *rtn)     */
/* {                           // read the Pentium Time Stamp Counter */
/*     __asm */
/*     { */
/*     _emit   0x0f            // complete pending operations */
/*     _emit   0xa2 */
/*     _emit   0x0f            // read time stamp counter */
/*     _emit   0x31 */
/*     mov     ebx,rtn */
/*     mov     [ebx],eax */
/*     mov     [ebx+4],edx */
/*     _emit   0x0f            // complete pending operations */
/*     _emit   0xa2 */
/*     } */
/* } */

#define RAND(a,b) (((a = 36969 * (a & 65535) + (a >> 16)) << 16) + (b = 18000 * (b & 65535) + (b >> 16))  )

void fillrand(char *buf, int len)
{   static unsigned long a[2], mt = 1, count = 4;
    static char          r[4];
    int                  i;

    if(mt) { 
	 mt = 0; 
	 /*cycles(a);*/
      a[0]=0xeaf3;
	 a[1]=0x35fe;
    }

    for(i = 0; i < len; ++i)
    {
        if(count == 4)
        {
            *(unsigned long*)r = RAND(a[0], a[1]);
            count = 0;
        }

        buf[i] = r[count++];
    }
}    

int encfile(char *in, char *out, aes *ctx, char* fn)
{   char            inbuf[16], outbuf[16];
	unsigned long   i = 0, l = 0;
	size_t          flen = strlen(in);  /* Get the length of the input string */

	//fillrand(outbuf, 16);
	char* iv = "1234567890abcdef";		/* Set an IV for CBC mode */
	memcpy(out, iv, 16);            /* Write the IV to the output string */
	out += 16;                          /* Move the output pointer forward */

	fillrand(inbuf, 1);                 /* Make top 4 bits of a byte random */
	l = 15;                             /* And store the length of the last block in the lower 4 bits */
	inbuf[0] = (char)((flen & 15) | (inbuf[0] & ~15));

	while (i < flen)                    /* Loop to encrypt the input string */
	{
		size_t read_len = (flen - i) < l ? (flen - i) : l; /* Calculate how many bytes to read */
		memcpy(inbuf + 16 - l, in + i, read_len); /* On 1st round byte[0] is the length code */
		i += read_len;

		if (read_len < l) break;        /* If end of the input string reached */

		for (size_t j = 0; j < 16; ++j) /* XOR in previous cipher text */
			inbuf[j] ^= outbuf[j];

		encrypt(inbuf, outbuf, ctx);    /* And do the encryption */

		memcpy(out, outbuf, 16);        /* Write the encrypted block to the output string */
		out += 16;                      /* Move the output pointer forward */

		l = 16;                         /* Set up for next round to read 16 bytes */
	}

	if (l == 15)                        /* Adjust for extra byte in the first block */
		++i;

	if (i < flen)                       /* If bytes remain to be output */
	{
		while (i < 16)                  /* Clear empty buffer positions */
			inbuf[i++] = 0;

		for (size_t j = 0; j < 16; ++j) /* XOR in previous cipher text */
			inbuf[j] ^= outbuf[j];

		encrypt(inbuf, outbuf, ctx);    /* Encrypt and output it */

		memcpy(out, outbuf, 16);        /* Write the encrypted block to the output string */
	}

	return 0;
}


int rijndeal_wrap(int golden)
{
	char* in = "Standard input need to be decode";
	//xil_printf("in: %s\n", in);
	char* out = malloc(32);
	int err = 0;

    aes ctx[1];

    char* pointer_input = (char*)0x40000020;
    char* key = malloc(sizeof(char)*32);
    if(golden == 1){
    	unsigned int ck_counter;
		//reading counter in pmcounter
		asm volatile ("MRC p15, 0, %0, C9, C13, 0" :"=r"(ck_counter));
		srand(ck_counter);
		for(int i = 0; i < 32; i++){
			key[i] = rand() % 256;
			pointer_input[i] = key[i];
		}

    }else{
    	for(int i = 0; i < 32; i++){
			key[i] = pointer_input[i];
		}
    }
    //char* key = "44444Vx�����ܺ	�eC!4Vx�����ܺ	�eC+";
    //xil_printf("key: %s\n", key);
	set_key(key, 32, enc, ctx);

	err = encfile(in, out, ctx, NULL);
	//xil_printf("err: %d\n", err);

	//xil_printf("out: %s\n", out);
	int corr = 1;
	char* pointer_gold = (char*)0x40000100;
	if(golden){
		for(int i = 0; i < 32; i++){
			pointer_gold[i] = out[i];
		}
	}else{

		char* gold_output = malloc(sizeof(char)*32);
		for(int i = 0; i<32; i++ ){
			if(pointer_gold[i] != out[i]){
				corr = 0;
			}
		}

		//xil_printf("corr: %d\n", corr);
		char* pointer = (char*)0x40000008;
		if(corr){
			pointer[0] = 1; //correct
		}else{
			pointer[0] = 0;	//not correct
		}
	}

    return corr;
}
