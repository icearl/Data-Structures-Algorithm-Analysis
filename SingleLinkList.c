

#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>

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

//节点定义
typedef struct  Node {
	int data;//数据域
	struct Node * PNext;//指针域，存放下一个节点的地址
} Node, *PNode;

#pragma endregion

//helloWorld 测试
void hello(void) {
	printf("hello, world");
	system("pause");
	return 0;
}

//新建节点-测试
int node_test(void) {
	Node node1;
	node1.data = 111;
	printf("%d", node1.data);
	system("pause");
	return 0;
}

#pragma region 建表
//建表1（头插法、手动值）
//返回值：头节点（指针）
PNode create_list_head_hand()
{
	int len, i;
	printf("请输入链表的长度：len=\n");
	scanf("%d", &len);
	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;
	for (i = 0;i<len;i++)
	{
		int val;
		printf("请输入第 %d 个元素的值：", i + 1);
		scanf("%d", &val);
		PNode PNew = malloc(sizeof(Node));
		PNew->data = val;
		PNew->PNext = PHead->PNext;
		PHead->PNext = PNew;
	}
	return PHead;
}

//建表2（头插法、随机值）
PNode create_list_head_random() {
	int len, i;
	printf("请输入链表的长度：len=\n");
	scanf("%d", &len);
	//创建空链表，包含一个头节点
	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;

	for (i = 0;i<len;i++)
	{
		PNode PNew = malloc(sizeof(Node));
		PNew->data = rand() % 100 + 1;

		PNew->PNext = PHead->PNext;
		PHead->PNext = PNew;
	}
	return PHead;
}

//建表3（尾插法）
PNode create_list_tail_hand()
{
	int len, i;

	printf("请输入链表的长度：len=\n");
	scanf("%d", &len);

	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;

	PNode PTail = PHead;

	for (i = 0;i<len;i++)
	{
		int val;

		printf("请输入第 %d 个元素的值：", i + 1);
		scanf("%d", &val);

		PNode PNew = malloc(sizeof(Node));

		PNew->data = val;

		PNew->PNext = NULL;
		PTail->PNext = PNew;

		PTail = PNew;
	}
	return PHead;
}

//建表4（尾插法）
PNode create_list_tail_random()
{
	int len, i;
	srand(time(0));

	printf("请输入链表的长度：len=\n");
	scanf("%d", &len);
	printf("\n");

	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;

	PNode PTail = PHead;

	for (i = 0;i<len;i++)
	{

		PNode PNew = malloc(sizeof(Node));

		PNew->data = rand() % 1000 + 1;

		PNew->PNext = NULL;
		PTail->PNext = PNew;

		PTail = PNew;
	}
	return PHead;
}
#pragma endregion

//遍历
void traverse(PNode pHead)
{
	PNode p = pHead->PNext;
	printf("所有节点的值为：\n");
	while (p != NULL)
	{
		printf("%d    ", p->data);
		p = p->PNext;
	}
	printf("\n\n");
}

//获取 L 链表的第 i 元素，给到指针 *e
Status GetElem(PNode L, int i, ElemType *e) {
	int j;
	PNode p;
	p = L->PNext;
	j = 1;
	while(p && j < i) {
		p = p->PNext;
		j++;
	}
	
	if (!p || j > i) {
		return ERROR;
	}

	*e = p->data;
	printf("第%d个节点的值为%d\n", i, *e);
	return OK;
}

//判断是否为空
bool isempty(PNode pHead)
{
	if (NULL == pHead->PNext)
	{
		//printf
		return true;
	}
	else {
		return false;
	}
}

//获取链表的长度
int list_num(PNode pHead)
{
	int num = 0;
	PNode p = pHead->PNext;
	while (p != NULL)
	{
		num++;
		p = p->PNext;
	}
	return  num;
}

//在pHead队列里把val插入到pos位置
bool insert(PNode pHead, int val, int pos) {
	int i = 1;
	PNode p = pHead;
	//取到第 pos - 1 个节点
	while (p != NULL &&i<pos)//当i = pos - 1时，正好 p 取到第 pos - 1 个节点，然后i = pos，退出循环 
	{
		i++;
		p = p->PNext;
	}
	//如果插入位置过大，那么P=NULL,
	//如果插入的位置是0或者负数，那么i>pos
	if (i > pos || NULL == p){
		printf("插入位置不合法\n");
		return false;
	}
	//建节点
	PNode PNew = malloc(sizeof(PNode));
	PNew->data = val;
	//插入
	PNew->PNext = p->PNext;
	p->PNext = PNew;

	return true;
}

//删除
void delete (PNode PHead, int pos, int * deleVal)
{
	int i = 1;
	PNode p = PHead;
	PNode PPos = p->PNext;
	//取得 pos - 1 处的元素
	//我们要删除p后面的节点，所以p不能指向最后一个节点 p->next!=NULL
	while (p->PNext != NULL && i < pos) {

		p = p->PNext;
		i++;
	}
	if (i>pos || p->PNext == NULL) 
	{
		printf("删除位置不合法\n");
		return false;
	}
	PPos = p->PNext;
	p->PNext = PPos->PNext;
	
	*deleVal = PPos->data;
	free(PPos);

}

//main函数
int main(void) {
	//建立指针
	int a = 0;
	int *Ptr = &a;

	//建表
	PNode li_head = create_list_tail_random();
	//遍历
	traverse(li_head);

	//判断是否空表
	bool isEmp = isempty(li_head);
	log("是否为空：%d\n",isEmp);
	
	//获取长度
	printf("长度：%d\n", list_num(li_head));

	//插入
	insert(li_head, 999, 4);
	traverse(li_head);

	//删除
	delete (li_head, 3, Ptr);
	traverse(li_head);
	log("Ptr:%d", *Ptr);


	system("pause");
	return 0;
}
