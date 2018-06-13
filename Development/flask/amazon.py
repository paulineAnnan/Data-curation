import pymysql
class queries:
	def __init__(self,clientId,query,domain,sessionId,createdOn,formatCreatedOn):
		self.clientId = clientId
		self.query = query
		self.domain = domain
		self.sessionId = sessionId
		self.createdOn = createdOn
		self.formatCreatedOn = formatCreatedOn
	

	def save(self):
		queries = {}
		clientId = self.clientId
		query = self.query
		sessionId =self.sessionId	
		domain = self.domain
		createdOn= self.createdOn
		formatCreatedOn = self.formatCreatedOn

		con = None

		try :
			con = pymysql.connect('localhost','root', 'rancard', 'data_curation')
			cur = con.cursor()
			statement = "INSERT INTO queries(clientId,query,domain,sessionId,createdOn,formatCreatedOn) VALUES('"+ clientId +"', '"+ query +"','"+ domain +"', '"+ sessionId +"','"+ str(createdOn) +"','"+ str(formatCreatedOn) +"')"
			print("Insert statement : "+ statement)
			cur.execute(statement)
			con.commit()

			queries['query'] = self.query
			queries['clientId'] = self.clientId
			queries['domain'] = self.domain
			queries['sessionId'] = self.sessionId
			queries['createdOn'] = str(self.createdOn)
			queries['formatCreatedOn'] = str(elf.formatCreatedOn)



		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return queries

	@classmethod
	def get_id(self,clientId):
		return None
		








































