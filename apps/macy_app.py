import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import concurrent.futures

product_brands = []
product_names = []
current_prices = []
old_prices = []
ratings = []
product_urls = []

def scrape_macy(url):

    ua = UserAgent()
    userAgent = ua.random
    headers = {'User-Agent': userAgent}
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    sales_box = soup.find_all('div', class_ = "product-thumbnail-container")
    for box in sales_box:
        #product_brand
        if box.find('div', class_ = "product-brand medium") is not None:
            product_brand = box.find('div', class_ = "product-brand medium")
            product_brands.append(product_brand.text)
        else:
            product_brands.append('None')

        #product_names
        if box.find('div', class_ = "product-name medium") is not None:
            product_name = box.find('div', class_ = "product-name medium")
            product_names.append(product_name.text.lstrip())
        else:
            product_names.append('None')

            #current_prices
        if box.find('span', class_ = "discount price-reg") is not None:
            current_price = box.find('span', class_ = "discount price-reg")
            current_prices.append(current_price.text.rstrip())
        elif box.find('span', class_ = "price-reg") is not None:
            current_price = box.find('span', class_ = "price-reg")
            current_prices.append(current_price.text.rstrip())
        else:
            current_prices.append('None')

            #old_prices
        if box.find('span', class_ = "price-strike") is not None:
            old_price = box.find('span', class_ = "price-strike")
            old_prices.append(old_price.text.strip())
        else:
            old_prices.append('None')

        #ratings
        if box.select_one("div.rating > div > fieldset") is not None:
            rating = box.select_one("div.rating > div > fieldset")
            rating = rating['aria-label']
            ratings.append(rating.replace('Rated','').replace(' stars','').strip())
        else:
            ratings.append('None')

        #product_urls
        if box.find('a', class_ = "brand-and-name") is not None:
            product_url = box.find('a', class_ = "brand-and-name")
            product_url = product_url['href']
            product_urls.append('https://www.macys.com'+ product_url)
        else:
            product_urls.append('None')

    if soup.find('a', class_ = 'pagination-next') is None:
        a = 1
        b = 'e'
        a+b
    else:
        pass


    
# Streamlit UI and functionality
st.title("Macy's Product Scraper")

# Get user input URL
your_url = st.text_input("Please paste Macy's link (e.g., https://www.macys.com/shop/handbags-accessories?id=26846)")

if your_url:
    base_url, query_string = your_url.split('?', 1)
    index = 1

    while True:
        try:
            page = '/Pageindex/' + '{}?{}'.format(index, query_string)
            index += 1
            new_url = base_url + page
            scrape_macy(new_url)
            st.write(f"Scraping page in progress")
        except Exception as e:
            st.error(f"Error: {e}")
            break


    # Combine scraped data into a dataframe
    data = pd.DataFrame({
        'Product Brand': product_brands,
        'Product Name': product_names,
        'Current Price': current_prices,
        'Old Price': old_prices,
        'Rating': ratings,
        'Product URL': product_urls
    })
    data = data.drop_duplicates(subset=['Product URL'])
    data = data.reset_index(drop=True)

    

    # Display the result in a table
    st.write("Scraped Data Table:")
    st.dataframe(data)

    # Option to download the data
    st.download_button(
        label="Download Data as CSV",
        data=data.to_csv(index=False),
        file_name=f'{base_url.split('/')[-1]}.csv',
        mime="text/csv"
    )
