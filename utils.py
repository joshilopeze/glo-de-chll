from databricks import *
from pyspark.sql import DataFrame

def write_to_sql(df: DataFrame, table_name: str, jdbc_url: str, connection_properties: dict, mode: str = "append"):
    """
    Escribe un DataFrame a una tabla SQL usando JDBC.
    
    Parámetros:
    df: DataFrame a escribir.
    table_name: Nombre de la tabla a la que se escribirá.
    jdbc_url: URL de conexión JDBC a la base de datos.
    connection_properties: Propiedades de la conexión (usuario, driver, etc.).
    mode: Modo de escritura (por defecto "append").
    """
    df.write.jdbc(url=jdbc_url, table=table_name, mode=mode, properties=connection_properties)
    print(f"Datos escritos en la tabla {table_name} exitosamente.")


# Conexión JDBC
jdbc_url = "jdbc:sqlserver://db-sql-db.database.windows.net:1433;databaseName=db-de-v2;user=adminsql;password=password123.;encrypt=true;trustServerCertificate=false"

# Configura las propiedades de conexión
connection_properties = {
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}
