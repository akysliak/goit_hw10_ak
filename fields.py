import warnings


class Field():
    """
    Class representing a fild in a record of an address book.
    """
    # name of the object type
    name = "filed"

    def __init__(self, value: str):
        self.value = value

    def set_value(self, new_value: str):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def validate(self, value: str):
        return True

    '''
    def to_string(self):
        return str(self.value)
    '''


class Name(Field):
    """
    Class representing the contact name stored in a record of an address book.
    """
    def __init__(self, value: str):
        super(Name, self).__init__(value)
        self.name = "name"


class Phone(Field):
    """
    Class representing a phone number within a record of an address book.
    """
    def __init__(self, value: str):
        super(Phone, self).__init__(value)
        self.validate(value)
        self.name = "phone"

    def validate(self, phone: str):
        """
        Conducts a simple check if the given phone number is well-formed. Raises WARNING if it is not.
        NB: not a full check, only spots some incorrect features.
        :param phone: the phone number to be checked.
        :return: True if the phone number passes the simple check.
        """
        if phone.isdigit() or (phone[0] == "+" and phone[1:].isdigit()):
            return True
        warnings.warn(f"WARNING: the phone number '{phone}' is malformed.")


class Email(Field):
    """
    Class representing an email within a record of an address book.
    """
    def __init__(self, value: str):
        super(Email, self).__init__(value)
        self.validate(value)
        self.name = "e-mail"

    def validate(self, email: str):
        """
        Conducts a simple check if the given e-mail is well-formed. Raises WARNING if it is not.
        NB: not a full check, only spots some incorrect features.
        :param email: the e-mail to be checked.
        :return: True if the e-mail passes the simple check.
        """
        parts = email.split("@")
        if len(parts) == 2 and len(parts[1].split(".")) == 2:
            return True
        warnings.warn(f"WARNING: the email '{email}' is malformed.")


if __name__ == "__main__":
    # testing validate() methods
    print(Email("shf_4uh@d.re"))
    print(Phone("+36785295720958"))
