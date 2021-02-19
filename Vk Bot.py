import datetime
import time

import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

Sas = 0


# Главный словарь для регестрации по классам
Persons = {}

# Главная функция отправки сообщения пользователю
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

# Разделение времяного периода
now = datetime.datetime.now()
Month = now.month
Day = now.day

# API-ключ созданный ранее
token = "ee34b2142700ca1f2f6e59a48f41ef74ce55c0caa0b897ff4f069370e0981ff4a71805fa5101c9790bb7a"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с Апи
api = vk_api.API(vk)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Место для создания цикла Сохранения параметров Регестрации (Пока что всё сохраняестся в оперативной памяти. Есть два развития: Сохранять по регестрации или сохранять все файлы через 5 минут (Это уменьшит нагрузку на сервер))



# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()
            IdPerson = event.user_id

            user = vk.method("users.get", {"user_ids": IdPerson})

            print(IdPerson)

            # Каменная логика ответа
            if request == "привет":
                write_msg(IdPerson, "Здравствуй " + user[0]["first_name"] + " ♥")
            elif request == "регестрация":
                if not IdPerson in Persons:
                    write_msg(IdPerson,
                              "Ох да ты не зарегестрирован. Напиши номер класса и букву вместе с командой /reg. Например /reg 9ж")
            elif request == "пока":
                write_msg(IdPerson, "Пока((")
            elif request == "что делаешь?" or request == "что делаешь":
                write_msg(IdPerson, "Я пока что мало что умею.")

            # Всякие команды
            elif request[0] == "/":
                # Команда регистрации в словаре Persons
                if request.split(' ')[0] == "/reg":
                    if not IdPerson in Persons:
                        if len(request.split(' ')) == 2:
                            Persons[IdPerson] = request.split(' ')[1]
                            print(Persons)
                            write_msg(IdPerson,
                                      "Сервер каждые пять минут сохраняет новых пользователей так чтобы проверить остались ли вы в списке напишите /ILIST")
                        else:
                            write_msg(IdPerson, "У вас возникла ошибка &#128532;, вы ввели или слишком много букв &#128579; или не ввели не единой буквы!!!&#128545;")
                    else:
                        write_msg(IdPerson,
                                  "Изивини ты уже зарегестрирован. Однако ты можешь изменить значение в любое время командой /rereg и цыфра класса плюс буква &#9786;")
                # Команда для проверки есть ли пользователь в словаре Persons
                if request.split(' ')[0] == "/ilist":
                    if IdPerson in Persons:
                        write_msg(IdPerson,
                                  "Вы в первоначальном списке♥, к сожилению мы пока что не обновляли сотояние серверов.")
                    else:
                        write_msg(IdPerson,
                                  "Вы не зарегестрированы, для регистрации используйте команду /reg (Номер класса Буква клаcса) Например /reg 9ж")


            else:
                write_msg(IdPerson, "Непон...")
