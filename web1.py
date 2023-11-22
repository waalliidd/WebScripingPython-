import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.copaco.com/fr-fr/hardware/category/ordinateurs-portables-comcomlap"
    page = requests.get(url)

    if page.status_code == 200:
        src = page.content
        soup = BeautifulSoup(src, 'html.parser')
        list_books = soup.find_all("div", {'class':'product-tile-list row'})
        if list_books:
            book1 = list_books[0].find('div')  # Accessing the first element
            if book1:
                print(book1)
                print(page.status_code)
        else:
                print("Book element not found inside product-tile-list.")
                
                 
    else:
        print("Product-tile-list row element not found.")

if __name__ == "__main__":
    main()

    