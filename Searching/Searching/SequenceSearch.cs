using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Searching {
    class SequenceSearch {
        public int Search(int[] array, int key) {
            for (int index = 0; index < array.Length; index++) {
                if (array[index] == key)
                    return index;
            }
            return -1;
        }
    }
}
