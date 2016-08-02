###C# Coursework
Each of the files and folders above is described in the sections below.

####Tutorial Series
Each folder contains files from a tutorial series. More detailed descriptions can be found within each.
* Banas Tutorial contains files from following a C# video tutorial.
* LINQtutorial contains files from following a LINQ tutorial.
* SerializationDeserialization contains files from following a tutorial on serialization and deserialization in C#.


####Code First Drill
CodeFirstDrill is a file that creates and modifies a Code First database using Entity Framework in Visual Studio. It was made 
by following a Microsoft tutorial by Rowen Miller: https://msdn.microsoft.com/en-us/data/jj193542.aspx. </br></br>
Objective: 
* Write an application that performs data access using Entity Framework Code First.</br></br>

Steps Taken:</br>
* Rowen used Visual Studio 2012. I used Visual Studio 2015, and it was very similar. A key difference I discovered,
was that I had to download SQL Server Data Tools to get the same database-viewing options. 
The version used in the tutorial evidently came with this capability built-in.
* Classes of blogs and posts were written in C#. These classes will later translate into sections of the database.
* Using the "virtual" keyword in front of navigation properties enables lazy loading, which will allow SQL to automatically query and populate these properties when they are accessed.
* Entity Framework was added to the project using the NuGet package.
* Derived contexts could then be defined.

(To be continued)
