from Model.group import Group
import random


def test_delete_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create_group(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    app.group.open_groups_page()
    new_groups = db.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
