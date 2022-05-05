from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("task1").master("local[2]").getOrCreate()

df = spark.read.option('header', True).option('sep', ',').option('inferSchema', True).csv('owid-covid-data.csv')
df_result = df.select('iso_code', 'location', (col('total_cases_per_million') * 100 / 1000000).alias('percent')).filter(col('iso_code').startswith('OWID') == False).sort(desc('total_cases_per_million')).where(col('date') == '2021-03-31').limit(15)
df_result.write.csv('tmp/task1', header=True)
print('task1 is finished')

spark.stop()

