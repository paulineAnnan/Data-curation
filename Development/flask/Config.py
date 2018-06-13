import pymysql
class Config:
	def __init__(self,resUrl,name,category,createdOn):
		self.resUrl = resUrl
		self.name = name
		self.category = category
		self.createdOn = createdOn
	

	def save(self):
		config = {}
		name = self.name
		createdOn =self.createdOn	
		resUrl = self.resUrl
		category = self.category

		con = None

		try :
			con = pymysql.connect('localhost','root', 'rancard', 'data_curation')
			cur = con.cursor()
			statement = "INSERT INTO Config(resUrl,domainName,categoryId,createdOn) VALUES('"+ resUrl +"', '"+ name +"','"+ category +"', '"+ str(createdOn) +"')"
			print("Insert statement : "+ statement)
			cur.execute(statement)
			con.commit()

			config['domainName'] = self.name
			config['resourceUrl'] = self.resUrl
			config['categoryId'] = self.category
			config['createdOn'] = str(self.createdOn)

		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return config

	@classmethod
	def get_id(self,id):
		return None
		

