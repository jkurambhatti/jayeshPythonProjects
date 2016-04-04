'''
    in this project we  will be downloading any text file from internet(for eg: a .csv file)
    in this case we will download all stock data i.e historical prices of stocks any company
    finance.yahoo has data in .csv file
    and then we will write to a file
'''



import urllib

sbi_url = "http://real-chart.finance.yahoo.com/table.csv?s=SBIN.NS&d=3&e=1&f=2016&g=d&a=0&b=1&c=1996&ignore=.csv"

def download_stock_data(url):
    r = urllib.urlopen(url)
    fw = open("sbi_history1", "w")

    for i in r:
        st = str(i)
        fw.write(st)

    fw.close()

download_stock_data(sbi_url)











