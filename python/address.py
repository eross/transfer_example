import addressbook_pb2
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
