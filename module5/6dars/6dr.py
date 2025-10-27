import requests
import json
import threading
import time

post_url = "https://dummyjson.com/posts"
comment_url = "https://dummyjson.com/comments"

r = requests.get(post_url)
data = r.json()

print(data['posts'])

def download_as_file(file_path, url):
    r = requests.get(url)
    with open(file_path, 'w+') as f:
        f.write(r.text)
    print('sending ....')
    time.sleep(2)
    print('alredy sent')

t1 = threading.Thread(target=download_as_file, args=("posts.json", post_url))
t2 = threading.Thread(target=download_as_file, args=("comments.json", comment_url))

t1.start()
t2.start()

print('all done')