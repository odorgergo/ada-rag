from pyspark import SparkContext, SparkConf
import sys
import geopy as gp

def find_location(lat, lon):
    locator = gp.geocoders.Nominatim()
    return locator.reverse(str(lat)+','+str(lon)).raw['address']

def append_location(x):
        a = x.split('\t')
    #try:
        lat = float(a[10])
        lon = float(a[11])
        location = find_location(lat,lon)
        try:
            country = location['country_code']
        except:
            country = "NaN1"
        try:
            canton = location['state']
        except:
            canton = "NaN1"
        try:
            postcode = location['postcode']
        except:
            postcode = "NaN1"
    #except:
    #    country = "NaN2"
    #    canton = "NaN2"
    #    postcode = "NaN2"
        return x + '\t' + country + '\t' + canton + '\t' + postcode + '\t' + a[10] + '\t' + a[11]
    

input_filename = sys.argv[1]
output_dir = sys.argv[2]

conf = SparkConf().set("spark.hadoop.validateOutputSpecs", "false")
spark = SparkContext.getOrCreate(conf=conf)
data_rdd = spark.textFile(input_filename)

data_rdd = data_rdd.map(append_location)

data_rdd.saveAsTextFile(output_dir)
