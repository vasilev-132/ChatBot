import datetime
import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

Sas = 0
print(True)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

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

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()

            user = vk.method("users.get", {"user_ids": event.user_id})

            print(event.user_id)

            # Каменная логика ответа
            if request == "привет":
                if event.user_id == 314984632:
                    write_msg(event.user_id, "Привет " + "Господин " + user[0]["first_name"])
                elif event.user_id == 267591369:
                    write_msg(event.user_id, "Привет " + "Госпожа " + user[0]["first_name"])
                else:
                    write_msg(event.user_id, "Привет")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            elif request == "что делаешь?" or request == "что делаешь":
                write_msg(event.user_id, "Приветствуюсь))) Иди делай уроки.")
                if event.user_id == 267591369 or event.user_id == 314984632:
                    write_msg(event.user_id, "Ой какое сегодя число? хм? Ща взгляну!")
                    write_msg(event.user_id, str(now.day) + "." + str(now.month) + "." + str(now.year))
                    if Month <= 1:
                        if Day == 31:
                            write_msg(event.user_id, "Можешь отдыхать завтра страдать♥")
                        else:
                            write_msg(event.user_id, "Пока отдыхай")
                    else:
                        write_msg(event.user_id, "Иди работай!")
            elif request == "кинь картинку" or request == "кинь мужика" or request == "требую мужика":
                write_msg(event.user_id, "https://sun9-22.userapi.com/impg/Rk-LzqG-6f9TpH2r6Ifdty3ORjg0wAHThP87fg/zBZThssYeZg.jpg?size=1042x1080&quality=96&sign=4cb8119cbaf1712268d7e5e58093d71d&type=album")
            else:
                write_msg(event.user_id, "Непон...")