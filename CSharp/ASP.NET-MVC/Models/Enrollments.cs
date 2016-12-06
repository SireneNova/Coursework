namespace ContosoUniversity.Models
{
    public enum Grade
    {
        A, B, C, D, F
    }

    public class Enrollment
    {
        public int EnrollmentID { get; set; }
        //classnameID
        public int CourseID { get; set; }
        //foreign key
        public int StudentID { get; set; }
        //foreign key
        public Grade? Grade { get; set; }
        //enum
        //? means it is nullable
        public virtual Course Course { get; set; }
        public virtual Student Student { get; set; }
    }
}