#include<stdio.h>
int main(){
 int n, i, j, k;
 int r=1;
 float rto;
 printf("Input the row & column of your matrix:\n");
 scanf("%d", &n);
 float a[n][n];
 printf("Input the elements of your matrix:\n");
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   scanf("%f", *(a+i)+j);
  }
 }
/*input*/

 float b[n][n];
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   b[i][j]=(i==j);
  }
 }
/*initialization of matrix L*/

 for(j=0;j<n-1;j++){
  if(a[j][j]==0){
   printf("The LU factorization does not exist!\n\n");
   r=0;
   break;
  }for(i=j+1;i<n;i++){
   rto=a[i][j]/a[j][j];
   for(k=j;k<n;k++){
    a[i][k]-=rto*a[j][k];
   }for(k=i;k<n;k++){
    b[k][j]+=rto*b[k][i];
   }
  }
 }
/*gaussian elimination*/

 if(r){
  printf("Succeed in LU factorization.\n\n");
 }printf("The matrix L:\n");
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   printf("%f ", *(*(b+i)+j));
  }printf("\n");
 }printf("\nThe matrix U:\n");
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   printf("%f ", *(*(a+i)+j));
  }printf("\n");
 }
/*output*/

 return 0;
}
