import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.shortened_length = 6

    def generate_shortened_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.shortened_length))

    def shorten_url(self, original_url):
        if original_url in self.url_mapping:
            return self.url_mapping[original_url]
        else:
            while True:
                short_url = self.generate_shortened_url()
                if short_url not in self.url_mapping.values():
                    self.url_mapping[original_url] = short_url
                    return short_url

    def expand_url(self, short_url):
        for original_url, shortened_url in self.url_mapping.items():
            if shortened_url == short_url:
                return original_url
        return "URL not found."

def main():
    shortener = URLShortener()

    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            original_url = input("Enter the URL to shorten: ")
            short_url = shortener.shorten_url(original_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the shortened URL: ")
            original_url = shortener.expand_url(short_url)
            print(f"Expanded URL: {original_url}")
        elif choice == '3':
            print("Good
