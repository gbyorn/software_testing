from Model.group import Group
import pytest
import random
import string


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + string.punctuation + (" " * 10)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


test_data = [Group(group_name=random_string("name", 10), group_header=random_string("header", 20),
                   group_footer=random_string("footer", 20))
             for i in range(1)]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_group(app, group):
    print(group)
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create_group(group)
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
