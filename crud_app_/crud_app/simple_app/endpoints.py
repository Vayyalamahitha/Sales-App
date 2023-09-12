import logging

from flask_pymongo import pymongo
from flask import jsonify, request
import pandas as pd
import json
from simple_app.ml import process
from flask import jsonify

l=[]
def project_api_routes(endpoints):
    
    @endpoints.route('/file_upload',methods=['POST'])
    def file_upload():
        try:
            file = request.files.get('file')
            df = pd.read_csv(file)
            global l
            l=process(df)
            status = {
                "statusCode":"200",
                "statusMessage":"File uploaded Successfully.",
                "res": "hello"
            }
        except Exception as e:
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        return status

    @endpoints.route('/get_data',methods=['GET'])
    def get_data():
        return l
    
    return endpoints