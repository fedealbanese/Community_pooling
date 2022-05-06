# Community_pooling
Improving LDA topic modeling in Twitter with graph community detection.
Paper: Albanese, F; Feuerstein, E. [Improved Topic Modeling in Twitter Through Community Pooling](https://arxiv.org/pdf/2201.00690.pdf). (SPIRE 2021)

## Abstract:

Social networks play a fundamental role in propagation of information and news. Characterizing the content of the messages becomes vital for different tasks, like breaking news detection, personalized message recommendation, fake users detection, information flow characterization and others. However, Twitter posts are short and often less coherent than other text documents, which makes it challenging to apply text mining algorithms to these datasets efficiently. Tweet-pooling (aggregating tweets into longer documents) has been shown to improve automatic topic decomposition, but the performance achieved in this task varies depending on the pooling method.

We propose a new pooling scheme for topic modelling in Twitter, which groups tweets whose authors belong to the same community (group of users who mainly interact with each other but not with other groups) on a user interaction graph. We present a complete evaluation of this methodology, state of the art schemes and previous pooling models in terms of the cluster quality, document retrieval tasks performance and supervised machine learning classification score. Results show that our Community polling method outperformed other methods on the majority of metrics in two heterogeneous datasets, while also reducing the running time. This is useful when dealing with big amounts of noisy and short user-generated social media texts. Overall, our findings contribute to an improved methodology for identifying the latent topics in a Twitter dataset, without the need of modifying the basic machinery of a topic decomposition model. 

![alt text](https://github.com/fedealbanese/Community_pooling/blob/main/Diagram.PNG?raw=true)

## Cite:

If you want to use some of this idea in your own work, you can cite our paper on topic modeling in social media with community pooling:
```
@inproceedings{albanese2021improved,
  title={Improved Topic Modeling in Twitter Through Community Pooling},
  author={Albanese, Federico and Feuerstein, Esteban},
  booktitle={International Symposium on String Processing and Information Retrieval},
  pages={209--216},
  year={2021},
  organization={Springer}
}
```
