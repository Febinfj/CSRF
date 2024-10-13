import requests
from bs4 import BeautifulSoup

def check_csrf_vulnerability(target_url):
    response = requests.get(target_url)
    page_content = BeautifulSoup(response.text, 'html.parser')

    form_elements = page_content.find_all('form')
    for form in form_elements:
        token_field = form.find('input', {'name': 'csrf_token'})
        if token_field is None:
            print(f"Potential CSRF vulnerability detected on: {target_url}")

test_url = 'https://www.facebook.com'
check_csrf_vulnerability(test_url)
