# main python files
import psycopg2.pool
import os
import sys
from dotenv import load_dotenv

load_dotenv()

# buka koneksi
# Create a connection pool with a minimum of 2 connections and 
# a maximum of 3 connections
dbPool = psycopg2.pool.ThreadedConnectionPool(
	os.getenv('DB_MINCONN'),
	os.getenv('DB_MAXCONN'),
	host=os.getenv('DB_HOST'),
	database=os.getenv('DB_NAME'),
	user=os.getenv('DB_USER'),
	password=os.getenv('DB_PASS'),
	port=os.getenv('DB_PORT'))



def question_1():
	conn = dbPool.getconn()
	cursor = conn.cursor()
	cursor.execute("SELECT NOW()")
	result = cursor.fetchall()
	cursor.close()
	dbPool.putconn(conn)
	print(result)

	

def main():
	question_1()
	dbPool.closeall()
	return(0)

print("run main")
main()