#include 'define.h'

//����һ��ջ�ṹ
typeof struct {
	ElemType data[100];
	int top;
}SqStack;

//��ջ 
bool Push(SqStack *Stk, ElemType elem) {
	//��ջʱ������
	if (Stk->top == MAXSIZE - 1) {
		return ERROR;
	}

	//ջ��index��һ
	Stk->top++;
	//��Ԫ�ز嵽����
	Stk->data[Stk->top] = elem;

	return OK;
}

//��ջ
bool Pop(SqStack *Stk, ElemType elem) {
	if (Stk->top == -1) {
		return ERROR;
	}

	*elem = Stk->data[Stk->top];
	Stk->top--;
	return OK;
}
