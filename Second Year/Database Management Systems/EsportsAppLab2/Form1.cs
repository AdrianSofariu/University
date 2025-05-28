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

        string parentTable;
        string childTable;
        string relationName;

        string parentQuery;
        string childQuery;

        string parentPK;
        string childFK;

        public Form1()
        {
            InitializeComponent();
            fillData();
        }

        void fillData()
        {
            //connection
            connection = new SqlConnection(getConnectionString());

            this.parentTable = ConfigurationManager.AppSettings["parentTable"];
            this.childTable = ConfigurationManager.AppSettings["childTable"];
            this.relationName = ConfigurationManager.AppSettings["relationship"];

            this.parentQuery = ConfigurationManager.AppSettings["parentSelect"];
            this.childQuery = ConfigurationManager.AppSettings["childSelect"];

            this.parentPK = ConfigurationManager.AppSettings["parentPK"];
            this.childFK = ConfigurationManager.AppSettings["childFK"];

            //SqlAdapters
            table1Adapter = new SqlDataAdapter(parentQuery, connection);
            table2Adapter = new SqlDataAdapter(childQuery, connection);
            dataset = new DataSet();
            table1Adapter.Fill(dataset, parentTable);
            table2Adapter.Fill(dataset, childTable);

            //insert, update, deletes commands for table2
            cmdBuider = new SqlCommandBuilder(table2Adapter);

            //add parent child relation
            dataset.Relations.Add(relationName, dataset.Tables[parentTable].Columns[parentPK], dataset.Tables[childTable].Columns[childFK]);

            //bind data to grid
            table1Bs = new BindingSource();
            table1Bs.DataSource = dataset.Tables[parentTable];
            table2Bs = new BindingSource(table1Bs, relationName);

            dataGridView1.DataSource = table1Bs;
            dataGridView2.DataSource = table2Bs;
        }

        string getConnectionString()
        {
            return ConfigurationManager.ConnectionStrings["connection"].ConnectionString;
        }

        private void refresh()
        {
            //select all data from table Teams into the adapter
            table2Adapter.SelectCommand = new SqlCommand(childQuery, connection);
            dataset.Tables[childTable].Clear();
            table2Adapter.Fill(dataset, childTable);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                table2Adapter.Update(dataset, childTable);
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
