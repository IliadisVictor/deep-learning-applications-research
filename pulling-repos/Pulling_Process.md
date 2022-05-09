## Repository Selection
### Initial Batch Collected - Inclusion Criteria

The initial selection of repositories dependent on the selected libraries was done in the following ways:
1. For fast.ai , Keras and Pytorch we used Github's REST API to search for each library separately repositories with package management configuration files that include the library as a keyword . Query example `` keras filename:package.json`` for the files package.json,setup.py,requirements.txt .
2. for Brain.js MXNet and Tensorflow we scraped the dependency graph of each library main repository for projects that are dependent on them . 

### Total Dependent repositories collected 27215
* Brain.js 2200
* Tensorflow 19812
* MXNet 2267 
* Keras 1299  
* fast.ai 232 
* Pytorch 1374 
* BigDL 31



Stratified sampling on them : 

### Filter on stars > 100 result 341
* Brain.js  16 selected
* Tensorflow  100 selected
* MXNet    77 selected
* Keras   47 selected 
* fast.ai   8 selected
* Pytorch  90 selected
* BigDL 2 selected

<!-- to avoid personal projects -->
### Filter on contributors >=3 to deter personal projects :
* 243 from 340 

<!-- Inactive and outdated projects -->
### Last commit sooner than a year :
* 243 to 197 

### Natural Language not English : 
* 197 to 188

<!-- Repository types , filtering out project that are not software development or implementation projects -->
### Repository Type filtered excluded Platforms for use , toolkits , frameworks , libraries ,  books ,extensions ,collections 

* 188 to 35 6 of them being examples released by the developing teams themselves 

