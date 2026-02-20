def is_very_long(password):
    if len(password) > 12:
        return True


def is_digit(password):
    return any(letter.isdigit() for letter in password)


def has_lower_letter(password):
    return any(letter.islower() for letter in password)


def has_upper_letter(password):
    return any(letter.isupper() for letter in password)


def has_symbol(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def main():
    password = list(input('Введите пароль: '))
    score = 0
    is_very_long(password)
    is_digit(password)
    has_symbol(password)
    has_lower_letter(password)
    has_upper_letter(password)
    if is_digit(password):
        score += 2
    if is_very_long(password):
        score += 2
    if has_lower_letter(password):
        score += 2
    if has_upper_letter(password):
        score += 2
    if has_symbol(password):
        score += 2
    print('Рейтинг пароля:', score)


if __name__ == '__main__':
    main()
