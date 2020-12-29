# Seaborn

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
- scatter plot by groups

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
# multi-plot histogram
g = sns.FacetGrid(tips, col = "time")
g.map(plt.hist, "tip")

# multi-plot scatter plot
g = sns.FacetGrid(tips, col = "sex", hue = "smoker")
g.map(plt.scatter, "total_bill", "tip", alpha =.7)
```