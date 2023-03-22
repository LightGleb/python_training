# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Глеб",
                      middlename="Николаевич",
                      lastname="Коротченко",
                      nickname="Clight",
                      photo="D:\\test.jpg",
                      title="Аватарка",
                      company="ООО У чёрта на куличиках",
                      address="Спб, ул. Энгельса, д. 6, корпус 1, кв. 901",
                      mobile="+7 934 845 33 44",
                      email="prorocker7@gmail.com",
                      homepage="vk.com/clight",
                      bday="24",
                      bmonth="March",
                      byear="1990",
                      address2="www.ленинград.ru",
                      phone2="+7 666 666 66 67",
                      notes="Как то так :)")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact_from_home_page(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_first_contact_from_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Глеб",
                      middlename="Николаевич",
                      lastname="Коротченко",
                      nickname="Clight",
                      photo="D:\\test.jpg",
                      title="Аватарка",
                      company="ООО У чёрта на куличиках",
                      address="Спб, ул. Энгельса, д. 6, корпус 1, кв. 901",
                      mobile="+7 934 845 33 44",
                      email="prorocker7@gmail.com",
                      homepage="vk.com/clight",
                      bday="24",
                      bmonth="March",
                      byear="1990",
                      address2="www.ленинград.ru",
                      phone2="+7 666 666 66 67",
                      notes="Как то так :)")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact_from_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
