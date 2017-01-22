using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeFirstDrill
{
    class Program
    {
        static void Main(string[] args)
        {
            //After making the context below (blogcontext), perform data access using it:
            using (var db = new BlogContext())
            {
                Console.Write("Enter a name for a new blog: ");
                var name = Console.ReadLine();

                //now can create a new instance of the blog class with the name assigned
                var blog = new Blog { Name = name };
                db.Blogs.Add(blog);
                db.SaveChanges();

                //selects new blogs from the db ordered by name:
                var query = from b in db.Blogs
                            orderby b.Name
                            select b;
                //foreach over the results to write out each name to the console:
                foreach (var item in query)
                {
                    Console.WriteLine(item.Name);
                }            
            }
        }
    }

    public class Blog
    {
        //No dependency on entity framework here, plain old clr object:
        public int BlogID { get; set; }
        public string Name { get; set; }

        //"virtual" enables an EF feature  lazy loading, 
        //which means EF queries and populates the contents of these 
        //properties when you try to access them.
        public virtual List<Post> Posts { get; set; }
    }

    public class Post
    {
        public int PostId { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }

        public int BlogId { get; set; }
        public virtual Blog Blog { get; set; }
    }

    //Add entity framework to classes using nuget.
    //Then define derived context, which derived from db context, a base type from EF.
    //Represents a session w the database, and allows to query and save data:
    public class BlogContext : DbContext
    {
        //on context define property that is a dbset for every type in the model.
        //dbset allows to query and save instances of those types.
        public DbSet<Blog> Blogs { get; set; }
        public DbSet<Post> Posts { get; set; }
        
    }

}
