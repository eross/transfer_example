from flask import Flask
import flask
import sys
import hashlib
import traceback

import addressbook_pb2
from addressbook_pb2 import Person

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"


@app.route("/person", methods=['POST'])
def add_person():
    ACCEPTED="{'transaction': 'Accepted'}"
    REJECTED="{'transaction': 'Rejected'}"
    data = flask.request.get_data()
    if data:
        try:
            person = Person()
            person.ParseFromString(data)
        except:
            print "Exception"
            traceback.print_exc()
            return REJECTED
        print "Received..."
        print person
        return ACCEPTED
    else:
        return REJECTED

        
    

address_book = addressbook_pb2.AddressBook()
person = address_book.person.add()

person.id = 12L
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phone.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

person = address_book.person.add()
person.id=52
person.name = "somebody else"


f=open("testit","wb")
f.write(address_book.SerializeToString())
f.close()

f=open("testit","rb")
address_book = addressbook_pb2.AddressBook()
address_book.ParseFromString(f.read())
for person in address_book.person:
    print person.name, person.id, person.email
    print "email is there: ", person.HasField("email")
f.close()

print type(address_book)

if __name__ == "__main__":
    app.run()