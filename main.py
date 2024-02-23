region = input(
    'Если Ваш регион - Чукотка, Сахалин или Камчатка, введите "да".\nЛюбой другой символ (символы) означает "нет": ').lower()

if region == 'да':
    print(f'Ваша ставка: 2%')
else:
    base_rate = 15
    children = input('Введите "да", если у Вас больше трёх детей.\nЛюбой другой символ (символы) означает "нет": ')

    salary_project = input(
        'Введите "да", если у Вас есть зарплатный проект в нашем банке.\nЛюбой другой символ (символы) означает "нет": ').lower()
    insurance = input(
        'Введите "да", если Вы согласы оформить страховку в нашем банке.\nЛюбой другой символ (символы) означает "нет": ').lower()

    discount_children = 0
    discout_salary_project = 0
    discount_insurance = 0

    if children == 'да':
        discount_children = 1
    if salary_project == 'да':
        discout_salary_project = 0.5
    if insurance == 'да':
        discount_insurance = 1.5
    print(f'Ваша ставка: {base_rate - discount_children - discout_salary_project - discount_insurance}%')