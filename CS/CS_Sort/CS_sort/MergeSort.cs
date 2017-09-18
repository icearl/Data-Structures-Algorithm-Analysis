using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class MergeSort {
        public void Sort(int[] arr) {
            MSort(arr, 0, arr.Length - 1);
        }

        void MSort(int[] arr, int left, int right) { 
            if(left < right) {
                int mid = (left + right) / 2;

                MSort(arr, left, mid);
                MSort(arr, mid + 1, right);

                Merge(arr, left, mid, right);
            }
        }

        void Merge(int[] array, int first, int mid, int last) {
            int indexA = first;     //左侧子表的起始位置
            int indexB = mid + 1;   //右侧子表的起始位置
            int[] tempArr = new int[last + 1]; //声明数组（暂存左右子表的所有有序数列）：长度等于左右子表的长度之和。
            int tempIndex = 0;
            while (indexA <= mid && indexB <= last) //进行左右子表的遍历，如果其中有一个子表遍历完，则跳出循环
            {
                if (array[indexA] <= array[indexB]) //此时左子表的数 <= 右子表的数
                {
                    tempArr[tempIndex++] = array[indexA++];    //将左子表的数放入暂存数组中，遍历左子表下标++
                }
                else//此时左子表的数 > 右子表的数
                {
                    tempArr[tempIndex++] = array[indexB++];    //将右子表的数放入暂存数组中，遍历右子表下标++
                }
            }
            //有一侧子表遍历完后，跳出循环，将另外一侧子表剩下的数一次放入暂存数组中（有序）
            while (indexA <= mid) {
                tempArr[tempIndex++] = array[indexA++];
            }
            while (indexB <= last) {
                tempArr[tempIndex++] = array[indexB++];
            }

            //将暂存数组中有序的数列写入目标数组的制定位置，使进行归并的数组段有序
            tempIndex = 0;
            for (int i = first; i <= last; i++) {
                array[i] = tempArr[tempIndex++];
            }
        }
    }
}
