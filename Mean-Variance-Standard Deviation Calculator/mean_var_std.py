def calculate(lst):
  import numpy as np

  if len(lst) != 9:
    raise ValueError('List must contain nine numbers.')
    return "List must contain nine numbers."
  
  a = np.asarray([lst[0:3], lst[3:6], lst[6:9]])
    
  #Mean
  mean_c = np.mean(a, axis=0).tolist()
  mean_r = np.mean(a, axis=1).tolist()
  mean = np.mean(a)
  mean = [mean_c,mean_r,mean]
    
  # Variance
  var_c = np.var(a, axis=0).tolist()
  var_r = np.var(a, axis=1).tolist()
  var = np.var(a)
  var = [var_c,var_r,var]

  # standard Deviation
  std_c = np.std(a, axis=0).tolist()
  std_r = np.std(a, axis=1).tolist()
  std = np.std(a)
  std= [std_c,std_r,std]

  # MAX
  max_c = np.max(a, axis=0).tolist()
  max_r = np.max(a, axis=1).tolist()
  max1 = np.max(a)
  max1 = [max_c,max_r,max1]

  # MIN
  min_c = np.min(a, axis=0).tolist()
  min_r = np.min(a, axis=1).tolist()
  min1 = np.min(a)
  min1 = [min_c,min_r,min1]

  # SUM
  sum_c = np.sum(a, axis=0).tolist()
  sum_r = np.sum(a, axis=1).tolist()
  sum1 = np.sum(a)
  sum1 = [sum_c,sum_r,sum1]

  calculations = {'mean':mean,'variance':var,'standard deviation': std,'max':max1, 'min': min1, 'sum': sum1}

  return calculations