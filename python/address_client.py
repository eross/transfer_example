import addressbook_pb2
import requests
import os
import hashlib

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

person = addressbook_pb2.Person()
person.name="Eric"
person.id=42
pdata = person.SerializeToString()

print "Sending person..."
headers = {'Content-Type':'application/octet-stream'}


print "Good...."
resp=requests.post("http://localhost:5000/person",data=pdata, headers=headers)
print resp
print resp.text

print "Bad...."
resp=requests.post("http://localhost:5000/person",data="bad data", headers=headers)
print resp
print resp.text

