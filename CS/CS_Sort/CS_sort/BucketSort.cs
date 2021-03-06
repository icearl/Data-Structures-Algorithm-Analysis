﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class BucketSort {
        public int[] Sort(int[] arr) {
            int arrMax = arr.Max();
            int arrLen = arr.Length;

            // 初始化桶  
            LinkedList<int>[] bucket = new LinkedList<int>[arrLen];
            for (int i = 0; i < arrLen; i++) {
                bucket[i] = new LinkedList<int>();
            }
            // 元素分装各个桶中  
            for (int i = 0; i < arrLen; i++) {
                int bucketIndex = arr[i] * arrLen / (arrMax + 1);
                InsertIntoLinkList(bucket[bucketIndex], arr[i]);
            }
            // 从各个桶中获取各元素按个插入  
            int index = 0;
            for (int i = 0; i <= arrLen - 1; i++) {
                foreach (var item in bucket[i]) {
                    arr[index++] = item;
                }
            }
            return arr;
        }

        /// <summary>  
        /// 按升序插入 linklist   
        /// </summary>  
        /// <param name="linkedList"> 要排序的链表 </param>  
        /// <param name="num"> 要插入排序的数字 </param>  
        private static void InsertIntoLinkList(LinkedList<int> linkedList, int num) {
            // 链表为空时，插入到第一位  
            if (linkedList.Count == 0) {
                linkedList.AddFirst(num);
                return;
            }

            else {
                int length = linkedList.Count;
                for (int i = 0; i < length; i++) {
                    if (linkedList.ElementAt(i) > num) {
                        LinkedListNode<int> node = linkedList.Find(linkedList.ElementAt(i));
                        linkedList.AddBefore(node, num);
                        return;
                    }
                }
                linkedList.AddLast(num);
            }
        }
    }
}
