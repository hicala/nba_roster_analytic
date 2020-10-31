#!/usr/bin/env python
# coding: utf-8

# In[1]:


# If you don't have Beautiful Soup, install with 'conda install beautifulsoup' in terminal
# Python requires us to explicitly load the libraries that we want to use:
import requests
import bs4
import re


# In[2]:


# Load a webpage into python so that we can parse it and manipulate it.
URL = 'https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks'


# In[3]:


# Control of Connection
# We just turned the website code into a Python object. 
response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text, "html.parser")


# In[4]:


# find all the tags with class city or number
data = soup.findAll(attrs={'class':['inline']})


# In[5]:


f = open('hilca_nba_team_roster.csv','w') # open new file, make sure path to your data file is correct
f.write("Name\tPos\tAge\tHT\tWT\tCollege\tSalary" + "\n") # write headers


# In[6]:


results = []
for element in data:
    TAG_RE = re.compile(r'<[^>]+>')
    text = TAG_RE.sub('', str(element))
    results.append(text)


# In[7]:


i = 0
j = 0
for item in results:
    if not item:
        i = 0
        j = j + 1
        if j > 1: f.write("\n")
    else:
        i = i + 1
        if (i == 1): f.write(item + "\t") # write name and add tabulator
        if (i == 2): f.write(item + "\t") # write pos and add tabulator
        if (i == 3): f.write(item + "\t") # write age and add tabulator
        if (i == 4): f.write(item + "\t") # write ht and add tabulator
        if (i == 5): f.write(item + "\t") # write wt and add tabulator
        if (i == 6): f.write(item + "\t") # write college and add tabulator
        if (i == 7): f.write(item) # write salary and add tabulator


# In[8]:


f.close() # close file

