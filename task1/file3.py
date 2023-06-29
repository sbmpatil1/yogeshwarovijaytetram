 import numpy as np
import pandas as pd

def create_series():
  data = np.random.randint(1, 10, 10)
  index = np.arange(1, 11)
  series = pd.Series(data, index=index)
  return series

if __name__ == "__main__":
  series = create_series()
  print(series)
