## Домашняя работа к занятию “MLOps/DataOps”
## **Цель задания**

На основе полученных знаний необходимо настроить окружение и провести обучение модели.

## **Задание**:

1. Устанавливаем и настраиваем conda
2. Устанавливаем и настраиваем python3
3. Устанавливаем и настраиваем mlflow
4. Настраиваем переменные:
   export MLFLOW_TRACKING_URI=http://localhost
   export MLFLOW_S3_ENDPOINT_URL=http://localhost:9000
5. Настраиваем MinIO
6. Берём модель отсюда https://github.com/sachua/mlflow-docker-compose
7. Проводим её обучение:
   mlflow models serve -m S3://mlflow/0/98bdf6ec158145908af39f86156c347f/artifacts/model -p 1234

Домашнее задание выполните в файле readme.md в github репозитории.

## **Результат**:
В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории. Приложите:
- Показать рабочую модель через curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}' http://127.0.0.1:1234/invocations

