from Model.group import Group


def test_create_group(app, db, json_groups, check_ui):
    group = json_groups
    app.group.open_groups_page()
    old_groups = db.get_groups_list()
    app.group.create_group(group)
    app.group.open_groups_page()
    new_groups = db.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
