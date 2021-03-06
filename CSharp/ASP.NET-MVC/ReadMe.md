### ASP.Net MVC Application in C# - The Contoso University
___

#### Objective
Create an ASP.NET MVC web application for a fictional university using Entity Framework and Visual Studio. Tutorial from MSDN:
https://www.asp.net/mvc/overview/getting-started/getting-started-with-ef-using-mvc/creating-an-entity-framework-data-model-for-an-asp-net-mvc-application

#### Steps Taken
Followed the steps oulined in the link above, summarized below:

**Created Web Project**
* In Visual Studio, a C# an asp.net web application. 
* Changed to authentication settings to have no authentication.

**Set up site style by editing VIEWS folder**
* In Views\Shared\_Layout.cshtml:
  * Changed each occurrence of "My ASP.NET Application" and "Application name" to "Contoso University".
  * Added menu entries for Students, Courses, etc in an unordered list so they would appear in a collapsible navigation bar.
* In Views\Home\Index.cshtml:
  * Swapped the html so that the home page will now display information about Contoso University rather than ASP.Net.
* Viewed site by pressing ctrl f5.

**Installed Entity Framework**
* Opened NuGet package manager in Tools.
* Opened Package Manager Console and Ran "Install-Package EntityFramework" command. 

**Created the Data Model by editing MODELS folder**
* Created student, enrollment, and course data models as classes in separate cs files in the Models folder. These will serve as entity classes, which define tables in the data model.
  * The classes contain scale-up properties such as Name and ID, which will correspond to columns in a table. Example: `public int ID { get; set; }`
  * Courses and Students can have any number of Enrollments. These relationships between the classes/entities are defined by navigation properties. They contain a "virtual" keyword to enable lazy loading, a feature of EF which allows it to automatically query and populate the contents of these properties when they are accessed. Example: `public virtual ICollection<Enrollment> Enrollments { get; set; }` 
  * In the Enrollment class an enumerable, Grade, was used to define the attribute for the Grade property.
  * The Course class contained a DatabaseGenerated attribute, which allows for entering a primary key rather than have one be generated by the database automatically.

**Created the Database Context in the DAL folder**
* Created the DAL (Data Access Layer) folder in the Project Folder (ContosoUniversity) in the Solution Explorer.
* In this folder, created a database context class, the main class that coordinates EF functionality for a given data model. It allows for querying and selecting data. Here it is named SchoolContext.cs.
* Placed code in the file with DBSets class in the model eg: `public DbSet<Student> Students { get; set; }`. Entity sets correspond to tables and entities correspond to rows in tables.
* The connection string was explicitly stated even though it didn't need to be: `public SchoolContext() : base("SchoolContext")
{
}` This connects to the Web.config file and takes the name of the class file by default.
* Prevented table names from being pluralized with the "modelBuilder.Conventions.Remove" statement in the OnModelCreating method. 

**Set up EF to Write the Database** (DAL folder)
* Used Entity Framework to initialize a database and populate it with test data (student names etc). 
  * Made a an initializer class, SchoolInitializer.cs, in the DAL folder.
  * Used the Seed method in the class to automatically populate the db by matching with the correct DBSet.
  * This is dropped and re-created whenever the model changes.
* Initializer class is referenced in web.config in order to be used.

**Set up EF to use LocalDB** by editing web.config, a project file
* Added a connection string specifying to use MSSQLLocalDB (for Visual Studio 2015).

**Created Student Controller and Views** to create web page that displays data on students
* Controllers folder:
  * Added New Scaffold Item by right clicking folder.
  * Selected MVC 5 Controller with views (.cshtml files), using Entity Framework. 
  * Added controller and specified settings in the next dialogue box.
  * The scaffolder created a StudentController.cs file and views to go with it.
  * Observed the elements of the controller file: 
     * A class variable has been created that instantiates a database context object.
     * The Index action method gets a list of students from the Students entity set.
   * The Student\Index.cshtml view displays the list in a table.

**Viewed the Database**
* Opened the server explorer by going to Tools, Connect to Database, and cancelling. Edit: SQL Server Data Tools is now its own separate application of Visual Studio 2015. The server explorer and database shows up right away. 
* Right-clicked on a table to view the data.
* Navigated to the student section of the web application.


#### Results
An MVC web application with ASP.NET and Entity Framework has a lot of interconnected components, and I have a better understanding of how they work together and why. I didn't run into any issues unless I made a mistake (I lost connection during the first Entity Framework install, and it didn't install). A controller and views were only created for the student data table, so only this table's data was able to be viewed on a web page. I may try to add controllers and views for the other tables later.
