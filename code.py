import pandas as pd


orders_df = spark.read.format("csv").option('inderschema',True).load('/public/data/hello')

customers_df = spark.read.format("csv").option('inderschema',True).load('/public/data/hello')