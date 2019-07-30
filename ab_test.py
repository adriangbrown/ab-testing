#!/usr/bin/python

from scipy.stats import norm
import numpy as np
import pandas as pd

def data_processing():
  """ Read csv and convert to pandas dataframe """

  df = pd.read_csv('/Users/adrianbrown-mac/Google Drive/Python/ab/flash_ab.csv', sep='|', skiprows=2, header=None, names=['email_group', 'customer_id', 'send_flag', 'open_flag'])
  return df

def z_test(data):
  """ Calculates the proportional conversion rate for each group and corresponding Z score and P Value """

  # filter control and test groups
  test = data[data['email_group'].str.contains('double')] 
  control = data[data['email_group'].str.contains('single')]
  
  # select success flag field for each group, convert to array and calculate mean
  control = np.array(control.iloc[:, 3])
  test = np.array(test.iloc[:, 3])
  mu_control = control.mean()
  mu_test = test.mean()
  print 'mu_control=', mu_control, 'mu_test=', mu_test 
  
  # calculate variance and standard deviation
  var_control = mu_control * (1-mu_control)
  var_test = mu_test * (1-mu_test)
  print 'var_control=', var_control, 'var_test=', var_test
  
  n_control = len(control) 
  n_test = len(test)
  print 'n_control=', n_control, 'n_test=', n_test
  
  z_score = (mu_test - mu_control)/np.sqrt(var_test/n_test + var_control/n_control)
  print 'z_score=', z_score
  p_value = norm.sf(abs(z_score)) # 1-sided test
  # p_value_2 = norm.sf(abs(z_score))*2 # 2-sided test

  print '{0:.5f}'.format(p_value)

if __name__ == '__main__':
  z_test(data_processing())
