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
            var people = new List<Person>
            {
                new Person{FirstName="John", LastName = "Doe", Age = 25},
                new Person{FirstName="Jane", LastName = "Doe", Age = 26},
                new Person{FirstName="John", LastName = "Williams", Age = 40},
                new Person{FirstName="Samantha", LastName = "Williams", Age = 34},
                new Person{FirstName="Bob", LastName = "Walters", Age = 12},
            };

            var result = from p in people
                         //where p.Age < 30 && p.LastName=="Doe"
                         orderby p.LastName descending
                         group p by p.LastName;
                         //select p;

            foreach (var item in result) //with group, result is a grouped enumerable
            {
                //Console.WriteLine("{0} - {1}", item.FirstName, item.LastName); //gives number
                Console.WriteLine(item.Key + " - " + item.Count());
                foreach (var p in item)
                {
                    Console.WriteLine("\t{0}, {1}", p.LastName, p.FirstName);
                }
            }

        }
    }

    public class Person
    {
        public string FirstName { get; set; } //prop, then press tab twice
        public string LastName { get; set; }
        public int Age { get; set; }
    }
}
