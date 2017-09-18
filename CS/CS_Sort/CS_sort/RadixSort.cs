using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class RadixSort {
        /// 基数排序（内排使用计数排序）  
        /// </summary>  
        /// <param name="arrayToSort">要排序的数组</param>  
        /// <param name="maxDigit">数字的最大位数，比如999,maxDigit = 3 </param> 
        /// <returns>排序后的结果</returns>  
        public void Sort(int[] arrayToSort, int maxDigit) {
            // 从低位到高位遍历，执行 maxDigit 次稳定排序
            for (int i = 0; i <= maxDigit - 1; i++) {
                // 输出排好的数组
                int[] sortedArray = new int[arrayToSort.Length];
                // 计数数组
                int[] countingArray = new int[10];
                // 初始化计数数组  
                for (int j = 0; j <= 9; j++) {
                    countingArray[j] = 0;
                }

                // 元素计数  
                for (int j = 0; j <= arrayToSort.Length - 1; j++) {
                    // 把目前要比较的位从每个元素中分离出来
                    int splitNum = (int)(arrayToSort[j] / Math.Pow(10, i)) - (int)(arrayToSort[j] / Math.Pow(10, i + 1)) * 10;
                    countingArray[splitNum]++;
                }
                // 计数小与等于某元素的个数
                for (int j = 1; j < 10; j++) {
                    countingArray[j] += countingArray[j - 1];
                }

                for (int j = arrayToSort.Length - 1; j >= 0; j--) {
                    int splitNum = (int)(arrayToSort[j] / Math.Pow(10, i)) - (int)(arrayToSort[j] / Math.Pow(10, i + 1)) * 10;
                    int splitNumIndex = countingArray[splitNum] - 1;
                    sortedArray[splitNumIndex] = arrayToSort[j];

                    countingArray[splitNum]--;
                }

                Array.Copy(sortedArray, arrayToSort, sortedArray.Length);
            }
        }
    }
}
