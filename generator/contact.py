from Model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file name of contacts"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

numbers = 5
file_name = "data/contacts.json"

for option, attribute in opts:
    if option == "-n":
        numbers = int(attribute)
    elif option == "-f":
        file_name = attribute


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + (" " * 10)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))]).rstrip()


test_data = [Contact(first_name=random_string("firstname", 10), middle_name=random_string("middlename", 10),
                     last_name=random_string("lastname", 10), nickname=random_string("nickname", 10),
                     title=random_string("title", 15), company=random_string("title", 15),
                     address=random_string("title", 20), home_phone=random_string("h", 5),
                     mobile_phone=random_string("m", 5), work_phone=random_string("w", 5),
                     fax=random_string("fax", 5), first_email=random_string("first", 5),
                     second_email=random_string("second", 5), third_email=random_string("third", 5),
                     homepage=random_string("homepage", 10), b_day=str(random.randint(1, 31)),
                     b_month=random.choice(['October', 'April', 'May']), b_year=str(random.randint(1980, 2010)),
                     a_day=str(random.randint(1, 31)), a_month=random.choice(['November', 'June', 'July']),
                     a_year=str(random.randint(1980, 2010)), second_address=random_string("secondaddr", 10),
                     second_home=random_string("s", 5), second_notes=random_string("secondnote", 10))
             for i in range(numbers)]

contacts_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file_name)

with open(contacts_file, "w") as data_file:
    jsonpickle.set_encoder_options("json", indent=2)
    data_file.write(jsonpickle.encode(test_data))

