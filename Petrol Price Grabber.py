import bs4, requests, re

def outputPetrolPrice(Url): #Outputs the Petrol Price web element including price, changetype and change amount
    global soup
    
    res = requests.get(Url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    Ron95price = checkforprice(Ron95_dict['type'],Ron95_dict['row'])
    Ron95_dict.setdefault('price',Ron95price[0].text.strip()) #adds a price key and a price value to Ron95 dict
    Ron97price = checkforprice(Ron97_dict['type'],Ron97_dict['row'])
    
    Dieselprice = checkforprice(Diesel_dict['type'],Diesel_dict['row'])      
    return [Ron95_dict['price'],Ron97price[0].text.strip(),Dieselprice[0].text.strip()]


def checkforprice(Type,Row): # Checks for Petrol Type based on Row, runs exception if not in
    global soup
    
    Typesoup = soup.select(Selector_Type(Row))
    if Type not in Typesoup[0].text.strip():
        raise Exception(Type+' not present')
    Pricesoup = soup.select(Selector_Price(Row))
    return Pricesoup 

def Selector_Type(Row): # Shortens type selector for other function 
    Selector_Type = '#post-1282 > div > table:nth-of-type(1) > tbody > tr:nth-of-type('+str(Row)+') > td:nth-of-type(1)'
    return Selector_Type

def Selector_Price(Row): # Shortens price selector for other function 
    Selector_Price = '#post-1282 > div > table:nth-of-type(1) > tbody > tr:nth-of-type('+str(Row)+') > td:nth-of-type(2)'
    return Selector_Price

def web_to_values(webdata):        #takes the web data and strips and convert into values
    mo = re.compile(r'\d\.\d\d')
    searchstring = (webdata)
    numresult = re.findall(webdata,searchstring)
    print('-------')
    print(numresult[0])
    if '↓'in searchstring:
        print('decrease')
    elif '↑' in searchtring:
        print('increase')
    else:
        raise Exception ('Neither increase nor decrease detected')
    print(numresult[1])
    return







#Dictionaries Used
Ron95_dict = {'type':'Ron95','row':'3'} #type aka. label and row on stle selector
Ron97_dict = {'type':'Ron97','row':'4'}
Diesel_dict = {'type':'Diesel','row':'5'}

#Data List Used
Petrol_dict = {'Ron95':Ron95_dict,'Ron97':Ron97_dict,'Diesel':Diesel_dict}

price = outputPetrolPrice('https://www.petrolpricemalaysia.my/')

print(Petrol_dict['Ron95']['row']+' Woo '+ Petrol_dict['Ron95']['price'])
print(price[0])
print(price[1])
print(price[2])







# take each of this string, and strip it to its raw value

#RM 2.29 (↓ RM0.01)


for i in range(3):
    mo = re.compile(r'\d\.\d\d')
    searchstring = price[i]
    numresult = re.findall(mo,searchstring)
    print('-------')
    print(numresult[0])
    if '↓'in searchstring:
        print('decrease')
    elif '↑' in searchtring:
        print('increase')
    else:
        raise Exception ('Neither increase nor decrease detected')
    print(numresult[1])

# Ron95 = {'price':'','changetype':'','changeamt':''}
# Ron97 = {'price':'','changetype':'','changeamt':''}
# Diesel = {'price':'','changetype':'','changeamt':''}
