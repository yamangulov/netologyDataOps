from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task2").master("local[2]").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

df = spark.read.option('header', True).option('sep', ',').option('inferSchema', True).csv('owid-covid-data.csv').filter(col('iso_code').startswith('OWID') == False).withColumn('week_of_month', date_format(col('date'), 'W')).withColumn('month', month(col('date'))).withColumn('year', year(col('date')))
march_last_week_number = df.filter((df.month == 3) & (df.year == 2021)).select(max('week_of_month').alias('value'))
march_last_week_number = march_last_week_number.first()['value']
df_result = df.filter((col('week_of_month') == march_last_week_number) & (col('month') == 3) & (col('year') == 2021)).groupby('location', 'date').max('new_cases').sort(desc('max(new_cases)')).limit(10)
df_result.write.csv('tmp/task2', header=True)

print('task2 is finished')

spark.stop()