import pymysql

class Database:

    def __init__(self):
       self.con = pymysql.connect(user='root', host='localhost', password='MRAK#7899@yk', db='pythonconnect')

       q = "CREATE TABLE IF NOT EXISTS user(userId int primary key, user_name varchar(100), phone varchar(12))"

       cur = self.con.cursor()
       cur.execute(q)
    #    print("Table Created Successfully!")

    #Inserting data into the table

    def insert_data(self, userId, user_name, phone):
        q = """insert into user(userId, user_name, phone) 
            values({},'{}','{}') """.format(userId, user_name, phone)
      
        cur  = self.con.cursor()
        cur.execute(q)
        self.con.commit()
        print("Inserted successfully!")
        print()
    
    #fetch data
    def get_data(self):
        cur = self.con.cursor()
        q = "select * from user"
        cur.execute(q)
        res = cur.fetchall()
        for x in res:
            print("UserId: ", x[0])
            print("UserName: ", x[1])
            print("Phone: ", x[2])
            print()
    
    #delete
    def delete_user(self, userId):
         cur = self.con.cursor()
         q = "delete from user where userId = {}".format(userId)
         cur.execute(q)
         print("Deleted")
         self.con.commit()
         print()
    
    #update
    def update(self, userId, newName, newPhone):
        cur = self.con.cursor()
        q = "update user set user_Name= '{}', phone='{}' where userId = {}".format(newName, newPhone, userId)
        print(q)
        cur.execute(q)
        self.con.commit()
        print("Updated")
        print()
