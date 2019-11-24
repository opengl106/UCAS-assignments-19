int lu31(){
 int n, i, j, k, maxr;
 int r=1;
 float rto, inchg;
 double m;
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

 float b[n][n], p[n][n];
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   p[i][j]=b[i][j]=(i==j);
  }
 }
/*initialization of matrix L and P*/

 for(j=0;j<n-1;j++){
  m=fabs((double)a[j][j]); maxr=j;
  for(i=j;i<n;i++){
   if(fabs((double)a[i][j])>m){
    m=fabs((double)a[i][j]); maxr=i;
   }
  }if(maxr!=j){
   for(k=0;k<j;k++){
    inchg=p[j][k]; p[j][k]=p[maxr][k]; p[maxr][k]=inchg;
    inchg=b[j][k]; b[j][k]=b[maxr][k]; b[maxr][k]=inchg;
   }for(k=j;k<n;k++){
    inchg=p[j][k]; p[j][k]=p[maxr][k]; p[maxr][k]=inchg;
    inchg=a[j][k]; a[j][k]=a[maxr][k]; a[maxr][k]=inchg;    
   }
  }
/*partial pivoting*/

  if(a[j][j]==0){
   printf("The matrix is not invertible!\n\n");
   r=0;
   break;
  }for(i=j+1;i<n;i++){
   rto=a[i][j]/a[j][j];
   for(k=j;k<n;k++){
    a[i][k]-=rto*a[j][k];
   }b[i][j]=rto;
  }
 }
/*gaussian elimination*/

 if(r){
  printf("Succeed in PA=LU factorization.\n\n");
 }printf("The matrix P:\n");
 for(i=0;i<n;i++){
  for(j=0;j<n;j++){
   printf("%f ", *(*(p+i)+j));
  }printf("\n");
 }printf("\nThe matrix L:\n");
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
