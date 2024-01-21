import pandas as pd
from Data.data import TableOneState,TableOneDistrict,TableTwo

def creatingDataframe():
    # creating dataframe from dictionary
    TableOneState_df = pd.DataFrame.from_dict(TableOneState,orient='index')
    TableOneDistrict_df = pd.DataFrame.from_dict(TableOneDistrict,orient='index')
    TableTwo_df = pd.DataFrame.from_dict(TableTwo,orient='index')
    
    # using transpose because the length of the list is not equal
    TableOneDistrict_df = TableOneDistrict_df.transpose()
    TableOneState_df = TableOneState_df.transpose()
    TableTwo_df = TableTwo_df.transpose()
    
    return TableOneState_df,TableOneDistrict_df,TableTwo_df