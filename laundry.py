from flask import Flask, render_template, request, flash, url_for, send_from_directory
import db
from forms import Clothes, Today, Today2
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get('LAUNDRY_KEY')


@app.route('/')
def start():
    return render_template('index.html', form = Today(request.form))
    
@app.route('/favicon.ico')
def get_icon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'll.ico')
    
@app.route('/closet')
def closet():
    return render_template('closet.html', form = Clothes(request.form))

@app.route('/closet', methods=['GET', 'POST'])
def build_closet():
    form = Clothes(request.form)
    if request.method == 'POST' and form.validate():
        item = {'type': form.category.data, 'item': form.item.data, 'color': form.color.data, 
                'brand': form.brand.data, 'price': float(form.price.data), 'worn': []}
        db.add_to_closet(item)
        print "added", item['item']
        #flash(form.item.data,'added to your closet.')
    return render_template('closet.html', form=form)
    
@app.route('/<category>', methods=['GET', 'POST'])
def wear(category):
    print "received", category, "request"
    form = Today2(request.form)
    form.items.choices = [(i['_id'],i['item']) for i in db.find_category(category)]
    if request.method == 'POST': #and form.validate():  #look into validate and why returning False here
        print form.items.data
        db.worn(form.items.data)
        print db.find_item(form.items.data)
    return render_template('index.html', form=Today(request.form))
    
@app.route('/', methods=['GET', 'POST'])
def closet_items():
    form = Today(request.form)
    print "request received"
    if request.method == 'POST' and form.validate():
        category = form.category.data
        form2 = Today2(request.form)
        form2.items.choices = [(i['_id'],i['item']) for i in db.find_category(category)]
        return render_template('today.html', form=form2, category=category)
    return render_template('index.html', form=form, category='category')
    
if __name__ == '__main__':
    app.debug = True
    app.run()