using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cs_Test
{
    class Program
    {
       
        static void Main(string[] args)
        {

            int[] arr = { 7, 3, 1, 0, 0, 6 };
            PrintAll(arr);
            //int[] outNums = BubbleSort(arr);
            Array.Sort(arr);
            Console.Write("\n");
            PrintAll(arr);
            //Console.Write(arr[2]);
            int sum = 0;
            for (int i = 0; i < arr.Length; i = i + 2)
            {
                sum += arr[i];
            }
            Console.Write("\n{0}",sum);
            //return sum;

        }
        static void PrintAll(int[] arr)
        {
            foreach (int i in arr)
            {
                Console.Write(i);
            }
        }

       
        static int[] BubbleSort(int[] inNums)
        {
            int i, j; 
            for (i = 0; i < inNums.Length - 1; i++)
            {
                for (j = inNums.Length - 2; j >= i; j--)
                {
                    if (inNums[j] > inNums[j + 1])
                    {
                        int temp = inNums[j];
                        inNums[j] = inNums[j + 1];
                        inNums[j + 1] = temp;
                    }
                }
            }
            return inNums;
        }

    }
}
