from password_maker import PasswordGenerator
import random

user_letters = random.randint(4,14)
user_numbers = random.randint(4,14)
user_symbols = random.randint(4,14)

user_password = PasswordGenerator(user_letters, user_numbers, user_symbols)
user_password.letters_maker()
user_password.numbers_maker()
user_password.symbols_maker()

