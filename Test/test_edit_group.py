from Model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(group_name='TestGroup1', group_header='TestHeader1', group_footer='TestFooter1')
    group.group_id = old_groups[0].group_id
    app.group.edit(group)
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
