# A NBA Statistical Analytical Research: Atlanta Hawks Roster. 2019-2020

## Summary

This study is part of a serie of statistical analysis in the composition and salary earned by main and key players in the NBA. The maing goal is to get all the information to run a prediction mmodel to simulate a fucntion from the performance versus Salary

I am using Beautiful Soup for the this Python app. Beautiful Soup is a Python library for parsing data out of HTML and XML files (aka webpages). It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

The major concept with Beautiful Soup is that it allows you to access elements of your page by following the CSS structures, such as grabbing all links, all headers, specific classes, or more. It is a powerful library. Once we grab elements, Python makes it easy to write the elements or relevant components of the elements into other files, such as a CSV, that can be stored in a database or opened in other software.

The data I used came from Atlanta Hawks Roster. Reference: https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks

## Main goal

+ To access all of the content from the source code of the webpage with Python
+ Parse and extract data. 
+ Save the info in CSV file for further analysis.

## Methodology

1. Import Modules
2. Get the URL link
3. Navigate the URL Data Structure
4. Testing out data requests
5. Write data to a file in pseudo-code:
    + Open up a file to write in and append data. 
    + Write headers
    + Run for loop that will make it clean the HTML tags and add their values in an array results
    + Run for loop that will write elements of the array to file
    + When complete, close the file
6. The output file in CSV format.

## Data info extracted:

Name, POS ,Age ,HT ,WT ,College and Salary of Team Roster
