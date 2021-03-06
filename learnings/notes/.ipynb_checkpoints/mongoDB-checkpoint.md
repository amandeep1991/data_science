1. Arrays:
    * $elemMatch

```mongodb
    boxOffice: [ { "country": "USA", "revenue": 228.4 },
             { "country": "Australia", "revenue": 19.6 },
             { "country": "UK", "revenue": 33.9 },
             { "country": "Germany", "revenue": 16.2 },
             { "country": "France", "revenue": 19.8 } ]

    db.movieDetails.find({"boxOffice.country": "Germany", "boxOffice.revenue": {$gt: 17}}) # returns this record (with all the values)
    
    db.movieDetails.find({"boxOffice.country": "Germany", "boxOffice.revenue": {$gt: 228}})
    
    use video
    martian = db.movieDetails.findOne({title: "The Martian"})
    martian
    delete martian._id;
    martian
    martian.boxOffice = [
        {"country": "USA", "revenue": 228.4},
        {"country": "Australia", "revenue": 19.6},
        {"country": "UK", "revenue": 33.9},
        {"country": "Germany", "revenue": 16.2},
        {"country": "France", "revenue": 19.8}
    ]
    db.movieDetails.insertOne(martian);
    
    db.movieDetails.find({boxOffice: {$elemMatch: {"country": "Germany", "revenue": {$gt: 17}}}})
    
    db.movieDetails.find({boxOffice: {$elemMatch: {"country": "Germany", "revenue": {$gt: 16}}}})
    
```

* Insert new field in every document:
```javascript
db.gsk_feedback.update(
  {},
  { $set: {"app_version": "v1"} },
  false,
  true
)
```