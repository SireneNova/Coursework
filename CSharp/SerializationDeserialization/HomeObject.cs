using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SerializingDemo
{
    [Serializable]
    class HomeObject
    {
        int yearBuilt = 0;
        public enum TYPE { SINGLE_FAMILY, TOWN_HOME, CONDO };
        TYPE htype;

        public HomeObject()
        {
        }

        public void setYear(int year)
        {
            yearBuilt = year;
        }

        public int getYear()
        {
            return yearBuilt;
        }

        public TYPE getHomeType()
        {
            return htype;
        }

        public void setHomeType(TYPE type_)
        {
            htype = type_;
        }

        public string printContent()
        {
            string msg = "HomeType: " + htype + "Year Built: " + yearBuilt;
            return msg;
        }
    }
}
