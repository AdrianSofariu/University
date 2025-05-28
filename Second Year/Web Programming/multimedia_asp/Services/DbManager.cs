using System.Data;
using MySql.Data.MySqlClient;
using Microsoft.Extensions.Configuration;

namespace multimedia_app_asp.Services
{
    public class DbManager
    {
        private readonly string _connectionString;

        public DbManager(IConfiguration configuration)
        {
            _connectionString = configuration.GetConnectionString("MySqlConnection");
        }

        public MySqlConnection GetConnection()
        {
            var conn = new MySqlConnection(_connectionString);
            return conn;
        }

        public DataTable ExecuteQuery(string query, params MySqlParameter[] parameters)
        {
            using var conn = GetConnection();
            conn.Open();
            using var cmd = new MySqlCommand(query, conn);
            cmd.Parameters.AddRange(parameters);
            using var adapter = new MySqlDataAdapter(cmd);
            var table = new DataTable();
            adapter.Fill(table);
            conn.Close();
            return table;
        }

        public int ExecuteNonQuery(string query, params MySqlParameter[] parameters)
        {
            using var conn = GetConnection();
            conn.Open();
            using var cmd = new MySqlCommand(query, conn);
            cmd.Parameters.AddRange(parameters);
            int res = cmd.ExecuteNonQuery();
            conn.Close();
            return res;
        }
    }
}
