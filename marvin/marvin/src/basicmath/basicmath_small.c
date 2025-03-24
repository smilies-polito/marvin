#include "snipmath.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "FreeRTOS.h"
/* The printf's may be removed to isolate just the math calculations */

int basicmath(int golden)
{
  double X;
  int x;
  struct int_sqrt q;

  int* pointer_input = (int*)0x40000020;
  double* pointer_input_double = (double*)0x40000020;
  if(golden == 1){
	  unsigned int ck_counter;
	  //reading counter in pmcounter
	  asm volatile ("MRC p15, 0, %0, C9, C13, 0" :"=r"(ck_counter));
	  srand(ck_counter);
	  x = rand()%1000;
	  pointer_input[0] = x;
	  X = ((double)rand() / RAND_MAX) * 360.0;
	  pointer_input_double[1] = X;
  }else{
	  x = pointer_input[0];
	  X = pointer_input_double[1];
  }
  //printf("The double is: %f\n", X);
  usqrt(x, &q);
  //xil_printf("\nsqrt(%3d) = %2d\n", x, q.sqrt);
  double rad = deg2rad(X);
  //printf("%f degrees = %f radians\n", X, rad);
  double deg = rad2deg(rad);
  //printf("%f radians = %f degrees\n", rad, deg);

  int* pointer_gold = (int*)0x40000100;
  double* pointer_gold_double = (double*) 0x40000100;
  int corr = 1;
  if(golden == 1){
	  pointer_gold[0] = q.sqrt;
	  pointer_gold_double[1] = deg;
  }else{
	  int gold_sqrt = pointer_gold[0];
	  double gold_deg = pointer_gold_double[1];

	  if (gold_sqrt != q.sqrt || gold_deg != deg){
		  corr = 0;
	  }
	  char* pointer = (char*)0x40000008;
	  if(corr){
		pointer[0] = 1; //correct
	  }else{
		pointer[0] = 0;	//not correct
	  }
  }

  return corr;
}
