from gtts import gTTS #Подключили библиотеку
ru = str('Добрый день!') #Задали текст на русском языке
de = str('Guten tag!') #Задали текст на немецком языке (в качестве примера)
en = str('Hello everybody') #engl
 
tts_ru = gTTS(ru, lang='ru') #Обозначили язык нашего текста
tts_de = gTTS(de, lang='de') #Обозначили язык нашего текста
tts_eng = gTTS(en, lang='en') #---en?
with open('hello.mp3', 'wb') as f: #Создали файл в который будем писать звук из текста
    tts_ru.write_to_fp(f) #Записываем в файл озвучку русского текста
    tts_de.write_to_fp(f) #Записываем в файл озвучку немецкого текста
    tts_eng.write_to_fp(f) #eng
