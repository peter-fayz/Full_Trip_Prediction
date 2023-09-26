import requests
import pandas as pd

test= {'paid at': [0] ,
         'accepts marketing':['no'],
         'billing province':['ALX'],
         'shipping province':['ALX'],
         'payment method':['Cash on Delivery (COD)'],
         'source':['web'],
         'created month':[2],
         'created day':[5],
         'shipping':[60],
         'total':[267.85],
         'lineitem quantity':[10]}

pd.DataFrame(test).to_json('test.json')

df = pd.read_json('test.json')

print(df)

dff = df.to_json()

url = 'http://localhost:8085/api'

params = (
    ('key', 'Full_Trip_Prediction'), 
         )


r = requests.post(url , data=dff , params = params)



'''test= {'paid at': [0,1,0,0,1] ,
         'accepts marketing':['no','no','yes','no','yes'],
         'billing province':['ALX','out of egypt','C','IS','C'],
         'shipping province':['ALX','out of egypt','C','IS','C'],
         'payment method':['Cash on Delivery (COD)','others','Cash on Delivery (COD)','Cash on Delivery (COD)',
                           'Cash on Delivery (COD)'],
         'source':['web','shopify_draft_order','web','shopify_draft_order','web'],
         'created month':[2,7,8,9,4],
         'created day':[5,2,7,11,4],
         'shipping':[60,3000,50,35,50],
         'total':[267.85,5511.5,1542,150,500],
         'lineitem quantity':[10,15,20,2,4]}'''