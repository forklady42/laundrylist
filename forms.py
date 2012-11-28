from flask.ext.wtf import Form, TextField, DecimalField, SelectField, validators
#MultiDict is the basis of form--allows HTML form elements to pass multiple values for the same key
from werkzeug.datastructures import MultiDict

'''
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='must match')
    ])
    confirm = PasswordField('Repeat')
'''

clothes_categories =[('',''), ('access', 'accessory'), ('dress', 'dress'), ('outer', 'outerwear'), 
                     ('pants', 'pants'), ('shirt', 'shirt'), ('shoes', 'shoes'),  
                     ('skirt', 'skirt')]
    
class Clothes(Form):
    category = SelectField('Category', [validators.Required(message="Please select a category.")], 
                            choices=clothes_categories)
    item = TextField('Item', [validators.Required(message="Item description is required.")])
    color = TextField('Color')
    brand = TextField('Brand')
    price = DecimalField('Price', places=2)
    
    def reset(self):
        blankData = MultiDict([ (self.price, None)])
        self.process(blankData)
    
class Category(Form):
    category = SelectField('', [validators.Required(message="Please select a category.")], 
                            choices=clothes_categories, id="category")
                            
class Today(Form):
    items = SelectField('', [validators.Required(message="Select desired item.")])