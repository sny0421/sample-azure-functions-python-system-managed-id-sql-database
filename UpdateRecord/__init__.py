import azure.functions as func
import logging
import os
import pyodbc
import requests
import struct
import sys
from ..shared_code import sql_database_connect as sdc
 
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Start function: UpdateRecord')

    try:
        db_id = req.params.get('id')
        name = req.params.get('name')
    except:
        return func.HttpResponse(
            "Please put a valid parameters in the request",
            status_code=400
        )
    
    try:
        # Get access token
        token_struct = sdc.get_sql_access
        # Load environment variables
        driver = os.environ['SQL_DRIVER']
        sql_server = os.environ['SQL_SERVER']
        sql_database = os.environ['SQL_DATABASE']
        # Connect SQL Database
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+sql_server+';PORT=1433;DATABASE='+sql_database+';', attrs_before = { 1256:bytearray(token_struct) })
        logging.info('connected to {} on {}'.format(sql_server,sql_database))
        cursor = conn.cursor()
        # Execute SQL query
        cursor.execute("UPDATE test SET name = ? WHERE id = ?", name, db_id)
        cursor.commit()
        logging.info('finished')
    except BaseException as error:
        logging.info('An exception occurred: {}'.format(error))
        return func.HttpResponse(
            'An exception occurred: {}'.format(error),
            status_code=200
        )
    return func.HttpResponse(
        "UserID {} updated.".format(db_id),
        status_code=200
    )
