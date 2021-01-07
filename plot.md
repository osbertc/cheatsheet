# Seaborn

- Seaborn is a Python data visualization library based on matplotlib. 
- It provides a high-level interface for drawing attractive and informative statistical graphics.

```python 
import seaborn as sns
```
## histogram

```python
# create histogram
ttbill = sns.distplot(tips.total_bill)

# set lables and titles
ttbill.set(xlabel = 'Value', ylabel = 'Frequency', title = "Total Bill")

```

## scatter plot

```python 
sns.scatterplot(x = "total_bill", y = "tip", data = tips)

lm = sns.lmplot(x = 'Age', y = 'Fare', data = titanic, hue = 'Sex', fit_reg=False)
```

## pair plot

- Pair compare matrix
- Plot pairwise relationships in a dataset
- [read more](https://seaborn.pydata.org/generated/seaborn.pairplot.html)

```python
sns.pairplot(tips)
```

## strip plot 
- scatter plot by groups (hue = "colName")
- only alone categorical axis, spread out dots when you have many points and they overlap (jitter = True / 1)

```python
sns.stripplot(x = "tip", y = "day", hue = "sex", data = tips, jitter = True)
```

## box plot

```python
sns.boxplot(x = "day", y = "total_bill", hue = "time", data = tips)
```

## creates FacetGrid
- FacetGrid = Multi-plot grid for plotting conditional relationships

```python
# multi-plot **histogram**
g = sns.FacetGrid(tips, col = "time")
g.map(plt.hist, "tip")

# multi-plot **scatter plot**
g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
g.map(plt.scatter, "total_bill", "tip", alpha =.7)
```

## Pie Chart
```python

# First groupby the data by delivery type
chart_sex = titanic_Pid.groupby("Sex")["Sex"].count()
chart_sex

# 1. simplified pie chart
chart_sex.plot.pie(autopct="%.1f%%")

# 2. Using matplotlib
pie, ax = plt.subplots(figsize=[10,6])
labels = data.keys()

# Create a pie chart
plt.pie(
    # using chart_sex
    x=chart_sex,
    
    # with the labels being officer names
    labels = labels
    
    # with no shadows
    shadow = False,
    
    # with colors
    colors = ['blue','red'],
    
    # with one slide exploded out
    explode = (0.15 , 0),
    
    # with the start angle at 90%
    startangle = 90,
    
    # with the percent listed as a fraction
    autopct = '%1.1f%%'
    )

plt.title("Delivery Tips by type", fontsize=14)

pie.savefig("DeliveryPieChart.png")
```



