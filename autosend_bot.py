from simple_vk_bot import Bot  # базовый класс бота из файла simple_bot

import random  # генератор случайных чисел
import schedule  # выполнение отложенных задач
import time  # работа с датой и временем (используется только для логов)


class AutoSendBot(Bot):
    """
        Этот бот прекрасно подойдет для рассылок, здесь мы должны наследоваться от класса Bot
    """

    # прозвища, участвующие в генерации фраз
    sweets_names = [
            "Настёна",
            "Пупс",
            "Настюха",
            "Анастейша",
            "Солнышко",

    ]

    def __init__(self):
        """
        Иинициализируем бота
        """
        super().__init__()

        # создание расписания отправки сообщений
        self.create_schedule()

        # отправка сообщения заданному пользователю по расписанию
        while True:
            schedule.run_pending()

    def wish_good_morning(self):
        """
        Отправка случайного пожелания доброго утра
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.sweets_names[random.randint(0, len(self.sweets_names) - 1)]
        phrases = [
            "Доброе утро, {}! Как спалось?".format(pet_name),
            "Утро, {}! Какой план у тебя на день?".format(pet_name),
            "утро, {}".format(pet_name),
            "доброе утро, {}, какой сон тебе снился сегодня?".format(pet_name),
            "утро, уже позавтракала?".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def talk_about_lunch(self):
        """
        Отправка случайного сообщения про обед
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.sweets_names[random.randint(0, len(self.sweets_names) - 1)]
        phrases = [
            "угадай, чем я сегодня обедал, {}".format(pet_name),
            "приятного аппетита, {}!".format(pet_name),
            "а что ты любишь кушать, {}?".format(pet_name),
            "Что ты поела сегодня, {}?".format(pet_name),
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def ask_how_the_day_was(self):
        """
        Отправка случайного вопроса про то, как у собеседника идут дела
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.sweets_names[random.randint(0, len(self.sweets_names) - 1)]
        phrases = [
            "как твой день проходит, {}?".format(pet_name),
            "чем занималась сегодня, {}?".format(pet_name),
            "Признавайся, что делала весь день, {}?".format(pet_name),
            "чего успела натворить за сегодня, {}?".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def wish_good_night(self):
        """
        Отправка случайного пожелания на ночь
        Сообщение будет отправлено пользователю с default_user_id (можно изменить при вызове функци отправки сообщения)
        """
        pet_name = self.sweets_names[random.randint(0, len(self.sweets_names) - 1)]
        phrases = [
            "Доброй ночи, {}!".format(pet_name),
            "Сладких снов, {})".format(pet_name),
            "спи крепко, {}".format(pet_name),
            "спокнойно ночи тебе, {}, завтра продолжим".format(pet_name)
        ]
        message = phrases[random.randint(0, len(phrases) - 1)]
        self.send_message(message_text=message)

    def create_schedule(self):
        """
        Создание расписания отправки сообщений со случайным временем в заданном промежутке
        Используется время сервера
        """

        # отправка сообщения в утренние часы в случайный момент
        morning_time = "0" + str(random.randint(7, 9)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(morning_time).do(self.wish_good_morning)

        # отправка сообщения в обеденное время в случайный момент
        lunch_time = str(random.randint(12, 14)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(lunch_time).do(self.talk_about_lunch)

        # отправка сообщения в вечернее время в случайный момент
        evening_time = str(random.randint(18, 20)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(evening_time).do(self.ask_how_the_day_was)

        # отправка сообщения поздним вечером в случайный момент
        night_time = str(random.randint(22, 23)) + ":" + str(random.randint(10, 59))
        schedule.every().day.at(night_time).do(self.wish_good_night)

        # перезапуск формирования случайного расписания ровно в полночь
        schedule.every().day.at("00:00").do(self.restart_schedule)

        # вывод созданного расписания
        print(f"Расписание на {time.strftime('%d.%m.%Y')}:"
              f"\n{morning_time}\n{lunch_time}\n{evening_time}\n{night_time}\n")

    def restart_schedule(self):
        """
        Перезапуск бота для обвновления расписания
        """
        schedule.clear()
        self.create_schedule()