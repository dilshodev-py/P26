# import psycopg2
#
#
# con = psycopg2.connect(
#     dbname = "lesson_1",
#     user = "postgres",
#     password = "1",
#     host = "localhost",
#     port =5432
# )
#
#
# cursor = con.cursor()
# query1 = "select * from categories"
# query2 = "insert into categories (name) values ('Telefon') returning id"
# cursor.execute(query2)
# con.commit()
# print(cursor.fetchall())




