/* Quick sort algorithm to sort strings */
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "xil_printf.h"
#include "qsort.h"

/* Swaps position of strings in array (char**) */
void swap(const char **a, const char **b) {
	const char *temp = *a;
	*a = *b;
	*b = temp;
}

void quicksort(char const * arr[], unsigned int length) {
	unsigned int i, piv = 0;
	if (length <= 1)
		return;
	xil_printf("");
	for (i = 0; i < length; i++) {
		// if curr str < pivot str, move curr into lower array and  lower++(pvt)
		if (strcmp(arr[i], arr[length -1]) < 0) 	//use string in last index as pivot
			swap(arr + i, arr + piv++);
	}
	//move pivot to "middle"
	swap(arr + piv, arr + length - 1);

	//recursively sort upper and lower
	quicksort(arr, piv++);			//set length to current pvt and increase for next call
	quicksort(arr + piv, length - piv);
}

void generate_random_string(char *str, int length) {
    const char charset[] = "abcdefghijklmnopqrstuvwxyz";
    for (int i = 0; i < length; i++) {
        int key = rand() % (sizeof(charset) - 1);
        str[i] = charset[key];
    }
    str[length] = '\0'; // Null-terminate the string
}

int qsort_wrap(int golden) {
	int count = 10;

	char* pointer_input = (char*)0x40000420;
	char* input[count];

	if(golden > 0){
		if (golden == 1){
			unsigned int ck_counter;
			//reading counter in pmcounter
			asm volatile ("MRC p15, 0, %0, C9, C13, 0" :"=r"(ck_counter));
			srand(ck_counter);
			xil_printf("input_seed: %d\n", ck_counter);
		}else{
			//xil_printf("input_seed: %d\n", golden);
			srand(golden);
		}
		//generate input
		for (int i = 0; i < count; i++) {
			int length = 7; // Random length between 1 and MAX_STRING_LENGTH
			input[i] = (char *)malloc((length + 1) * sizeof(char)); // Allocate memory for the string
			if (input[i] == NULL) {
				fprintf(stderr, "Memory allocation failed\n");
				return -1;
			}
			generate_random_string(input[i], length);
		}
		//xil_printf("\nGolden input:\n");
		// Save the input in the fpga memory
		for (int i = 0; i<count; i++){
			for(int j = 0; j < 8; j++){
				pointer_input[i*8+j] = input[i][j];
			}
			//xil_printf("%s\n", input[i]);
		}

	}else{ //Take input from the fpga memory
		//xil_printf("\nRead golden input:\n");
		for (int i = 0; i<count; i++){
			input[i] = malloc(sizeof(char)*8);
			for(int j = 0; j < 8; j++){
				input[i][j] = pointer_input[i*8+j];
			}
			//xil_printf("%s\n", input[i]);
		}
	}
	//char const *arr[] = {"Kurt", "Vonneguts", "Commencement", "Address", "at", "MIT", "Ladies", "and", "gentlemen", "of", "the", "class", "of", "97", "Wear", "sunscreen", "If", "I", "could", "offer", "you", "only", "one", "tip", "for", "the", "future", "sunscreen", "would", "be", "it", "The", "longterm", "benefits", "of", "sunscreen", "have", "been", "proved", "by", "scientists", "whereas", "the", "rest", "of", "my", "advice", "has", "no", "basis"};
	//char const *sol[] = {"97", "Address", "Commencement", "I", "If", "Kurt", "Ladies", "MIT", "The", "Vonneguts", "Wear", "advice", "and", "at", "basis", "be", "been", "benefits", "by", "class", "could", "for", "future", "gentlemen", "has", "have", "it", "longterm", "my", "no", "of", "of", "of", "of", "offer", "one", "only", "proved", "rest", "scientists", "sunscreen", "sunscreen", "sunscreen", "the", "the", "the", "tip", "whereas", "would", "you"};
	quicksort(input, count);

	int corr = 1;
	int* pointer_gold = (int*)0x40000500;
	if(golden > 0){
		//xil_printf("\nWrite Golden output\n");
		for (int i = 0; i<count; i++){
			for(int j = 0; j < 8; j++){
				pointer_gold[i*8+j] = input[i][j];
			}
			//xil_printf("%s\n", input[i]);
		}
	}else{
		// Read gold
		//xil_printf("\nread Golden output\n");
		//input[0][0] = 15;
		char *gold[count];
		for (int i = 0; i<count; i++){
			gold[i] = malloc(sizeof(char)*8);
			for(int j = 0; j < 8; j++){
				gold[i][j] = pointer_gold[i*8+j];
			}
			//xil_printf("%s\n", gold[i]);
		}
 		int i = 0;
 		//xil_printf("\nfaulty:\n");
		for(i=0;i<count;i++){
		  if(strcmp(input[i], gold[i]) != 0){
			  corr = 0;
		  }
		  //xil_printf("%s\n", input[i]);
		}
		char* pointer = (char*)0x40000008;
		if(corr == 1){
		  pointer[0] = 1; //correct
		  //xil_printf("corr");
		}else{
		  pointer[0] = 0; //not correct
		  //xil_printf("not corr");
		}

	}
	return corr;

}
