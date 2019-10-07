# Basket-Analysis-with-FP-Growth
Market basket analysis with **FP-Growth** algorithm.
Association rules mining on online retail transactions dataset.
Finding item sets with items that are frequently purchased together.

### Data set:
Data used in the analysis is taken from https://archive.ics.uci.edu/ml/datasets/Online+Retail

[Link to dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/)

It is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.



### Tools:
* Python 3
* Mlextend
* Pandas
* Excel



### parameters summary:

#### Support 
support is fraction of transactions that contain item X or itemset (X+Y)

support = 0.05 for example means that the item appears in 5% of the transactions

#### Confidence 
confidence is how often item Y appears in the transactions that contain item X

confidence 0.27 for example means that item Y appears in 27% of all transactions with item X

#### Lift 
lift is how much our confidence will increase that Y will be purchased once X is added to the basket

lift > 1: item Y is likely to be purchased when item X is purchased

lift < 1: item Y is unlikely to be purchased when item X is purchased

lift = 1.4 for example means that once item X is purchased the likelihood that item Y will be purchased increases 40%

#### Conviction 
conviction = 1.32 for example means that the rule would be incorrect 32% more often if the association between X and Y was and accidental chance

