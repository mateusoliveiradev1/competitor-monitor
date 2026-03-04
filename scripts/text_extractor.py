import sys, requests
from bs4 import BeautifulSoup

def extract(url):
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        print(text[:3000]) # Return first 3000 chars to avoid context bloat
    except Exception as e:
        print(f"Extraction failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    extract(sys.argv[1])
