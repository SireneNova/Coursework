// create this class by deriving from the System.Data.Entity.DbContext class. 
// In your code you specify which entities are included in the data model. 
// You can also customize certain Entity Framework behavior. 

using ContosoUniversity.Models;
using System.Data.Entity;
using System.Data.Entity.ModelConfiguration.Conventions;
//added reference to system.data.entity in references, right click
//didn't do anything
//updated target framework version in project-->properties
//didn't help

namespace ContosoUniversity.DAL
{
    public class SchoolContext : DbContext
    {

        public SchoolContext() : base("SchoolContext")
        {
        }
        //constructor

        public DbSet<Student> Students { get; set; }
        public DbSet<Enrollment> Enrollments { get; set; }
        public DbSet<Course> Courses { get; set; }
        //You could have omitted the DbSet<Enrollment> and DbSet<Course> statements and it would work the same. 
        //The Entity Framework would include them implicitly because the Student entity references the Enrollment entity and the Enrollment entity references the Course entity.

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Conventions.Remove<PluralizingTableNameConvention>();
        }
    }
}