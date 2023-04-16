## learning

I made this project for my learning

## Tools
Python language is used for coding.
Python language has a library Requests which can make http/https requests.

## Test Scenarios Implemented
- Validation of Status Code
- Validation of City & Country Name 
- Validation of number of weather predictions returned by call
- Validation of values for temperature
- Validation of population tag (example for test failure)
 
## CICD
CircleCI is used for CICD. 
(signup required) Builds available at https://app.circleci.com/pipelines/github/rohitaroramsa/OpenWeatherAPI?invite=true
I preferred CircleCI as it runs over a server compared to jenkins which requires local setup and hence difficult to share the setup.


## Project Structure
Assessment project is built across multiple folders: 
- features: All the .feature files (Gherkin files/BDD Files) are present inside this folder.
- features/Steps: All the step definitions are present inside this folder. file name should match the feature file name.
- features/environment.py: To be used as common fixture (before Tests) for most of the Test.

## Setup & Installations
#### Python
Python can be downloaded from [Download Python link](https://www.python.org/downloads/).


#### Dependencies & Installation
This Python based Test Automation project has 2 major python dependecies:
- Behave (For BDD Test Implementation)
- Requests (for GET operation)

They both are written in file requirement.txt. When user will open this file in any modern Python IDE such as PyCharm Community Edition, IDE will suggest downloading these dependencies and will download itself.
Users can also run following commands inside Terminal/command prompt to install these python dependencies:
```sh
$  pip install requirements.txt 
```
or install them individually:
```sh
$ pip install requests 
$ pip install behave
```

## Execution
##### Way 1 using Terminal 
In terminal, go to the path of root folder using command cd <path>. Afterwards you can run following command:
```sh
$ python -m behave --no-capture --no-capture-stderr --no-logcapture
```
This command will execute all feature inside features & steps folder.
Python behave terminal command also accepts several paramters which are available on behave official documentation site [Behave Documetation Link](https://behave.readthedocs.io/en/latest/index.html). 

##### Way 2 using python file
I have created a python file features_runner.py which can be run as simple python file. It will also execute features files in the path specified inside the file. It's a wayaround to use terminal and running behave command. I can also configure any CLI parameters in this file.