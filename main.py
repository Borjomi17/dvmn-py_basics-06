def is_very_long(password):
    return len(password) > 12


def is_digit(password):
    return any(letter.isdigit() for letter in password)


def has_lower_letter(password):
    return any(letter.islower() for letter in password)


def has_upper_letter(password):
    return any(letter.isupper() for letter in password)


def has_symbol(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def main():
    password = input('Введите пароль: ')
    score = 0

    checks = [
        is_digit,
        is_very_long,
        has_lower_letter,
        has_upper_letter,
        has_symbol
    ]

    for check in checks:
        if check(password):
            score += 2

    print('Рейтинг пароля:', score)


if __name__ == '__main__':
    main()
