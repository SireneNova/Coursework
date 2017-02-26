
###Code First Drill
CodeFirstDrill is a file that creates and modifies a Code First database using Entity Framework (EF) in Visual Studio. It was made 
by following a Microsoft tutorial by Rowen Miller: https://msdn.microsoft.com/en-us/data/jj193542.aspx. 

####Objective: 
* Write an application that performs data access using Entity Framework Code First.

####Steps Taken:
* Rowen used Visual Studio 2012. I used Visual Studio 2015, and it was very similar. A key difference I discovered, was that I had to download SQL Server Data Tools to get the same database-viewing options. The version used in the tutorial evidently came with this capability built-in.
* Wrote plain classes of blogs and posts in C#. Blogs can have many posts. These classes, domain classes, have no dependency on EF, but will later translate into sections of the database after EF is used.
* **Added Properties to classes**:
  * Added scale-up properties such as name and ID.
  * Added navigation properties, which defined the relationships between classes (blog.post and post.blog)
  * The "virtual" keyword was used in front of navigation properties to enable lazy loading, a feature of EF which allows it to automatically query and populate the contents of these properties when they are accessed.
* **Added Entity Framework** to the project using the NuGet package.
* **Created a context**:
   * A context, BlogContext, could then be defined, derived from the DBContext, a base type in Entity Framework. A context represents a session with the database, which allows for querying and selecting data.
   * In the context, defined a property that is a DBSet for every type in model. DBSets allow for querying and saving instances of the types.
* **Accessed, queried, and displayed the data using the context**: 
   * The context was wrapped in a "using" statement.
   * A blog was defined with a name to be entered in by a user from the console.
   * Created a LINQ query that selects all blogs from the database ordered by name.
   * Displayed the name of each blog to the console with a loop function.
* **Ran the program**, entered a blog name, and observed that the program worked.
* Opened localDB in the SQL Server Object Explorer and **observed the database schema that Code First had created**:
   * Code first had created a database based on the way it conventionally reads the code in the program.
* **Used Code First Migrations** to make changes to the database schema:
   * Opened the Packages Manager (PM) Console and ran "Enable-Migrations" command, which enabled code-first migrations for the blog context.
   * The command added a configurations file with migrations settings.
   * The command also added an InitialCreate migration, which represents the first change already made to the database (creating the blog and post table).
   * Changed the domain model by adding a property. Added a URL property to the blog class.
   * Ran Add-Migration command to scaffold the changes into a new migration. Named it "AddURL". Full entry: "Add-Migration AddURL".
   * Applied changes to database by running "Update-Database".
* **Overrode Code First conventions** using data annotations and fluent api.
   * Data annotations:
     * Added a property with an unconventional name, "Username", instead of "UserID", a format Code First expects.
     * Added "[Key]" data annotation to the username property so that the unconventional name could be used.
     * Ran "Add-Migration AddUser" and then "Update-Database" in PM Console.
     * Observed that the new Username table was successfully added to the database.
   * Fluent API:
     * Changed the conventional naming of a column, "DisplayName", by overriding the OnModelCreating method inside the derived context, setting the name to "display_name".
     * Added migration and applied changes.
     * Observed that the new name was changed in the database.

####Results
I learned about how Entity Framework Code First works and was reminded of what Entity Framework is and why it is useful. I remembered that Entity Framework can also be used to create classes and databases DB First and Model First. 

The tutorial showed me: 
* how to create a Code First model
* how to create a database from that model
* how to change the database using Code First Migrations as the model changes
* how to override code first defaults using Data Annotations and Fluent API

I saw how a database structure was generated from a class structure and portrayed within the Visual Studio SQL Server Object Explorer. I also noticed that the data itself was not portrayed.

I discovered I needed SQL Server Data Tools add-on for Visual Studio to view the SQL Server Object Explorer, so I learned how that works and how Visual Studio accesses servers. Edit: When I first installed SSDT in 2016, the toolset was an add-on. Most recently Visual Studio with SSDT appears to be a separate application. 
