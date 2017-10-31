import sqlite3

def main():
	try:
		con = sqlite3.connect('test.db')
		cur = con.cursor()
		cur.executescript(""" DROP TABLE IF EXISTS pets;
				CREATE TABLE pets(Id INT, Name TEXT, Price INT);
				INSERT INTO pets VALUES(1,'cat',200);
				INSERT INTO pets VALUES(2,'dog',400);""")
		pets =((3,'s',40),(4,'cv',51))
		cur.executemany('INSERT INTO pets VALUES(?,?,?)',pets)
		con.commit()
		cur.execute("SELECT * FROM pets")
		data = cur.fetchall()
		for row in data:
			print(row)
	except sqlite3.Error:
		if con:
			con.rollback()
			print("rollbacked!!")
	finally:
		if con:
			con.close()
if __name__=="__main__":
	main() 
