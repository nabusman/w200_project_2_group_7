import pandas as pd

# Load data from stata
df = pd.read_stata('GSS7216_R1a.dta', convert_categoricals = False)

# Save data as HDFStore
store = pd.HDFStore('store.h5')
store['df'] = df