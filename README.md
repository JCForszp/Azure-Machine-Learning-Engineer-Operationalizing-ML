
# Machine Learning Engineer With Microsoft Azure Nanodegree Program / Project 2: operationalizing Machine Learning

## Summary

This project is meant to demo two different processings available on Azure Machine Learning Studio, both relating to the same dataset (a bank marketing data that can be retrieved [here](https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv).  
- The first processing, that will be demoed in the first section of this document, consists in identifying the best prediction model, deploying it in Azure and consuming it from a local python script.   
- The second processing consists in the setup of a complete pipeline totally driven by the Azure Python SDK. The corresponding Jupyter notebook (with the details of the execution steps) can be found in the starter files folder, shortcut [here](https://github.com/JCForszp/nd00333_AZMLND_C2/blob/master/starter_files/aml-pipelines-with-automated-machine-learning-step.ipynb) ).  

The [starter_files](https://github.com/JCForszp/nd00333_AZMLND_C2/tree/master/starter_files) folder, in this repository, contains the list of all final versions of the files (data, scripts, shell files) needed to replicate all steps mentioned below. 


## Architectural Diagram

The structure of this document follows the organization / architecture of the Azure environment. 
As we will go through each individual step of the two processes, it makes sense to keep the same organization to ensure that the transition between every step remaains clear and fluid. 

The overall structure will be hence the following:
  
![Architecture and document structure](https://user-images.githubusercontent.com/36628203/124170564-e1588300-daa7-11eb-8c44-56fddda19702.png)


## Part 1 - Identification & Deployment of the best predictive model with Azure ML Studio

### Section 1 - Authentication & Dataset registration

#### 1.1 Authentication

Azure has severa kinds of authentication. We will use the simplest, the interactive one that is sufficient to cover local deployment and experimentation.
As I am using the Udacity account, I skipped the creation of the Service Principal. 
The first screen below shows the successful az login.   
  
![image](https://user-images.githubusercontent.com/36628203/124171073-5f1c8e80-daa8-11eb-9796-a52415310699.png)

The second command tells us that the Azure Machine Learning extension is properly installed.   

![image](https://user-images.githubusercontent.com/36628203/124171095-65ab0600-daa8-11eb-8a22-b8356860c5d0.png)

#### 1.2 Dataset retrieval & registration

Now that the authentication part is done, the next step is to get into the Azure Machine Learning studio and import the dataset we need by using the command [Create dataset / Upload] that allows to directly retrieve it from an http: address.

The screenshot below below shows that the dataset was correctly imported.  
It now appears in the tab 'Registered dataset'.

![image](https://user-images.githubusercontent.com/36628203/124171165-7fe4e400-daa8-11eb-998e-5e9578fae227.png)




### Section 2 - AutoML - Best Model Identification & deployt

#### 2.1 Create experiment & compute cluster

The next step consists in defining and launching the experiment.  
I am not going into the detail of each step of the sequence, as the screenshots below give a good summary of the options and outcomes.  
The screen below shows that the experiment I defined was successfully completed.  
We can also see the compute target I defined to specifically run this experiment.  
![image](https://user-images.githubusercontent.com/36628203/124171202-896e4c00-daa8-11eb-8a16-11a0478c0640.png)

We can access the detail of the completed run by clicking on its name (in our case "JCF-Bank_Mktg_Experiment-01").  
The right pane is the most interesting, as it shows that automl determined that the best model, after tuning its hyper-parameters, reached an accuracy of 92%.    
  
This is reasonable, keeping in mind that the dataset is highly imbalanced and shows a null-accuracy close to 89%.
Anyway,automl shows that the best model we can get within the constraints given, is a "Voting Ensemble" model, as shown below:  

![image](https://user-images.githubusercontent.com/36628203/124171221-90955a00-daa8-11eb-887a-99c36b6c7844.png)

I copied below a summary of the key metrics (the various AUC curves), which are good, keeping in mind that our dataset is slightly flawed and would need some data cleansing to give more accurate figures.  

![image](https://user-images.githubusercontent.com/36628203/124171243-97bc6800-daa8-11eb-8be2-b6d6cc38b989.png)

#### 2.2 Deployment of best model

Now that we know which model ends up with the best accuracy, it's time to deploy it. that will allow to interact with the HTTP API service.
The screen below shows the definition of the deployment run. Besides the name and the description, we provide two major settings:  
a. we enable "authentication"  
b. as both Azure Container Instance (ACI) and Azure Kubernetes Service (AKS), we specify below that we are using ACI for the deployment of our compute instance.  

![image](https://user-images.githubusercontent.com/36628203/124171742-406ac780-daa9-11eb-8de2-2ec52f5eac91.png)

Once the run is completed, we can access a detail of the newly created Endpoint.  
It confirms that the deployment was successful ('Deployment state' shown as healthy) and provide already with two important objects for later steps:  
- the URI of the scope file
- the Swagger JSON file we will need for documenting the JSON payload we need to interact with the endpoint. 
Please note, at the bottom of the screen, that logging ('Application Insights') is disabled at this stage.  

![image](https://user-images.githubusercontent.com/36628203/124171761-4496e500-daa9-11eb-870d-32ec805be18d.png)

#### 2.3 Enabling logging

The next step will now to enable Application Insights that will allow us to detect anomalies and visualize performance at a later stage.  
As the endpoint is already created, we need to change this setting using the Python SDK.  
Amongst other things, the script [logs.py](https://github.com/JCForszp/nd00333_AZMLND_C2/blob/master/starter_files/logs.py) contains the python command we need for this activation:  
```
# enable application insight
service.update(enable_app_insights=True)
```
the execution of this script gives a very verbose output...  

![image](https://user-images.githubusercontent.com/36628203/124171808-4fea1080-daa9-11eb-80c6-0f8339c31f2b.png)

... nevertheless, if we get back to the detail of the endpoint, we can see now that Application Insights is enabled.

![image](https://user-images.githubusercontent.com/36628203/124171832-55475b00-daa9-11eb-8b31-142286d06cf5.png)

the detail screen provides also an Application Insights URI that gives access to a cockpit that shows key metrics such as response time, number of requests or number of failed requests.   

![image](https://user-images.githubusercontent.com/36628203/124171846-5bd5d280-daa9-11eb-8b99-d582592d848c.png)




### Section 3 - Accessing and consuming endpoints

#### 3.1 Documenting Endpoints with Swagger

As we saw, the endpoint detail screen provides a swagger.json file that we can now use in Swagger to document automatically our endpoint.  
Swagger provides a template input payload. It not only shows the list of items that needs to be provided, but also the type of data (green for strings, red for numeric).  
So, it shows clearly the content of the API for the model:  

![image](https://user-images.githubusercontent.com/36628203/124171869-65f7d100-daa9-11eb-871e-3e438eb604cd.png)

I copy / pasted the JSON template from Swagger into the python script [endpoint.py](https://github.com/JCForszp/nd00333_AZMLND_C2/blob/master/starter_files/endpoint.py) and changed values manually to test, as shown below:  

![image](https://user-images.githubusercontent.com/36628203/124171884-698b5800-daa9-11eb-91fc-bb507505c91e.png)

#### 3.2 Consuming deployed services

Now that our endpoint is deployed and our python script contains an input payload to POST, we can execute it in the shell.
We only receive the response of the endpoint, which is, in our case below "No".  

![image](https://user-images.githubusercontent.com/36628203/124172016-99d2f680-daa9-11eb-8829-f48f25205253.png)

#### 3.3 benchmarking

Benchmarking tells us how healthy is out connection to the endpoint, with average time for requests and number of failed requests.  
The screenshot below shows that Apache Benchmark (AB) is running against the HTTP API using the authentication keys we provided.  

![image](https://user-images.githubusercontent.com/36628203/124172211-d4d52a00-daa9-11eb-9b08-5fbded426126.png)




## Part 2 - Automating the creation, training and publishing with a pipeline driven from the Azure Python SDK


### 1. Pipeline creation

The aim of this part is to define a pipeline that automates the handling of the dataset, the definition and execution of the automl step and the deployment. 
This is done using the python SDK, and the Jupyter Notebook used for that is available [here](https://github.com/JCForszp/nd00333_AZMLND_C2/blob/master/starter_files/aml-pipelines-with-automated-machine-learning-step.ipynb).  

After launching the Notebook, we can see that the pipeline was correctly created:  

![image](https://user-images.githubusercontent.com/36628203/124172369-06e68c00-daaa-11eb-94e7-5579b4d4caec.png)

The following screenshot shows that the bank marketing dataset was already process and the automl step is now running (green bar on the left side of the box): 

![image](https://user-images.githubusercontent.com/36628203/124172385-0c43d680-daaa-11eb-9fb3-a167fa5b462f.png)

### 2. Pipeline publishing

Once the pipeline is completed, 

![image](https://user-images.githubusercontent.com/36628203/124172396-1239b780-daaa-11eb-82db-b29b27e7d870.png)
![image](https://user-images.githubusercontent.com/36628203/124172445-241b5a80-daaa-11eb-9af5-87a9d6ae5996.png)
![image](https://user-images.githubusercontent.com/36628203/124172458-2aa9d200-daaa-11eb-95d0-2dc47e2b9f75.png)


## Screen Recording
[Screen recording](https://youtu.be/M10-TOFYvAM)

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
