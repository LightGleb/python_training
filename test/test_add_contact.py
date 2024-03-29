# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
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
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


