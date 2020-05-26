
# About the Project:

This Project is all about integration of Machine Learning with Devops i.e Continous Integration and deployment of Ml models.In this Jenkins is used to automate the ML CNN model (cnndogandcatmodel.py in my case) untill a desired accuracy is achieved.

## Solution:

* Job 1 : Under this job a Poll SCM is created which will keep an eye on github repository every minute.This job will automatically copy everything in the folder of my RHEL 8 os.

* Job 2 : ON success of job1 it will trigger job 2. This job will launch docker container containing all the library that are required to run a CNN model.

* Job 3 : After successfully launching the OS Jenkins will trigger this job. This job will run CNN model code in order to train the model (cnndogandcatmodel.py in my case).

* Job 4 : If cnndogandcatmodel.py runs successfully but give less accuracy then jenkins should automatically tweak the code in order to increase the accuracy.To achive this jenkins will push tweakingmodel.py that will add more layer to cnndogandcatmodel.py .After tweaking the model it will trigger job3 which will again train the model upto the desired accuracy.

* Job 5 : This job will send notification through mail as soon as jenkins succeed in achieving desired accuracy. It will notify developer the CNN model with desired accuracy is achieved.

* Job 6 : Job 6 will monitor job3 if the container fails due to any reason ,it will automatically start the container again and trigger job 1

## For more about Project
[Click Here](https://www.linkedin.com/pulse/integration-devops-ml-cnn-model-tushar-kaundal)
