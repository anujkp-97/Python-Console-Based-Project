import pymysql

con = pymysql.connect(user='root', host='localhost', password='MRAK#7899@yk', db='pythonconnect')

cur = con.cursor()

# q = """CREATE TABLE worker (worker_id int not null primary key auto_increment,
#         first_name varchar(20), last_name varchar(20), 
#         salary int(15), joining_data DATETIME, department varchar(25))"""

# q = """ insert into worker(worker_id, first_name, last_name, salary, joining_data, department) values
#         (002, 'Ankit','Prasad', '2000', '14-03-24', 'Cloud Engineer'),
#         (003, 'Aniket','Singh', '2000', '11-03-24', 'Engineer'),
#         (004, 'Anuj','Pal', '2000', '14-03-24', 'Cloud'),
#         (005, 'Divyank','Singh', '2000', '14-03-24', 'Admin'),
#         (006, 'Jayant','Kumar', '2000', '14-03-24', 'Sales')
#    """

cur.execute("Select worker_id, first_name, department, salary from worker")
# print(*list(cur.fetchmany(2)), sep="\n")

res = cur.fetchall()

# for x in res:
#     print(x)


# con.commit()