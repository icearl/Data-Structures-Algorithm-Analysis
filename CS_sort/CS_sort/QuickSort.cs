using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class QuickSort {
        public void Sort(int[] arr) {
            QSort(arr, 0, arr.Length - 1);
        }

        void QSort(int[] arr, int L, int R) {
            if(L < R) {
                int pivot = RandomizedPartition(arr, L, R);
                QSort(arr, L, pivot - 1);
                QSort(arr, pivot + 1, R);
            }
        }

        int Partition(int[] arr, int L, int R) {
            int pivot = arr[L];
            while(L < R) {
                // 从右端开始比较
                //（1）假如从右端过来的数比分隔数要大，则不用处理
                //（2）假如从右端过来的数比分隔数要小，则需要挪到分隔线左边
                while (L < R && arr[R] >= pivot) {
                    R--;
                }
                // 把右边的小数移到左边，然后左边这个位置以后就不遍历了
                if (L < R) {
                    Swap(arr, L, R);
                    L++;
                }
                // 从从端开始比较
                //（1）假如从左端过来的数比分隔数要小，则不用处理
                //（2）假如从左端过来的数比分隔数要大，则需要挪到分隔线右边
                while (L < R && arr[L] <= pivot) {
                L++;
                }
                // 把左边的小数移到左边，然后右边这个位置以后就不遍历了
                if (L < R) {
                    Swap(arr, L, R);
                    R--;
                }
            }
            return L;


        }
        int RandomizedPartition(int[] arr, int L, int R) {
            Random ran = new Random();
            int n = ran.Next(L, R);
            Swap(arr, L, n);
            return Partition(arr, L, R);
        }
        void Swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}
