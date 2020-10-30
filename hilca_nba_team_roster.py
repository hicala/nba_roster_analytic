import requests
import bs4
from bs4 import BeautifulSoup as bs


# load and get the website
response = requests.get('http://duspviz.mit.edu/_assets/data/county_housing_stats.html')

# create the soup
soup = bs4.BeautifulSoup(response.text, "html.parser")

# find all the tags with class city or number
data = soup.findAll(attrs={'class':['name','fips','tot-pop','median-income','no-housing-units','med-home-val','owner-occupied','house-w-debt','house-wo-debt']})

# print 'data' to console
print(data)

# Output file

f = open('hilca_us_stats_data.csv','a') # open new file, make sure path to your data file is correct

p = 0 # initial place in array
l = len(data)-1 # length of array minus one


f.write("County, State, FIPS Code, Total Pop, Median Income ($), No. of Housing Units, Median Home Value ($), No. of Owner Occupied Housing Units, No. of Owner Occ. Housing Units with Debt, No. of Owner Occ. Housing Units without Debt\n") #write headers


while p < l: # while place is less than length
    f.write(data[p].string + ", ") # write county and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write FIPS and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Total Pop and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Median Income and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Housing Units and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write Median Home Value and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Owner Occupied Housing Units and add comma
    p = p + 1 # increment
    f.write(data[p].string + ", ") # write No. of Owner Occ. Housing Units with Debt and add comma
    p = p + 1 # increment
    f.write(data[p].string + "\n") # write No. of Owner Occ. Housing Units without Debt and line break
    p = p + 1 # increment

    
f.close() # close file