project:
take CSV exported from CME Gateway to calculate if user is meeting CME requirements

input:
csv file called 'CMEgateway.csv'
several examples are here for testing, use CMEgateway_All.csv

program:
parse out unnecessary data?
divide by year (will be doing rolling 3 calendar year lookbacks)
divide into MPCEC and SAM totals

output:
determine if meeting MPCEC (>=75 per rolling lookback) for each lookback year
i.e. Show 'PASS' if meeting from 2020 - 2022, 2019 - 2021, etc.

determine if meeting SAM only if not doing OLAs (>=15 per rolling lookback)