import requests
import csv

def fetch_and_print_posts():
    """
    JSONPlaceholder API-dən postları alır və başlıqlarını ekrana çap edir.
    """
    # API-dən məlumat alırıq
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Status kodunu çap edirik
    print(f"Status Code: {response.status_code}")
    
    # Əgər sorğu uğurludursa (status kodu 200)
    if response.status_code == 200:
        # JSON məlumatını Python obyektinə çeviririk
        posts = response.json()
        
        # Hər bir postun başlığını çap edirik
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    JSONPlaceholder API-dən postları alır və CSV faylına yazır.
    """
    # API-dən məlumat alırıq
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Əgər sorğu uğurludursa
    if response.status_code == 200:
        # JSON məlumatını Python obyektinə çeviririk
        posts = response.json()
        
        # Yalnız lazım olan sahələri (id, title, body) saxlayırıq
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # CSV faylına yazırıq
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Sahə adlarını təyin edirik
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Başlıqları yazırıq
            writer.writeheader()
            
            # Məlumatları yazırıq
            for post in structured_posts:
                writer.writerow(post)
