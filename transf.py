# import package
from pyspark.sql import *


if __name__ == "__main__":
  
  spark = pyspark.sql.DataFrame()
  fire_df = spark.read \
      .format("csv") \
      .option("header","true") \
      .option("inferSchema", "true") \
      .load("/fire_project/data/sf-fire-calls.csv")

  
