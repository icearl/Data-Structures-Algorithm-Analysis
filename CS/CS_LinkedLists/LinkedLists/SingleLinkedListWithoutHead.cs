using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedLists {
    
    // 单链表
    class SingleLinkedListWithoutHead<Item> {
        // 结点类定义
        class Node<Data> {
            public Data item;
            public Node<Data> next;

            //构造器：无参数  
            public Node() {
                item = default(Data);
                next = null;
            }
            //构造器：数据域，尾结点  
            public Node(Data val) {
                item = val;
                next = null;
            }
        }
        // 头结点
        private Node<Item> head;
        // 尾结点
        private Node<Item> tail;
        // 元素个数
        private int N;
        //构造器  
        public SingleLinkedListWithoutHead() {
            head = null;
            tail = null;
            N = 0;
        }

        // 求链表 长度 O(n)
        public int GetLength() {
            int len = 0;
            for (Node<Item> x = head; x != null; x = x.next) {
                len++;
            }
            return len;
        }
        // 求链表 长度 O(1)
        public int Size() {
            return N;
        }

        // 清空链表 O(1)
        public void Clear() {
            head = null;
        }
        // 判断单链表是否为空 O(1) 
        public bool IsEmpty() {
            // 或者: N == 0.
            return head == null;
        }
        // 头部 - 插入 O(1)
        public void InsertBeginning(Item another) {
            // 或 Node<Item> newNode = new Node(another);
            Node<Item> newNode = new Node<Item>();
            newNode.item = another;
            newNode.next = null;

            if (IsEmpty()) {
                head = newNode;
                tail = head;
            } else {
                newNode.next = head;
                head = newNode; 
            }
           

            N++;
        }
        // 头部 - 删除 O(1) （边界条件不太对）
        public Item RemoveBeginning() {
            Item oldheadItem = head.item;

            head = head.next;

            N--;

            return oldheadItem;
        }
        // 尾部 - 插入 O(1)
        public void InsertEnd(Item another) {
            Node<Item> newNode = new Node<Item>();
            newNode.item = another;
            newNode.next = null;

            if (IsEmpty()) {
                tail = newNode;
                head = tail;
            } else {
                tail.next = newNode;
                tail = newNode;
            }

            N++;
        } 
        // 删除第一个值为 data 的节点 O(n) （不太对）
        //public void Remove(Item data) {
        //    if (IsEmpty()) {
        //        Console.WriteLine("Empty Linked List");
        //        return -1;
        //    }
        //    Node<Item> current = head;
        //    while (current.next != null) {
        //        if (current.next.item.Equals(data)) {
        //            current.next = current.next.next;
        //            break;
        //        } else {
        //            current = current.next;
        //        }
        //    }
        //}
        // 获取第 k 个节点的值
        public Item GetElem(int i) {
            if (IsEmpty() || i < 0 || i > Size()) {
                Console.WriteLine("LinkList is empty or position is error! ");
                return default(Item);
            }
            // 指向 head 的结点
            Node<Item> p = head;

            int j = 1;

            while (p.next != null && j < i) {
                ++j;
                p = p.next;
            }
            if (j == i) {
                return p.item;
            } else {
                Console.WriteLine("The " + i + "th node is not exist!");
                return default(Item);
            }
        }
        // 遍历输出
        public void travel() {
            if (IsEmpty()) {
                Console.WriteLine("Empty Linked List");
            } else {
                for (Node<Item> x = head; x != null; x = x.next) {
                    Console.WriteLine(x.item);
                }
            }
        }
        // 测试 - 只用节点，简单测试
        public void Test1() {
            Node<String> head = new Node<String>();
            Node<String> second = new Node<String>();
            Node<String> third = new Node<String>();
            head.item = "to";
            second.item = "be";
            third.item = "or";
            head.next = second;
            second.next = third;
            for (Node<String> x = head; x != null; x = x.next) {
                Console.WriteLine(x.item);
            }
        }
        // 测试-使用函数
        public void Test2() {
            SingleLinkedListWithoutHead<String> list = new SingleLinkedListWithoutHead<string>();
            list.travel();
            list.InsertBeginning("ice");
            list.InsertBeginning("is");
            list.InsertBeginning("a");
            list.InsertBeginning("good");
            list.InsertBeginning("boy");
            //Console.WriteLine("nice:{0}", list.RemoveBeginning());
            list.InsertEnd("fuck");
            list.InsertEnd("you");
            //list.Remove("a");

            list.travel();
            Console.WriteLine(list.GetLength());
            Console.WriteLine(list.GetElem(-1)); 
            //Console.WriteLine(list.IsEmpty());
            //Console.WriteLine(default(int));
            //Console.WriteLine(default(String));
            //Console.WriteLine(default(bool));
        }
    }
}
