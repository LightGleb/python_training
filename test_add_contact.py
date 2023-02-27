# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_contact(self, wd, contact):
        # Нажатие на кнопку "add new"
        wd.find_element_by_link_text("add new").click()
        # Заполнение формы контакта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Условие для пропуска заполнения поля при передаче пустого значения атарибута contact.photo
        if contact.photo != "":
            wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Условие для пропуска заполнения поля при передаче пустого значения атарибута contact.bday
        if contact.bday != "":
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
            wd.find_element_by_xpath(f"//option[@value='{contact.bday}']").click()
        # Условие для пропуска заполнения поля при передаче пустого значения атарибута contact.bmonth
        if contact.bmonth != "":
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
            wd.find_element_by_xpath(f"//option[@value='{contact.bmonth}']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # Нажатие на кнопку "Enter"
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="Глеб",
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
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="",
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
        self.return_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
