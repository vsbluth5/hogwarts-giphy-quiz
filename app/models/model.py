import requests
import random

def shout(word):
    return word.upper() + "!!"
    


def getURL(choice1, choice2, choice3, key):
    reqURL = 'https://api.giphy.com/v1/gifs/search?api_key='
    reqURL += key
    photoList = []
    words = choice1+'+'+choice2+'+'+choice3
    reqURL += '&q='+words +'&limit=25&offset=0&rating=G&lang=en'
    print(reqURL)
    response = requests.get(reqURL).json()
    #response = requests.get('https://api.giphy.com/v1/gifs/search?api_key=GpJ1t8MrfqMR5DRO29FQQ9EKKPJ9qajd&q=Ryan+Gosling&limit=25&offset=0&rating=G&lang=en').json()
    #print (resrand = random.randint(1,25)ponse.data[0].images.original.url) from javascript
    for r in range(3):
        rand = random.randint(1,25)
        theData = response['data']
        theData = theData[rand]
        theData = theData['images']
        theData = theData['original']
        theData = theData['url']
        photoList.append(theData)
    return (photoList)
    
    #return "static/micropig.jpg"