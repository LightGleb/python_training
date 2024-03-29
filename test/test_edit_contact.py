# -*- coding: utf-8 -*-
from random import randrange
from model.contact import Contact


def test_edit_some_contact_from_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
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
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index_from_home_page(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact_from_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
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
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index_from_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
