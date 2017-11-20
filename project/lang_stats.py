from pyspark import SparkContext, SQLContext
import numpy as np
sc = SparkContext.getOrCreate()

sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

rdd1=sc.textFile("hdfs:/user/odor/lang")
rdd1=rdd1.map(lambda x: x.split("\t"))

a=sorted(rdd1.map(lambda x: x[21]).countByValue().items(), key=lambda x: x[1],reverse=True)

with open('spark_out.txt', 'w') as f:
    for line in a:
        f.write(str(line)+"\n")

