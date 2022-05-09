## Chapter 2: Data Selection for the study

### 2.1 Target Data
What are the target data , and what do we aim to capture from the data we want to obtain .

### 2.1.1 Repository Mining Source Selection 
Which data source type we are going to use from the available software mining infrastructure ? (farias et al) 
why Github , opposed to other available options.
* Define the type of repository we will collect
* Provide a clear link between data collected , sources , and research questions

### 2.2 Frameworks and Libraries Selection Strategy . 
The primary selection criteria for the selected repositories will be their use of major deep learning libraries , the selection of said libraries is going to be executed as follows.
The original list will be obtained through keyword searching 
and then filtered by the following criteria 
* Inclusion Criteria
  * Project Popularity 
  * More than 5 years of ongoing project life
* Exclusion Criteria 
  * No longer actively maintained  
Also include:
* Search Strings : Keywords used in search engines to amass the initial batch . 
### 2.3 Repositories Search Strategy 
* Selection Timing :
The date of the extraction of data can heavily effect the return repositories , and must be noted.
* Inclusion Criteria
  * Dependent on selected frameworks and libraries
  * Popularity ( Above 100 Stars )
* Exclusion Criteria 
  * Natural Language
  * Contributing Team Smaller than 3 
  * Last Commit More than a year .  
  * Repository Type (Toolkits , Frameworks , removed )

### 2.3.1 Perils Faced Mining Github 
https://link.springer.com/article/10.1007/s10664-015-9393-5 
Justification of Criteria ,why have we selected the criteria we did ? 
**Ex. :**
* Most Projects are personal (few committers)
* Inactive Projects
* Projects that don't practice  pull requests 
* Source ( Github ) Evolving future inability to replicate the scraping 
* Github API does not expose the desired data


### 2.4 Search execution and data extraction . 
Registry of the selection process of repositories , documentation of each step , report of results

* Reasoning for not using the official GitHub API 
  * 1. Does not have an endpoint returning repositories dependent on x library
  * 2  You can only search for keywords inside x file ex ``tensorflow package.json``
  * 3. The api returns only the first 1000 results. 
* Scraper explanation / Documentation 
* Data stored and processed during the selection and extraction , Where was it stored (Stereo)? 

**Initial Selection**
The initial search is executed with the only initial criteria being that the project's collected are dependent on the selected library list , and that they have above 100 stars, 
before quality filtering.
* Explain here the search algorithm (beautifulsoup)

**Quality Evaluation**
After the initial batch was collected it was filtered by the criteria we defined in 2.3 discarding x repositories , leaving us with y repositories a mere p% from the initial batch. 

**Final Randomized Selection**
Finally from the repositories that have been filtered for quality we select , through a pseudo randomizer x repositories. 

**Data extraction**
Include extraction date , that will be the same as the selection to avoid reproducibility issues 
* Mining algorithm , downloading the source code of repos .

Because like mentioned before there is no dedicated API call to getting repositories that use
a specific library we did the following work around

Search considerations [https://docs.github.com/en/search-github/searching-on-github/searching-code]
For each of the selected libraries we used a github search query ,
looking 

