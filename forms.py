from flask.ext.wtf import Form, TextField, DecimalField, SelectField, validators
#from wtforms import Form, TextField, PasswordField, validators

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
    
class Today(Form):
    category = SelectField('', [validators.Required(message="Please select a category.")], 
                            choices=clothes_categories)
                            
class Today2(Form):
    items = SelectField('', [validators.Required(message="Select desired item.")])