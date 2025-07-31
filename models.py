import peewee

database = peewee.SqliteDatabase('reviews.db')

class Review(peewee.Model):
    name = peewee.CharField()
    text = peewee.CharField()
    rating = peewee.IntegerField()
    date = peewee.CharField()
    company = peewee.CharField() #url
    class Meta:
        database = database
    

database.connect()
database.create_tables([Review], safe=True)