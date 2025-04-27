import requests

API_KEY = 'YOUR_API_KEY_HERE'  # Получи ключ на https://cryptopanic.com/developers/api/
BASE_URL = 'https://cryptopanic.com/api/v1/posts/'

def fetch_latest_news():
    params = {
        'auth_token': API_KEY,
        'kind': 'news',
        'public': 'true',
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        print("\n📰 Последние новости из мира блокчейна:\n")
        for post in data.get('results', [])[:10]:
            title = post.get('title')
            url = post.get('url')
            print(f"🔹 {title}\n   {url}\n")

    except Exception as e:
        print(f"❌ Ошибка при получении новостей: {e}")

if __name__ == '__main__':
    fetch_latest_news()
