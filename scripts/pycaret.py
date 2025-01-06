from pycaret.time_series import *

# Select only the target column
df_target = df[['Close']]

# PyCaret setup
ts = setup(data=df_target, target='Close', session_id=123)