using multimedia_app_asp.Models;
using MySql.Data.MySqlClient;
using System.Data;
using System.IO;

namespace multimedia_app_asp.Services.DAL
{
    public class FileRepository
    {
        private readonly DbManager _dbManager;

        public FileRepository(DbManager dbManager)
        {
            _dbManager = dbManager;
        }

        public List<MultimediaFile> GetAll(int userId)
        {
            try
            {
                string query = "SELECT * FROM multimedia_files WHERE user_id = @userId";
                var parameters = new MySqlParameter[]
                {
                    new MySqlParameter("@userId", userId)
                };
                var table = _dbManager.ExecuteQuery(query, parameters);
                var files = new List<MultimediaFile>();

                foreach (DataRow row in table.Rows)
                {
                    files.Add(new MultimediaFile
                    {
                        Id = Convert.ToInt32(row["id"]),
                        Title = row["title"].ToString(),
                        Format = row["format"].ToString(),
                        Genre = row["genre"].ToString(),
                        Path = row["path"].ToString(),
                        UserId = Convert.ToInt32(row["user_id"])
                    });
                }

                return files;
            }
            catch (Exception ex)
            {
                throw new Exception("Error retrieving multimedia files.", ex);
            }

        }

        public MultimediaFile? GetById(int id)
        {
            try
            {
                var table = _dbManager.ExecuteQuery("SELECT * FROM multimedia_files WHERE id = @id",
                    new MySqlParameter("@id", id));

                if (table.Rows.Count == 0)
                    return null;

                var row = table.Rows[0];

                return new MultimediaFile
                {
                    Id = Convert.ToInt32(row["id"]),
                    Title = row["title"].ToString(),
                    Format = row["format"].ToString(),
                    Genre = row["genre"].ToString(),
                    Path = row["path"].ToString(),
                    UserId = Convert.ToInt32(row["user_id"])
                };
            }
            catch (Exception ex)
            {
                throw new Exception($"Error retrieving multimedia file with id={id}.", ex);
            }
        }

        public bool Delete(int id)
        {
            try
            {
                int affected = _dbManager.ExecuteNonQuery("DELETE FROM multimedia_files WHERE id = @id",
                    new MySqlParameter("@id", id));
                return affected > 0;
            }
            catch (Exception ex)
            {
                throw new Exception($"Error deleting multimedia file with id={id}.", ex);
            }
        }

        public bool Update(MultimediaFile file)
        {
            try
            {
                int affected = _dbManager.ExecuteNonQuery(@"
                    UPDATE multimedia_files
                    SET title = @title, format = @format, genre = @genre, path = @path
                    WHERE id = @id",
                    new MySqlParameter("@title", file.Title),
                    new MySqlParameter("@format", file.Format),
                    new MySqlParameter("@genre", file.Genre),
                    new MySqlParameter("@path", file.Path),
                    new MySqlParameter("@id", file.Id));
                return affected > 0;
            }
            catch (Exception ex)
            {
                throw new Exception($"Error updating multimedia file with id={file.Id}.", ex);
            }
        }

        public bool Insert(MultimediaFile file, int userId)
        {
            try
            {
                int affected = _dbManager.ExecuteNonQuery(@"
                    INSERT INTO multimedia_files (title, format, genre, path, user_id)
                    VALUES (@title, @format, @genre, @path, @userId)",
                    new MySqlParameter("@title", file.Title),
                    new MySqlParameter("@format", file.Format),
                    new MySqlParameter("@genre", file.Genre),
                    new MySqlParameter("@path", file.Path),
                    new MySqlParameter("@userId", userId));

                return affected > 0;
            }
            catch (Exception ex)
            {
                throw new Exception("Error inserting new multimedia file.", ex);
            }
        }

        public List<string> GetGenres()
        {
            try
            {
                var genres = new List<string>();
                var table = _dbManager.ExecuteQuery("SELECT DISTINCT genre FROM multimedia_files");

                foreach (DataRow row in table.Rows)
                    genres.Add(row["genre"].ToString()!);

                return genres;
            }
            catch (Exception ex)
            {
                throw new Exception("Error retrieving genres.", ex);
            }
        }
    }
}
