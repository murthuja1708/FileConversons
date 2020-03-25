# -*- coding: utf-8 -*-


import json
import pandas as pd

contact=r'C:\Users\murthuja.mohammed\Documents\aql\Member_Contact.json'
commun=r'C:\Users\murthuja.mohammed\Documents\aql\Member_Communication.json'
link=r'C:\Users\murthuja.mohammed\Documents\aql\Member_link.json'

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
final_merge=contact_merge.merge(link_df,on="identifier").to_json('test.json',orient="records")