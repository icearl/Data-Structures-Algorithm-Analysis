using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LinkedLists {
    class Queue<Item> {
        private Node nil = new Node(default(Item)); // link to least recently added node
        private Node tail; // link to most recently added node
        private int N; // number of items on the queue
        public Queue() {
            Node nil = new Node(default(Item));
            tail = nil;
            N = 0;
        }
       
        class Node { // nested class to define nodes
            public Item item;
            public Node next;
            //构造器：无参数
            public Node() {
                item = default(Item);
                next = null;
            }
            //构造器：数据域，尾结点
            public Node(Item val) {
                item = val;
                next = null;
            }
        }
        public bool IsEmpty() {
            return nil.next == null;
        } // Or: N == 0.

        public int size() {
            return N;
        }
        public void enqueue(Item another) { // Add item to the end of the list.
            Node newNode = new Node(another);

            if (IsEmpty()) {
                nil.next = newNode;
            }

            tail.next = newNode;
            tail = newNode;

            N++;
        }
        public Item dequeue() { // Remove item from the beginning of the list.k
            if (IsEmpty()) {
                Console.WriteLine("Empty Linked List");
                return default(Item);
            }

            Item oldFirstItem = nil.next.item;

            nil.next = nil.next.next;

            if (IsEmpty()) {
                tail = nil;
            }

            N--;

            return oldFirstItem;
        }
        // 测试
        public void Test() {
            Queue<int> q = new Queue<int>();
            q.enqueue(111);
            q.enqueue(2);
            q.enqueue(333);
            q.enqueue(4);
            q.dequeue();
            while (q.size() > 0) {
                Console.WriteLine(q.dequeue());
            }
        }

    }
}