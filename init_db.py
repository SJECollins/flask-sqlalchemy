from testproject import app, db
from testproject.models import User

with app.app_context():
    db.create_all()
