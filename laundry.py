from flask import Flask, render_template, request, flash, url_for, send_from_directory, jsonify
import db
from forms import Clothes, Today, Category
import json
import os
from bson import json_util

app = Flask(__name__)
app.secret_key = 'testing1234' #os.environ.get('LAUNDRY_KEY')


@app.route('/')
def start():
    return render_template('index.html', form = Category(request.form))
    
@app.route('/favicon.ico')
def get_icon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'll.ico')
    


@app.route('/closet/view/<category>', methods=('GET', 'POST'))
def view_closet(category):
    items=db.find_category(category)
    return json.dumps(items, default=json_util.default)

@app.route('/closet/view', methods=('GET', 'POST'))
def view():
    return render_template('view_closet.html', form = Category(request.form))

@app.route('/closet', methods=('GET', 'POST'))
def add_item_to_closet():
    form = Clothes(request.form)
    if request.method == 'POST': #and form.validate_on_submit():
        price = form.price.data
        if price is not None:
            price = float(price)

        item = {
                'type': form.category.data, 
                'item': form.item.data, 
                'color': form.color.data, 
                'brand': form.brand.data, 
                'price': price, 
                'worn': [],
                }
        db.add_to_closet(item)
        print "added", item['item']    # need to add logging!!
        form.reset()
        #flash(form.item.data,'added to your closet.')
    return render_template('closet.html', form=form)

@app.route('/closet', methods=('GET'))
def closet():
    return render_template('closet.html', form = Clothes(request.form))
    
@app.route('/<category>', methods=('GET', 'POST'))
def wear(category):
    print "received", category, "request"
    form = Today(request.form)
    form.items.choices = [(i['_id'],i['item']) for i in db.find_category(category)]
    if request.method == 'POST': #and form.validate():  #look into validate and why returning False here
        db.worn(form.items.data)
        print 'worn updated for', db.find_item(form.items.data)['item']
    return render_template('index.html', form=Category(request.form))
    
@app.route('/', methods=('GET', 'POST'))
def closet_items():
    form = Category(request.form)
    print "request received"
    if request.method == 'POST' and form.validate():
        category = form.category.data
        form2 = Today(request.form)
        form2.items.choices = [(i['_id'],i['item']) for i in db.find_category(category)]
        return render_template('today.html', form=form2, category=category)
    return render_template('index.html', form=form, category='category')
    
if __name__ == '__main__':
    app.debug = True
    app.run()