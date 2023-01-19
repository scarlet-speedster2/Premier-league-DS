import pandas as pd



def getdata(urls):

    l = len(urls)


    for i in range(0,l):

        df = pd.read_html(urls[i])
        print(df)


        for j in range(0,len(df)):

            df[j].to_csv("data.csv",mode="a",sep="|")





n = int(input("Enter the number of urls"))

urls = []

for i in range(0,n):

    ele = input()
    urls.append(ele)



#print(urls)
getdata(urls)





