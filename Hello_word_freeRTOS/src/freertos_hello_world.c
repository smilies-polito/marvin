/*
    Copyright (C) 2017 Amazon.com, Inc. or its affiliates.  All Rights Reserved.
    Copyright (c) 2012 - 2022 Xilinx, Inc. All Rights Reserved.
	SPDX-License-Identifier: MIT


    http://www.FreeRTOS.org
    http://aws.amazon.com/freertos


    1 tab == 4 spaces!
*/

/* FreeRTOS includes. */
#include "FreeRTOS.h"
#include "task.h"
#include "queue.h"
#include "timers.h"
/* Xilinx includes. */
#include "xil_printf.h"
#include "xparameters.h"
#include "ff_stdio.h"
#define TIMER_ID	1
#define DELAY_10_SECONDS	10000UL
#define DELAY_1_SECOND		1000UL
#define TIMER_CHECK_THRESHOLD	9
/*-----------------------------------------------------------*/

/* The Tx and Rx tasks as described at the top of this file. */
static void prvTxTask( void *pvParameters );
/*-----------------------------------------------------------*/

/* The queue used by the Tx and Rx tasks, as described at the top of this
file. */
static TaskHandle_t xTxTask;
char HWstring[15] = "Hello World";
long RxtaskCntr = 0;

#if (configSUPPORT_STATIC_ALLOCATION == 1)
#define QUEUE_BUFFER_SIZE		100

uint8_t ucQueueStorageArea[ QUEUE_BUFFER_SIZE ];
StackType_t xStack1[ configMINIMAL_STACK_SIZE ];
StackType_t xStack2[ configMINIMAL_STACK_SIZE ];
StaticTask_t xTxBuffer,xRxBuffer;
StaticTimer_t xTimerBuffer;
static StaticQueue_t xStaticQueue;
#endif



int main( void )
{
	xil_printf( "VSSTE (Very Stupid Single Task Example) from Freertos example main\r\n" );

#if ( configSUPPORT_STATIC_ALLOCATION == 0 ) /* Normal or standard use case */
	/* Create the two tasks.  The Tx task is given a lower priority than the
	Rx task, so the Rx task will leave the Blocked state and pre-empt the Tx
	task as soon as the Tx task places an item in the queue. */
	xTaskCreate( 	prvTxTask, 					/* The function that implements the task. */
					( const char * ) "Tx", 		/* Text name for the task, provided to assist debugging only. */
					configMINIMAL_STACK_SIZE, 	/* The stack allocated to the task. */
					NULL, 						/* The task parameter is not used, so set to NULL. */
					tskIDLE_PRIORITY + 1,		/* The task runs at the idle priority. */
					&xTxTask );




#endif


	/* Start the tasks and timer running. */
	vTaskStartScheduler();

	/* If all is well, the scheduler will now be running, and the following line
	will never be reached.  If the following line does execute, then there was
	insufficient FreeRTOS heap memory available for the idle and/or timer tasks
	to be created.  See the memory management section on the FreeRTOS web site
	for more details. */
	for( ;; );
}


static void confPMU(){
	int events[6] = {0x66, 0x67, 0x48, 0x5C, 0x23, 0x25};
	// Enable user-mode access to performance counters
	asm volatile ("MCR p15, 0, %0, C9, C14, 0\n\t" :: "r"(1));
	//Enable bit in pmcr
	asm volatile ("MCR p15, 0, %0, C9, C12, 0\n\t" :: "r"(0x41093009));
	// Enable all counters in pmcntenset
	asm volatile ("MCR p15, 0, %0, c9, c12, 1\t\n" :: "r"(0x8000003f));
	for(int i = 0; i < 6; i++){
		// select PC in pmselr (solo ultimi 4 bit = 8 counters)
		asm volatile ("MCR p15, 0, %0, c9, c12, 5\t\n" :: "r"(i));
		// select event to track in pmxevtyper
		asm volatile ("MCR p15, 0, %0, C9, C13, 1" :: "r"(events[i]));
	}
}

#include <stdio.h>

static void readPMU(){
	FILE_F *fp = f_open("res", "w");
	if(fp == NULL){
		printf("Error opening file.\n");
		return;
	}
	fprintf(fp, "\n");
	xil_printf("reading the PMU\n\n");
	unsigned int counter_value;
	unsigned int evn_type;
	for(int i = 0; i < 6; i++){
		//selecting counter in pmselr
		asm volatile ("MCR p15, 0, %0, C9, C12, 5" :: "r"(i));
		//reading event type in pmxevtyper
		asm volatile ("MRC p15, 0, %0, C9, C13, 1" :"=r"(evn_type));
		//reading counter in pmxevncntr
		asm volatile ("MRC p15, 0, %0, C9, C13, 2" :"=r"(counter_value));
		xil_printf("Event type: %d Counter: %d\n", evn_type, counter_value);
		//fprintf(fp, "Event type: %d Counter: %d\n", evn_type, counter_value);
	}

	//fclose(fp);
}

static void bubbleSort()
{
inizio:	xil_printf("Start bubble sort\n");
		int n = 5;
		int v[] = {4, 9, 6, 12, 3};
		int i,k;
		int temp;
		for(i = 0; i<n-1; i++) {
		 for(k = 0; k<n-1-i; k++) {
		         if(v[k] > v[k+1]) {
		          temp = v[k];
		          v[k] = v[k+1];
		          v[k+1] = temp;
		         }
		 }
		}
		/* Delay for 1 second. */
		//vTaskDelay( x1second );
		xil_printf("Result:\n");
		for(int i = 0; i < 5; i++){
			xil_printf(" %d", v[i]);
		}
fine:	xil_printf("Task finished\n");
}

/*-----------------------------------------------------------*/
static void prvTxTask( void *pvParameters )
{
	confPMU();
	bubbleSort();
	readPMU();
}

/*-----------------------------------------------------------*/


