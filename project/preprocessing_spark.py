from pyspark import SparkContext, SQLContext
import numpy as np
sc = SparkContext.getOrCreate()

sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.parquet.compression.codec","snappy")

from langdetect import detect, detect_langs
import re

with open("/dlabdata1/odor/twitter-swisscom/twex.tsv", 'r') as f:
    read_data = f.read()


pattern_bn=re.compile("\n")
read_data=pattern_bn.sub(" ",read_data)

pattern=re.compile("\d{4,}\t\d{4,}\t\d{4}\-\d{2}\-\d{2}\s\d{2}:\d{2}:\d{2}")
read_data=pattern.sub(lambda x: "1a2b8c6d921hifuhg3ufb23f@#"+x.group(),read_data).split("1a2b8c6d921hifuhg3ufb23f@#")
read_data=read_data[1:]


def splitter(x):
    l=x.split("\t")
    if len(l)>20:
        l = l[0:3]+["".join(l[3:-16])]+l[-16:]
    return l

read_data=list(map(splitter,read_data))

rdd1=sc.parallelize(read_data)

with open("/home/yazdania/ada-rag/project/twitter-swisscom/schema.txt", 'r') as f:
    schema_all=f.read()
schema_list=map(lambda x: x.split()[1],schema_all.split("\n")[0:-2])
schema=dict(zip(schema_list, list(range(len(schema_list)))))

#lang_codes=pd.read_csv("twitter-swisscom/language-codes_csv.csv")
#lang_codes.set_index("alpha2",inplace=True)

#rdd1=rdd1.sample(False,0.00001)
#rdd1=rdd1.map(lambda x: x.split("\t"))

def strip(x):
    e = re.sub(r'http\S+', '', x[schema["text"]])
    e = re.sub(r'#\S+', '', e)
    e = re.sub(r'@\S+', '', e)
    x.append(e)
    return x

rdd1=rdd1.map(strip)
schema["text_stripped"]=len(schema)


def translate(x):
    try:
        t=detect(x[schema["text_stripped"]].decode("utf-8"))
    except:
        t="NaN"
    x.append(t)
    return x

rdd1=rdd1.map(translate)
schema["lang"]=len(schema)

##rdd1.take(10)

def toTSVLine(data):
  return pattern_bn.sub(" ", '\t'.join(str(d) for d in data))

lines = rdd1.map(toTSVLine)
lines.saveAsTextFile('hdfs:/user/yazdania/ADA/lang')



#sorted(rdd2.map(lambda x: x[schema["lang"]]).countByValue().items())

#with open('spark_out.txt', 'w') as f:
#    for line in rdd1.take(2):
#        f.write(str(line)+"\n")
