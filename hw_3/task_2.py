def person(name, lastname, year, city, email, ph_number):
    print(f"Инфо: {lastname} {name} {year} г. рождения, город: {city}, тл: {ph_number}, email: {email}")


person(
    name=input('Введите имя: '),
    lastname=input('Введите фамилию: '),
    year=input('Введите год рождения: '),
    city=input('Введите город проживания: '),
    ph_number=input('Введите контактный телефон: '),
    email=input('Введите email: ')
)
