using System;
using System.Collections.Generic;

namespace ContosoUniversity.Models
{
    public class Student
    {
        public int ID { get; set; }
        //can be simply ID or classnameID
        public string LastName { get; set; }
        public string FirstMidName { get; set; }
        public DateTime EnrollmentDate { get; set; }

        public virtual ICollection<Enrollment> Enrollments { get; set; }
        //navigation property, will hold entities related to enrollment. studentID and primary key.
        //virtual to allow for lazy loading and similar EF functionality
    }
}