using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Delegates are used to pass methods as arguments to other methods
// A delegate can represent a method with a similar return type and attribute list
delegate double GetSum(double num1, double num2);

namespace BanasCSharpTutorial
{
    class Program
    {
        static void Main(string[] args)
        {
            // ---------- ANONYMOUS METHODS ----------
            // An anonymous method has no name and its return type is defined by the return used in the method

            GetSum sum = delegate (double num1, double num2) {
                return num1 + num2;
            };

            Console.WriteLine("5 + 10 = " + sum(5, 10));

            //-See more at: http://www.newthinktank.com/2015/07/learn-c-one-video/#sthash.aY8Gro6z.dpuf
        }
    }
}
