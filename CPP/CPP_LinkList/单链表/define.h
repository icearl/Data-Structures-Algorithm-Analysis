
#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>
#include<stdlib.h>

#pragma region log大法

#define log printf //启用log

//禁用log，使log函数为空：
//void log(str) {
//	return 0;
//}
#define log0(message) \
    printf("第%d行：%s\n", __LINE__, message);
#define log1() \
    printf("第%d行：log大法\n",  __LINE__);

#pragma endregion

#pragma region define

#define OK 1
#define ERROR 0

typedef int Status;
typedef int ElemType;
#define MAXSIZE 100
#pragma endregion
