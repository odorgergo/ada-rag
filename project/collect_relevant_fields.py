from pyspark import SparkContext, SparkConf
import sys
import pickle

"""
The schema of the new dataset is the schema of the old dataset, plus these new columns (with indices starting from 0):
20: repetition of text
21: language
22: country (the abbreviated country code - NaN if coordinates are non-existent)
23: state/canton (NaN if non-applicable or coordinates non-existent)
24: postcode

Other columns we need are:
2: date and time of creation in the format 'yyyy-mm-dd hh:mm:ss'
4: longitude
5: latitude
"""

input_filename = sys.argv[1]
output_dir = sys.argv[2]
if (output_dir[len(output_dir)-1:len(output_dir)] != '/'):
    output_dir += '/'
conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
spark = SparkContext.getOrCreate(conf=conf)
data_rdd = spark.textFile(input_filename)
rdd2 = data_rdd.map(lambda x: x.split('\t'))
rdd2 = rdd2.map(lambda x: {'datetime': x[2], 'long': x[4], 'lat': x[5], 'lang': x[21], 'country': x[22], 'canton': x[23], 'postcode': x[24]})
output_list = rdd2.collect()
print('collected!')
pickle.dump(output_list, open(output_dir+'dataset.pkl'))
