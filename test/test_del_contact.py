# -*- coding: utf-8 -*-

def test_delete_first_contact_from_home_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_home_page()
    app.session.logout()


def test_delete_first_contact_from_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_contact()
    app.session.logout()
