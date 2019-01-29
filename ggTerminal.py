from tabulate import tabulate
import pandas as pd

#Get Sky Sports Racing Race URL
raceurl=raw_input('Enter SSR URL: ')

#Download source
dfs = pd.read_html(raceurl)[0]

#Convert HTML table to Pandas Dataframe
df = pd.DataFrame(data=dfs)

#Drop blank/ extra columns
df.drop(df.columns[[2,8,10,9]], axis=1, inplace=True)

#Rename columns
df.columns = ['No', 'Form', 'Horse', 'Age', 'Weight', 'Trainer', 'Jockey']

#Get rid of days since last run
df['Horse'].str.replace('\d+', '')

#Output table
#print(df)

print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))