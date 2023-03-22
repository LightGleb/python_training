# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_first_contact_from_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
