
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
The two screens below shows the successful az login, and the proof that the Azure Machine Learning extension is properly installed. 
![image](https://user-images.githubusercontent.com/36628203/124171073-5f1c8e80-daa8-11eb-9796-a52415310699.png)
![image](https://user-images.githubusercontent.com/36628203/124171095-65ab0600-daa8-11eb-8a22-b8356860c5d0.png)

#### 1.2 Dataset retrieval & registration
![image](https://user-images.githubusercontent.com/36628203/124171165-7fe4e400-daa8-11eb-998e-5e9578fae227.png)


### Section 2 - AutoML - Best Model Identification & deployt

#### 2.1 Create experiment & compute cluster
![image](https://user-images.githubusercontent.com/36628203/124171202-896e4c00-daa8-11eb-8a16-11a0478c0640.png)
![image](https://user-images.githubusercontent.com/36628203/124171221-90955a00-daa8-11eb-887a-99c36b6c7844.png)
![image](https://user-images.githubusercontent.com/36628203/124171243-97bc6800-daa8-11eb-8be2-b6d6cc38b989.png)

#### 2.2 Deployment of best model
![image](https://user-images.githubusercontent.com/36628203/124171742-406ac780-daa9-11eb-8de2-2ec52f5eac91.png)
![image](https://user-images.githubusercontent.com/36628203/124171761-4496e500-daa9-11eb-870d-32ec805be18d.png)

#### 2.3 Enabling logging
![image](https://user-images.githubusercontent.com/36628203/124171808-4fea1080-daa9-11eb-80c6-0f8339c31f2b.png)
![image](https://user-images.githubusercontent.com/36628203/124171832-55475b00-daa9-11eb-8b31-142286d06cf5.png)
![image](https://user-images.githubusercontent.com/36628203/124171846-5bd5d280-daa9-11eb-8b99-d582592d848c.png)


### Section 3 - Accessing and consuming endpoints

#### 3.1 Documenting Endpoints with Swagger
![image](https://user-images.githubusercontent.com/36628203/124171869-65f7d100-daa9-11eb-871e-3e438eb604cd.png)
![image](https://user-images.githubusercontent.com/36628203/124171884-698b5800-daa9-11eb-91fc-bb507505c91e.png)

#### 3.2 Consuming deployed services
![image](https://user-images.githubusercontent.com/36628203/124172016-99d2f680-daa9-11eb-8829-f48f25205253.png)

#### 3.3 benchmarking
![image](https://user-images.githubusercontent.com/36628203/124172211-d4d52a00-daa9-11eb-9b08-5fbded426126.png)

## Part 2 - Automating the creation, training and publishing with a pipeline driven from the Azure Python SDK
### 1. Pipeline creation
![image](https://user-images.githubusercontent.com/36628203/124172369-06e68c00-daaa-11eb-94e7-5579b4d4caec.png)
![image](https://user-images.githubusercontent.com/36628203/124172385-0c43d680-daaa-11eb-9fb3-a167fa5b462f.png)

### 2. Pipeline publishing
![image](https://user-images.githubusercontent.com/36628203/124172396-1239b780-daaa-11eb-82db-b29b27e7d870.png)
![image](https://user-images.githubusercontent.com/36628203/124172445-241b5a80-daaa-11eb-9af5-87a9d6ae5996.png)
![image](https://user-images.githubusercontent.com/36628203/124172458-2aa9d200-daaa-11eb-95d0-2dc47e2b9f75.png)


## Screen Recording
[Screen recording](https://youtu.be/M10-TOFYvAM)

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
