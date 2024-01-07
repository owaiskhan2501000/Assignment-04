class UserProfile:
    def __init__(self, username, email, password, security_question):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__security_question = security_question

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_security_question(self):
        return self.__security_question

    def set_email(self, new_email):
        if "@" in new_email and "." in new_email:
            self.__email = new_email
        else:
            print("Invalid email format. Please provide a valid email address.")

    def set_password(self, current_password, new_password):
        if current_password == self.__password:
            self.__password = new_password
            print("Password successfully updated.")
        else:
            print("Incorrect current password. Password update failed.")

    def set_security_question(self, new_security_question):
        if isinstance(new_security_question, str):
            self.__security_question = new_security_question
        else:
            print("Invalid security question. Please provide a valid string.")

