from Model.group import Group


def test_create_group(app):
    app.group.open_groups_page()
    app.group.create(Group(group_name='TestGroup', group_header='TestHeader', group_footer='TestFooter'))
    app.group.open_groups_page()
