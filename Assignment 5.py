#1.	Create database – restaurant, create collection – rescollection Insert the documents into collections.

from pymongo import MongoClient
import json

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    db = client['restuarantDB']
    collection = db['rescollection']

    with open(r'C:\restaurants-dataset(2).json','r', encoding='utf-8') as file:
        record = file.read()
        record = record.replace('\n','')
        record = record.replace('}{','},{')
        record = '[' + record + ']'
        file_data = json.loads(record)

    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)        

#2.  Display all the documents in the collection rescollection.
    print("Display all the documents in the collection rescollection")
    cursor = collection.find({})

    for document in cursor:
        #print(document)


     
#3.	Display the fields restaurant_id, name, borough, and zip code, but exclude the field _id for all the documents in the collection restaurant.

    # field_dis = collection.find({},{'restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1,'_id':0}).limit(30);

     field_dis = collection.aggregate([{'$group':{'_id':{'RestuarantId':'$restaurant_id','name':'$name','borough':'$borough','cuisine':'$cuisine'}}},{'$limit':20}])
     for item in field_dis:
         print(item)

    '''

## to be executed in mongoDB 

# 4.	Find the restaurants who achieved a score more than 90.

    db.rescollection.find({'grades':{'$elemMatch':{'score':{'$gt':90}}}})



# 5.	Show the restaurants that achieved a score, more than 80 but less than 100.

db.rescollection.find({'grades' : { '$elemMatch':{'score':{'$gt ': 80 , '$lt' :100}}}});

 

# 6.	Write Query to show the restaurants that do not prepare any cuisine of american & their grade score > 70.

db.rescollection.find({'$and': [{'cuisine' : {'$ne' :'American '}},

                       {'grades.score' : {'$gt' : 70}},]});

                       

# 7.	Write a MongoDB query to arrange the name of the cuisine in an ascending order and for that same borough arranged in descending order.

db.rescollection.find().sort({'cuisine':1,'borough': -1,});
                           

# 8.	Write a MongoDB query to arrange the name of the cuisine in descending order.

db.rescollection.find().sort({'cuisine':-1,});

                           

# 9.	Show the restaurant Id, name, borough and cuisines for those restaurants which prepared dish except 'American' and 'Chinese' or restaurant's name begins with letter 'Bil'.

db.rescollection.find({'$or':[{'name': '/^Bil/'},{'$and': [

       {'cuisine' : {'$ne' :'American '}}, 

       {'cuisine' : {'$ne ':'Chinese'}}]}]},{'restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1});

      

# 10.	 Show the restaurant Id, name, borough and cuisines and score for restaurant's name begins with letter 'Bil'.

db.rescollection.find([{'$or':{'name': '/^Bil/'},{'restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1, 'grades.score':1}}]);

 

#11.	Show the restaurant Id, name, borough and cuisines and score for restaurant serving “Indian” as cuisines. 

db.rescollection.find([{$match: {cuisine:”Indian”}}],{“restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1, 'grades.score':1});



#12.	Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'bi' as last three letters for its name.

db.rescollection.find({name: /bi$/},{'restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1,'grades.score':1});

 

# 13.	Write a MongoDB query to find the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' as last three letters for its name.

db.rescollection.find({name: /il$/},{'restaurant_id' : 1,'name':1,'borough':1,'cuisine' :1,'grades.score':1});



# 14.	Write a query to show all the restaurant Id, name, borough, cuisines, and score for those restaurants which contain 'il' anywhere in its name.

db.rescollection.find({'name': /.*il*/},{'restaurant_id':1,'name':1,'borough':1,'cuisine' :1, 'grades.score':1});

 

# 15.	Write a MongoDB query which will select the restaurant Id, name and grades for those restaurants which returns 0 as a remainder after dividing the score by 7.

db.rescollection.find({'grades.score':{$mod : [7,0]}},{'restaurant_id' : 1,'name':1,'grades':1});

 

# 16.	Show document/record counts that has street and not street in addresses. 

db.rescollection.find({'address.street':{ $exists : true }});

 

# 17.	Write a MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168 

db.rescollection.find({'cuisine' : {$ne : 'American '},

'grades.score' :{$gt: 70},'address.coord' : {$lt : -65.754168}});
'''
