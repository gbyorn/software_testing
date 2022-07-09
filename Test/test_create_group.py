from Model.group import Group


def test_create_group(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter')
    app.group.create_group(group)
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
