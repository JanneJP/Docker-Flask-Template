from project import db


class Placeholder(db.Model):
    __tablename__ = "placeholder"

    id = db.Column(db.Integer, primary_key=True)
    test_string = db.Column(db.String, nullable=False)

    def __init__(self, test_string):
        self.test_string = test_string

    def __repr__(self):
        return f'<Placeholder({self.test_string})>'
