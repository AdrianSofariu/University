using System;
using System.Data;
using MySql.Data.MySqlClient;
using multimedia_app_asp.Models;

namespace multimedia_app_asp.Services.DAL
{
    public class UserRepository
    {
        private readonly DbManager _dbManager;

        public UserRepository(DbManager dbManager)
        {
            _dbManager = dbManager;
        }

        public User? GetByUsername(string username)
        {
            try
            {
                using var conn = _dbManager.GetConnection();
                conn.Open();

                using var cmd = new MySqlCommand("SELECT * FROM users WHERE username = @username", conn);
                cmd.Parameters.AddWithValue("@username", username);

                using var reader = cmd.ExecuteReader();
                if (reader.Read())
                {
                    return new User
                    {
                        Id = reader.GetInt32("id"),
                        Username = reader.GetString("username"),
                        PasswordHash = reader.GetString("password_hash")
                    };
                }
                return null;
            }
            catch (MySqlException ex)
            {
                throw new Exception("Database error while fetching user by username.", ex);
            }
            catch (Exception ex)
            {
                throw new Exception("Unexpected error while fetching user by username.", ex);
            }
        }

        public void AddUser(User user)
        {
            try
            {
                using var conn = _dbManager.GetConnection();
                conn.Open();

                string query = "INSERT INTO users (username, password_hash) VALUES (@username, @password_hash)";
                var parameters = new MySqlParameter[]
                {
                    new MySqlParameter("@username", user.Username),
                    new MySqlParameter("@password_hash", user.PasswordHash)
                };

                _dbManager.ExecuteNonQuery(query, parameters);
            }
            catch (MySqlException ex)
            {
                throw new Exception("Database error while adding a new user.", ex);
            }
            catch (Exception ex)
            {
                throw new Exception("Unexpected error while adding a new user.", ex);
            }
        }
    }
}
