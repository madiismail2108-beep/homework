from dataclasses import dataclass
import psycopg2

conn=psycopg2.connect(
    dbname='n70',
    user='postgres',
    password='1234',
    host='localhost',
    port='5432'
)

cur=conn.cursor()
@dataclass
class commit:
    func: callable
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        conn.commit()
        print(" Changes committed to database (commit).")
        return result
    
@dataclass
class User:
    username: str
    role: str

@dataclass  
class permission_required:
    func: callable

    def __call__(self, user, *args, **kwargs):
        if user.role == "admin":
            print(f"this user  {user.username} have permission.")
            return self.func(user, *args, **kwargs)
        else:    
            print('changing id added to database (commit)')
            return None


@commit
@permission_required
def create_post(user: User, title: str, content: str):
    cur.execute(
        "INSERT INTO posts (title, content, author) VALUES (%s, %s, %s)",
        (title, content, user.username)
    )
    print(f"Post was created by:'{title}' {user.username} .")

@commit
@permission_required
def delete_post(user: User, post_id: int):
    cur.execute("DELETE FROM posts WHERE id = %s", (post_id,))
    print(f"Post was deleted by: {post_id} {user.username}")

