from datetime import date
from pymongo import Connection
from bson.objectid import ObjectId

connection = Connection()
db = connection.walkin
closet = db.closet

def add_to_closet(item):
    return closet.insert(item)
    
    
def find_category(category):
    items = []
    for i in closet.find({'type': category}):
        items.append(i)
    return items
        
def find_item(id):
    #closet.find_one({'item': item})
    return closet.find_one({'_id': ObjectId(id)})
    
def worn(id):
    dates = find_item(id).get('worn')
    if dates:
        dates.append(date.today().isoformat())
    else:
        dates = [date.today().isoformat()]
    closet.update({'_id': ObjectId(id)}, {'$set': {'worn': dates}}, upsert=True)
    
def best_buy(category):
    items = find_category(category)
    best_buy = None
    cost_ratio = float('inf')
    for i in items:
        if i.get('worn') and i.get('price') and i.get('price')/len(i.get('worn')) < cost_ratio:
            best_buy = i
            cost_ratio = i.get('price')/len(i.get('worn'))
    return best_buy
    
def favorite(category):
    items = find_category(category)
    fav = None
    num_worn = 0
    for i in items:
        if i.get('worn') and len(i.get('worn')) > num_worn:
            fav = i
            num_worn = len(i.get('worn'))
    return fav
    
def donate(category):
    items = find_category(category)
    donate = None
    num_worn = float('inf')
    for i in items:
        if (i.get('worn') and len(i.get('worn')) < num_worn) or i.get('worn')==None:
            fav = i
            num_worn = len(i.get('worn'))
    return fav
    
if __name__ == "__main__":
    closet.remove({})
    item1 = {'type': 'dress', 'color': 'black', 'brand': 'anthro', 'price': 50}
    item2 = {'type': 'dress', 'color': 'red', 'brand': 'gap', 'other': 'hand-me down', 'price': 20}
    item3 = {'type': 'shoes', 'sub-type': 'heels', 'color': 'black'}
    
    add_to_closet(item1)
    add_to_closet(item2)
    add_to_closet(item3)
    
    #worn(find_item(item1)['_id'])
    #worn(find_item(item1)['_id']) 
    #worn(find_item(item2)['_id'])
    
    print favorite('dress')
    print
    print best_buy('dress')
    print
    
    print find_category('dress')
    closet.remove({})