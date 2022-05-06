from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task2").master("local[2]").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

df = spark.read.option('header', True).option('sep', ',').option('inferSchema', True).csv('owid-covid-data.csv').filter(col('iso_code').startswith('OWID') == False).withColumn('day', dayofmonth(col('date'))).withColumn('month', month(col('date'))).withColumn('year', year(col('date')))

df_result = df.filter(((col('day') == 29) | (col('day') == 30) | (col('day') == 31)) & (col('month') == 3) & (col('year') == 2021))
df_result = df.join(df_result.groupby('location').agg(max('new_cases').alias('new_cases')), on='new_cases', how='leftsemi').select('date', 'location', 'new_cases').sort(desc('new_cases')).limit(10)
df_result.write.csv('tmp/task2', header=True)

print('task2 is finished')

spark.stop()