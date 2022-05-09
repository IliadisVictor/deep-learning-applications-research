# deep-learning-applications-research
The objective of this project is to empirically investigate the software engineering practices associated with the development of deep learning applications. This will be done in the following steps.

* Systematically identify major deep learning libraries, e.g. through keyword searching
* Obtain a list of deep learning projects by finding those that have the identified libraries as a dependency. This can be done by analyzing package management configuration files.
* Analyze the projects to answer the following research questions
  * How are parts of the machine learning pipeline implemented?
  * Which parts are engineered (e.g. under configuration management, continuous integration, build automation, testing) using SWEBOK best practices?
  * What tools are used to aid software engineering practices?
  * What tools are missing?


## Collection algorithms

In the ``pulling-repos\Pulling_Process.md`` you can find the documentation for the collection and filtering steps , and the code used to execute said steps and collection.



## Repositories Used
In the ``pulling-repos\finalrepos.csv``  you can find after the whole collecting and filtering process the repositories i am using.


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

