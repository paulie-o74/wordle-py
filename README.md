# A WORDLE clone
(Developer: Paul Thomas O'Riordan)

![Screenshot of terminal](/assets/welcome.png)

[View live site](https://)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Scope](#scope)
    4. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals 

- To successfully replicate the popular online game "WORDLE" in an app run only in the terminal, using similar logic and hints to replicate the experience of playing online. 
- Official game can be found at https://www.powerlanguage.co.uk/wordle/
- Rules are as following:
- Guess the WORDLE in 6 tries.
- Each guess must be a valid 5 letter word. Hit the enter button to submit.
- After each guess, you will receive hints to show how close your guess was to the word.

### User Goals
- To be able to play a game similar to the popular online game WORDLE.
- To receive feedback relating to how close the game was.
- To be able to log in to the system with pre-determined log in credentials.

### Site Owner Goals
- Create an application that functions in a similar manner to that which can be found on WORDLE.
- Create an application which users will be able to follow intuitively.
- Create an application which is fit for purpose and does not have any bugs.

## User Experience
### Target Audience
- Online gamers
- People on their coffee break

### User Stories

#### First-time User 
1. As a first time user, I want to know what is expected of me on the log in screen
2. As a first time user, I want to receive feedback on whether I logged in successfully or not.
3. As a first time user, I want to be told the rules of the game.
4. As a first time user, I want the menu and gameplay to be easy to follow and intuitive. 

#### Site Owner
6. As the site-owner, I want the user to be able to log in while receiving feedback and be told the rules before anything else is asked of the user.
7. As the site-owner, I want the game to give accurate feedback to the user on whether or not their guess was correct
8. As the site-owner, I want the game to give accurate feedback to the user on whether or not they have letters in the correct position.
9. As the site-owner, I want the game to give accurate feedback to the user on whether or not they have any correct letters in the wrong position.

### Scope
In this first version, the application is housed in the terminal, ideally this would work in tandem with other software in the future to either deploy it online or build a mobile app. 

### User Manual

<details><summary>Click Here for instructions for use</summary>

#### Overview

- Users are greeted with a welcome screen calling for user to input username and password.
- Users are then reminded of the rules.
- Rules are as following:
- Guess the WORDLE in 6 tries.
- Each guess must be a valid 5 letter word. Hit the enter button to submit.
- After each guess, you will receive hints to show how close your guess was to the word.

- Log on credentials are listed below:
![Screenshot of log on credentials](/assets/logon.png)

## Technical Design

### Flow Chart

Below you can see the flowchart, created with [lucidchart.com](https://www.lucidchart.com/pages/)

![Screenshot of log on flowchart](/assets/flowchart.png)

### Data models

For this project I have used the following features:
- list comprehension making a list from an iteration, a more succint way to create a list from a for loop. 
- Dictionaries e.g. in the username/password checking. 
- Enumerate, which keeps track of how many times you have iterated.
- Google sheets API.  JUSTIFICATION: I have chosen to use Google Sheets API so that the required data for the app will persist outside of the app, the application will then be able to check log on credentials and the list of words which can be added to in the future.
- Random JUSTIFICATION: I wanted to be able to choose a number at random as an index to pull a different word from the word list each time the game is played. 

## Technologies Used

### Languages

- [Python 3](https://www.python.org/)

### Frameworks and Tools

1. [Heroku](https://heroku.com/) - Heroku was used to deploy the project and to provide a virtual terminal to for examiners. 
2. [GitHub](https://github.com/) - GitHub was used as a remote repository to store project code. 
3. [Gitpod](https://gitpod.com/) - Gitpod was used as the main IDE for this project.
4. [lucidchart.com](https://www.lucidchart.com/pages/) - was used to draw flowchart.
5. [Google Sheets](https://www.google.co.uk/sheets/about/) - was used to store data outside of the program.  The word list and log on credentials are stored in 2 separate sheets.
6. [Google Cloud Platform](https://cloud.google.com/cloud-console/) - was used to manage access and permissions to the google services, google auth, sheets etc.

#### Libraries

### 3rd Party Libraries
1. [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION:  For the purposes of the project spec, I wanted to access and manipulate from googlesheets and to interact with the google API so I have chosen to use the gspread library for these functions.

2. [colorama](https://pypi.org/project/colorama/) - IMPORTANT: THIS WAS ONLY USED IN TESTING AS IT WOULD NOT WORK IN HEROKU (SEE TESTING.PY) JUSTIFICATION:  For the purposes of the project spec, I wanted to be able to give the user visual feedbaclk similar to the official game which gives color clues to help the users identify which letters they have in the correct position and which letters they have in the word but not in the correct position. 

## Features

### Main Menu



**This screen covers the following user stories:**

*1. 

### Vehicle Menu



<details><summary></summary>
<img src="">
</details>

**This screen covers the following user stories:**

*1. As a user I want the option to search vehicles or manage appraisals.*


#### Search vehicle



<details><summary></summary>
<img src="">
</details>


**This screen covers the following user stories:**



#### Remove Vehicle



<details><summary></summary>
<img src="">
</details>

**This screen covers the following user stories:**



### Appraisal Menu



<details><summary></summary>
<img src="">
</details>

**This screen covers the following user stories:**


## Validation

### Python Validation
The Python code of the each module was validated using [PEP8 Validation Service](http://pep8online.com/).  All modules returned a pass with 0 errors and 0 warnings.

<details><summary>run.py</summary>


<details><summary>testing.py</summary>



### Testing user stories

1. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find main menu       |      Select option 1       | User is presented with Vehicle sub-menu | Works as expected |
| Find main menu  |   Select option 2   | User is presented with Vehicle Appraisals submenu | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/user-story-1a.png">
<img src="/docs/testing/user-story-1b.png">
</details>

2. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Vehicle Menu  |   Select option 1   | Displays input reg | Works as expected |
| Find reg input prompt  |   Enter vehicle registration   | Returns prompt if vehicle exists to display vehicle details OR notifies if reg not found | Works as expected |
| Print vehicle details prompt  |   Select to display vehicle details   | Displays vehicle description | Works as expected |

<details><summary>Screenshots</summary>
<img src="">
<img src="">
</details>

3. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Appraisals Menu      |      Select option 1      | Prompt appears to enter vehicle registration | Works as expected |
| Enter vehicle registration prompt      |     User enters vehicle reg      |   If vehicle exists user prompted to enter appraisal details OR returns not found | Works as expected |
| Enter appraisal date and details  |  Prompt displayed to update database. |  Confirmation is shown that data has been uploaded  |Works as expected. |
| Update database prompt  |  Select to update OR cancel. |  Database updated with confirmation OR returns to Appraisal Menu  | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-3a.png">
<img src="docs/testing/user-story-3b.png">
<img src="docs/testing/user-story-3c.png">
</details>

4. .

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  Find Add Vehicle Menu Option     |      Enter vehicle details  |   Confirmation displayed with prompt to add to database | Works as expected |
| Update database prompt | Select to update OR cancel | Database updated with confirmation OR return to menu | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-4a.png">
<img src="docs/testing/user-story-4b.png">
</details>

5. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  Find Remove Vehicle Menu Option     |      Enter vehicle registration  |   Confirmation displayed with prompt to remove from database | Works as expected |
| Update database prompt | Select to update OR cancel | Database updated with confirmation OR return to menu | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-5a.png">
<img src="docs/testing/user-story-5b.png">
</details>

6. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Search Appraisal Option    |      Enter vehicle registration and confirm prompt if vehicle is located   |  User is presented with all appraisal data for the vehicle selected  | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-6.png">
</details>

7. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Vehicle Reg length Validation     |      Enter incorrect reg length     |  Error message displayed with reason and resubmit | Works as expected |
| Menu option validation  |  Enter menu option not within range or non numeric.  |  Error message displayed with reason and resubmit | Works as expected |
| Date validation  |  Enter date incorrect format |  Error message displayed with reason and resubmit | Works as expected |
| Vehicle Reg Validation (not for Add Vehicle Menu option)    |      Enter vehicle registration not contained within Google Sheet     |  Vehicle not found displayed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-7.png">
</details>

8. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|    Find menu options   |      Select menu options   |  User recieves acknowledgement from system  |  Works as expected  | Find vehicle input  |  Input vehicle details  |  User gets acknowledgement from system  |  Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-8a.png">
<img src="docs/testing/user-story-8b.png">
</details>

9. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Vehicle Menu  |   Select option 1   | Displays input reg | Works as expected |
| Find reg input prompt  |   Enter vehicle registration   | Returns prompt if vehicle exists to display vehicle details OR notifies if reg not found | Works as expected |
| Print vehicle details prompt  |   Select to display vehicle details   | Displays vehicle description | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-2a.png">
<img src="docs/testing/user-story-2b.png">
</details>

10.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Vehicle Menu  |   Add vehicle and confirm to add  | Google sheet is updated with vehcile details | Works as expected |
| Find Vehicle Menu  |   Remove vehicle and confirm to delete  | Google sheet is updated with vehcile details | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-10a.png">
<img src="docs/testing/user-story-10b.png">
</details>

11. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Appraisal Menu  |   Submit appraisals  | Google sheet is updated with appraisal details | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-11.png">
</details>

12. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Vehicle Reg length Validation     |      Enter incorrect reg length     |  Error message displayed with reason and resubmit | Works as expected |
| Menu option validation  |  Enter menu option not within range or non numeric.  |  Error message displayed with reason and resubmit | Works as expected |
| Date validation  |  Enter date incorrect format |  Error message displayed with reason and resubmit | Works as expected |
| Vehicle Reg Validation (not for Add Vehicle Menu option)    |      Enter vehicle registration not contained within Google Sheet     |  Vehicle not found displayed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-7.png">
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| 'Vehicle catalogue' not updating with additions or removals until programme termination and re-run |   Changed variable from being called at start of module to being a function   |
| 'Vehicle Appraisals' not updating with additions until programme termination and re-run | Changed variable from being called at start of module to being a function |
| Class inheritance failed | Correct use of super init | 
| On confirmation question for print vehicle details, no value caused traceback error  |  Added while loop to check for invalid entry  |
| Adding while loop on above caused infinate loop  |  Moved input field to interrupt  |
| Date validation failed when nonsence format added  |  Changed date validation to use datetime.strftime and datetime.strptime  |

## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are making a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/rashdogg74/wordle-py).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/rashdogg74/wordle-py).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

### Code

- **Code Institute** - for git template IDE and heroku deployment instructions.
- **Google** - for library [gspread](https://docs.gspread.org/en/latest/) and [APIS](https://developers.google.com/sheets/api)
- **Colorama** - for testing.py [colorama](https://pypi.org/project/colorama/)
- With the exception of the above, all code was written raw and occasional references to W3C schools, stackoverflow, . No code has been borrowed from other sources.

### Acknowledgements: 

- To my mentor Mo Shami for his guidance and direction.
- To the Code Institute online resources
- To my younger brother (seanie5011) for engaging in conversation and sharing his own experience with logic based applications
- To my partner Ashley for helping me through personal issues and helping me stay on task.