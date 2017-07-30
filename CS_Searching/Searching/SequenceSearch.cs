using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//一种无序（不要求有序）查找算法
namespace Searching {
    class SequenceSearch { 
        public int Search(int[] array, int key) {
            for (int i = 0; i < array.Length; i++) {
                if (array[i] == key)
                    return i;
            }
            return -1;
        }
    }
}
