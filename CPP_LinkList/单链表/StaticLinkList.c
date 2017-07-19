//#include<stdio.h>
//#include<malloc.h>
//#include<stdbool.h>
//
//#pragma region log大法
//
//#define log printf //启用log
//
////禁用log，使log函数为空：
//void log(str) {
//	return 0;
//}
//#define log0(message) \
//    printf("第%d行：%s\n", __LINE__, message);
//#define log1() \
//    printf("第%d行：log大法\n",  __LINE__);

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

// 初始化
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
// 申请一个空位置（得到空位置的下标）
int Malloc_SLL(StaticLinkList L) {
	int empFirst = L[0].cur;// 返回第一个空闲元素的下标

	if (L[0].cur) {
		L[0].cur = L[empFirst].cur;  //用了一个就要把下一个作为备用
	}
	return empFirst;
}
//释放不用的位置,放到备用链表中
void Free_SSL(StaticLinkList L, int pos) {
	L[pos].cur = L[0].cur;
	L[0].cur = pos;
}
//返回实际数据元素的个数
int ListLength(StaticLinkList L) {
	int num = 0;
	int pre = L[MAXSIZE - 1].cur;
	while (pre) {
		pre = L[pre].cur;
		num++;
	}
	return num;
}

// 插入


//结点插入
bool ListInsert(StaticLinkList L, int pos, ElemType elem) {
	int empty, pre, i;
	//最后一个元素的下标（最后一个元素的下标用来指向第一个实际元素）

	pre = MAXSIZE - 1;
	if (pos < 1 || pos>  ListLength(L) + 1) {
		return false;
	}
	// 得到空闲位置的坐标 j 
	empty = Malloc_SLL(L);
	if (empty) {
		//把新元素数据放在这个空闲位置
		L[empty].data = elem;
		//获取第 i - 1 个元素的 cur -> pre
		for (i = 1; i <= pos - 1; i++) {
			pre = L[pre].cur;
		}

		L[empty].cur = L[pre].cur;
		L[pre].cur = empty;
		return true;
	}
	return false;
}

//删除元素

//删除元素（没调好）
bool ListDelete(StaticLinkList L, int pos) {
	// pos 指的是第几个元素，而 dele 指的是第 pos 个元素对应在数组中的下标 index
	int dele, pre, i;
	if (pos < 1 || pos > ListLength(L)) {
		return false;
	}
	//最后一个元素，遍历到要删除元素的前一个元素
	pre = MAXSIZE - 1;
	for (i = 1; i <= pos - 1; i++) {
		pre= L[pre].cur;
	}
	//获取要删除元素的下标
	dele = L[pre].cur;
	//前一个元素的 cur 跳过 dele 到下一个元素
	L[pre].cur = L[dele].cur;

	Free_SSL(L, dele);
	log("\n删除了第%d个元素\n\n", pos);
	return true;

}

//遍历
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
	//建立结构体数组
	StaticLinkList SLL;

	//初始化
	InitList(SLL);

	//插入
	ListInsert(SLL, 1, 111);
	ListInsert(SLL, 1, 222);
	ListInsert(SLL, 1, 333);
	ListInsert(SLL, 4, 444);
	//下面这种输出方式的话， 其实不能体现实际元素链表的顺序，而是在数组中摆放的位置顺序
	//实际输出的话是：333, 222, 111, 444
	//而下面这行的输出是：111, 222, 333, 444
	//log("前几个元素:\n%d\n%d\n%d\n%d\n\n", SLL[1].data, SLL[2].data, SLL[3].data, SLL[4].data);
	//想按元素的链表顺序输出的话，就按下面这个函数来输出
	// 遍历输出
	ListTraverse(SLL);

	ListDelete(SLL, 2);
	//ListDelete(SLL, 1);
	//log("前几个元素:\n%d\n%d\n%d\n%d\n\n", SLL[1].data, SLL[2].data, SLL[3].data, SLL[4].data);
	// 遍历输出
	ListTraverse(SLL);


	return;
}
