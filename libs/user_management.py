"""User management module. It allows:
1. User registration
2. User login
"""
import os
import sys

from read_write import append
from read_write import read
from read_write import create


def login_menu():
    """Application login menu that returns the user option as a string.
    The user can choose to register, login and exit"""
    print('1.Register\n2.Login\n3.Exit')
    if not os.path.exists(r'user_data.csv'):
        create('user_data.csv')
    user_option = input('Your choice: ')
    if user_option not in ['1', '2', '3']:
        print('value error, please introduce a valid choice')
        return login_menu()
    return user_option


def main_menu():
    """Application main menu that returns the user option as a string.
    The user can choose to see user details or log out or exit"""
    print('1.User Details\n2.Log Out\n3.Exit')
    user_option2 = input('Your Choice: ')
    if user_option2 not in ['1', '2', '3']:
        print('value error, please introduce a valid choice')
        return main_menu()
    return user_option2


def get_user_data(for_register=False):
    """The user can input its username, password, name and email address"""
    if for_register:
        username_r = input('Username: ')
        password_r = input('Password: ')
        name_r = input('Name: ')
        email_r = input('E-mail: ')
        return username_r, password_r, name_r, email_r
    username_l = input('Username: ')
    password_l = input('Password: ')
    return username_l, password_l


def is_registered(username_or_email_check) -> bool:
    """Checks whether the user is already registered"""
    try:
        for user in read('user_data.csv'):
            if username_or_email_check in user:
                return True
        return False
    except FileNotFoundError as e:
        print(e)
        sys.exit(2)


def register_user(username_r, password_r, name_r, email_r):
    """Saves user data to database(.csv)"""
    if not is_registered(username_r):
        if not is_registered(email_r):
            try:
                append('user_data.csv', username_r, password_r, name_r, email_r)
                print('Successfully registered')
            except FileNotFoundError:
                print('the file does not exist')
        else:
            print('Email already registered')
    else:
        print('Username already used')


def login_user(username_login, password_login):
    """Saves user data to database(.csv file)"""
    if not is_registered(username_login):
        print('Please register first')
    else:
        try:
            for user in read('user_data.csv'):
                if password_login in user:
                    print('Successfully logged in!')
                    break
            else:
                print('Wrong password')
        except FileNotFoundError:
            print('The file does not exist')


def user_details(username_d: str, password_d: str) -> str:
    """
    Searches for Name and Email based on username and password
    :param username_d: Username used for login
    :param password_d: Password used for login
    :return: Name and Email
    """
    for user in read('user_data.csv'):
        if username_d in user and password_d in user:
            return f'######## User Details\nName: {user[2]}\nEmail: {user[3]}\n######'


if __name__ == '__main__':
    option = login_menu()
    while True:
        try:
            if option == '1':
                username, passwd, name, email = get_user_data(for_register=True)
                register_user(username, passwd, name, email)
                option = login_menu()
            elif option == '2':
                username, passwd = get_user_data(for_register=False)
                login_user(username, passwd)
                while option == '2':
                    option2 = main_menu()
                    if option2 == '1':
                        print(user_details(username, passwd))
                    elif option2 == '2':
                        option = login_menu()
                    else:
                        sys.exit(0)
            else:
                sys.exit(0)
        except ValueError as e:
            print('not a valid option. Try again')
