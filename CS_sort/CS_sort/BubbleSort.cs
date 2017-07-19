using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class BubbleSort {
        void Swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        public void SortOriginal(int[] arr) {
            
            for (int i = 0; i < arr.Length - 1; i++) {
                // 两两交换
                for (int j = arr.Length - 1; j > i; j--) {
                    // 后面的是否更小
                    if(arr[j] < arr[j - 1]) {
                        // 把小的换到前面
                        int temp = arr[j];
                        arr[j] = arr[j - 1];
                        arr[j - 1] = temp;
                    }
                }
            }
        }

        public void SortOptimized(int[] arr) {
            bool change = true;
            for (int i = 0; i < arr.Length - 1 && change; i++) {
                change = false;
                for (int j = arr.Length - 1; j > i; j--) {
                    if (arr[j] < arr[j - 1]) {
                        Swap(arr, j, j - 1);
                        //int temp = arr[j];
                        //arr[j] = arr[j - 1];
                        //arr[j - 1] = temp;

                        change = true;
                    }
                }
            }
        }

    }
}
