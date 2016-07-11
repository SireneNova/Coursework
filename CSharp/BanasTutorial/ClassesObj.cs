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
            // ---------- CLASSES & OBJECTS ----------
            //get, set

            Animal bulldog = new Animal(13, 50, "Spot", "Woof");

            Console.WriteLine("{0} says {1}", bulldog.name, bulldog.sound);

            // Console.WriteLine("No. of Animals " + Animal.getNumOfAnimals());

            //-See more at: http://www.newthinktank.com/2015/07/learn-c-one-video/#sthash.ROKFlo6m.dpuf
        }

    }
}