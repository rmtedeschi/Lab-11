data = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

#Add data to dictionary and then put dictionary in list:
#Hard coded it because the data is unorganized and I have no clue 
#how to do that automatically
dictitems = []
tempdict = {
    "Name": data[1],
    "Number": data[0],
    "Hourly": data[2]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[4],
    "Number": data[3],
    "Hourly": data[5]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[7],
    "Number": data[6],
    "Hourly": data[8]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[12],
    "Number": data[11],
    "Hourly": data[10]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[13],
    "Number": data[15],
    "Hourly": data[14]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[17],
    "Number": data[18],
    "Hourly": data[19]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[22],
    "Number": data[21],
    "Hourly": data[23]
}
dictitems.append(tempdict)

tempdict = {
    "Name": data[26],
    "Number": data[25],
    "Hourly": data[24]
}
dictitems.append(tempdict)

#Adding a key in each dictionary for the total hourly rate
for i in range(len(dictitems)):
    dictitems[i]['Total_hourly_rate'] = dictitems[i]['Hourly'] * 1.3


#Creating new list and adding dictionary information
#of the person to the new list if they meet the requirements

underpaid_salaries = []

for i in range(len(dictitems)):
    if dictitems[i]['Total_hourly_rate'] > 28.15 and dictitems[i]['Total_hourly_rate'] < 30.65:
        underpaid_salaries.append(dictitems[i])

#Creating a new list, calculating raises, and appending name + raise
#to the new list

company_raises = []

for i in range(len(dictitems)):
    if dictitems[i]['Hourly'] > 22 and dictitems[i]['Hourly'] < 24:
        dictitems[i]['Hourly'] = dictitems[i]['Hourly'] * .05
        company_raises.append(dictitems[i]['Name'])
        company_raises.append("5%")
    elif dictitems[i]['Hourly'] > 24 and dictitems[i]['Hourly'] < 26:
        dictitems[i]['Hourly'] = dictitems[i]['Hourly'] * .04
        company_raises.append(dictitems[i]['Name'])
        company_raises.append("4%")
    elif dictitems[i]['Hourly'] > 26 and dictitems[i]['Hourly'] < 28:
        dictitems[i]['Hourly'] = dictitems[i]['Hourly'] * .03
        company_raises.append(dictitems[i]['Name'])
        company_raises.append("3%")
    else:
        dictitems[i]['Hourly'] = dictitems[i]['Hourly'] * .02
        company_raises.append(dictitems[i]['Name'])
        company_raises.append("2%")


#printing out data:
print("\nDictionary items: \n\n", dictitems)
print("\nunderpaid salaries: \n\n", underpaid_salaries)
print("\nCompany raises: \n\n", company_raises)
