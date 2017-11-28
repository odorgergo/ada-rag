from pyspark import SparkContext, SparkConf
import sys
import pickle

"""
The output is a list of lists, and the schema of each list is as follows:
user id
text
date and time of creation
latitude
longitude
language
"""

input_filename = sys.argv[1]
output_dir = sys.argv[2]
if (output_dir[len(output_dir)-1:len(output_dir)] != '/'):
    output_dir += '/'
conf = SparkConf().set("spark.driver.maxResultSize", "30G")
spark = SparkContext.getOrCreate(conf=conf)
data_rdd = spark.textFile(input_filename)
rdd2 = data_rdd.map(lambda x: x.split('\t'))
rdd2 = rdd2.map(lambda x: [x[1], x[2], x[3], x[10], x[11], x[21]])
output_list = rdd2.collect()
print('collected!')
pickle.dump(output_list, open(output_dir+'dataset.pkl', mode='w'))
