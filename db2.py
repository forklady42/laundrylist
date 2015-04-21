from datetime import date
import mysql.connector
from bson.objectid import ObjectId

config = {
  'user': 'test',
  'password': 'secret',
  'host': '127.0.0.1',
  'database': 'closet',
  'raise_on_warnings': True,
}

def connect():
    """ Connect to MySQL database """
    try:
        connection = mysql.connector.connect(**config)
 
    except Error as e:
        print(e)


def add_to_closet(item):
    #'''Returns object id of item'''
    #return closet.insert(item) 
    
    
def find_category(category):
    '''
    Finds all items in a specified category and sorts
    based on number of times worn.
    '''
    items = []
    for i in closet.find({'type': category}).sort('worn_freq', -1):
        items.append(i)
    return items
        
def find_item(id):
    #closet.find_one({'item': item})
    return closet.find_one({'_id': ObjectId(id)})
    
def remove_item(id):
    closet.remove({'_id': ObjectId(id)})
    
def worn(id):
    dates = find_item(id).get('worn')
    dates.append(date.today().isoformat())
    closet.update({'_id': ObjectId(id)}, {'$set': {'worn': dates}, '$inc': {'worn_freq': 1}}, upsert=True)
    #closet.update({'_id': ObjectId(id)}, {'$inc': {'worn_freq': 1}}, upsert=True)
    
def best_buy(category):
    items = find_category(category)
    best_buy = None
    cost_ratio = float('inf')
    for i in items:
        if len(i.get('worn')) and i.get('price') and i.get('price')/len(i.get('worn')) < cost_ratio:
            best_buy = i
            cost_ratio = i.get('price')/len(i.get('worn'))
    return best_buy
    
def favorite(category):
    return find_category(category)[0]
    
def donate(category):
    items = find_category(category)
    return items[len(items)-1]
    
if __name__ == "__main__":
    '''
    closet.remove({})
    item1 = {'type': 'dress', 'color': 'black', 'brand': 'anthro', 'price': 50}
    item2 = {'type': 'dress', 'color': 'red', 'brand': 'gap', 'other': 'hand-me down', 'price': 20}
    item3 = {'type': 'shoes', 'sub-type': 'heels', 'color': 'black'}
    
    add_to_closet(item1)
    add_to_closet(item2)
    add_to_closet(item3)
    
    print find_category('dress')
    closet.remove({})
    '''
    print favorite('dress')['item']
    print best_buy('dress')['item']