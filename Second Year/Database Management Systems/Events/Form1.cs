using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MiniFacebook
{
    public partial class Form1 : Form
    {

        SqlConnection connection;
        SqlDataAdapter categoriesAdapter;
        SqlDataAdapter eventsAdapter;
        DataSet dataset;
        BindingSource categoriesBs;
        BindingSource eventsBs;
        SqlCommandBuilder cmdBuilder;

        string categoriesQuery;
        string eventsQuery;

        public Form1()
        {
            InitializeComponent();
            fillData();
        }

        private string getConnectionString()
        {
            return "Data Source=DESKTOP-K35UU70;Initial Catalog=EventsDB;Integrated Security=True";
        }

        private void fillData()
        {
            // Intialize connection
            connection = new SqlConnection(getConnectionString());

            // Define queries
            categoriesQuery = "SELECT * FROM Categories";
            eventsQuery = "SELECT * FROM CulturalEvents";

            // Initialize SqlDataAdapters
            categoriesAdapter = new SqlDataAdapter(categoriesQuery, connection);
            eventsAdapter = new SqlDataAdapter(eventsQuery, connection);
            dataset = new DataSet();
            categoriesAdapter.Fill(dataset, "Categories");
            eventsAdapter.Fill(dataset, "CulturalEvents");

            // Create command builder for Adapter
            cmdBuilder = new SqlCommandBuilder(eventsAdapter);

            // Add parent-child relation
            dataset.Relations.Add("Categories_Events", dataset.Tables["Categories"].Columns["CatId"], dataset.Tables["CulturalEvents"].Columns["CatId"]);

            // Bind data to BindingSources
            categoriesBs = new BindingSource();
            categoriesBs.DataSource = dataset.Tables["Categories"];
            eventsBs = new BindingSource(categoriesBs, "Categories_Events");

            dgvCategories.DataSource = categoriesBs;
            dgvCulturalEvents.DataSource = eventsBs;
        }

        private void refresh()
        {
            eventsAdapter.SelectCommand = new SqlCommand(eventsQuery, connection);
            dataset.Tables["CulturalEvents"].Clear();
            eventsAdapter.Fill(dataset, "CulturalEvents");
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                // Update the database with changes made in the DataSet
                eventsAdapter.Update(dataset, "CulturalEvents");
                refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error saving changes: " + ex.Message);

            }
        }

        private void Form1_Closed(object sender, FormClosedEventArgs e)
        {
            // Dispose of the connection when the form is closed
            if (connection != null && connection.State == ConnectionState.Open)
            {
                connection.Close();
                connection.Dispose();
            }
        }
    }
}
