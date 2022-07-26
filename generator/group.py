from Model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file name of groups"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

numbers = 5
file_name = "data/groups.json"

for option, attribute in opts:
    if option == "-n":
        numbers = int(attribute)
    elif option == "-f":
        file_name = attribute


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + (" " * 10)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))]).rstrip()


test_data = [Group(group_name=random_string("name", 10), group_header=random_string("header", 20),
                   group_footer=random_string("footer", 20))
             for i in range(numbers)]

groups_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file_name)

with open(groups_file, "w") as data_file:
    jsonpickle.set_encoder_options("json", indent=2)
    data_file.write(jsonpickle.encode(test_data))
