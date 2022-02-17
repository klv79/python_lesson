def info(name, surname, year, city, email, tel):
    result = f'{name} {surname} {year} года рождения, проживающий(ая) в городе {city}, ' \
             f'електронная почта: {email}, телефон: {tel}'
    return result

print(info(name=input('Введите имя '), surname=input('Введите фамилию '), year=int(input('Введите год рождения ')),
           city=input('Введите город проживания '), email=input('Введите электронную почту '), tel=int(input('Введите телефон '))))
