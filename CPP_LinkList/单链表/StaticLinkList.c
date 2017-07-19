//#include<stdio.h>
//#include<malloc.h>
//#include<stdbool.h>
//
//#pragma region log��
//
//#define log printf //����log
//
////����log��ʹlog����Ϊ�գ�
//void log(str) {
//	return 0;
//}
//#define log0(message) \
//    printf("��%d�У�%s\n", __LINE__, message);
//#define log1() \
//    printf("��%d�У�log��\n",  __LINE__);

//#pragma endregion
//
//#pragma region define
//
//#define OK 1
//#define ERROR 0
//
//typedef int Status;
//typedef int ElemType;
//#define MAXSIZE 100
//#pragma endregion

#include "define.h"

typedef struct
{
	ElemType data;
	int cur;
} Component, StaticLinkList[MAXSIZE];
#pragma endregion

// ��ʼ��
bool InitList(StaticLinkList L) {
	int i;
	for (i = 0; i < MAXSIZE - 2; i++) {
		L[i].data = -1;
		L[i].cur = i + 1;
	}
	L[MAXSIZE - 2].cur = 0;
	L[MAXSIZE - 1].cur = 0;
	return OK;
}
// ����һ����λ�ã��õ���λ�õ��±꣩
int Malloc_SLL(StaticLinkList L) {
	int empFirst = L[0].cur;// ���ص�һ������Ԫ�ص��±�

	if (L[0].cur) {
		L[0].cur = L[empFirst].cur;  //����һ����Ҫ����һ����Ϊ����
	}
	return empFirst;
}
//�ͷŲ��õ�λ��,�ŵ�����������
void Free_SSL(StaticLinkList L, int pos) {
	L[pos].cur = L[0].cur;
	L[0].cur = pos;
}
//����ʵ������Ԫ�صĸ���
int ListLength(StaticLinkList L) {
	int num = 0;
	int pre = L[MAXSIZE - 1].cur;
	while (pre) {
		pre = L[pre].cur;
		num++;
	}
	return num;
}

// ����


//������
bool ListInsert(StaticLinkList L, int pos, ElemType elem) {
	int empty, pre, i;
	//���һ��Ԫ�ص��±꣨���һ��Ԫ�ص��±�����ָ���һ��ʵ��Ԫ�أ�

	pre = MAXSIZE - 1;
	if (pos < 1 || pos>  ListLength(L) + 1) {
		return false;
	}
	// �õ�����λ�õ����� j 
	empty = Malloc_SLL(L);
	if (empty) {
		//����Ԫ�����ݷ����������λ��
		L[empty].data = elem;
		//��ȡ�� i - 1 ��Ԫ�ص� cur -> pre
		for (i = 1; i <= pos - 1; i++) {
			pre = L[pre].cur;
		}

		L[empty].cur = L[pre].cur;
		L[pre].cur = empty;
		return true;
	}
	return false;
}

//ɾ��Ԫ��

//ɾ��Ԫ�أ�û���ã�
bool ListDelete(StaticLinkList L, int pos) {
	// pos ָ���ǵڼ���Ԫ�أ��� dele ָ���ǵ� pos ��Ԫ�ض�Ӧ�������е��±� index
	int dele, pre, i;
	if (pos < 1 || pos > ListLength(L)) {
		return false;
	}
	//���һ��Ԫ�أ�������Ҫɾ��Ԫ�ص�ǰһ��Ԫ��
	pre = MAXSIZE - 1;
	for (i = 1; i <= pos - 1; i++) {
		pre= L[pre].cur;
	}
	//��ȡҪɾ��Ԫ�ص��±�
	dele = L[pre].cur;
	//ǰһ��Ԫ�ص� cur ���� dele ����һ��Ԫ��
	L[pre].cur = L[dele].cur;

	Free_SSL(L, dele);
	log("\nɾ���˵�%d��Ԫ��\n\n", pos);
	return true;

}

//����
bool ListTraverse(StaticLinkList L)
{
	log("List Traverse :\n\n ");
	int k = MAXSIZE - 1;
	while (L[k].cur != 0)
	{
		k = L[k].cur;
		log("%d\n",L[k].data);
	}

	log("\nend\n");
	return true;
}

void SLL_test() {
	//�����ṹ������
	StaticLinkList SLL;

	//��ʼ��
	InitList(SLL);

	//����
	ListInsert(SLL, 1, 111);
	ListInsert(SLL, 1, 222);
	ListInsert(SLL, 1, 333);
	ListInsert(SLL, 4, 444);
	//�������������ʽ�Ļ��� ��ʵ��������ʵ��Ԫ�������˳�򣬶����������аڷŵ�λ��˳��
	//ʵ������Ļ��ǣ�333, 222, 111, 444
	//���������е�����ǣ�111, 222, 333, 444
	//log("ǰ����Ԫ��:\n%d\n%d\n%d\n%d\n\n", SLL[1].data, SLL[2].data, SLL[3].data, SLL[4].data);
	//�밴Ԫ�ص�����˳������Ļ����Ͱ�����������������
	// �������
	ListTraverse(SLL);

	ListDelete(SLL, 2);
	//ListDelete(SLL, 1);
	//log("ǰ����Ԫ��:\n%d\n%d\n%d\n%d\n\n", SLL[1].data, SLL[2].data, SLL[3].data, SLL[4].data);
	// �������
	ListTraverse(SLL);


	return;
}
