<<<<<<< HEAD
import bs4, requests, re, os, datetime, pyperclip, webbrowser
=======
import bs4, requests, re, os, datetime
>>>>>>> 1dd2703397cdfec140d2adc45f65a5ecb747d2ea

def outputPetrolPrice(Url): #Outputs the Petrol Price web element including price, changetype and change amount to each petrol's dictionaries
    global soup

    res = requests.get(Url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    for petrol in Petrol_dict: 

        # Checks for type if it is present in row text
        Typesoup = soup.select(Selector_Type(Petrol_dict[petrol]['row']))
        if Petrol_dict[petrol]['type'] not in Typesoup[0].text.strip():
            raise Exception(Petrol_dict[petrol]['type']+' not present')

        # Cleans up the scraped data with regular expressions
        rawsoup = soup.select(Selector_Price(Petrol_dict[petrol]['row']))
        strippedsoup = rawsoup[0].text.strip() 
        mo = re.compile(r'\d\.\d\d')                                        #matching object regular expression
        numresult = re.findall(mo,strippedsoup)

        # Adds values into each petrol's dicts
        Petrol_dict[petrol]['currentprice']= numresult[0]
        if '↓'in strippedsoup: #checks if there is a positive or negative sign
            changesign = '-'
            changeword = 'decrease'
        elif '↑' in strippedsoup:
            changesign = '+'
            changeword = 'increase'
        else:
            raise Exception ('Neither increase nor decrease detected')
        Petrol_dict[petrol]['changesign'] = changesign
        Petrol_dict[petrol]['changeword'] = changeword
        Petrol_dict[petrol]['changeamount']= numresult[1]
    
    return

def Selector_Type(Row): # Shortens selector for petrol type 
    Selector_Type = '#post-1282 > div > table:nth-of-type(1) > tbody > tr:nth-of-type('+str(Row)+') > td:nth-of-type(1)'
    return Selector_Type

def Selector_Price(Row): # Shortens slector for petrol price
    Selector_Price = '#post-1282 > div > table:nth-of-type(1) > tbody > tr:nth-of-type('+str(Row)+') > td:nth-of-type(2)'
    return Selector_Price


#Dictionaries Used
Ron95_dict = {'type':'Ron95','row':'3'} #type aka. label and row on stle selector
Ron97_dict = {'type':'Ron97','row':'4'}
Diesel_dict = {'type':'Diesel','row':'5'}

#Data List Used
Petrol_dict = {'Ron95':Ron95_dict,'Ron97':Ron97_dict,'Diesel':Diesel_dict}

<<<<<<< HEAD

#Code Starts Here
price = outputPetrolPrice('https://www.petrolpricemalaysia.my/')
print (Petrol_dict)
=======

#Code Starts Here
price = outputPetrolPrice('https://www.petrolpricemalaysia.my/')
print (Petrol_dict)

# Gets the date for Wednesday's Price Change, assuming program is ran on the same week
today = datetime.date.today()
thisThur = today + datetime.timedelta(days=-today.weekday()+3, weeks=0)
nextWed = today + datetime.timedelta(days=-today.weekday()+2, weeks=1)

#Output XML:
>>>>>>> 1dd2703397cdfec140d2adc45f65a5ecb747d2ea

# Gets the date for Thursday's Price Change, assuming program is executed on the same week
today = datetime.date.today()
thisThur = today + datetime.timedelta(days=-today.weekday()+3, weeks=0)
nextWed = today + datetime.timedelta(days=-today.weekday()+2, weeks=1)

<<<<<<< HEAD
#Output XML:

XMLFile = open(os.path.join(os.getcwd(),'XML.xml'),'w')
XMLFile.write('''<?xml version="1.0" encoding="utf-8"?>
<feed>
<lastupdate>NEW WEEK ''' + thisThur.strftime("%d/%m/%y") + '''</lastupdate>
<ron95>'''+ Ron95_dict['currentprice']+'''</ron95>
<ron97>'''+ Ron97_dict['currentprice']+'''</ron97>
<diesel>'''+ Diesel_dict['currentprice']+'''</diesel>
<diff95>'''+Ron95_dict['changesign']+Ron95_dict['changeamount']+'''</diff95>
<diff97>'''+Ron97_dict['changesign']+Ron97_dict['changeamount']+'''</diff97>
<diffdiesel>'''+Diesel_dict['changesign']+Diesel_dict['changeamount']+'''</diffdiesel>
</feed>	''')
XMLFile.close()


#Output Facebook Post:

fbpost='''For the period, ''' + thisThur.strftime("%d %B %Y")  + ' (Thur) to ' + nextWed.strftime("%d %B %Y") + ''' (next Wed), new prices & changes (in RM):
RON 95 : RM'''+ Ron95_dict['currentprice']+''' per litre ('''+Ron95_dict['changeword']+''', '''+Ron95_dict['changesign']+Ron95_dict['changeamount']+''')
RON 97 : RM'''+ Ron97_dict['currentprice']+''' per litre ('''+Ron97_dict['changeword']+''', '''+Ron97_dict['changesign']+Ron97_dict['changeamount']+''')
Diesel, Euro 2M : RM'''+ Diesel_dict['currentprice']+''' per litre ('''+Diesel_dict['changeword']+''', '''+Diesel_dict['changesign']+Diesel_dict['changeamount']+''')

For current pricing, please download our app at: 
https://play.google.com/store/apps/details?id=alexanderzotov.petrolmalaysia&hl=en'''

print(fbpost)
pyperclip.copy(fbpost)
=======
#Output Facebook Post:

fbpost='''

For the period, ''' + thisThur.strftime("%d %B %Y")  + ' (Thur) to ' + nextWed.strftime("%d %B %Y") + ''' (next Wed), new prices & changes (in RM):
RON 95 : RM'''+ Ron95_dict['currentprice']+''' per litre ('''+Ron95_dict['changeword']+''', '''+Ron95_dict['changesign']+Ron95_dict['changeamount']+''')
RON 97 : RM'''+ Ron97_dict['currentprice']+''' per litre ('''+Ron97_dict['changeword']+''', '''+Ron97_dict['changesign']+Ron97_dict['changeamount']+''')
Diesel, Euro 2M : RM'''+ Diesel_dict['currentprice']+''' per litre ('''+Diesel_dict['changeword']+''', '''+Diesel_dict['changesign']+Diesel_dict['changeamount']+''')

For current pricing, please download our app at: 
https://play.google.com/store/apps/details?id=alexanderzotov.petrolmalaysia&hl=en'''

print(fbpost)


>>>>>>> 1dd2703397cdfec140d2adc45f65a5ecb747d2ea
