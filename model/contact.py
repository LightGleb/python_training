from sys import maxsize


class Contact:

    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 photo=None,
                 title=None,
                 company=None,
                 address=None,
                 mobile=None,
                 email=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.email = email
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        # Проверки для firstname и lastname нужны для того, чтобы при создании ообъекта Contact не передавать ему
        # никакие аргументы, в случае создании пустого контакта.
        return (self.id is None or other.id is None or self.id == other.id) \
            and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
            and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
