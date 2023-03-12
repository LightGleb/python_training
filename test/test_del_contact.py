# -*- coding: utf-8 -*-

def test_delete_first_contact_from_home_page(app):
    app.contact.delete_first_contact_from_home_page()


def test_delete_first_contact_from_contact(app):
    app.contact.delete_first_contact_from_contact()
