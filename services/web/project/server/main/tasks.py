# services/web/server/main/views.py


try:
    from pyspark import SparkContext, SparkConf
    from operator import add
except:
    print('error')


def create_task(words):
    conf = SparkConf().setAppName('letter count')
    sc = SparkContext(conf=conf)
    seq = words.split()
    data = sc.parallelize(seq)
    counts = data.map(lambda word: (word, 1)).reduceByKey(add).collect()
    sc.stop()
    return dict(counts)
