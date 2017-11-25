from pyspark import SparkContext, SparkConf
import sys
import geopy as gp

def find_location(lat, lon):
    locator = gp.geocoders.Nominatim()
    return locator.reverse(str(lat)+','+str(lon)).raw['address']

def append_location(x):
    a = x.split('\t')
    try:
        lat = float(a[5])
        lon = float(a[4])
        location = find_location(lat,lon)
        try:
            country = location['country_code']
        except:
            country = "NaN"
        try:
            canton = location['state']
        except:
            canton = "NaN"
        try:
            postcode = location['postcode']
        except:
            postcode = "NaN"
    except:
        country = "NaN"
        canton = "NaN"
        postcode = "NaN"
    return x + '\t' + country + '\t' + canton + '\t' + postcode
    

input_filename = sys.argv[1]
output_dir = sys.argv[2]

conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
spark = SparkContext.getOrCreate(conf=conf)
data_rdd = spark.textFile(input_filename)

data_rdd = data_rdd.map(append_location)

data_rdd.saveAsTextFile(output_dir)
