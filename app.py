import os 
import re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes_manager'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@my-first-cluster-hgde0.mongodb.net/recipes_manager?retryWrites=true'

mongo = PyMongo(app)


# -----Homepage------

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    if request.args.get('recipe_name') is not None: 
        recipenameregex = "\W*"+request.args.get("recipe_name")+"\W*"
        recipename = re.compile(recipenameregex, re.IGNORECASE)
        recipes=mongo.db.recipes.find({"recipe_name": recipename})
        return render_template("recipes.html", recipes=recipes)
        
    if request.args.get('preparation_time') is not None: 
        preparationtimeregex = "\W*"+request.args.get("preparation_time")+"\W*"
        preparationtime = re.compile(preparationtimeregex, re.IGNORECASE)
        recipes=mongo.db.recipes.find({"preparation_time": preparationtime})
        return render_template("recipes.html", recipes=recipes)

    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    return render_template('search.html', categories=mongo.db.categories.find())
    
    

# -----Charts------
@app.route('/charts')
def charts():
    return render_template("charts.html")
    
@app.route('/data')
def data():
    categories = mongo.db.categories
    results = categories.find()
    
    return jsonify({'results' : result['values']})
    
# ---End Charts----
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe,
                           categories=all_categories)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'recipe_intro':request.form.get('recipe_intro'),
        'ingredients': request.form.get('ingredients'),
        'description': request.form.get('description'),
        'preparation_time': request.form.get('preparation_time'),
        'photo_url': request.form.get('photo_url')
        
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

@app.route('/categories')
def categories():
    return render_template('categories.html',
                           categories=mongo.db.categories.find())
                           
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                           {'_id': ObjectId(category_id)}))                           

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('categories'))
    
@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.categories.insert_one(category_doc)
    return redirect(url_for('categories'))


@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')
    
    
@app.route('/recipe_single/<recipe_id>')
def recipe_single(recipe_id):
    return render_template("recipepage.html",
                           recipes=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))
                           


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
