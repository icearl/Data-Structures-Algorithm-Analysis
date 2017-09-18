using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Searching {
    class __main {
        static void Main(string[] args) {
            int[] arr = new int[] { 1, 3, 4, 5, 10, 13 };
            int index = BinarySearch.Search1(arr, 0, 5, 3);
            Console.WriteLine(index);
        }
    }
}
