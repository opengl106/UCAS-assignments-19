#include<stdio.h>
#include<math.h>
#include"lu.h"
#include"schmidt.h"
#include"householder.h"
#include"givens.h"
int main(){
 int lu31();
 int schmidt31();
 int householder31();
 int givens31();
 char comnd;
 start:
 printf("Choose the subprogram for matrix factorization.\nG for PA=LU factorization;\nS for Schmidt orthogonalization;\nH for Householder orthogonal reduction;\ng for Givens orthogonal reduction.\n");
 scanf("%c", &comnd);
 switch(comnd){
  case 'G': lu31(); break;
  case 'S': schmidt31(); break;
  case 'H': householder31(); break;
  case 'g': givens31(); break;
  default: goto start;
 }return 0;
}
