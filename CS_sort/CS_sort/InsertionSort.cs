using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class InsertionSort {
        public void Sort(int[] arr) {
            // 从第二的开始往前面排好的插入
            for(int i = 1; i < arr.Length; i++) {
                // 把比第 i 个元素大的都往后移一格
                // 存放要插入的元素
                int insertedItem = arr[i];
                // 把比 insertItem 大的后移一位，最后 j 停留在空位前一格
                int j = i -1; 
                while(j >= 0) {
                    if(arr[j] > insertedItem) {
                        arr[j + 1] = arr[j];
                    } else {
                        break;
                    }
                    j--;
                }
                arr[j + 1] = insertedItem;
            }
        }
    }
}
