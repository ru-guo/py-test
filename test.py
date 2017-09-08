from transwarp import db
db.create_engine(user='root', password='root', database='test', host='127.0.0.1', port=3306)
users = db.select('select * from user');
print	users