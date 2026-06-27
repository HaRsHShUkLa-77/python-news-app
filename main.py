

import requests

api_key = input('enter your API key From NEWS API: ')

def general(category=None):

    params = {
    "category": category
    }

    url = (f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}')

    try:
        if category is None:
            response = requests.get(url)
        else:
            response = requests.get(url, params= params)
    
        response.raise_for_status()

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
        return
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return 

    data = response.json()
    
    
    for index, i in enumerate(data['articles'][0:10], start=1):
        print(f'News No. : {index}' )
              
        print(f'Title: {i['title']}')
        
        print(f'Author : {i['author']}')
        
        print(f'Published on : {i['publishedAt']}')
        
        print(f'Source : {i['source']['name']}')
        
        print('Description : ', i['description'])
        
        print('---------------')
        
        print()


while True:

    print('---------- NEWS APP ----------')
    print('Enter 1 for General News ')
    print('Enter 2 for Sports News ')
    print('Enter 3 for Technology News ')
    print('Enter 4 for Business News ')
    print('Enter 5 for Entertainment News ')
    print('Enter 6 to Exit the App ')
    

    try:
        choice = int(input('Enter Your Number: '))
    except ValueError:
        print('enter a number please')
        continue

    if choice == 1:
        general()
        
    elif choice == 2:
        general('sports')

    elif choice == 3:
        general('technology')

    elif choice == 4:
        general('business')

    elif choice == 5:
        general('entertainment')

    elif choice == 6:
        print('thankyou visit again!')
        break
    
    else:
        print('enter a valid choice from the menu')

















        



