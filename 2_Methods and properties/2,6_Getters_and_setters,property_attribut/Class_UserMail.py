class UserMail:
    def __init__(self, login, mail):
        self.login = login
        self.__email = mail

    def get_email(self):
        return self.__email

    def set_email(self, new_mail):
        if '@' not in new_mail or new_mail.count('@') != 1:
            return print(f'ErrorMail:{new_mail}')
        elif '.' not in new_mail[new_mail.index('@') + 1:]:
            return print(f'ErrorMail:{new_mail}')
        self.__email = new_mail

    email = property(fget=get_email, fset=set_email)
