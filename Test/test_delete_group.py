from Model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    app.group.delete()
    app.group.open_groups_page()
