<h1 align="center">Síbín Lounge</h1>

 [View the live project here.](https://sibin-lounge.herokuapp.com/)

Síbín Lounge is a website where users can share their own cocktail creations/recipes and showcase them to the world. 

The word Síbín(pronounced "Shebeen") originated in Ireland between 1780–90. It referred to home brewed whiskey which was then sold illegally and soon came to refer to unlicensed premises that sold alcohol. 

This website was created by me for my third milestone project with Code Institute.

User details - 
username : admin 
Password : letmeinhere

## User Experience (UX) 

- ### User Stories
 -  #### First-time Visitor Goals: 
    1. As a first time visitor, I want to understand the main purpose of the site and learn more about what it has to offer
    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
    3. As a First Time Visitor, I want to be able to sign up to the website and create a profile
    4. As a First Time Visitor, I want to be able to submit a cocktail and save it to the website 
    5. As a First Time Visitor, I want to be able to search the website for other cocktails
    6. As a First Time Visitor, I want to be able to logout of my new profile

  - #### Returning Visitor Goals: 
    1. As a Returning Visitor, I want to be able to sign back in to my previously created profile
    2. As a Returning Visitor, I want to be able to edit a previously entered cocktail
    3. As a returning Visitor, I want to be able to delete a previously entered cocktail
    4. As a returning Visitor, I want to be able to check for more cocktails added by other users 

  - #### Frequent Visitor Goals 
    1. As a Frequent User, I want to be able to check for more cocktails added by other users 
    2. As a Frequent User, I want to be able to submit more cocktails and save them to the website 

-   ### Design
    -   #### Colour Scheme
        -   I chose black for body of the bar in keeping the the style of a Síbín which would be a dark secret, I then chose different shades of green in keeping with the Irish connection
    -   #### Typography
        -   I used Oswald for the main text throughout the site

    -   #### Imagery
        -   The main image of the site was taken from unsplash.com

*   ### Wireframes


## Features

 - #### Current Features
    - Responsive on all device sizes.
    - Home page with navbar and information about what the page is about
    - Collapsible Navigation bar for smaller devices
    - A database connected through MongoDb
    - Page that shows all drinks that have been entered into the database
    - Pop out cards that display more information on the drink when clicked
    - Search option for users to search the database for specific drinks or drinks with certain ingredients  
    - Log in option for existing users
    - Register option for new users
    - Log out option for users
    - New drink input option
    - Edit drink input option 
    - Delete drink input option 
    - Add new category option for Admin of the site

 - #### Future Features
    - Option to upload image of the drink when inputting
    - Option for users to rate the drinks 1-5 
    - To make it that all the users inputted drinks display on their profile

## Technologies used


1. [HTML](https://en.wikipedia.org/wiki/HTML)
    - Used for the structure of the site 
1. [CSS](https://en.wikipedia.org/wiki/CSS)
    - Used for styling the site 
1. [Python](https://www.python.org/)
    - Backend Programming Language
1. [JavaScript](https://www.javascript.com/)
    - Used for functionality on the site
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - A Python library
1. [Werkzueg](https://werkzeug.palletsprojects.com/en/1.0.x/)
    - Used for password hash
1. [PyMongo](https://pymongo.readthedocs.io/en/stable/)
    - Used to connect MonDb with Python
1. [MongoDB](https://en.wikipedia.org/wiki/MongoDB)
    - Used to create the database for the site
1. [Materialize](https://materializecss.com/)
    - Used for responsiveness throughout the site
1. [Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used for testing and viewing the site while in development
1. [Heroku](https://en.wikipedia.org/wiki/Heroku)
    - Was used to deploy the finished website
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import fonts used on the site
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to import icons
1. [jQuery:](https://jquery.com/)
    - Used with Materialize to help with functionality
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/stephenoc390/SOCPhotography-Milestone1/blob/master/assets/readme/html-validator.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/stephenoc390/SOCPhotography-Milestone1/blob/master/assets/readme/css-validator.png)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a first time visitor, I want to understand the main purpose of the site and learn more about what it has to offer


    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.


    3. As a First Time Visitor, I want to be able to sign up to the website and create a profile


    4. As a First Time Visitor, I want to be able to submit a cocktail and save it to the website 


    5. As a First Time Visitor, I want to be able to search the website for other cocktails


    6. As a First Time Visitor, I want to be able to logout of my new profile


-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to be able to sign back in to my previously created profile


    2. As a Returning Visitor, I want to be able to edit a previously entered cocktail


    3. As a returning Visitor, I want to be able to delete a previously entered cocktail


    4. As a returning Visitor, I want to be able to check for more cocktails added by other users 



-   #### Frequent User Goals

    1. As a Frequent User, I want to be able to check for more cocktails added by other users 


    2. As a Frequent User, I want to be able to submit more cocktails and save them to the website 


    
    1. As a Frequent User, I want to check to see if there are any newly added images.

        1. The user would already be comfortable with the website layout and can easily the gallery section

### Further Testing 

-   The Website was tested on Google Chrome, Opera and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone6 & iPhoneX Plus.
-   Testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.



### Known Bugs

## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Login to Heroku
2. Create a new app, selecting the correct region
3. In the deployment method select connect to GitHub
4. Once connected to GitHub enter your repository name and select it once it appears
5. Once it is connected select the settings option at the top
6. In Convig Vars select reveal Convig Vars
7. Here you will input the data for - IP, PORT, SECRET_KEY, MONGO_DBNAME & MONGO_URI
8. After this return to the deploy tab
9. Selected enable automatic deploys
10. Selected deploy branch 
11. After a view moments you should see a message that says Your app was successfully deployed with the option to view it below

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/stephenoc390/sibin_lounge)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site in the "GitHub Pages" section.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/stephenoc390/sibin_lounge)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

## Credits

### Code

-   Coding ideas came from:
    - The [Code Institute](https://codeinstitute.net/) training videos and projects

### Media

-   Hero image credited (https://unsplash.com/photos/KROWD3mWRPw)

### Drink Recipes

-   All created by me 



