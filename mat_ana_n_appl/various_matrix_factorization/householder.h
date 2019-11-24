int householder31(){
 int M, N, i, j, k, t, u;
 float s0, s1, s2;
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
 float v[M][N];
 for(i=0;i<M;i++){
  for(j=0;j<M;j++){
   q[i][j]=(i==j);
  }
 }//initialization
 for(t=0; t<N&&t<M; t++){
  s0=0;
  for(i=t; i<M; i++){
   s0+=a[i][t]*a[i][t];
  }s0=sqrt(s0);
  for(i=t; i<M; i++){
   v[i][t]=(i==t)*s0-a[i][t];
  }//decide the reflect vector v for t-th time
  s2=0;
  for(i=t; i<M; i++){
   s2+=v[i][t]*v[i][t];
  }if(s2){
   for(u=t; u<N; u++){
    s1=0;
    for(i=t; i<M; i++){
     s1+=a[i][u]*v[i][t];
    }for(i=t; i<M; i++){
     a[i][u]-=2*s1*v[i][t]/s2;
    }
   }//convert matrix A into the next iteration version
  }
 }//diagonalize A into matrix R
 for(t--;t>=0;t--){
  s2=0;
  for(i=t; i<M; i++){
   s2+=v[i][t]*v[i][t];
  }if(s2){
   for(u=t; u<M; u++){
    s1=0;
    for(i=t; i<M; i++){
     s1+=q[i][u]*v[i][t];
    }for(i=t; i<M; i++){
     q[i][u]-=2*s1*v[i][t]/s2;
    }
   }
  }
 }//iteratively calculate matrix Q
 printf("\n\nHouseholder QR factorization succeeded.\nThe matrix Q:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<M;j++){
   printf("%f ", q[i][j]);
  }printf("\n");
 }printf("\nThe matrix R:\n\n");
 for(i=0;i<M;i++){
  for(j=0;j<N;j++){
   printf("%f ", a[i][j]);
  }printf("\n");
 }return 0;
}
