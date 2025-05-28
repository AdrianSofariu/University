using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Web;
using System.Configuration;

namespace EsportsApp
{
    public partial class Form1: Form
    {
        SqlConnection connection;
        SqlDataAdapter table1Adapter;
        SqlDataAdapter table2Adapter;
        DataSet dataset;
        BindingSource table1Bs;
        BindingSource table2Bs;

        SqlCommandBuilder cmdBuider;

        string table1Query;
        string table2Query;

        public Form1()
        {
            InitializeComponent();
            fillData();
        }

        void fillData()
        {
            //connection
            connection = new SqlConnection(getConnectionString());

            this.table1Query = "SELECT * from Leagues";
            this.table2Query = "SELECT * from Teams";

            //SqlAdapters
            table1Adapter = new SqlDataAdapter(table1Query, connection);
            table2Adapter = new SqlDataAdapter(table2Query, connection);
            dataset = new DataSet();
            table1Adapter.Fill(dataset, "Leagues");
            table2Adapter.Fill(dataset, "Teams");

            //insert, update, deletes commands for table2
            cmdBuider = new SqlCommandBuilder(table2Adapter);

            //add parent child relation
            dataset.Relations.Add("Leagues_Teams", dataset.Tables["Leagues"].Columns["leagueId"], dataset.Tables["Teams"].Columns["leagueId"]);

            //bind data to grid
            table1Bs = new BindingSource();
            table1Bs.DataSource = dataset.Tables["Leagues"];
            table2Bs = new BindingSource(table1Bs, "Leagues_Teams");

            dataGridView1.DataSource = table1Bs;
            dataGridView2.DataSource = table2Bs;
        }

        string getConnectionString()
        {
            return "Data Source=DESKTOP-K35UU70;Initial Catalog=ESports;Integrated Security=True";
        }

        private void refresh()
        {
            //select all data from table Teams into the adapter
            table2Adapter.SelectCommand = new SqlCommand(table2Query, connection);
            dataset.Tables["Teams"].Clear();
            table2Adapter.Fill(dataset, "Teams");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                table2Adapter.Update(dataset, "Teams");
                refresh();

            }
            catch (Exception ex )
            {
                MessageBox.Show(ex.Message);
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
