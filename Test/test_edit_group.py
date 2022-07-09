from Model.group import Group
from random import randrange


def test_edit_group(app):
    if app.group.count_groups() == 0:
        app.group.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(group_name='TestGroup1', group_header='TestHeader1', group_footer='TestFooter1')
    group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, group)
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
