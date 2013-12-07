import peewee as pw
from peewee import *

myDB = pw.MySQLDatabase("vm", host="localhost", port=3306, user="root", passwd="sqlpass01")

class User(Model):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    class Meta:
        database = myDB
        order_by = ('username',)    

# when you're ready to start querying, remember to connect
myDB.connect()

User.create_table()

print 'db connect and user created'