using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Searching {
    class BinarySearch {
        // 递归版本
        public static int Search1(int[] arr, int left, int right, int key) {
            int mid = (left + right) / 2;
            if (left <= right) {
                if (arr[mid] == key) {
                    return mid;
                } else if (key < arr[mid]) {
                    return Search1(arr, left, mid - 1, key);
                } else {
                    return Search1(arr, mid + 1, right, key);
                }                 
            } else {
                return -1;
            }
            
            
        }
        // 非递归版本（迭代版本）
        public static int Search2(int[] arr, int key) {
            int left = 0;
            int right = arr.Length - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (arr[mid] == key) {
                    return mid;
                } else if (key < arr[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            return -1;
        }

    }
}
