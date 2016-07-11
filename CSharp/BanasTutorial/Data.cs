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
            bool canVote = true;
            char grade = 'A';
            
            //integer with max of 2,147,483,647
            int maxInt = int.MaxValue;

            //long max of 9,223,732,036,854,775,807
            long maxLong = long.MaxValue;

            //decimal max value of 79,228,163,514,264,337,593,543,950,335
            //look up biginteger for something bigger
            decimal maxDec = decimal.MaxValue;

            //float is 32 bit number with maxValue of 4.302823E+38 with 7 dec of precision
            float maxFloat = float.MaxValue;

            //double is 32 bit number with maxValue of 1.797683134E+308 with 15 dec of precision
            double maxDouble = double.MaxValue;

            Console.WriteLine("Max Int: " + maxInt);
            var anotherName = "Tom"; //can't define variable as different type other than string now (eg 2)
            //anotherName = 2 //not allowed. diff data type.

            //get data type with:
            Console.WriteLine("anotherName is a {0}", anotherName.GetTypeCode());
            
            // -See more at: http://www.newthinktank.com/2015/07/learn-c-one-video/#sthash.OvhiSPsr.dpuf


        }
    }
}
