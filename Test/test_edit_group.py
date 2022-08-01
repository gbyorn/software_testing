from Model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    old_groups = db.get_groups_list()
    index = random.randrange(len(old_groups))
    group = Group(group_name='TestGroup1', group_header='TestHeader1', group_footer='TestFooter1')
    group.group_id = old_groups[index].group_id
    app.group.edit_group_by_id(group.group_id, group)
    app.group.open_groups_page()
    new_groups = db.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
