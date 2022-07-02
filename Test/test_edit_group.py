from Model.group import Group


def test_edit_group(app):
    app.group.open_groups_page()
    app.group.edit(Group(group_name='TestGroup1', group_header='TestHeader1', group_footer='TestFooter1'))
    app.group.open_groups_page()
