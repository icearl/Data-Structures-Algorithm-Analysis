
#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>
#include<stdlib.h>

#pragma region log��

#define log printf //����log

//����log��ʹlog����Ϊ�գ�
//void log(str) {
//	return 0;
//}
#define log0(message) \
    printf("��%d�У�%s\n", __LINE__, message);
#define log1() \
    printf("��%d�У�log��\n",  __LINE__);

#pragma endregion

#pragma region define

#define OK 1
#define ERROR 0

typedef int Status;
typedef int ElemType;
#define MAXSIZE 100
#pragma endregion
