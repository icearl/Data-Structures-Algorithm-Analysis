using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Searching {
    class BinarySearch {
        // 递归版本
        public static int Search1(int[] arr, int low, int high, int key) {
            int mid = (low + high) / 2;
            if (low > high)
                return -1;
            else {
                if (arr[mid] == key)
                    return mid;
                else if (key < arr[mid])
                    return Search1(arr, low, mid - 1, key);
                else
                    return Search1(arr, mid + 1, high, key);
            }
        }
        // 非递归版本（迭代版本）
        public static int Search2(int[] arr, int key) {
            int low = 0;
            int high = arr.Length - 1;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (arr[mid] == key)
                    return mid;
                else if (key < arr[mid])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
            return -1;
        }

    }
}
