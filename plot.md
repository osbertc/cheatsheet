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