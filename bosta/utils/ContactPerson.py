class ContactPerson:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def toJSON(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }