# Marketplace Monitor
Project based in the [Final Degree Project](https://upcommons.upc.edu/bitstream/handle/2117/412036/188375.pdf?sequence=2&isAllowed=y) made by @maciasj. 

## How to execute
### Local development
For local development you need to:
1 - Install MySQL
2 - Create a MySQL database
3 - Fill local.env with MySQL settings
4 - Execute django server
You can find in the following subsections the required steps for doing it.
#### MySQL installation and database creation
#### Local execution
##### 1 - Install pipenv (if not already installed)
'''
pip install pipenv
'''
##### 2 - Install requirements
'''
pipenv install
'''

##### 3 - Execute virtual environment
'''
pipenv shell
'''

##### 4 - Execute django server
'''
python manage.py runserver
'''

## How to deploy
