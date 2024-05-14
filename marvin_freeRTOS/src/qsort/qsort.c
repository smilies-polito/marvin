/* Quick sort algorithm to sort strings */
#include <unistd.h>
#include <string.h>
#include <stdio.h>
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

void qsort_wrap(int argc, char** argv) {
	int count = 50;
	char const *arr[] = {"Kurt", "Vonneguts", "Commencement", "Address", "at", "MIT", "Ladies", "and", "gentlemen", "of", "the", "class", "of", "97", "Wear", "sunscreen", "If", "I", "could", "offer", "you", "only", "one", "tip", "for", "the", "future", "sunscreen", "would", "be", "it", "The", "longterm", "benefits", "of", "sunscreen", "have", "been", "proved", "by", "scientists", "whereas", "the", "rest", "of", "my", "advice", "has", "no", "basis"};

	char const *sol[] = {"97", "Address", "Commencement", "I", "If", "Kurt", "Ladies", "MIT", "The", "Vonneguts", "Wear", "advice", "and", "at", "basis", "be", "been", "benefits", "by", "class", "could", "for", "future", "gentlemen", "has", "have", "it", "longterm", "my", "no", "of", "of", "of", "of", "offer", "one", "only", "proved", "rest", "scientists", "sunscreen", "sunscreen", "sunscreen", "the", "the", "the", "tip", "whereas", "would", "you"};
	quicksort(arr, sizeof(arr) / sizeof(*arr));

	int i = 0;
	int corr = 1;
	for(i=0;i<count;i++){
	  if(strcmp(arr[i], sol[i]) != 0){
		  corr = 0;
	  }
	  //xil_printf("%s\n", array[i].qstring);
	}
	char* pointer = (char*)0x10100;
	if(corr == 1){
	  pointer[0] = 1; //correct
	  //xil_printf("corr");
	}else{
	  pointer[0] = 0; //not correct
	  //xil_printf("not corr");
	}

}
