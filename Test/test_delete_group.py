from Model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete()
    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups = old_groups[1:]
    assert old_groups == new_groups
