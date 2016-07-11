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
        int i = 0;
 
            while (i< 10)
            {
                // If i = 7 then skip the rest of the code and start with i = 8
                if (i == 7)
                {
                    i++; //jump up to 8
                    continue; //move on
                }
 
                // Jump completely out of the loop if i = 9
                if (i == 9)
                {
                    break;
                }
 
                // You can't convert an int into a bool : Print out only odds
                if ((i % 2) > 0) //odd number
                {
                    Console.WriteLine(i);
                }
                i++;
            }
 
            // The do while loop will go through the loop at least once
            string guess;
            do
            {
                Console.WriteLine("Guess a Number ");
                guess = Console.ReadLine();
            } while (! guess.Equals("15")); // How to check String equality
 
            // Puts all changes to the iterator in one place
            for(int j = 0; j< 10; j++) 
            {
                if ((j % 2) > 0)
                {
                    Console.WriteLine(j); //prints odd numbers
                }
            }
 
            // foreach cycles through every item in an array or collection
            string randStr = "Here are some random characters";
 
            foreach( char c in randStr)
            {
                Console.WriteLine(c);
            }
// See more at: http://www.newthinktank.com/2015/07/learn-c-one-video/#sthash.ROKFlo6m.dpuf

         
        }

    }
}