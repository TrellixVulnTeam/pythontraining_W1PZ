__author__ = 'dorota'
# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_name(app, db):
    if app.group.count() == 0:
        app.group.create()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="test")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    app.group.modify_first_group((Group(header="New header")))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
#    old_groups = app.group.get_group_list()
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test"))
#    app.group.modify_first_group((Group(footer="New footer")))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)