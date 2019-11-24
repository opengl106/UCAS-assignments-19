int schmidt31(){
 int M, N, i, j, k, t, u;
 float s;
 printf("Input the row and column of your matrix:\nExample: 3 4\n");
 scanf("%d %d", &M, &N);
 float a[M][N];
 printf("\nInput the elements of your matrix:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<N;j++){
   scanf("%f", *(a+i)+j);
  }
 }
/*input*/

 float q[M][N], r[N][N];
 float v[M];
 for(i=0;i<M;i++){
  for(j=0;j<N;j++){
   q[i][j]=0;
  }
 }for(i=0;i<N;i++){
  for(j=0;j<N;j++){
   r[i][j]=0;
  }
 }//initialization
 for(t=0; t<N; t++){
  for(i=0; i<M; i++){
   v[i]=a[i][t];
  }//take out the t-th column from matrix A
  for(u=0; u<t; u++){
   s=0;
   for(i=0; i<M; i++){
    s+=v[i]*q[i][u];
   }r[u][t]=s;
   for(i=0; i<M; i++){
    v[i]-=s*q[i][u];
   }
  }//decide the t-th column of matrix R, as well as orthogonalize the vector v
  s=0;
  for(i=0; i<M; i++){
   s+=v[i]*v[i];
  }s=sqrt(s);
  r[t][t]=s;
  if(s>0.000001){//the vector in Q maybe 0, where any fill-in toward matrix Q is unnecessary
   for(i=0; i<M; i++){
    q[i][t]=v[i]/s;
   }
  }//normalize v and fill into matrix Q
 }//orthogonalize the columns of matrix A
 
 printf("\n\nSchmidt QR factorization succeeded.\nThe matrix Q:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<N;j++){
   printf("%f ", q[i][j]);
  }printf("\n");
 }printf("\nThe matrix R:\n\n");
 for(i=0;i<N;i++){
  for(j=0;j<N;j++){
   printf("%f ", r[i][j]);
  }printf("\n");
 }return 0;
}
