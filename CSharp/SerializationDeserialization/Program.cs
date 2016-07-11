using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SerializingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            SerializeData sdata = new SerializeData("testBinaryFile.txt");

            HomeObject home = new HomeObject();
            home.setHomeType(HomeObject.TYPE.CONDO);
            home.setYear(2000);

            ComputerObject co = new ComputerObject();
            co.setType(ComputerObject.PC_TYPE.LINUX);
            co.setCost(0.0);

            ComputerObject co1 = new ComputerObject();
            co1.setType(ComputerObject.PC_TYPE.WINDOWS);
            co1.setCost(100.0);

            sdata.SerializeObject(home);
            sdata.SerializeObject(co);
            sdata.SerializeObject(co1);

            sdata.closeStream();

            sdata.DeserializeObjects();
            sdata.closeStream();
         }
    }
}
