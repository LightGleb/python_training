# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Глеб",
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
                               notes="Как то так :)"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="",
                               middlename="",
                               lastname="",
                               nickname="",
                               photo="",
                               title="",
                               company="",
                               address="",
                               mobile="",
                               email="",
                               homepage="",
                               bday="",
                               bmonth="",
                               byear="",
                               address2="",
                               phone2="",
                               notes=""))
