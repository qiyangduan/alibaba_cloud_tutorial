# Recommendation for Retail Shop, or Content (Video, Music, News etc)

## Business problem definition

Given some users and some items, and the history of each customer interacting each item, this solution should predict which user are likely to interact with which item.

## Solution Diagram

![System Architecture](https://octodex.github.com/images/yaktocat.png)

Basically, your sales website should be pushing customer purchase/click logs onto Alibaba cloud OSS, and then pull the recommendation result from Maxcompute Data Service for rendering result.

## Prerequisite
You need to setup your own cridentials for run the samples.

## Input Information
I am using a dataset from UCI for online retail sales. If you know more good content recommendation dataset, let me know, and we will make more approperiate version for advance content.

You may find original dataset from this [link on UCI](https://archive.ics.uci.edu/ml/datasets/Online+Retail#). I acknowledge and thank to provider by this reference:
```
    Daqing Chen, Sai Liang Sain, and Kun Guo, Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining, Journal of Database Marketing and Customer Strategy Management, Vol. 19, No. 3, pp. 197â€“208, 2012 (Published online before print: 27 August 2012. doi: 10.1057/dbm.2012.17).

```



## Output Information


## License

BSD Licensed.
