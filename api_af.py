import azure.functions as func
import json
import requests

# Configuración de la API de Databricks
DATABRICKS_URL = "https://adb-2509319697722617.17.azuredatabricks.net/api/2.0/jobs/run-appi"
DATABRICKS_TOKEN = ###

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:

        req_body = req.get_json()
        table = req_body.get("table")
        data = req_body.get("data")


        if table not in ["hired_employees", "departments", "jobs"]:
            return func.HttpResponse("Tabla inválida", status_code=400)
        
   
        if not data or len(data) > 1000:
            return func.HttpResponse("Longitud de datos inválida", status_code=400)


        payload = {
            "notebook_params": {
                "table": table,
                "data": json.dumps(data) 
            }
        }
        

        headers = {
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
            "Content-Type": "application/json"
        }
        

        response = requests.post(DATABRICKS_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return func.HttpResponse("Job de Databricks ejecutado correctamente", status_code=200)
        else:
            return func.HttpResponse(f"Error al ejecutar el Job en Databricks: {response.text}", status_code=500)

    except Exception as e:
        return func.HttpResponse(f"Error al procesar la solicitud: {str(e)}", status_code=500)
