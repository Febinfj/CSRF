import requests
from bs4 import BeautifulSoup

def csrf_scanner(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    csrf_vulnerable = False 

    for form in forms:
        csrf_token = form.find('input', {'name': 'csrf_token'})
        if not csrf_token:
            print(f"CSRF vulnerability found in form at: {url}")
            csrf_vulnerable = True

    if not csrf_vulnerable:
        print(f"No CSRF vulnerabilities found in forms at: {url}")


url = 'https://www.example.com'  
csrf_scanner(url)
