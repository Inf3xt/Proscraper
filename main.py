import json
import requests

with open('config.json', 'r') as f:
    data = json.load(f)

class Proscraper:
    def __init__(self):
        self.a = "a"
        self.session = requests.Session()
        self.proxy_type = "socks4"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"
        }

    def get_proxies(self, proxy_type=4):
        if proxy_type == 4: self.proxy_type = "socks4"
        elif proxy_type == 5: self.proxy_type = "socks5"
        elif proxy_type == 1: self.proxy_type = "http"
        else: pass
        
        for url in data['proxylists'][self.proxy_type]:
            x = self.session.get(
                url['url'],
                headers=self.headers
            ).text
            with open(f'{self.proxy_type}_proxies.txt', 'a') as f:
                f.write(x)
                
    def check_proxies(self, proxy_type=4, timeout=3):
        if proxy_type == 4: self.proxy_type = "socks4"
        elif proxy_type == 5: self.proxy_type = "socks5"
        elif proxy_type == 1: self.proxy_type = "http"
        else: pass

        with open(f'{self.proxy_type}_proxies.txt', 'r') as f:
            proxies = f.read().split()

        for proxy in proxies:
            proxies_d = {
                "http": f"socks4://{proxy}",
                "https": f"socks4://{proxy}"
            }
            try:
                requests.get("https://httpbin.org/ip", proxies=proxies_d, timeout=timeout)
                print("Working proxy! Adding to file!")
                with open(f'working_{self.proxy_type}_proxies.txt', 'a') as f:
                    f.write(f"{proxy}\n")
            except:
                print("Proxy is dead!")

    def check_proxies_2(self, proxy_type=4, timeout=3, threads=10):
        """
        This with threading to make it faster!
        """
        if proxy_type == 4: self.proxy_type = "socks4"
        elif proxy_type == 5: self.proxy_type = "socks5"
        elif proxy_type == 1: self.proxy_type = "http"
        else: pass

        with open(f'{self.proxy_type}_proxies.txt', 'r') as f:
            proxies = f.read().split()

        for proxy in proxies:
            proxies_d = {
                "http": f"socks4://{proxy}",
                "https": f"socks4://{proxy}"
            }
            



proscraper = Proscraper()
proscraper.get_proxies(proxy_type=4)
# proscraper.check_proxies(timeout=1)