# swe1-app
Django Polling App deployed to Aws Elastic Beanstalk


Instructions for UBUNTU OS to deploy project on AWS Elastic Beanstal:

1) Download repository and enter folder swe1-app and open terminal.
2) Install virtual environment:      virtualenv -p python env
3) activate virtual environment:     source env/bin/activate
4) change directory:                 cd SimplePoll
5) makemigrations:                   python manage.py makemigrations
6) migrate:                          python manage.py migrate
7) createsuperuser:                  python manage.py createsuperuser
8) run locally:                      python manage.py runserver
9) log in as superuser created in step 7
10) populate the question and choice field
11) logout as superuser
12) download awsebcli :              pip install awsebcli
13) initialize eb:                   eb init
14) create environment:              eb create Your_App_Name_given_in_step 6-env
15) check deployment status:         eb status
16) change allowed host to domain provided by aws in above steps.
17) deploy if green status :         eb deploy
18) open application:                eb open
19) Enjoy the application.  keep Smiling.
20) end the local run using Ctrl^C
21) terminate the application through elastic beanstalk dashboard on aws
22) deactivate virtual environment:   deactivate

