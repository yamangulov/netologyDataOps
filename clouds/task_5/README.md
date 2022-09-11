### Задание: Зашифровать бакет с помощью kms и убедится что только авторизованные сервисные аккаунты имеют туда доступ

**Данные для задания** – ваш аккаунт в Yandex.Cloud

Подключите в ваше облако

1. Создайте сервисный аккаунт для s3 с ролью storage.admin на фолдере и публичный s3 бакет ( не включайте в нем шифрование)
2. Загрузите в бакет какой нибудь объект ( назовите его FIRST) с помощью статических ключе сервисного аккаунта и настроенной утилиты s3cmd или aws-cli для этого ( метод put)
3. Создайте ключ kms и дайте сервисному аккаунту для s3 роль kms.keys.encrypterDecrypter на фолдер
4. Загрузите в бакет еще один объект ( назовите его SECOND) ( метод put)
5. Попробуйте прочитать оба объекта с помощью команды get используя aws-cli или s3cmd
6. Отзовите роль kms.encrypterDecrypter у сервисного аккаунта для доступа в s3
7. Попробуйте прочитать оба объекта еще раз используя aws-cli или s3cmd. У вас не дожно быть возможности прочитать объект SECOND
8. Также попробуйте обратится через интернет ( например curl по прямой ссылке объекта) в оба объекта - у вас должен быть доступ в объект , а во второй быть не должно

**Результат:**

Скриншоты результатов которые вы получили в пунктах 5 и 7

**Инструменты:**

1. Сервисные роли Storage, KMS, - [https://cloud.yandex.ru/docs/storage/security/](https://cloud.yandex.ru/docs/storage/security/) , [https://cloud.yandex.ru/docs/kms/security/](https://cloud.yandex.ru/docs/kms/security/)
2. Настройка утилит aws-cli , s3-cmd [https://cloud.yandex.ru/docs/storage/tools/aws-cli](https://cloud.yandex.ru/docs/storage/tools/aws-cli) , [https://cloud.yandex.ru/docs/storage/tools/s3cmd](https://cloud.yandex.ru/docs/storage/tools/s3cmd)
3. Шифрование бакета s3 [https://cloud.yandex.ru/docs/storage/operations/buckets/encrypt#add](https://cloud.yandex.ru/docs/storage/operations/buckets/encrypt#add)