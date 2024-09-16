#include "dijkstra.h"
#include <stdio.h>
#include "xil_printf.h"
#define NUM_NODES                          16
#define NONE                               9999
#define MAX_BUFFER_SIZE 1000

struct _NODE
{
  int iDist;
  int iPrev;
};
typedef struct _NODE NODE;

struct _QITEM
{
  int iNode;
  int iDist;
  int iPrev;
  struct _QITEM *qNext;
};
typedef struct _QITEM QITEM;

QITEM *qHead = NULL;




int AdjMatrix[NUM_NODES][NUM_NODES] = {
    {10, 28, 5, 11, 19, 14, 1, 26, 3, 7, 15, 13, 9, 21, 23, 22},
    {20, 17, 3, 7, 12, 29, 15, 8, 25, 30, 12, 17, 18, 5, 24, 11},
    {29, 19, 26, 12, 23, 13, 25, 1, 16, 5, 3, 29, 11, 28, 15, 18},
    {4, 13, 22, 2, 21, 4, 13, 1, 12, 8, 17, 4, 13, 19, 27, 13},
    {8, 10, 10, 8, 28, 19, 5, 7, 1, 14, 30, 5, 26, 17, 29, 1},
    {26, 6, 29, 20, 18, 21, 2, 3, 10, 10, 23, 13, 1, 3, 29, 13},
    {16, 28, 26, 19, 4, 30, 20, 6, 8, 12, 27, 22, 7, 20, 4, 1},
    {3, 25, 2, 27, 28, 30, 9, 15, 15, 13, 9, 28, 22, 20, 24, 10},
    {10, 17, 12, 1, 1, 28, 11, 21, 6, 28, 17, 20, 26, 27, 6, 28},
    {18, 1, 22, 21, 6, 19, 29, 7, 8, 12, 21, 5, 15, 10, 8, 1},
    {26, 2, 25, 15, 20, 25, 1, 30, 10, 17, 8, 21, 9, 2, 7, 5},
    {10, 19, 12, 19, 7, 28, 22, 11, 10, 1, 8, 8, 13, 19, 20, 9},
    {9, 29, 25, 3, 5, 3, 25, 20, 18, 12, 1, 18, 26, 18, 1, 2},
    {26, 7, 1, 14, 1, 15, 14, 21, 3, 11, 20, 30, 8, 19, 20, 19},
    {27, 10, 1, 14, 4, 29, 3, 6, 22, 9, 6, 28, 30, 20, 5, 15},
    {1, 7, 14, 1, 17, 10, 26, 19, 18, 2, 3, 2, 6, 27, 2, 15}
};

int g_qCount = 0;
NODE rgnNodes[NUM_NODES];
int ch;
int iPrev, iNode;
int i, iCost, iDist;


void print_path (NODE *rgnNodes, int chNode)
{
  if (rgnNodes[chNode].iPrev != NONE)
    {
      print_path(rgnNodes, rgnNodes[chNode].iPrev);
    }
  //xil_printf (" %d", chNode);
  fflush(stdout);
}

void print_path_str(NODE *rgnNodes, int chNode, char *pathBuffer) {
    if (rgnNodes[chNode].iPrev != NONE) {
        print_path_str(rgnNodes, rgnNodes[chNode].iPrev, pathBuffer);
    }

    char tempBuffer[MAX_BUFFER_SIZE];
    sprintf(tempBuffer, " %d", chNode);
    strcat(pathBuffer, tempBuffer);
}

void enqueue (int iNode, int iDist, int iPrev)
{
inizio: xil_printf("");
  QITEM *qNew = (QITEM *) malloc(sizeof(QITEM));
  QITEM *qLast = qHead;

  if (!qNew)
    {
      //fprintf(stderr, "Out of memory.\n");
      exit(1);
    }
  qNew->iNode = iNode;
  qNew->iDist = iDist;
  qNew->iPrev = iPrev;
  qNew->qNext = NULL;

  if (!qLast)
    {
      qHead = qNew;
    }
  else
    {
      while (qLast->qNext) qLast = qLast->qNext;
      qLast->qNext = qNew;
    }
  g_qCount++;
  //               ASSERT(g_qCount);
}


