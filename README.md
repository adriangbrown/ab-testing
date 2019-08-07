# Flash Sale AB test

## Getting Started
Requirements:  csv with a/b test data, python on computer
Files used in this example:
  -flash_ab.py
  -flash_ab.csv

## Walk-through of flash_ab.py
libraries imported:  scipy for calculating p value, pandas to process data

Functions

data_processing() - reads csv file with customer, a/b group and success flags

testing()
  -read in data_processing() for data
  -filter control and test groups into seperate dataframes
  -create an array out of the success flag field and determine mean for each group
  -calculate variance for each group
  -calculate population sizes
  -calculate Z score (proportions test) and p values to determine significance
