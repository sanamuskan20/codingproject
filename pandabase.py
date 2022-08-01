import pandas as pd

fields={ 'first_name':[],
        'last_name':[],
        'date_of_birth':[],
        'address':[]}

df = pd.DataFrame(fields)
df.to_csv('pandasbase.csv')