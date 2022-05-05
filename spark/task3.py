from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("task3").master("local[2]").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

df = spark.read.option('header', True).option('sep', ',').option('inferSchema', True).csv('owid-covid-data.csv').withColumn('week_of_month', date_format(col('date'), 'W')).withColumn('month', month(col('date'))).withColumn('year', year(col('date')))

march_last_week_number = df.filter((df.month == 3) & (df.year == 2021)).select(max('week_of_month').alias('value'))
march_last_week_number = march_last_week_number.first()['value']

df_filtered = df.filter((col('week_of_month') == march_last_week_number) & (col('month') == 3) & (col('year') == 2021) & (col('location') == 'Russia'))
df_window = Window.partitionBy().orderBy('date')
df_result = df_filtered.withColumn('prev_new_cases', lag(df_filtered.new_cases).over(df_window))
df_result = df_result.withColumn('delta', df_result.new_cases - df_result.prev_new_cases).select('date', 'prev_new_cases', 'new_cases', 'delta')

df_result.write.csv('tmp/task3', header=True)

print('task3 is finished')

spark.stop()