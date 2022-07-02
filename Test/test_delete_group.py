def test_delete_group(app):
    app.group.open_groups_page()
    app.group.delete()
    app.group.open_groups_page()
