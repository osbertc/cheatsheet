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
# simplified pie chart
chart_sex.plot.pie(autopct="%.1f%%")

#Using matplotlib
pie, ax = plt.subplots(figsize=[10,6])
labels = data.keys()
plt.pie(x=data, autopct="%.1f%%", explode=[0.05]*4, labels=labels, pctdistance=0.5)
plt.title("Delivery Tips by type", fontsize=14);
pie.savefig("DeliveryPieChart.png")
```
