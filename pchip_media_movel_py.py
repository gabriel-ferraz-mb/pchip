# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:27:26 2022

@author: gabriel.ferraz
"""
import sys
import numpy as np
import pandas as pd
import json
pd.options.mode.chained_assignment = None  # default='warn'
#pd.set_option('display.max_rows', None, 'display.max_columns', None)

#Get last samples extracted folder
def execute(json_str):
    
    stud_obj = json.loads('{"date": "11/07/2021 00:00:00", "value":"0.89621"},{"date": "14/07/2021 00:00:00", "value":"0.74108"},{"date": "16/07/2021 00:00:00", "value":"0.91226"},{"date": "19/07/2021 00:00:00", "value":"0.89969"},{"date": "21/07/2021 00:00:00", "value":"0.91781"},{"date": "24/07/2021 00:00:00", "value":"0.86071"},{"date": "26/07/2021 00:00:00", "value":"0"},{"date": "29/07/2021 00:00:00", "value":"0.88994"},{"date": "31/07/2021 00:00:00", "value":"0.89271"},{"date": "03/08/2021 00:00:00", "value":"0.85904"},{"date": "05/08/2021 00:00:00", "value":"0.77219"},{"date": "08/08/2021 00:00:00", "value":"0.83248"},{"date": "10/08/2021 00:00:00", "value":"0"},{"date": "13/08/2021 00:00:00", "value":"0.83234"},{"date": "15/08/2021 00:00:00", "value":"0.76973"},{"date": "18/08/2021 00:00:00", "value":"0.74372"},{"date": "20/08/2021 00:00:00", "value":"0"},{"date": "23/08/2021 00:00:00", "value":"0"},{"date": "25/08/2021 00:00:00", "value":"0"},{"date": "28/08/2021 00:00:00", "value":"0.72097"},{"date": "30/08/2021 00:00:00", "value":"0.70967"},{"date": "02/09/2021 00:00:00", "value":"0"},{"date": "04/09/2021 00:00:00", "value":"0"},{"date": "07/09/2021 00:00:00", "value":"0"},{"date": "09/09/2021 00:00:00", "value":"0"},{"date": "12/09/2021 00:00:00", "value":"0.61738"},{"date": "14/09/2021 00:00:00", "value":"0"},{"date": "17/09/2021 00:00:00", "value":"0"},{"date": "19/09/2021 00:00:00", "value":"0"},{"date": "22/09/2021 00:00:00", "value":"0.30943"},{"date": "24/09/2021 00:00:00", "value":"0.60651"},{"date": "27/09/2021 00:00:00", "value":"0.57606"},{"date": "29/09/2021 00:00:00", "value":"0"},{"date": "02/10/2021 00:00:00", "value":"0.33412"},{"date": "04/10/2021 00:00:00", "value":"0"},{"date": "07/10/2021 00:00:00", "value":"0"},{"date": "09/10/2021 00:00:00", "value":"0"},{"date": "12/10/2021 00:00:00", "value":"0"},{"date": "14/10/2021 00:00:00", "value":"0"},{"date": "17/10/2021 00:00:00", "value":"0"},{"date": "19/10/2021 00:00:00", "value":"0.19574"},{"date": "22/10/2021 00:00:00", "value":"0.20327"},{"date": "24/10/2021 00:00:00", "value":"0.17668"},{"date": "27/10/2021 00:00:00", "value":"0.1689"},{"date": "29/10/2021 00:00:00", "value":"0.16926"},{"date": "01/11/2021 00:00:00", "value":"0.17016"},{"date": "03/11/2021 00:00:00", "value":"0"},{"date": "06/11/2021 00:00:00", "value":"0"},{"date": "08/11/2021 00:00:00", "value":"0.19643"},{"date": "11/11/2021 00:00:00", "value":"0.19825"},{"date": "13/11/2021 00:00:00", "value":"0.20241"},{"date": "16/11/2021 00:00:00", "value":"0"},{"date": "18/11/2021 00:00:00", "value":"0"},{"date": "21/11/2021 00:00:00", "value":"0.24047"},{"date": "23/11/2021 00:00:00", "value":"0"},{"date": "26/11/2021 00:00:00", "value":"0"},{"date": "28/11/2021 00:00:00", "value":"0"},{"date": "01/12/2021 00:00:00", "value":"0.36846"},{"date": "03/12/2021 00:00:00", "value":"0.35605"},{"date": "06/12/2021 00:00:00", "value":"0"},{"date": "08/12/2021 00:00:00", "value":"0"},{"date": "11/12/2021 00:00:00", "value":"0"},{"date": "13/12/2021 00:00:00", "value":"0"},{"date": "16/12/2021 00:00:00", "value":"0"},{"date": "18/12/2021 00:00:00", "value":"0"},{"date": "21/12/2021 00:00:00", "value":"0.49682"},{"date": "23/12/2021 00:00:00", "value":"0.65689"},{"date": "26/12/2021 00:00:00", "value":"0"},{"date": "28/12/2021 00:00:00", "value":"0"},{"date": "31/12/2021 00:00:00", "value":"0"},{"date": "02/01/2022 00:00:00", "value":"0"}]')
    #stud_obj = json.loads(json_str)
    df = pd.json_normalize(stud_obj)
    #Set the path with the last samples extracted
    
    # set 0 to Nan
    df["value"].replace("0",np.nan, inplace=True)           
    
    #Set date to DateTimeIndex
    df["date"] = pd.to_datetime(df['date'],dayfirst=True)
    df["value"] = pd.to_numeric(df["value"])
    df = df.sort_values(by="date")
    df = df.set_index('date')
    
    
    #interpolate "time"
    interp =df.interpolate(method = "time")
    
    #Seta NDVI de -1 a 1 
    interp[interp < -1] = -1
    interp[interp >  1] =  1
    interp["value"].fillna(0, inplace = True)
    interp
    out = interp.to_json(orient='table')#.split('"data":')[1]
    return out
    
def main(input_Csharp):  
    #print("TESTE")
    results = execute(input_Csharp)
          
    #now = datetime.now()
    print (results)
    #now = now.strftime("%d-%m-%Y %H:%M:%S")
    #with open('D:\\CONSOLE_APPS\\identificacao_cultura\\file_' + now + '.txt', 'a') as file:
        #file.write(results)
    return results
    

if __name__ == '__main__':
    main(sys.argv[1])

