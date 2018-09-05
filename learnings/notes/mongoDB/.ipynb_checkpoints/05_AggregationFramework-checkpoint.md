# Aggregation Framework

1. Simple Aggregation Framework
    * If I wanted to find no. of products from each manufacturer:
        * in sql we would write:
        ```sql
            select manufacturer, count(*) from products group_by manufacturer
        ```
        * in mongodb:
            ```mongo
                use agg
                
                db.products.aggregate([
                    {$group:
                        {
                            _id:"$manufacturer",
                            num_products: {$sum:1}
                        }
                    }
                ])
            ```
            ![05.01.AggregationQueryExecution.jpg](img/05.01.AggregationQueryExecution.jpg)
            
2. MongoDb uses **Aggregation Pipeline**:
    * Example - Collection->Project->Match->Swap->sort
    
    * Brief description of each stage in the pipeline:
        1.  ```$project``` : (reshape               - 1:!)
        2.  ```$match  ``` : (filter                - n:1) 
        3.  ```$group  ``` : (aggregate             - n:1) 
        4.  ```$sort   ``` : (sort                  - 1:1) 
        5.  ```$skip   ``` : (skip                  - n:1) 
        6.  ```$limit  ``` : (limit                 - n:1) 
        7.  ```$unwind ``` : (normalize(flatten)    - n:1) 
        8.  ```$out    ``` : (output                - n:1) 
        9.  ```$redget ``` : (authorization         ) 
        10. ```$geonear``` : (location based query  ) 
            
3. Compound Grouping
    * sql example
        ```sql
            select manufacturer, category, count(*) from products
            group_by manufacturer, category 
        ```
        
    * in mongoDB
        ```mongo
            use agg
            
            db.products.aggregate([
                {$group: 
                    {
                        _id: {
                            "manufacturer": "$manufacturer",
                            "category": "$category"
                        },
                        
                        num_products: {$sum:1} ##REPLACE_ME##
                        
                    }    
                }
            ])
        ```
        
4. _id can also be complex in mongoDB:

    ```mongo
        db.foo.insert({_id:{name: "andrew", class:"m101"}, hometown:"NY"})
    ```       
    
    
5. Aggregation (```$group```) Expressions Overview: [examples are shown below are the line (denoted by '##REPLACE_ME##') to be replaced in above example]
    * **```$sum```** - ```sum_prices: {$sum:"$price"}```
        ```mongo
            db.zips.aggregate([{"$group":{"_id":"$state", "population":{$sum:"$pop"}}}])
        ```
    * **```$avg```** - ```sum_prices: {$avg: "$price"}```
        ```mongo
            db.zips.aggregate([{"$group":{"_id":"$state", "average_pop":{$avg:"$pop"}}}])
        ```
    * **```$addtoSet```** - Add unique values in an array/set
        ```mongo
            use agg
            
            db.products.aggregate([
                {$group:
                    {
                        _id:{
                            "maker":"$manufacturer"
                        },
                        categories: {$addToSet: "$Category"}
                    }
                }
            ])
        ```
    * **```$push```** - same as $addToSet, but it can add duplicate entries 
    * **```$min```** - ```maxprice: {$max: "$price"}```
    * **```$max```** - 
    * **```$first```** - [must be used with sort]
    * **```$last```** - [must be used with sort]
    
    **NOTE**: We can do **DOUBLE GROUPING**. Eg - avg of every students' avg marks
        ```mongo
            use agg
            
            db.grades.aggregate([
                {
                    '$group': 
                        {
                            _id: {class_id:"$class_id", student_id:"$student_id"},
                            'average': {"$avg":"$score"}
                        }
                },
                {
                    '$group': 
                        {
                            _id: "$_id.class_id",
                            'average': {"$avg":"$average"}
                        }
                },
            ])
        ```
        
        **Sample Question**
        ```mongo
            > db.fun.find()
                { "_id" : 0, "a" : 0, "b" : 0, "c" : 21 }
                { "_id" : 1, "a" : 0, "b" : 0, "c" : 54 }
                { "_id" : 2, "a" : 0, "b" : 1, "c" : 52 }
                { "_id" : 3, "a" : 0, "b" : 1, "c" : 17 }
                { "_id" : 4, "a" : 1, "b" : 0, "c" : 22 }
                { "_id" : 5, "a" : 1, "b" : 0, "c" : 5 }
                { "_id" : 6, "a" : 1, "b" : 1, "c" : 87 }
                { "_id" : 7, "a" : 1, "b" : 1, "c" : 97 }
                
            db.fun.aggregate([{$group:{_id:{a:"$a", b:"$b"}, c:{$max:"$c"}}}, {$group:{_id:"$_id.a", c:{$min:"$c"}}}])
            
            Answer - 52, 22
        ```
    
6.  $project
    * Can do following:
        1. remove keys
        2. add new keys
        3. reshape keys - put a key in some document
        4. Use some simple functions on keys
            * ```$toUpper```
            * ```$toLower```
            * ```$add```
            * ```$multiply```
            
    * Example:
        ```mongo
            use agg
            
            db.products.aggregate([
              {
                $project:
                  {
                    _id:0, # remove key
                    'maker': {$toLower: '$manufacturer'}, # add new key
                    'details': {
                                  'category':'$category', # reshape
                                  'price': {"$multiply": ["$price", 10]} # simple function
                               },
                    'item': "$name "
                  }
              }
            ])
        ```