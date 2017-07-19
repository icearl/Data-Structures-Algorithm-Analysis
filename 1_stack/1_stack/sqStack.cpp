#include 'define.h'

//定义一个栈结构
typeof struct {
	ElemType data[100];
	int top;
}SqStack;

//入栈 
bool Push(SqStack *Stk, ElemType elem) {
	//满栈时，报错
	if (Stk->top == MAXSIZE - 1) {
		return ERROR;
	}

	//栈顶index加一
	Stk->top++;
	//新元素插到上面
	Stk->data[Stk->top] = elem;

	return OK;
}

//出栈
bool Pop(SqStack *Stk, ElemType elem) {
	if (Stk->top == -1) {
		return ERROR;
	}

	*elem = Stk->data[Stk->top];
	Stk->top--;
	return OK;
}