void dequeue (int *piNode, int *piDist, int *piPrev)
{
  QITEM *qKill = qHead;

  if (qHead)
    {
      //                 ASSERT(g_qCount);
      *piNode = qHead->iNode;
      *piDist = qHead->iDist;
      *piPrev = qHead->iPrev;
      qHead = qHead->qNext;
      free(qKill);
      g_qCount--;
    }
}


int qcount (void)
{
  return(g_qCount);
}

int dijkstra(int chStart, int chEnd, int golden)
{

	int corr = 1;

	for (ch = 0; ch < NUM_NODES; ch++)
    {
      rgnNodes[ch].iDist = NONE;
      rgnNodes[ch].iPrev = NONE;
    }

	if (chStart == chEnd)
    {
      //xil_printf("Shortest path is 0 in cost. Just stay where you are.\n");
    }
	else
    {
      rgnNodes[chStart].iDist = 0;
      rgnNodes[chStart].iPrev = NONE;

      enqueue (chStart, 0, NONE);

     while (qcount() > 0)
	{
	  dequeue (&iNode, &iDist, &iPrev);
	  for (i = 0; i < NUM_NODES; i++)
	    {
	      if ((iCost = AdjMatrix[iNode][i]) != NONE)
		{
		  if ((NONE == rgnNodes[i].iDist) ||
		      (rgnNodes[i].iDist > (iCost + iDist)))
		    {
		      rgnNodes[i].iDist = iDist + iCost;
		      rgnNodes[i].iPrev = iNode;
		      enqueue (i, iDist + iCost, iNode);
		    }
		}
	    }
	}
     fine:	xil_printf("");
     // Initialize the buffer to hold the path string
    char pathBuffer[MAX_BUFFER_SIZE];
    pathBuffer[0] = '\0'; // Ensure the buffer is empty initially
    print_path_str(rgnNodes, chEnd, pathBuffer);
    //xil_printf("Exe: %s\n", pathBuffer);
    int* pointer_gold = (int*)0x40000300;
    if(golden == 1){
    	int i = 0;
    	while(pathBuffer[i] != '\0'){
    		pointer_gold[i] = pathBuffer[i];
    		i++;
    	}
    	pointer_gold[i] = '\0';
    }else{
    	char golden_path[MAX_BUFFER_SIZE];
    	int i = 0;
		while(pointer_gold[i] != '\0'){
			golden_path[i] = pointer_gold[i];
			i++;
		}
		golden_path[i] = '\0';
		//xil_printf("gold: %s\n", golden_path);

		int result = strcmp(pathBuffer, golden_path);
		if(result != 0){
			corr = 0;
		}
		char* pointer = (char*)0x40000008;
		if(corr){
			pointer[0] = 1; //correct
		}else{
			pointer[0] = 0;	//not correct
		}
    }
    }
	return corr;
}

int dijkstra_wrap(int golden) {
	int init = 0;
	int fine = 0;

	char* pointer_input = (char*)0x40000220;
	if (golden == 1){
		unsigned int ck_counter;
		//reading counter in pmcounter
		asm volatile ("MRC p15, 0, %0, C9, C13, 0" :"=r"(ck_counter));
		srand(ck_counter);
		init = rand() % NUM_NODES;
		fine = rand() % NUM_NODES;
		pointer_input[0] = init;
		pointer_input[4] = fine;
	}else{
		init = pointer_input[0];
		fine = pointer_input[4];
	}
	//xil_printf("\ninit: %d\n", init);
	//xil_printf("\nfine: %d\n", fine);
	return dijkstra(init,fine, golden);
}
