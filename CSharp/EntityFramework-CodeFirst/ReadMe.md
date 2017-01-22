
###Code First Drill
CodeFirstDrill is a file that creates and modifies a Code First database using Entity Framework (EF) in Visual Studio. It was made 
by following a Microsoft tutorial by Rowen Miller: https://msdn.microsoft.com/en-us/data/jj193542.aspx. 

####Objective: 
* Write an application that performs data access using Entity Framework Code First.

####Steps Taken:
* Rowen used Visual Studio 2012. I used Visual Studio 2015, and it was very similar. A key difference I discovered, was that I had to download SQL Server Data Tools to get the same database-viewing options. The version used in the tutorial evidently came with this capability built-in.
* Wrote plain classes of blogs and posts in C#. Blogs can have many posts. These classes, domain classes, have no dependency on EF, but will later translate into sections of the database after EF is used.
* Added Properties to classes:
  * Added scale-up properties such as name and ID.
  * Added navigation properties, which defined the relationships between classes (blog.post and post.blog)
  * The "virtual" keyword was used in front of navigation properties to enable lazy loading, which allows SQL to automatically query and populate these properties when they are accessed.
* Added Entity Framework to the project using the NuGet package.
* Created a context:
   * A context, BlogContext, could then be defined, derived from the DBContext, a base type in Entity Framework. A context represents a session with the database, which allows for querying and selecting data.
   * In the context, define a property that is a DBSet for every type in model. DBSets allow for querying and saving instances of the types.
* Accessed, queried, and displayed the data using the context: 
   * The context was wrapped in a "using" statement.
   * A blog was defined with a name to be entered in by a user from the console.
   * Created a LINQ query that selects all blogs from the database ordered by name.
   * Displayed the name of each blog to the console with a loop function.
