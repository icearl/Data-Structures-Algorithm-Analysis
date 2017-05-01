

#include<stdio.h>
#include<malloc.h>
#include<stdbool.h>

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

//�ڵ㶨��
typedef struct  Node {
	int data;//������
	struct Node * PNext;//ָ���򣬴����һ���ڵ�ĵ�ַ
} Node, *PNode;

#pragma endregion

//helloWorld ����
void hello(void) {
	printf("hello, world");
	system("pause");
	return 0;
}

//�½��ڵ�-����
int node_test(void) {
	Node node1;
	node1.data = 111;
	printf("%d", node1.data);
	system("pause");
	return 0;
}

#pragma region ����
//����1��ͷ�巨���ֶ�ֵ��
//����ֵ��ͷ�ڵ㣨ָ�룩
PNode create_list_head_hand()
{
	int len, i;
	printf("����������ĳ��ȣ�len=\n");
	scanf("%d", &len);
	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;
	for (i = 0;i<len;i++)
	{
		int val;
		printf("������� %d ��Ԫ�ص�ֵ��", i + 1);
		scanf("%d", &val);
		PNode PNew = malloc(sizeof(Node));
		PNew->data = val;
		PNew->PNext = PHead->PNext;
		PHead->PNext = PNew;
	}
	return PHead;
}

//����2��ͷ�巨�����ֵ��
PNode create_list_head_random() {
	int len, i;
	printf("����������ĳ��ȣ�len=\n");
	scanf("%d", &len);
	//��������������һ��ͷ�ڵ�
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

//����3��β�巨��
PNode create_list_tail_hand()
{
	int len, i;

	printf("����������ĳ��ȣ�len=\n");
	scanf("%d", &len);

	PNode PHead = malloc(sizeof(Node));
	PHead->PNext = NULL;

	PNode PTail = PHead;

	for (i = 0;i<len;i++)
	{
		int val;

		printf("������� %d ��Ԫ�ص�ֵ��", i + 1);
		scanf("%d", &val);

		PNode PNew = malloc(sizeof(Node));

		PNew->data = val;

		PNew->PNext = NULL;
		PTail->PNext = PNew;

		PTail = PNew;
	}
	return PHead;
}

//����4��β�巨��
PNode create_list_tail_random()
{
	int len, i;
	srand(time(0));

	printf("����������ĳ��ȣ�len=\n");
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

//����
void traverse(PNode pHead)
{
	PNode p = pHead->PNext;
	printf("���нڵ��ֵΪ��\n");
	while (p != NULL)
	{
		printf("%d    ", p->data);
		p = p->PNext;
	}
	printf("\n\n");
}

//��ȡ L ����ĵ� i Ԫ�أ�����ָ�� *e
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
	printf("��%d���ڵ��ֵΪ%d\n", i, *e);
	return OK;
}

//�ж��Ƿ�Ϊ��
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

//��ȡ����ĳ���
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

//��pHead�������val���뵽posλ��
bool insert(PNode pHead, int val, int pos) {
	int i = 1;
	PNode p = pHead;
	//ȡ���� pos - 1 ���ڵ�
	while (p != NULL &&i<pos)//��i = pos - 1ʱ������ p ȡ���� pos - 1 ���ڵ㣬Ȼ��i = pos���˳�ѭ�� 
	{
		i++;
		p = p->PNext;
	}
	//�������λ�ù�����ôP=NULL,
	//��������λ����0���߸�������ôi>pos
	if (i > pos || NULL == p){
		printf("����λ�ò��Ϸ�\n");
		return false;
	}
	//���ڵ�
	PNode PNew = malloc(sizeof(PNode));
	PNew->data = val;
	//����
	PNew->PNext = p->PNext;
	p->PNext = PNew;

	return true;
}

//ɾ��
void delete (PNode PHead, int pos, int * deleVal)
{
	int i = 1;
	PNode p = PHead;
	PNode PPos = p->PNext;
	//ȡ�� pos - 1 ����Ԫ��
	//����Ҫɾ��p����Ľڵ㣬����p����ָ�����һ���ڵ� p->next!=NULL
	while (p->PNext != NULL && i < pos) {

		p = p->PNext;
		i++;
	}
	if (i>pos || p->PNext == NULL) 
	{
		printf("ɾ��λ�ò��Ϸ�\n");
		return false;
	}
	PPos = p->PNext;
	p->PNext = PPos->PNext;
	
	*deleVal = PPos->data;
	free(PPos);

}

//main����
int main(void) {
	//����ָ��
	int a = 0;
	int *Ptr = &a;

	//����
	PNode li_head = create_list_tail_random();
	//����
	traverse(li_head);

	//�ж��Ƿ�ձ�
	bool isEmp = isempty(li_head);
	log("�Ƿ�Ϊ�գ�%d\n",isEmp);
	
	//��ȡ����
	printf("���ȣ�%d\n", list_num(li_head));

	//����
	insert(li_head, 999, 4);
	traverse(li_head);

	//ɾ��
	delete (li_head, 3, Ptr);
	traverse(li_head);
	log("Ptr:%d", *Ptr);


	system("pause");
	return 0;
}
