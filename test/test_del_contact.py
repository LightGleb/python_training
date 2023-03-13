# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.delete_first_contact_from_home_page()


def test_delete_first_contact_from_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.delete_first_contact_from_contact()
