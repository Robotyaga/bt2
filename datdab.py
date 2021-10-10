import sqlite3

class SQLighter:

	def __init__(self, database_file):
		self.connection = sqlite3.connect('database.db')
		self.cursor = self.connection.cursor()

	def get_subscriptions(self, status = True):
		with self.connection:
			return self.cursor.execute("SELECT * FROM 'date' WHERE 'date_name' = ?", (date_name,)).fetchhall()

	def close(self):
		self.connection.close()		