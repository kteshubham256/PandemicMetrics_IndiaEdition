from Data.data import *


    
def reading(json_data_One,json_data_Two):
    # iterating json_data_one
    for state in json_data_One:
        try:
            for district in json_data_One[state]["districts"]:
                for s_c_t in ["delta","delta7","delta21_14","total"]:
                    delta_data = json_data_One[state].get(s_c_t, {})
                    for type in ["confirmed", "deceased", "recovered", "vaccinated1", "vaccinated2","tested","other"]:
                        value = delta_data.get(type,"null")
                        TableOneState[f"state_{s_c_t}_{type}"].append(value)
                TableOneState["state"].append(state)
                TableOneState["district"].append(district)
                TableOneState["state_population"].append(json_data_One[state]["meta"]["population"])
                TableOneDistrict["district"].append(district)
                    
                for delta_type in ["delta", "delta7", "delta21_14","meta","total"]:
                    delta_data = json_data_One[state]["districts"][district].get(delta_type, {})
                    if delta_type == "meta":
                            v = delta_data.get("population", "null")
                            TableOneDistrict["population"].append(v)
                    else:
                        for covid_type in ["confirmed", "deceased", "recovered", "vaccinated1", "vaccinated2","tested"]:
                            value = delta_data.get(covid_type, "null")
                            TableOneDistrict[f"{covid_type}_{delta_type}"].append(value)
        except Exception as e:
            print(state,e)

    # iteration for json_data_Two
    for state in json_data_Two:
        try:
            for dates in json_data_Two[state]["dates"]:
                TableTwo["state_code"].append(state)
                TableTwo["dates"].append(dates)
                for covid_type in ["delta","delta7","total"]:
                    delta_data = json_data_Two[state]["dates"][dates].get(covid_type, {})
                    for type in ["confirmed", "deceased", "recovered", "vaccinated1", "vaccinated2","tested","other"]:
                        value = delta_data.get(type,"null")
                        TableTwo[f"{type}_{covid_type}"].append(value)
        except Exception as e:
            print(e)