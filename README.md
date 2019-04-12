[![Build Status](https://)](https://)
# Flask Cooking Recipes-Book
This project/repositary contains the code for a platform/application to store Cooking recipes. Users will be able to add, modify, delete recipes, categorise them and do basic searches.
This application has mainly been built using technologies as Python and the Flask framework.

## UX
This platform hass been built to be fully responsive so it works perfectly on any device screen size.

### User stories

Below are some of the potential stories that users can follow:

- A new user should be able to:
    - Visualize a homepage with all the basic functionalities as adding new recipe button so they can easily start.
    - Visualize the main navigation (sticky) with links to the main sections.
    - Visualize a search bar for finding recipes.
    - User always have the option to go back to the main dashboard at any times by cliking the homepage options or cancel buttons.

- When a user would like to add a new recipe, they should be able to:
    - Access a complete form that capture all fields needed for a recipe to be useful. Those fields are the following:
        - Recipe name. 
        - Introduction text explaining what the recipe is about.
        - Preparation time.
        - All ingredients required.
        - Type of cuisine to categorize recipe.
        - Preparation insutrctions.
        - An image for visual identification.
    - To access a submit button to send the form data.
    - See a cancel button in case they would like to return to the dashboard.

- Users who wants to view all recipes should have access to a main dashboard (homepage) that shows all recipes. Each recipe will be visualised on a card that will have the folowing:
    - A decriptive image.
    - Recipe title name
    - Preparation time
    - Cuisine type or category
    - link to the full recipe page

- When users wants to see find recipes, they should:
    - Be able to find by keyword
    - Be able to find by preparation time.
    - Be able to find by cuisine type.


- A a user who wants to view the full recipe listing, I should:
    - click on a recipe card from the all recipes page and be taken to a page where I should:
        - see a page detailing all recipe fields:
            - Recipe name. 
            - Introduction text explaining what the recipe is about.
            - Preparation time.
            - All ingredients required.
            - Type of cuisine to categorize recipe.
            - Preparation insutrctions.
            - An image for visual identification.
            - Edit/delete buttons.

- Users who wants to delete a recipe, they should be able to delete recipes from:
     - Specific recipe page which will remove the recipe form the database.
     - the dashboard card which will remove the recipe form the database.

- User who wants to edit a recipe, they should be able to edit recipes from:
     - Specific recipe page which will redirect to a edit page where users will be able to edit one or all fields and update the database.
     - The dashboard card in their dashboard to a edit page where users will be able to edit one or all fields and update the database.

- Users who wants to see all types of cuisines (or categories), they should see a link to "cuisines" 
- where they will be able to see a list of all cuisines with the following:
- 
    - cuisine name.
    - edit button.
    - delete button.
    - add button


## Testing and validation
#### Testing
- The platform has been tested on all modern desktop and mobile browsers to ensure cross compatibility and functionalities.
- The site was tested to be responsive and to ensure it would be correctly displayed across mobile devices.
- I ensured that each one of the user stories were thoroughly tested to be functional without errors.
- Testing for this project was implemented manually. The majority of testing covered the various Flask routes. Some examples of issues/tests on routes:
- When on the homepage, when clicking on a recipe category and no recipes for such a category exist then the user will be directed to the all recipes route.
- When using the search bar, if nothing is input into the search field then the user will shown al recipes.
- When sorting recipes by parameters i.e. newest/oldest, votes desc/asc etc. - if such a parameter is not recorded in any given document, it is omitted from the sorted list which is returned.
- On the add recipe form all necessary fields i.e. title, cuisine etc. - were given the `required` tag to ensure the user did not submit empty/partially filled recipes.
- For text-area and inputs, a `max-length` was added to restrict input length.

#### Python linting
- All code was linted and formatted to the [Pep8](https://www.python.org/dev/peps/pep-0008/) standard.

## Features overview
- Add a recipe.
- Edit recipes.
- Search for recipes.
- Add cuisines.
- Edit cuisines.

### Features I'd like to implement in future versions
- User authentication system
- Sharable recipes.
- Export to PDF.
- Implement search caching/indexing.

## Challenges
- Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store.

- Managing routes and URL's with Flask was also very interesting and I learned a great deal from reading the documentation around Flask and MongoDB.


## Technologies Used
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [jQuery](https://jquery.com/) - for DOM manipulation.
- [Bootstrap](https://getbpptstrap.com) - Bootstrap is used as the primary CSS framework.
- [Flask](http://flask.pocoo.org/) - MVT (Mode-View-Template) framework used to build the application. 
- [MongoDB](https://www.mongodb.com/) - Relational database store for model data.
- [Heroku](https://www.heroku.com/) - Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Travis-CI](https://travis-ci.com) - Test and deploy code projects.
- [mLab](https://mlab.com/) - Database-as-a-Service for MongoDB.


## Production Deployment
I have written an article on the rest of the process which is available [here](https://dev.to/davedodea/how-to-deploy-a-python-app-toheroku-5djn).

- A live version of this app is available [here](https://glacial-brook-98593.herokuapp.com/).

- The Flask application is deployed to a Heroku instance.

- The MongoDB is deployed to an mLab instance.

- Testing is triggered via TravisCI upon PR's to the GitHub repository.

- Once TravisCI builds successfully, deployment is carried out on Heroku.

##### The process I took was as follows:
- Set up a new instance of a Heroku app, along with a mLab instance.
- Store the necessary config variables in the Heroku app settings.
- Set the necessary  variables in the Flask app settings.
- Set up Travis-CI to trigger when pushes are made to the repository, set up with a yml config file.
- Set up a automatic deployment hook on Heroku to trigger once Travis-CI has completed.
- Deploy by pushing to GitHub

- If you wish to deploy - ensure you have set the following config vars set in Heroku app settings:
```
    - 'IP'
    - 'MONGO_URI'
    - 'PORT'
```

## Install/deploy locally
### Ensure to comment out the `#For Heroku deployment` section of `app.py` when deploying locally.
### Uncomment the `#For local deployment` section

This is the process I have tested to enable local development and deployment.
- Clone the repository.

- CD into the repository.

- Activate a virtual environment using `pipenv shell`.

- ### **Important** Ensure you have set the environment variables in `env.py`: 
    ```python
    import os

    # assessor DB user details
    os.environ['MONGO_URI'] = 'mongodb://codeinst:codeinstitute2019@ds125402.mlab.com:25402/testmenudb'
    os.environ['MONGO_DBNAME'] = 'testmenudb'
    ```
- Install requirements: `pipenv install`

- Run the server: `python3 app.py`



## Databse schema:
- The main MongoDB collection `recipes` takes he following schema.

```json
{
    "_id": {
        "$oid": "5c78652fe64d1e68d7eba7a6"
    },
    "title": "Chocolate cake",
    "description": "Dark chocolate sponge cake",
    "method": "Mix all ingredients. Bake for 35 mins at 180C",
    "ingredients": [
        "Chocolate",
      "6 Eggs",
      "125ml millke",
      "200g Flour"
    ],
    "meal": "dessert",
    "serves": "4",
    "cooking-time": "30",
    "prep-time": "10",
    "cuisine": "French",
    "user": "Dave",
    "last_modified": "Thu Feb 28 22:48:15 2019"
  }
```

## References:
- PyMongo docs: https://api.mongodb.com/python/current/tutorial.html
- Flask docs: http://flask.pocoo.org/docs/1.0/

## Credits

### Third-party
- [Materialize CSS](https://materializecss.com/) CSS framework implementing Material design guidelines

- [Font awesome](fontawesome.com/v4.7.0/icons/) for app icon set.

- [Hover CSS](http://ianlunn.github.io/Hover/) for CSS on hover animations.

- [Unsplash](https://unsplash.com) for images.