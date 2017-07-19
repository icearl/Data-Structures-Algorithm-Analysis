using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedLists {
    class Stack<Item> {
        // 栈顶结点
        private Node nil = new Node();
        // 元素个数
        private int N;
        // 结点嵌套类
        class Node {
            public Item item;
            public Node next;
        }
        // 判断栈是否为空
        public bool IsEmpty() {
            // 或者: N == 0.
            return nil.next == null; 
        } 

        // 获取栈大小
        public int size() {
            return N;
        }

        // push:Add item to top of stack.
        public void push(Item item) { // 
            Node newNode = new Node();
            newNode.item = item;
            newNode.next = nil.next;

            nil.next = newNode;

            N++;
        }
        // pop:Remove item from top of stack. 
        public Item pop() {
            if (IsEmpty()) {
                Console.WriteLine("Empty Stack");
                return default(Item);
            }
            Item oldFirstItem = nil.next.item;

            nil.next = nil.next.next;

            N--;
            return oldFirstItem;
        }
        // 测试
        public void test() {
            Stack<String> stack = new Stack<String>();
            stack.push("ice");
            stack.push("arl");
            stack.push("111");
            stack.push("222");
            stack.pop();
            while(stack.size() > 0) {
                Console.WriteLine(stack.pop());
            }
        }
    }
}
