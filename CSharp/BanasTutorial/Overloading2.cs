using System;

namespace ConsoleApplication2
{
    class Overload
    {
        static public int getSum(int num1 = 1, int num2 = 1)
        {
            return num1 + num2;
        }

        static public double getSum(double num1, double num2)
        {
            return num1 + num2;
        }

        public static void Main()
        {
            Console.WriteLine(getSum(3, 4));
            Console.WriteLine(getSum(num2: 3.4, num1: 4.5));
        }

    }
}
