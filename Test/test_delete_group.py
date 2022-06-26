def test_delete_group(app):
    app.open_home_page()
    app.session.login(username='admin', password='secret')
    app.group.open_groups_page()
    app.group.delete()
    app.group.open_groups_page()
    app.session.logout()
