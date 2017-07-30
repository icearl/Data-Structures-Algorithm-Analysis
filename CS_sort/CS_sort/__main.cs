using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS_sort {
    class __main {
        static void Main(string[] args) {
            //__main.moreSort();
            __main.voidSort();
        }
        static void voidSort() {
            int[] array = new int[] { 11, 333, 123, 2, 55, 43, 9999, 5 };
            var S = new QuickSort();
            S.Sort(array);
            foreach (int item in array) {
                Console.Write("{0} ", item);
            }
        }
        //    static void moreSort() {
        //        int[] array = new int[] { 11, 333, 123, 44, 2, 9999, 5 };
        //        //var S = new HeapSort();
        //        //int[] sortedArr = S.Sort(array);
        //        int[] sortedArr = HeapSort.Sort(array);
        //        foreach (int item in sortedArr) {
        //            Console.Write("{0} ", item);
        //        }
        //    }
    }
}
