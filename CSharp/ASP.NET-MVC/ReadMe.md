###ASP.Net MVC Application in C# - The Contoso University
___

####Objective
Create an ASP.NET MVC 5 web application for a fictional university using Entity Framework 6 and Visual Studio. 
https://www.asp.net/mvc/overview/getting-started/getting-started-with-ef-using-mvc/creating-an-entity-framework-data-model-for-an-asp-net-mvc-application

####Steps Taken
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
* Created student, enrollment, and course data models as classes in the Models folder. These will serve as entity classes, which define tables in the data model. 
* 
* Prevented table names from being pluralized

DAL FOLDER
* Created the DAL (Data Access Layer) folder.
* In this folder, created a database context class, the main class that coordinates EF functionality for a given data model. Here it is named SchoolContext.cs.

WROTE DATABASE
* Used Entity Framework to write a database and populate it with test data. 
  - This is done using the Seed method in initializer class to automatically populate
  - This is dropped and re-created whenever the model changes
* Initializer class is referenced in web.config to be used

LOCALDB
* Set up EF to use LocalDB (lightweight express) by editing web.config

CREATE WEB PAGE
Now you'll create a web page to display data, and the process of requesting the data will automatically 
trigger the creation of the database. 
You'll begin by creating a new controller. But before you do that, build the project to make the model and 
context classes available to MVC controller scaffolding.
When you click Add, the scaffolder creates a StudentController.cs file and a set of views (.cshtml files)
that work with the controller. 


Visual Studio opens the Controllers\StudentController.cs file. You see a class variable has been created that instantiates a database context object:


The Index action method gets a list of students from the Students entity set by reading the Students property of the database context instance:
The Student\Index.cshtml view displays this list in a table:


Added a student controller with views automatically by adding a scaffold item
-this creates a web page that displays data?
-the class variable is found in the Controllers\StudentControllers.cs file. The Index method in the file gets a list of students from the Students entity set by reading the Students property of the database context instance

####Results
