from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("task3").master("local[2]").getOrCreate()
spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")

df = spark.read.option('header', True).option('sep', ',').option('inferSchema', True).csv('owid-covid-data.csv').withColumn('day', dayofmonth(col('date'))).withColumn('month', month(col('date'))).withColumn('year', year(col('date')))

df_filtered = df.filter(((col('day') == 28) | (col('day') == 29) | (col('day') == 30) | (col('day') == 31)) & (col('month') == 3) & (col('year') == 2021) & (col('location') == 'Russia'))
df_window = Window.partitionBy().orderBy('date')
df_result = df_filtered.withColumn('prev_new_cases', lag(df_filtered.new_cases).over(df_window))
df_result = df_result.withColumn('delta', df_result.new_cases - df_result.prev_new_cases).select('date', 'prev_new_cases', 'new_cases', 'delta')
df_result = df_result.filter(col('date') != '2021-03-28')

df_result.write.csv('tmp/task3', header=True)

print('task3 is finished')

spark.stop()