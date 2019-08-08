# Flash Sale AB test - Determine whether the results from an A/B test are significant, and if so make a decision to change current initiatives or maintain status quo.

## Approach - Process csv that includes the customer id, group name (A/B), and success event flag.  From there conduct a Z test to determine if the mean proportional success average of each group (in this case purchase conversion, calculate the variance, n-counts of each group, and finally a Z score, and p value.  P value will determine if significance falls within a pre-determined level of confidence

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
