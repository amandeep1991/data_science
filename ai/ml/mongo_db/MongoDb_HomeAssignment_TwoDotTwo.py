import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
grades = db.grades

temp_id=""
count = 0
for record in grades.find({
    'type': 'homework'
    }).sort([('student_id', 1), ('score', 1)]):
    if temp_id != record['student_id']:
        record_returned = grades.delete_one({"_id":record['_id']})
        count+=1
    temp_id = record['student_id']

print("Total items deleted: ",count)

# ll = [ grade for grade in grades.find({'type':'homework'}).sort([('student_id',1), ('score',1)]) ]
# lowest_score = []
# temp_id = ""
# for record in ll:
#     if temp_id!=record['student_id']:
#         lowest_score.append(record)
#     temp_id = record['student_id']
# len(lowest_score)

# How to view document fields in mongo shell?
Object.keys(db.gsk_feedback.findOne())