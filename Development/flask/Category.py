import pymysql

class Category:
	def __init__(self,name,createdOn):
		self.name = name
		self.createdOn = createdOn

	def save(self):

		category = None
		name = self.name
		createdOn = self.createdOn

		con = None

		try :
			con = pymysql.connect('localhost','root', 'rancard', 'data_curation')
			cur = con.cursor()
			statement = "INSERT INTO Category(name,createdOn) VALUES('"+ name +"', '"+ str(createdOn) +"')"
			print("Insert statement : "+ statement)
			cur.execute(statement)
			con.commit()
		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return category

	def delete(self,id):
		category = None
		

		con = None

		try :
			con = pymysql.connect("dbname='data_curation' user= 'root'")

			cur =con.cursor()
			cur.execute(" DELETE FROM category WHERE  id = " + id)

			row = cursor.fetchone()

			while row is not None:
				print(row)
				row = cursor.fetchone()

		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return category


	def update(self,id,name):
		category = None
		

		con = None

		try :
			con = pymysql.connect("dbname='data_curation' user= 'root'")

			cur =con.cursor()
			cur.execute(" UPDATE category SET name = " + name + "WHERE  id = " + id + "")

			row = cursor.fetchone()

			while row is not None:
				print(row)
				row = cursor.fetchone()

		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return category

	def select(self,id,name,createdOn):
		category = None
		self.name = name
		self.createdOn =createdOn
		

		con = None

		try :
			con = pymysql.connect("dbname='data_curation' user= 'root'")

			cur =con.cursor()
			cur.execute(" SELECT FROM category WHERE  id = " + id , name = " + name , createdOn = " + createdOn + "")

			row = cursor.fetchone()

			while row is not None:
				print(row)
				row = cursor.fetchone()

		except Exception as e:
			print(str(e))
		finally:
			if con != None:
				try:
					con.close()
				except Exception as e:
					print(str(e))
		return category


	@classmethod
	def get_id(self, id):

	 	return None
