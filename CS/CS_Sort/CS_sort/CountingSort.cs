using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class CountingSort {
        public int[] Sort(int[] arr, int k) {
            // 排序后的结果存储
            int arrLen = arr.Length;
            int[] sortedArr = new int[arrLen];
            // 计数数组
            int[] countingArr = new int[k];
            // 计数数组初始化为 0
            // 包括 0 和 k
            for (int i = 0; i <= k; i++) {
                countingArr[i] = 0;
            }
            // 单个元素计数(经过该步骤,countingArr[i]的含义为数字 i 的个数为countingArr[i])
            for (int i = 0; i <= arrLen - 1; i++) {
                countingArr[arr[i]]++;
            }
            // 计算小于等于某数的个数(经过该步骤countingArray[i]的含义为小于等于数字i的元素个数为countingArray[i])
            for (int i = 1; i <= k - 1; i++) {
                countingArr[i] += countingArr[i - 1];
            }
            // 得到排序后的结果
            for (int i = 0; i <= arrLen - 1; i++) {
                // arr[i] 是第 countingArr[arr[i]] 个元素，因为 sortedArr 下标从 0 开始，所以要 -1
                int index = countingArr[arr[i]] - 1;
                sortedArr[index] = arr[i];
                countingArr[arr[i]]--;
            }
            return sortedArr;
        }
    }
}
