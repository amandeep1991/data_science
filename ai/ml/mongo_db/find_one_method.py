import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.school

scores = db.scores


def find_by_id(id):
    global query, projections
    try:
        query = {
            'student_id': id,
            'score'     : {
                '$gt': 0,
                '$lt': 100
                }
            }
        projections = {
            "student_id": 1,
            'score'     : 1,
            "_id"       : 0
            }
        doc = scores.find_one(query, projections)
    except Exception as e:
        print("Unexpected Error: ", type(e), e)

    print(doc)


find_by_id(10)

print("##############################")

cursor_object = scores.find(query, projections)
for each_record in cursor_object:
    print(each_record)


# ll = [ grade for grade in grades.find({'type':'homework'}).sort([('student_id',1), ('score',1)]) ]
