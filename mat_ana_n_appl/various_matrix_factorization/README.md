# 矩阵的分解

## 介绍

一个实现矩阵各种分解的简易C程序。

## 功能

1. 通过Gaussian Elimination，实现方阵A的PA=LU分解，其中P是行交换矩阵，L是下三角矩阵，U是上三角矩阵。
2. 通过Schmidt正交化，完成矩阵A（m×n）的A=QR因子分解。其中Q（m×n）的列向量是矩阵A的列向量的正交化，R（n×n）是上三角矩阵。
3. 通过Householder镜面反射操作，实现矩阵A（m×n）的A=QR因子分解。其中Q（m×m）是正交矩阵，R（m×n）是矩阵A的列向量的上三角化的结果。
4. 通过Givens旋转操作实现2所述的操作。

## 使用

将所有文件放于同一文件夹下，编译并运行matfact.c:
```bash
gcc -o matfact matfact.c -lm
./matfact
```
按照程序提示，选择需要的分解类型。\
按照程序提示，先输入矩阵的行列数m n，再输入矩阵的entries。\
如果分解成功，程序会输出结果。

## 运行示例

见running example.png。
