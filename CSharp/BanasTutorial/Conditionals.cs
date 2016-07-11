using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BanasCSharpTutorial
{
    class Program
    {
        static void Main(string[] args)
        {
            // Relational Operators : > < >= <= == !=
            // Logical Operators : && || ^ !

            // If Statement
            int age = 17;

            if ((age >= 5) && (age <= 7))
            {
                Console.WriteLine("Go to elementary school");
            }
            else if ((age > 7) && (age < 13))
            {
                Console.WriteLine("Go to middle school");
            }
            else {
                Console.WriteLine("Go to high school");
            }

            if ((age < 14) || (age > 67))
            {
                Console.WriteLine("You shouldn't work");
            }

            Console.WriteLine("! true = " + (!true));
            
            // Ternary Operator

            bool canDrive = age >= 16 ? true : false;
            int canDrive = age >= 16 ? 1 : 2;

            // Switch is used when you have limited options
            // Fall through isn't allowed with C# unless there are no statements between cases
            // You can't check multiple values at once

            switch (age)
            {
                case 0:
                    Console.WriteLine("Infant");
                    break;
                case 1:
                case 2:
                    Console.WriteLine("Toddler");

             // Goto can be used to jump to a label elsewhere in the code
                    goto Cute;
                default:
                    Console.WriteLine("Child");
                    break;
            }
            // Label we can jump to with Goto
            Cute:
            Console.WriteLine("Toddlers are cute");

            -See more at: http://www.newthinktank.com/2015/07/learn-c-one-video/#sthash.OvhiSPsr.dpuf

        }

    }
}