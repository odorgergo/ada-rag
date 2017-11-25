from pyspark import SparkContext, SparkConf
import sys

input_filename = sys.argv[1]
output_dir = sys.argv[2]
language_codes_list = open('twitter-swisscom/language-codes_csv.csv', mode='r').readlines()
language_codes_list += ['NaN']
language_codes_set = set([x.split(',')[0] for x in language_codes_list])

conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")

spark = SparkContext.getOrCreate(conf=conf)
data_rdd = spark.textFile(input_filename)

data_rdd = data_rdd.filter(lambda x: x.count('\t') == 21)
data_rdd = data_rdd.filter(lambda x: str(x.split('\t')[21]) in language_codes_set)
data_rdd = data_rdd.filter(lambda x: len(x.split('\t')[3].split()) > 2)

data_rdd.saveAsTextFile(output_dir)
