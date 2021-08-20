# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import pyjokes
import os
import keyboard
import wikipedia
import random

# настройки
opts = {
    "alias": ('кеша', 'кеш', 'инокентий', 'иннокентий', 'кишун', 'киш',
              'кишаня', 'кяш', 'кяша', 'кэш', 'кэша'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час', 'сколько времени', 'время'),
        "radio": ('воспроизведи радио', 'включи радио', 'радио'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', 'анектод'),
        "music": ('включи музыку','можно музыку', 'музыка'),
        "stopm": ('выключи музыку', 'стоп музыка'),
        "playm": ('продолжай', 'продолжить', 'плей', 'плэй', 'пуск'),
        "keshastop": ('остановись', 'отключение'),
        "pause": ('пауза', 'стоп'),
        "yandex": ('браузер', 'яндекс пожалуйста', 'интернет'),
        "music1": ('включи бесприданницу', 'включи бесприданница','можно бесприданницу', 'можно бесприданница'),
        "music2": ('включи каникулы','можно каникулы'),
        "music3": ('включи мальчик на девятке','можно мальчик на девятке', 'включи мальчика на девятке','можно мальчика на девятке'),
        "music4": ('включи пушка','можно пушка', 'включи пушку','можно пушку'),
        "music5": ('включи симпл димпл','можно симпл димпл')
    }
}

# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        speak("Голос не распознан!")
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        speak("Неизвестная ошибка, проверьте интернет!")
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # воспроизвести радио
        os.system("D:\\stream\\Jarvis\\res\\radio.m3u")

    elif cmd == 'music':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\ironman.mp3")

    elif cmd == 'music1':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\Бесприданница.mp3")

    elif cmd == 'music2':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\Каникулы.mp3")

    elif cmd == 'music3':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\Мальчик_на_девятке.mp3")

    elif cmd == 'music4':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\Пушка.mp3")

    elif cmd == 'music5':
        # воспроизвести музыку
        os.system("D:\\stream\\Jarvis\\res\\Симпл_Димпл.mp3")

    elif cmd == 'stopm':
         # выключить музыку
        keyboard.send("alt+F4")

    elif cmd == 'pause':
        # пауза
        keyboard.send("space")

    elif cmd == 'keshastop':
        # выключить кешу
        keyboard.send("ctrl+c")

    elif cmd == 'yandex':
        # открыть браузер
        os.system("C:\\Users\\Sergey\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe")

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak(pyjokes.get_joke())

    else:
        speak('Команда не распознана, повторите!')
        print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[1].id)

# forced cmd test
#speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

speak("Добрый день, повелитель")
speak("Кеша слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1) # infinity loop