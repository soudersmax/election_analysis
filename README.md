# Election Analysis
## Project Overview
The purpose of this project is to create a script to perform an audit on local congressional election results. This audit must include: 

1. Total number of votes cast
2. County Turnout Breakdown
   1. Number and percentage of votes from each county
   2. Determine county with the largest voter turnout
3. Candidate Vote Breakdown
4. Winning Candidate Summary
   1. Name, vote count, and vote percentage of winning candidate


## Resources

- Software: Python 3.7.6, Visual Studio code 1.47.3
- Data Source: election_results.csv

## Results

The analysis of the election results shows that:

- There were 369,711 total votes in the precinct
- County Turnout 
  - Denver: 82.8% (306,055 ballots)
  - Jefferson: 10.5% (38,855 ballots)
  - Arapahoe: 6.7% (24,801 ballots) 
- Candidate Results:
  - Diana DeGette: 73.8% (272,892 votes)
  - Charles Casper Stockham: 23.0% (85,213 votes)
  - Raymon Anthony Doane: 3.1% (11,606 votes)
- Final Winner:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

## Summary

​	By using a database of ballot ID, county, and candidate selection, this script automatically calculates the total votes, the votes by county, the votes by candidate, and the winning candidate. This could easily be expanded or altered to fit any election or election scenario. 

​	For example, to use this tool at a state level, one could compile a database that includes all of the above as well as an additional field entitled "Precinct." The script could be modified to include all of the same information *as well as a precinct breakdown*. Because the precinct is a step higher in the hierarchy of election data, it would be easy to create an additional loop to run through precincts, calculating the same information as we have here for county and so on, providing detailed results for a state-based popular election. 

​	The script could also be modified to work for electoral college-based elections. By creating a dictionary with (key) District and (value) electoral votes assigned to that district, it could distribute them as earned through the popular vote and create an output that also includes a summation of each candidates number and percentage of electoral votes and the winner of the electoral plurality. 

