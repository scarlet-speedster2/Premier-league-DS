import pandas as pd

import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"




def getdata(urls):

    l = len(urls)


    for i in range(0,l):

        df = pd.read_html(urls[i])
        print(df)


        for j in range(0,len(df)):

            df[j].to_csv("data.csv",mode="a",sep="|")





n = int(input("Enter the number of urls"))

urls = []

opener = AppURLopener()
for i in range(0,n):

    ele = input()
    urls.append(opener.open(ele))



#print(urls)
getdata(urls)





