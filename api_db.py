
table = dbutils.widgets.get("table")
data = json.loads(dbutils.widgets.get("data"))


jdbc_url = "jdbc:sqlserver://db-sql-db.database.windows.net:1433;databaseName=db-de-v2;user=adminsql;password=password123.;encrypt=true;trustServerCertificate=false"
connection_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

df = spark.read.json(spark.sparkContext.parallelize([json.dumps(data)]))


df.write.jdbc(url=jdbc_url, table=table, mode="append", properties=connection_properties)

dbutils.notebook.exit("Data inserted correctly")
