# -*- coding: utf-8 -*-


import json
import pandas as pd
import os

dirs=['ExcelFiles','JsonFiles','csvFiles']

for i in dirs:
    if i not in os.listdir():
        os.mkdir(i)
        
final_path=os.path.join(os.getcwd(),'JsonFiles')
contact=r'JsonFiles\Member_Contact.json'
commun=r'JsonFiles\Member_Communication.json'
link=r'JsonFiles\Member_link.json'
output_file_name="members.json"

with open(contact,'r') as con:
    contact_data=json.loads(con.read())
    
with open(commun,'r') as com:
    commun_data=json.loads(com.read())
    
with open(link,'r') as l:
    link_data=json.loads(l.read())
    
link_df=pd.DataFrame(link_data)
commun_df=pd.DataFrame(commun_data)
contact_df=pd.DataFrame(contact_data)

contact_merge=contact_df.merge(commun_df,on="identifier")
final_merge=contact_merge.merge(link_df,on="identifier").to_json(os.path.join(final_path,output_file_name),orient="records")