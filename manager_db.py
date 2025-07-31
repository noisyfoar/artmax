from models import Review, database

class DBManager:
    def is_review_exists(self, company, name, text):
        return Review.select().where(
            (Review.company == company) &
            (Review.name == name)       &
            (Review.text == text)
        ).exists()

    def save_review(self, company, name, text, rating, date):
        try:
            Review.create(
                company=company,
                name=name,
                text=text,
                rating=rating,
                date=date
            )
            return True
        except Error:
            return False

    def save_reviews(self, reviews_data, url):
        new_count = 0
        with database.atomic(): 
            for data in reviews_data:
                if not self.is_review_exists(url, data[0], data[1]):
                    self.save_review(
                        company=url,
                        name=data[0],
                        text=data[1],
                        rating=data[3],
                        date=data[2]
                    )
                    new_count += 1
        return new_count

    def get_reviews(self, company):
        return Review.select().where(Review.company == company)