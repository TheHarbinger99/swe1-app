# swe1-app
Django Polling App deployed to Aws Elastic Beanstalk

# Instructions for UBUNTU OS to deploy project on AWS Elastic Beanstalk
1) Download repository and enter folder swe1-app and open terminal.
2) Install virtual environment:      virtualenv -p python env
3) activate virtual environment:     source env/bin/activate
4) change directory:                 cd SimplePoll
5) download awsebcli :               pip install awsebcli
6) initialize eb:                    eb init
7) create environment:               eb create Your_App_Name_given_in_step 6-env
8) check deployment status:          eb status
9) deploy if green status :          eb deploy
10) open application:                eb open
11) Enjoy the application.  keep Smiling.

