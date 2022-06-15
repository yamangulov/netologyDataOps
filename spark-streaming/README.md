В рамках домашнего задания Вам необходимо повторить действия, проведенные на вебинаре:

1) установить Kafka
2) Установить Spark
3) Настроить IDE
В качестве генератора сообщений можете использовать код producer.py (он находится в блоке “Материалы к занятию Spark Streams-2”).

Ваша задача - запустить код на Structure Streaming на основе сгенерированных данных и отобразить в консоле результат join (Static + Stream).

В качестве артефакта - прикрепите скрин консоли, в которой виден timestamp сообщения и успешный результат join.

Дополнительное задание: найти в коде приложения пример работы функции агрегата, адаптировать его под входной поток и прислать скрин консоли (в нем должны быть показаны количества событий каждого из пользователя).**

При установке Spark на Windows может потребоваться добавить дополнительные в системные библиотеки hadoop.dll
Скачать их можно отсюда:

https://github.com/amihalik/hadoop-common-2.6.0-bin

Подробнее об этом можете посмотреть в топике

https://stackoverflow.com/questions/18630019/running-apache-hadoop-2-1-0-on-windows/19758140#19758140