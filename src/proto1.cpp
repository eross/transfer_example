//============================================================================
// Name        : proto1.cpp
// Author      : Eric Ross
// Version     :
// Copyright   : Hewlett Packard, Inc
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include "addressbook.pb.h"
using namespace std;

int main() {
	GOOGLE_PROTOBUF_VERIFY_VERSION;
	string s;
	tutorial::Person *person;

	tutorial::AddressBook address_book;

	person = address_book.add_person();
	person->set_id(32);
	person->set_name("Eric");
	cout << person << endl;

	fstream output("testit", ios::out | ios::trunc | ios::binary);

	address_book.SerializeToOstream(&output);
	cout << s << endl;

	google::protobuf::ShutdownProtobufLibrary();




	cout << "Hi" << endl; // prints !!!Hello World!!!
	return 0;
}
