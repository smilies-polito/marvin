#ifndef SHA_H
#define SHA_H

/* NIST Secure Hash Algorithm */
/* heavily modified from Peter C. Gutmann's implementation */

/* Useful defines & typedefs */

typedef unsigned char BYTE;


#define SHA_BLOCKSIZE		64
#define SHA_DIGESTSIZE		20

typedef struct {
    unsigned long digest[5];		/* message digest */
    unsigned long count_lo, count_hi;	/* 64-bit bit count */
    unsigned long data[16];		/* SHA data buffer */
} SHA_INFO;

int sha(int golden);

#endif /* SHA_H */
