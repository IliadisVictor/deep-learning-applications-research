# deep-learning-applications-research
The objective of this project is to empirically investigate the software engineering practices associated with the development of deep learning applications. This will be done in the following steps.

* Systematically identify major deep learning libraries, e.g. through keyword searching
* Obtain a list of deep learning projects by finding those that have the identified libraries as a dependency. This can be done by analyzing package management configuration files.
* Analyze the projects to answer the following research questions
  * How are parts of the machine learning pipeline implemented?
  * Which parts are engineered (e.g. under configuration management, continuous integration, build automation, testing) using SWEBOK best practices?
  * What tools are used to aid software engineering practices?
  * What tools are missing?


## Scrapper Functionality
Using python we have created a small tool that by giving as input in the variable url , the page url of the github repository of our selected project dependents (from the dependency graph in the Insights tab) [Tensorflow Example](https://github.com/tensorflow/tensorflow/network/dependents) , we can extract a specific number of dependent github projects above a desired start threshold .

For the purposes of my research i have also implemented a randomized return of 3 dependent projects from the list that only has repos above the threshhold.

**Note** If less repositories are returned than the ones you have asked for in the ``repos_list`` , it means there are not enough repositories above the star threshold . 

## Repositories Used
In the ``pulling-repos`` files you can find the 10 or less project's we are going to use in the analysis in different files for each different major deep learning library in csv form. We have setted a minimum amount of 100 starts , some projects dont have enough repos above that threshold.


## Machine Learning Pipeline

Typical Machine Learning Components

* Data validation
* Data cleanup
* Feature extraction (labelling and dimensionality reduction)
* Model training
* Model Evaluation
* Model Validation - Executing Predictions
* Deployment
* Monitoring
* Re-Training Trigger


![Pipeline](/images/automatic-pipeline.png
)