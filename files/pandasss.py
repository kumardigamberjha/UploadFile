import vaex
import pandas as pd
import numpy as np
n_rows = 1000000
n_cols = 2
df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, n_cols)), columns=['col%d' % i for i in range(n_cols)])

file_path = 'big_file.xlsx'
df.to_fwf(file_path, index=False)