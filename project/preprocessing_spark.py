from pyspark import SparkContext, SQLContext
import io
import json
import numpy as np
sc = SparkContext.getOrCreate()

sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

import os
import pandas as pd
import json
#import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
#from langdetect import detect, detect_langs
#import unicodedata
import re

from pyspark.sql.functions import *
from pyspark.sql.types import *

rdd1=sc.textFile("hdfs:/user/odor/twex2.tsv")

schema=pd.read_csv("/dlabdata1/odor/twitter-swisscom/schema.txt",sep="\s+",quoting=csv.QUOTE_NONE,header=None)
schema.drop([0,3,4,5],axis=1,inplace=True)

#lang_codes=pd.read_csv("/dlabdata1/odor/twitter-swisscom/language-codes_csv.csv")
#lang_codes.set_index("alpha2",inplace=True)

rdd1=rdd1.map(lambda x: x.split("\t"))
df=rdd1.toDF(list(schema[1].values))

udf = UserDefinedFunction(lambda x: re.sub(r'http\S+', '', x), StringType())
udf2= UserDefinedFunction(lambda x: re.sub(r'#\S+', '', x),StringType())
udf3 = UserDefinedFunction(lambda x: re.sub(r'@\S+', '', x),StringType())

df=df.withColumn("text_stripped", udf(df["text"]))
df=df.withColumn("text_stripped", udf2(df["text_stripped"]))
df=df.withColumn("text_stripped", udf3(df["text_stripped"]))

#df=df.select(*[udf(column).alias('text') if column == 'text' else column for column in df.columns])

def translate(x):
    try:
        t=detect(x)
    except:
        t=np.nan
    return t

udf4= UserDefinedFunction(lambda x: translate(x),StringType())
#udf5 = UserDefinedFunction(lambda x: lang_codes.English[x] if not pd.isnull(x) else "Undetected")


df=df.withColumn("lang", udf2(df["text_stripped"]))
#df=df.withColumn("language", udf3(df["text_stripped"]))
