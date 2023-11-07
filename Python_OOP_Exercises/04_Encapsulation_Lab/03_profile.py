class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_valid_len = len(value) >= 8
        is_upper_case_presented = any(char for char in value if char.isupper())
        is_digit_presented = any(char for char in value if char.isdigit())

        if is_valid_len and is_upper_case_presented and is_digit_presented:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or "
                             "more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return (f'You have a profile with username: "{self.username}" and '
                f'password: {"*" * len(self.password)}')


# test code
profile_with_invalid_password = Profile('My_username', 'My-password')
print(profile_with_invalid_password)
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# print(profile_with_invalid_username)
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
