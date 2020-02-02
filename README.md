
# Lazy Human AI Teams
Vihang Agarwal, Samarth Mendke

Studying Human AI teams and analysing Human Factors that improve team performance.

We are inspired by this idea in psychology that humans are competent by
nature and our mental effort is parsimonious. This motivates us to identify Human effort as a task dimension. In this study we show that optimising Human Effort in an active learning paradigm improves overall team performance. Human AI teams are modelled through an active learning pipeline and their shared goal is to annotate text.

![](https://github.com/vihang-ag/LazyAIteams/blob/master/images/workflow.png)

We also designed a very simple interface and its variant to seamlessly carry out our experiments.

![test image size](https://github.com/vihang-ag/LazyAIteams/blob/master/images/interface1.png){:height="500px" width="400px"}

![test image size](https://github.com/vihang-ag/LazyAIteams/blob/master/images/interface2.png){:height="500px" width="400px"}


## Metrics

We used three metrics to be evaluated in our study. The table below defines these metrics.

![](https://github.com/vihang-ag/LazyAIteams/blob/master/images/metric.png)


## Results
Resulting Accuracy and Effort estimates for the baselines (active learning with maximum entropy sampling and random sampling) and the proposed experiment. 

![](https://github.com/vihang-ag/LazyAIteams/blob/master/images/results.png =300x300)

Average over 5 experiments to ensure validity



## Setting up the Interface

### Requirements
MySQL

flask

flask-cors

pymysql

### Setup

Running the interface requires mysql without any password set. If you decide to set the password, update it in the ```Interface1Basic/newserver.py``` file.

```
1. Make a sql database with name annotationdbname and update it with the data in annnotationdbname.sql

2. Once such a database exists, run the file newserver.py in the terminal

3. Open the index.html file in a browser and start annotating
```

## Experiments

### Requirements
Python 3.5

PyTtorch >= 1.0

numpy

matplotlib


### Instructions to run the experiments

All active learning experiments are simulted, where annotation data was collected before the experiment.

The folder contains three python files for running the baselines and proposed experiment.

The datasets are dictionaries of vector featurized sentences. All sentences in the datasets 
were featurized before training to save time.

```
Active learning with maximum entropy sampling: 
  run python simple_mlp.py
```

Displays Train/Test accuracy at each iteration
Each iteration is an update with a batch size of 12

```
Random sampling baseline experiment:
  run python simple_mlp_random.py
```

Displays Average effort and examples seen after each iteration

```
Sampling for low human effort:
  run python simple_mlp_lowrandomeffort.py  
```

#### Dataset
The file ```data/train_vector_dict_480.json``` contains vectorized sentences from the train set for active learning experiment.

The file ```data/newtrain_vector_dict_480.json``` contains vectorized sentences from the train set for the proposed experiment.

#### Notes
All scripts use a simple multilayer perceptron model for classification. 
Read the report at ```https://vihang-ag.github.io/pdfs/Lazy_Human_AI_teams.pdf```





