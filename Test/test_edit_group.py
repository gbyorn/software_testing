from Model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
    app.group.edit(Group(group_name='TestGroup1', group_header='TestHeader1', group_footer='TestFooter1'))
    app.group.open_groups_page()
