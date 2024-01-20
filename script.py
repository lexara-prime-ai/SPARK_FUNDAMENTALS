from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.csv("./data/people.csv", header=True)
df.createOrReplaceTempView("organizations")

results = spark.sql("SELECT * FROM organizations").show()

print(results)
