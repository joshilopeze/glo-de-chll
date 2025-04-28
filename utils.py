from databricks import *
from pyspark.sql import DataFrame

def write_to_sql(df: DataFrame, table_name: str, jdbc_url: str, connection_properties: dict, mode: str = "append"):

    df.write.jdbc(url=jdbc_url, table=table_name, mode=mode, properties=connection_properties)
    print(f"Data correctly written to {table_name} .")


# JDBC connection
jdbc_url = "jdbc:sqlserver://db-sql-db.database.windows.net:1433;databaseName=db-de-v2;user=adminsql;password=password123.;encrypt=true;trustServerCertificate=false"

# configure the connection properties
connection_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}
