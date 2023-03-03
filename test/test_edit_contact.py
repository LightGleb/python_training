# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact_from_home_page(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_from_home_page(Contact(firstname="Иван",
                                                          middlename="Иванович",
                                                          lastname="Иванов",
                                                          nickname="Ivanko",
                                                          photo="D:\\test2.jpg",
                                                          title="Авище",
                                                          company="ООО У демона на куличиках",
                                                          address="Спб, ул. Энгельса, д. 7, корпус 3, кв. 921",
                                                          mobile="+7 934 855 44 79",
                                                          email="prorocker888@gmail.com",
                                                          homepage="vk.com",
                                                          bday="25",
                                                          bmonth="April",
                                                          byear="1991",
                                                          address2="ввв.ленинград.ру",
                                                          phone2="+7 666 666 66 66",
                                                          notes="Как то так :()"))
    app.session.logout()


def test_edit_first_contact_from_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_from_contact(Contact(firstname="Иван",
                                                        middlename="Иванович",
                                                        lastname="Иванов",
                                                        nickname="Ivanko",
                                                        photo="D:\\test2.jpg",
                                                        title="Авище",
                                                        company="ООО У демона на куличиках",
                                                        address="Спб, ул. Энгельса, д. 7, корпус 3, кв. 921",
                                                        mobile="+7 934 855 44 79",
                                                        email="prorocker888@gmail.com",
                                                        homepage="vk.com",
                                                        bday="25",
                                                        bmonth="April",
                                                        byear="1991",
                                                        address2="ввв.ленинград.ру",
                                                        phone2="+7 666 666 66 66",
                                                        notes="Как то так :()"))
    app.session.logout()
