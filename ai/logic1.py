import urllib.parse
import requests
from config1 import POLLINATIONS_API_KEY

class Polination_ai():
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        


    def generation_image(self, prompt_text):
        prompt = urllib.parse.quote(prompt_text)
        url = f"https://image.pollinations.ai/prompt/{prompt}?model=flux&width=1024&height=1024"

        headers = {"Authorization": f"Bearer {POLLINATIONS_API_KEY}"}

        try:
            response = requests.get(url, headers=headers, timeout=40)
            if response.status_code == 200:
                return response.content
            else:
                print(f"Ошибка API Pollinations: Статус {response.status_code}")
                return None
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return None




