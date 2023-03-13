from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_data):
        wd = self.app.wd
        # Нажатие на кнопку "add new"
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_data)
        # Нажатие на кнопку "Enter"
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def edit_first_contact_from_home_page(self, new_contact_data):
        # Открытие домашней страницы, если мы ещё не на ней
        self.app.open_home_page()
        self.select_first_contact()
        self.click_first_pencil_icon()
        self.fill_contact_form(new_contact_data)
        self.click_button_update()
        self.return_to_home_page()

    def edit_first_contact_from_contact(self, new_contact_data):
        wd = self.app.wd
        # Открытие домашней страницы, если мы ещё не на ней
        self.app.open_home_page()
        self.open_first_contact()
        # Нажать на кнопку "Modifiy"
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        self.click_button_update()
        self.return_to_home_page()

    def delete_first_contact_from_home_page(self):
        wd = self.app.wd
        # Открытие домашней страницы, если мы ещё не на ней
        self.app.open_home_page()
        self.select_first_contact()
        # Нажать на кнопку "Delete"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Подтвердить удаление
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def delete_first_contact_from_contact(self):
        wd = self.app.wd
        # Открытие домашней страницы, если мы ещё не на ней
        self.app.open_home_page()
        self.click_first_pencil_icon()
        # Нажатие на кнопку "Delete"
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_to_home_page()

    def open_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def click_button_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def click_first_pencil_icon(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name != "photo":
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath(f"//option[@value='{text}']").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
