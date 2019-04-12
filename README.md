[![Build Status](https://recipes-manager-flask.herokuapp.com/)](https://recipes-manager-flask.herokuapp.com/)
# Flask Cooking Recipes-Book
This project/repositary contains the code for a platform/application to store Cooking recipes. Users will be able to add, modify, delete recipes, categorise them and do basic searches.
This application has mainly been built using technologies as Python and the Flask framework.

## UX
This platform hass been built to be fully responsive so it works perfectly on any device screen size.

- Initial Wireframes can be found [here](https://)

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
- The platform has been tested to be fully responsive and that is correctly displayed across all of type devices.
- The platform has been tested to ensure that all of the user stories were functional without errors.
- The platform has been tested to cover the various Flask routes. 
- On the add recipe form all necessary fields i.e. title, cuisine etc. - were given the `required` tag to ensure the user did not submit empty/partially filled recipes.
- The platform has been tested to ensure all text-area and inputs are perfectly funcioning and sending/reciving corrct data.


## Features overview
- See all recipes overview (cards)
- Search recipes by keyword, time and cuisine.
- Add a recipe.
- Edit recipes.
- Remove a recipe.
- Add cuisines.
- Edit cuisines.
- Delete cuisines.

### Features I'd like to implement in future versions
- User a registation/authentication system.
- More advance analytcs section.
- Sharable recipes.
- Export to PDF.


## Challenges
- Flask and MongoDB integration was a great learning experience but tricky at times. 
- Creating the logic and routes on python has been the biggest challenge for me.


## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [MaterilizeCss](https://materializecss.com) - Materilize has been used as the primary HTML/CSS framework.
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript) - to activate Materilize elements and for DOM manipulation.
- [Flask](http://flask.pocoo.org/) - Python framework used to build the platform. 
- [MongoDB](https://www.mongodb.com/) - Relational database store for model data.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - Interface to manage MongoDB manually.
- [Heroku](https://www.heroku.com/) - Platform used to import the entirely platfom into the cloud.


## Production Deployment

See a live version of this platform [here](https://recipes-manager-flask.herokuapp.com/).

##### The process I took was as follows:

- Create Heroku repositery.
- Login to Heroku: heroku login
- Open your project, create a local git repository: git init
- Add Heroku as remote: git remote add origin https://recipes-manager-flask.herokuapp.com/
- Add changes: git add .
- Commit changes: $ git commit -am "make it better"
- Push changes: git push heroku master


## Databse schema:

There two types of collection within MongoDB. one is the actual recipes and then the cuisines types called categories. See below an example of how they are both structured:

- The main MongoDB collection `recipes` takes he following schema.

```json
{
    "_id": {
        "$oid": "5ca5f9c11c9d440000fcef84"
    },
    "recipe_name": "Pizza Margarita",
    "category_name": "Italian",
    "recipe_intro": "This is a classic pizza",
    "description": "Mix all ingredients. Bake for 35 mins at 180C",
    "ingredients": "Cheese, flower, eggs, tomato sauce, oil, ham",
    "prep-time": "19 min",
  }
```
- The second MongoDB collection `categories` takes he following schema.

```json
{
    "_id": {
        "$oid": "5ca5f9c11c9d440000fcef54"
    },
    "category_name": "Italian",
  }
```

## References:
- PyMongo docs: https://api.mongodb.com/python/current/tutorial.html
- Flask docs: http://flask.pocoo.org/docs/1.0/

### Acknowledgements

-

#### Licence
Copyright (c) 2019 Lucas Suarez