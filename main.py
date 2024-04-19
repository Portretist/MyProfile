# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ' '
age = 0
phone = ' '
email = ' '
index = ' '
adress = ' '
information = ''
# social links
entrepreneur_registration_number = '' #ОГРНИП
personal_tax_number = '' #ИНН
bank = ''
checking_account = '' #Расчётный счёт
correspondent_account = '' #Корреспондентский счет
bank_identification_code = '' #БИК



def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter, adress_parameter, information_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19: years_parameter = 'лет'
    elif age_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'

  


    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес: ', adress_parameter)
    if information:
            print('')
            print('Дополнительная информация:')
            print(information_parameter)




def entrepreneur_info(entrepreneur_registration_number_parameter, personal_tax_number_parameter, checking_account_parameter, bank_parameter, bank_identification_code_parameter, correspondent_account_parameter):
  print('\nИнформация о предпринимателе')
  print('ОГРНИП:', entrepreneur_registration_number_parameter)
  print('ИНН:', personal_tax_number_parameter)
  print('Банковские реквизиты')
  print('Расчётный счёт:', checking_account_parameter)
  print('Банк: ', bank_parameter)
  print('БИК:', bank_identification_code_parameter)
  print('Корреспондентский счёт:', correspondent_account_parameter)




def CheckNumber(number_parameter):
  number_count = 0
  while number_parameter > 0:
    number_count += 1
    number_parameter //= 10
  return number_count



    

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                        # validate user age
                        age = int(input('Введите возраст: '))
                        if age > 0:
                            break
                        print('Возраст должен быть положительным')

                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for phone_symbol in user_phone:
                    if phone_symbol == '+' or ('0' <= phone_symbol <= '9'):
                        phone += phone_symbol


                email = input('Введите адрес электронной почты: ')
                user_index = input('Введите почтовый индекс: ')
                for index_symbol in user_index:
                      if '0' <= index_symbol <= '9':
                          index += index_symbol
                adress = input('Введите почтовый адрес (Без индекса): ')
                information = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input entrepreneur information
              while True:
                entrepreneur_registration_number = int(input('Введите ОГРНИП: '))
                entrepreneur_registration_numberCheck = CheckNumber(entrepreneur_registration_number)
                if entrepreneur_registration_numberCheck == 15:
                  break
                  
                else:
                  print('ОГРНИП должен содержать 15 цифр')
              personal_tax_number = int(input('Введите ИНН: ')) 
              while True:
                checking_account = int(input('Введите расчётный счёт: ')) 
                checking_accountCheck = CheckNumber(checking_account)
                if checking_accountCheck == 20:
                  break
                  
                else:
                  print('Расчётный счёт должен содержать 20 цифр')
              bank = input('Введите название банка: ')
              bank_identification_code = int(input('Введите БИК: '))
              correspondent_account = int(input('Введите корреспондентский счет: ')) 
              
                
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, adress, information)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, adress, information)

                # print entrepreneur information
                entrepreneur_info(entrepreneur_registration_number, personal_tax_number, checking_account, bank, bank_identification_code, correspondent_account)
              
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')
