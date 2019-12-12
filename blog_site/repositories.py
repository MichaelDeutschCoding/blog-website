import hashlib
from blog_site import db
from blog_site.models import User, Blog

class UsersRepository:
    def register(self, email,
                 first_name,
                 last_name,
                 password,
                 username):
        user = User(email=email,
                    username=username,
                    f_name=first_name,
                    l_name=last_name,
                    password=hashlib.sha256(password.encode('utf-8')).digest())
        db.session.add(user)
        db.session.commit()


class BlogsRepository:
    def add_blog(self,user_id,
                 title,
                 content,
                 tags):
        tags = [t.strip() for t in tags.split(',')]
