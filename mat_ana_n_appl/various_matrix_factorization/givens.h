int givens31(){
 int M, N, i, j, k, t, u;
 float c, s, r, x, y;
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

 float q[M][M];
 float v[M];
 for(i=0;i<M;i++){
  for(j=0;j<M;j++){
   q[i][j]=(i==j);
  }
 }//initialization
 for(t=0; t<N&&t<M; t++){
  for(i=t+1; i<M; i++){
   r=sqrt(a[t][t]*a[t][t]+a[i][t]*a[i][t]);
   c=a[t][t]/r;
   s=a[i][t]/r;
   for(u=t; u<N; u++){
    x=a[t][u];
    y=a[i][u];
    a[t][u]=x*c+y*s;
    a[i][u]=-x*s+y*c;
   }for(u=0; u<M; u++){
    x=q[t][u];
    y=q[i][u];
    q[t][u]=x*c+y*s;
    q[i][u]=-x*s+y*c;   }
  }
 }//factorization
 printf("\n\nGivens QR factorization succeeded.\nThe matrix Q:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<M;j++){
   printf("%f ", q[j][i]);
  }printf("\n");
 }printf("\nThe matrix R:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<N;j++){
   printf("%f ", a[i][j]);
  }printf("\n");
 }return 0;
}

