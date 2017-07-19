// 单链表
class SingleLinkedListWithHead<Item> {
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

    // 哑结点
    private Node<Item> nil = new Node<Item>(default(Item));

    // 头结点
    //private Node<Item> head;

    // 尾结点
    private Node<Item> tail;

    // 元素个数
    private int N;

    // 构造器  
    public SingleLinkedListWithHead() {
        Node<Item> nil = new Node<Item>(default(Item));
        //head = null;
        tail = nil;
        N = 0;
    }

    // 求链表 长度 O(n)
    public int GetLength() {
        int len = 0;
        for (Node<Item> x = nil.next; x != null; x = x.next) {
            len++;
        }
        return len;
    }
    // 求链表 长度 O(1)
    public int Size() {
        return N;
    }

    // 遍历输出
    public void Travel() {
        if (IsEmpty()) {
            Console.WriteLine("Empty Linked List");
        } else {
            for (Node<Item> x = nil.next; x != null; x = x.next) {
                Console.WriteLine(x.item);
            }
        }
    }

    // 清空链表 O(1)
    public void Clear() {
        nil.next = null;
    }

    // 判断单链表是否为空 O(1) 
    public bool IsEmpty() {
        // 或者: N == 0.
        return nil.next == null;
    }

    // 头部 - 插入 O(1)
    public void InsertBeginning(Item another) {
        Node<Item> newNode = new Node<Item>(another);

        if (IsEmpty()) {
            tail = newNode;
        }

        newNode.next = nil.next;
        nil.next = newNode;
        //Console.WriteLine(nil.next.item);
        N++;
    }

    // 头部 - 删除 O(1) 
    public Item RemoveBeginning() {
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

    // 尾部 - 插入 O(1)
    public void InsertEnd(Item another) {
        Node<Item> newNode = new Node<Item>(another);

        if (IsEmpty()) {
            nil.next = newNode;
        }

        tail.next = newNode;
        tail = newNode;

        N++;
    }

    // 搜索第一个值为 data 的节点，返回这个节点
    private Node<Item> Search(Item data) {
        if (IsEmpty()) {
            Console.WriteLine("Empty Linked List");
        }
        Node<Item> current = nil.next;
        while (current != null) {
            if (current.item.Equals(data)) {
                return current;
            } else {
                current = current.next;
            }
        }
        return null;
    }

    //public void logSearch(Item data) {
    //    Node<Item> tempNode = Search(data);
    //    Console.WriteLine(tempNode.item);
    //}

    // 删除第一个值为 data 的节点 O(n) （不太对，需要讨论头结点和尾结点）
    //public void Remove(Item data) {
    //    Node<Item> tempNode = Search(data);
    //    tempNode
    //}


    // 获取第 k 个节点的值
    public Item GetElem(int i) {
        if (IsEmpty() || i < 0 || i > Size()) {
            Console.WriteLine("LinkList is empty or position is error! ");
            return default(Item);
        }
        // 指向 head 的结点
        Node<Item> p = nil.next;

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


    // 测试 - 只用节点，简单测试
    public void Test1() {
        Node<String> first = new Node<String>();
        Node<String> second = new Node<String>();
        Node<String> third = new Node<String>();

        first.item = "to";
        second.item = "be";
        third.item = "or";

        first.next = second;
        second.next = third;

        for (Node<String> x = first; x != null; x = x.next) {
            Console.WriteLine(x.item);
        }
    }

    // 测试-使用函数
    public void Test2() {
        SingleLinkedListWithHead<String> list = new SingleLinkedListWithHead<string>();
        list.Travel();
        list.InsertBeginning("ice");
        list.InsertBeginning("is");
        list.InsertBeginning("a");
        list.InsertBeginning("good");
        list.InsertBeginning("boy");
        //Console.WriteLine("nice:{0}", list.RemoveBeginning());
        list.InsertEnd("fuck");
        list.InsertEnd("you");
        //list.Remove("a");
        list.RemoveBeginning();
        list.Travel();
        Console.WriteLine(list.GetLength());
        //list.logSearch("you");
        //Console.WriteLine(list.GetElem(-1));
        //Console.WriteLine(list.IsEmpty());
        //Console.WriteLine(default(int));
        //Console.WriteLine(default(String));
        //Console.WriteLine(default(bool));
    }
}