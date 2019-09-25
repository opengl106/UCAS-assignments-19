# 矩阵的LU分解

## 介绍

一个实现矩阵LU分解的简易C程序。

## 功能

1. 完成可逆矩阵A的A=LU因子分解，其中L是下三角矩阵而U是上三角矩阵；\
2. 对于包含行列式为零的leading principal minor的可逆矩阵A，求出令PA可分解为LU的P并求出PA=LU，其中P为row-switching elementary matrices的连乘，L是下三角矩阵而U是上三角矩阵。该过程中矩阵P的操作包含部分主元法的运用（partial pivoting）。

## 使用

### 对于功能1的实现：

编译并运行LUF.c:
```bash
gcc -o LUF LUF.c
./LUF
```
按照程序提示，先输入n×n矩阵的行列数n，再输入矩阵的entries。\
如果分解成功，程序会输出矩阵L与U。\
如果矩阵含有为零的leading principal minor，分解会失败并提示，同时输出中间运算结果。

### 对于功能2的实现：

编译并运行PALUF.c:
```bash
gcc -o PALUF PALUF.c
./PALUF
```
按照程序提示，先输入n×n矩阵的行列数n，再输入矩阵的entries。\
如果分解成功，程序会输出矩阵P、L与U。\
如果矩阵不可逆，分解会失败并提示，同时输出中间运算结果。

## 运行示例

见running example.png。
