namespace multimedia_app_asp.Models
{
    public class MultimediaFile
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Format { get; set; }
        public string Genre { get; set; }
        public string Path { get; set; }
        public int UserId { get; set; } // Foreign key to User table
    }
}
