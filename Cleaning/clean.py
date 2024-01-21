import pandas as pd

def cleaningDataframe(TableOneState,TableOneDistrict,TableTwo):
    # eliminating column of tableone
    TableOneDistrict = TableOneDistrict.drop(["tested_delta21_14","deceased_delta21_14","deceased_delta21_14","recovered_delta21_14","vaccinated1_delta21_14","vaccinated2_delta21_14"],axis=1)
    TableOneState = TableOneState.drop(["state_delta21_14_other","state_delta21_14_tested","state_delta21_14_deceased","state_delta21_14_recovered","state_delta21_14_vaccinated1","state_delta21_14_vaccinated2"],axis=1)

    #Performing join on table one and creating final TableOne
    TableOne = pd.merge(TableOneState, TableOneDistrict, on=["district", "district"])


    # replacing null with 0
    TableOne["population"] = TableOne["population"].replace('null','N/A')
    TableOne.replace('null','0',inplace=True)
    TableTwo.replace('null','0',inplace=True)


    # changing datatype of each column
    columns_to_exclude_tableOne = ["state","district","state_population","population"]
    columns_to_exclude_tableTwo = ["state_code","dates"]


    columns_to_convert_tableOne = [col for col in TableOne.columns if col not in columns_to_exclude_tableOne]
    columns_to_convert_tableTwo = [col for col in TableTwo.columns if col not in columns_to_exclude_tableTwo]

    TableOne[columns_to_convert_tableOne] = TableOne[columns_to_convert_tableOne].astype(int)
    TableTwo[columns_to_convert_tableTwo] = TableTwo[columns_to_convert_tableTwo].astype(int)
    TableTwo["dates"] = pd.to_datetime(TableTwo["dates"])
    
    return TableOne,TableTwo