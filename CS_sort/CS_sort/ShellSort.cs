using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class ShellSort {
        public void Sort(int[] a) {
            int len = a.Length;
            int i, j, gap;

            // gap为步长，每次减为原来的一半。
            for (gap = len / 2; gap > 0; gap /= 2) {
                // 遍历 gap 个组，对每一组都执行直接插入排序
                for (i = 0; i <= gap - 1; i++) {
                    // 对每组进行插入排序
                    for (j = i + gap; j <= len - 1; j += gap) {
                        // 如果a[j] < a[j-gap]，则寻找a[j]位置，并将后面数据的位置都后移。
                        if (a[j] < a[j - gap]) {
                            int temp = a[j];
                            int k = j - gap;
                            while (k >= 0) {
                                if(a[k] > temp) {
                                    a[k + gap] = a[k];
                                    k -= gap;
                                }
                            }
                            a[k + gap] = temp;
                        }
                    }
                }

            }
        }
    }
}
