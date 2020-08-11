# Pandas cheatsheet  

<!-- TOC -->

- [Pandas cheatsheet](#pandas-cheatsheet)
  - [quicklink](#quicklink)
  - [General rules](#general-rules)
  - [Import data](#import-data)
  - [Command for dataframe](#command-for-dataframe)
  - [df.loc and df.iloc](#dfloc-and-dfiloc)
  - [Datetime function](#datetime-function)
    - [datetime assign as index](#datetime-assign-as-index)
    - [select row between two non-indexed datetime](#select-row-between-two-non-indexed-datetime)
    - [date offset alias](#date-offset-alias)
  - [Commond for column of dataframe](#commond-for-column-of-dataframe)
  - [df.groupby and calculator](#dfgroupby-and-calculator)
  - [Lambda function](#lambda-function)
    - [Example: lambda function that will capitlaize strings](#example-lambda-function-that-will-capitlaize-strings)
- [.isin](#isin)
  - [The Mojave Desert states](#the-mojave-desert-states)
  - [Filter for rows in the Mojave Desert states](#filter-for-rows-in-the-mojave-desert-states)

<!-- /TOC -->



## quicklink  
[pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)    

[datacamp, pandas](https://datacamp-community-prod.s3.amazonaws.com/9f0f2ae1-8bd8-4302-a67b-e17f3059d9e8)    

[datacamp, data science](http://datacamp-community-prod.s3.amazonaws.com/9fb0cc3f-19fb-4be8-8d3f-68f10a95cc16)  

## General rules  
| Javascript | Python     |
|-           |-           |
|Object      |Dictionaries|
|Arrays      |Lists       |

## Import data 

- For sep = ',' 
    - df = pd.read_csv(url, index_col = 'column_name') 
    - *CSV: comma separated values*
- For sep = '\t'
    - df = pd.read_table(url, index_col = 'column_name')
- df['Column 1'] = df.col1  
eg, discipline[discipline['Yellow Cards'] > 2] = discipline[discipline.yellow_cards] > 2]
- set column 1 as index 
    - df.set_index('col1')
 

## Command for dataframe  

| Command for dataframe | Remark |  
| --------------------- | ------ |  
| df.info()                                                        | summary of dataframe                                                      |   
| df.shape                                                         | dimension of dataframe                                                    |   
| len(df)                                                          | length of dataframe                                                       |
| df.count()                                                       | by default, get the count of each column                                  |  
| df.index                                                         | the index (row labels)                                                    |   
| df.columns                                                       | list out all column_name as a list                                        |   
| df.dtypes                                                        | list the type of data                                                    |     
| df.describe()                                                    | descriptive statistics of string columns                                  |   
| df.describe(include = 'all')                                     | descriptive statistics, ingore datatypes                                  | 
| df.function.reset_index()                                        | reset_index with origin index, if index not available then auto generate  |
| df.function.unstack()                                            | return df without hierarchical index labels                               |
| new_df = df1.append(df2, ignore_index=True, sort=False)          | Join df1 and df2 into a single DataFrame called new_df                    | 

## df.loc and df.iloc 

| df.loc[] and df.iloc[] | Remarks | 
| ---------------------- | ------- |   
| df.loc[a:b]                                                      | select a range of rows from a to b                            |   
| df.loc[df.col1 conditions] <br>eg. df.loc[df.age >= 15]          | select rows, filter by col1 conditions                        |  
| df.loc[(df.col1 conditions), ['col1', 'col2']]                   | select col1 and col2 of rows, filter by col1 condition        |  
| if values of **index** is used as filter: <br>df.loc[['index1','index2'],['col1','col2','col3']]<br>eg, army.loc[['Maine','Alaska'],['deaths','size','deserters']]                      | Select the 'col1', 'col2' and 'col3' columns from 'index1' and 'index2'   |
| if values of **column** is used as filter <br>df.loc[df.col1.isin(['value1','value2','value3']),['col2','col3']] <br> eg, euro12.loc[euro12.Team.isin(['England','Italy','Russia']), ['Team','Shooting_Accuracy']] | Select the columns 'col2', 'col3' based on 'value1' and 'value2' of col1 |  
| df.iloc[a:b,c:d] <br>eg. df.iloc[1:3,2:4]                        | select rows index(a:b) and columns index(c:d)                 |   
| df.iloc[[a,b],[c,d]] <br>eg. df.iloc[[1,3],[2,4]]                | select rows index(a) and (b) and columns index(c) and (d)     |   
| df.iloc[[a:b]] <br>eg. df.iloc[[1:3]]                            | select rows index(a:b)                                        | 
| df.loc[["index5"]].iloc[:,2]                                     | select the third cell in the row index named index5           |

## Datetime function

| | |
| --- | --- |
| df.loc[pd.Timestamp('YYYY-MM-DD'):pd.Timestamp('YYYY-MM-DD')].head(1) | inspect the first row of specified period of datetime |
| df.loc['YYYY'].head(1) | inspect the first row of specified year |
|||

### datetime assign as index
```python
df.date_col = pd.to_datetime(df.date_col,format="%Y%m%d")

df.idxmax(0) #Get the row label of the maximum value in Pandas series
```


### select row between two non-indexed datetime
```python
start_time = '2019-01-01'
end_time = '2020-01-01'

df[(df['DateTime'] > start_time) & (df['DateTime'] <= end_time)]
```

### date offset alias   
- https://pandas.pydata.org/pandas-docs/version/0.9.1/timeseries.html
- some example:
```python
df.sample(20) # random sample 20 rows

df.resample('S').sum() # 'S' indicates seconds 
df.resample('T').sum() # 'T' indicates minutes 
df.resample('W').sum() # 'M' indicates week 
df.resample('M').sum() # 'M' indicates month 
df.resample('Q').sum() # 'Q' indicates quarter
df.resample('A').sum()
df.resample('AS').sum()
```


## Commond for column of dataframe

| Commond for column of dataframe | Remark |  
| ---                             | ---    |   
| df[['col1','col2','col3']]                                                 | printe the column 1, 2 and 3                           |
| df.col1.dtype                                                              | type of data for a particluar column                   |   
| df.col1.describe()                                                         | descriptive statistics of col1                         |   
| df['col1'] +-*/ df['col2']                                                  col1 plus / minus / mutliple / divide by col2           |  
| df.col1.value_counts().count()                                             | count the number of distinct values of col1            |   
| df.sort_values(by=['col1', 'col2'], ascending = False)                     | sorting 1st by col1, then 2nd by col2, decsending      |    
| df[df.col1 > number]  <br> eg. euro12[euro12.Goals > 6]                    | filter rows based on col1 values > 6                   |   
| df[df.col1.str.startswith('xxx')]<br>eg. euro12[euro12.Team.str.startswith('G')]| filter rows based on col1 values starts with 'xxx'|  
| df['col'] = temp_col<br>eg, chipo['peritem_price'] = peritem_price         | add newly generated column into dataframe, assign column name 'col'|
| df.drop(columns=['col1'])                                                  | drop col1                                              |  
| df[df.col1 == 'xxx']<br>eg, chipo[chipo.item_name == 'Veg Salad']          | select rows with "xxx" from column 1                   |
| df[df.col1 != 'xxx']<br>eg, chipo[chipo.item_name != 'Veg Salad']          | select rows without "xxx" from column 1                |
| df[df.col1 == 'xxx'].mean()       | select rows with "xxx" from column 1, give mean for all columns                                 |

## df.groupby and calculator

| Aggregated statistics with groups | Remark |  
| ---                               | ---    |
| df.groupby('col1').describe( )                                                         | decsciptive statistics of all columns grouped-by col1                     |
| df.groupby(['col1','col2']).col3.describe( )                                           | decsciptive statistics of col3 grouped-by col1 and col2                   |
| df.col1.sum( )                                                                         | sum of all value of a particular column (col1)                            | 
| df.agg(['sum','min','max','mean'])                                                    | Aggregate these functions over the rows                                   |
| df.col1.agg(['min','max','mean'])                                                     | Aggregate these functions over col1                                       |
| df.agg({'col1' : ['sum','min'], 'col2' : ['min','max']})                              | Different aggregations per column                                         |
| df.agg('mean', axis='columns')<br>add<br>sub<br>mul<br>div<br>mod # return whole number<br>pow<br>tbc       | Aggregate over the columns<br>+<br>-<br>*<br>/<br>//<br>**<br>%       |
| combine both <br> df.groupby[('col1','col2')].col3.agg(['sum','min','max','mean'])    | Aggregate these functions over grouped col3, grouped-by col1 and col2     |
| col1_pct_change = col1.pct_change( ) | percentage change of column 1 |
| col1.fillna(0, inplace=True) <br> pct_change.fillna(0, inplace=True) | Replace NaN values with 0 |

 = arithmetic operators: +, -, *, /, //, %, **


## Lambda function 

 ```python 
 df['new column name'] = df['column name'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')
 ```

### Example: lambda function that will capitlaize strings

```python
cap = lambda x: x.capitalize()  # only first letter upper case
upper = lambda x: x.upper()     # all letter upper case
lower = lambda x: x.lower()     # all letter lower case

df['col1'] = df['col1'].apply(cap)
df['col1'] = df['col1'].apply(upper)
df['col1'] = df['col1'].apply(lower)
```

# .isin
## The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
## Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]



