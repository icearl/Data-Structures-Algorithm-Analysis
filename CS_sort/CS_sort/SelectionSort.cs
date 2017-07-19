using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class SelectionSort {
        void Swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        public void Sort(int[] arr) {
            for(int i = 0; i < arr.Length - 1; i++) {
                // 选出第 i 小的元素的下标
                int minIndex = i;
                for(int j = i + 1; j <= arr.Length - 1; j++) {
                    if(arr[j] < arr[minIndex]) {
                        minIndex = j;
                    }
                }
                // 保证第一个是第 i 小的
                if(minIndex != i) {
                    Swap(arr, minIndex, i);
                }

            }
        }
    }
}
