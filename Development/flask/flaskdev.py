import pymysql
from flask import Flask
from flask import Response
from flask import request
from datetime import datetime
from logging.handlers import RotatingFileHandler
import requests as req

import json
from Category import Category 
from Config import Config
from amazon import queries

import logging

app = Flask(__name__)

formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('application.log', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route("/", methods = ['GET'])
def index():
	status = 200
	data = {}
	data['message'] = "Welcome to training data aquisition application."
	jsonData = json.dumps(data)
	return Response(jsonData, status=status, mimetype='application/json')


@app.route('/config', methods = ['GET', 'POST'])
def getAndCreatedConfig():
	status = 200
	data = {}
	if request.method == 'GET':
		print('Hello')

	elif request.method == 'POST':
		config_resUrl = request.args.get('configResourceUrl')
		config_name = request.args.get('configName')
		config_category = request.args.get('categoryId')
		config = Config(config_resUrl, config_name, config_category, datetime.now())
		config_data = config.save()
		data['message'] = ""
		data['data'] = config_data

	jsonData = json.dumps(data)
	return Response(jsonData, status=status, mimetype='application/json')

@app.route("/config/<id>", methods = ['PUT', 'DELETE'])
def updateOrDeleteConfig(id):
	status = 200
    
    

	return Response()

@app.route("/category", methods = ['GET', 'POST'])
def getAndCreatedCategory():
	status = 200
	data = None
	print("Request parameters passed : "+ str(request.args))
	if request.method == 'GET':
		print("get triggered")
	elif request.method == 'POST':
		category_name = request.args.get('categoryName')
		category = Category(category_name, datetime.now())
		category.save()
		print('Yay')

	json_data = json.dumps(data)
	
	return Response(json_data, status = 200, mimetype='application/json')

@app.route("/configuration",methods = ["GET"])
def getQueries():
	status = 200
	data = None
	indQueryList = []
	if request.method == 'GET':
		config_id = request.args.get("configId")
		con = None

		try :
			con = pymysql.connect('localhost','root', 'rancard', 'data_curation')

			cur =con.cursor()
			cur.execute(" SELECT resUrl FROM Config WHERE  id = " + config_id + "")

			resUrlTuple= cur.fetchone()
			resUrlString = resUrlTuple[0]

			result = req.get(resUrlString)
			resultDict = result.json()
			queriesList = resultDict.get("queries")
			for elementIndex in range(len(queriesList)):
				indQuery = queriesList[elementIndex].get('query')
				indQueryList.append(indQuery)
			indQuerySet = set(indQueryList)
			print(indQuerySet)
				#indQuery.replace("'","\'")
				#indQuerySet.add(indQuery)
			for element in indQuerySet:	
				statement = """INSERT INTO DataStore(ConfigId,Query) VALUES (""" + config_id + """, \"""" + element + """\")"""
				print(statement)
				cur.execute(statement)
				con.commit()

			#while row is not None:
			#	print(type(row))
			#	print(row)
			#	row = cur.fetchone()

		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
	
	return "done"
 

@app.route("/category/<category_id>", methods = ['PUT', 'DELETE'])
def updateAnddeleteCategory(category_id):
	if request.method =='PUT':
		status = 200
		print("updated")

	elif request.method == 'DELETE':
		status = 200
		print("")
		return Response()

sandbox = "http://sandbox.rancardmobility.com:9092/3rd-provider-integration/v1/request/queries?domain=amazon.com"

@app.route("/queries", methods=['GET'])
def getResource(resourceProvider):
	if request.method == 'GET':
		status = 200
		jsonData = req.get(resourceProvider)
		print(type(jsonData))
		queries = jsonData['queries']
	for query in queries:
			query = amazon()
			query.save()
	return Response(jsonData, status = 200, mimetype='application/json')
	
	if __name__ == '__main__':
		app.run()