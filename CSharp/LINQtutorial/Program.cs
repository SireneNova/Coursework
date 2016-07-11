using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EastwoodLINQtutorial
{
    class Program
    {
        static void Main(string[] args)
        {
            var sample = "I enjoy writing uber-software in C#";

            //vowels out of sen
            var result = from c in sample.ToLower()
                         where c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
                         orderby c
                         group c by c;
                         //orderby c //alphabetical order/ascending, can do descending too
                         //select c; //don't need select when using group

            foreach (var item in result) //with group, result is a grouped enumerable
            {
                //Console.WriteLine(item);
                //Console.WriteLine(item.Key); //need this with group
                Console.WriteLine("{0} - {1}", item.Key, item.Count()); //first param, second
            }

        }
    }
}
