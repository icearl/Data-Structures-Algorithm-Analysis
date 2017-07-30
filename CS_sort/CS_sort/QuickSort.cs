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

        void QSort(int[] arr, int left, int right) {
            if(left < right) {
                int pivot = RandomizedPartition(arr, left, right);
                QSort(arr, left, pivot - 1);
                QSort(arr, pivot + 1, right);
            }
        }

        int RandomizedPartition(int[] arr, int left, int right) {
            Random ran = new Random();
            int t = ran.Next(left, right);
            Swap(arr, left, t);
            return Partition(arr, left, right);
        }

        int Partition(int[] arr, int left, int right) {
            int pivot = arr[left];
            while(left < right) {
                // 从右端开始比较
                //（1）假如从右端过来的数比分隔数要大，则不用处理
                //（2）假如从右端过来的数比分隔数要小，则需要挪到分隔线左边
                while (left < right && arr[right] >= pivot) {
                    right--;
                }
                // 把右边的小数移到左边，然后左边这个位置以后就不遍历了
                if (left < right) {
                    Swap(arr, left, right);
                    left++;
                }
                // 从从端开始比较
                //（1）假如从左端过来的数比分隔数要小，则不用处理
                //（2）假如从左端过来的数比分隔数要大，则需要挪到分隔线右边
                while (left < right && arr[left] <= pivot) {
                left++;
                }
                // 把左边的小数移到左边，然后右边这个位置以后就不遍历了
                if (left < right) {
                    Swap(arr, left, right);
                    right--;
                }
            }
            return left;
        }
        
        void Swap(int[] arr, int i, int j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}
