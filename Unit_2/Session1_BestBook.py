'''
Problem 7: Best Book
Imagine you are working on a book review software like Goodreads. Write a function named highest_rated() that returns the book with the highest rating.

The function should take in a list of dictionaries named books as a parameter. Each dictionary represents data associated with a book, including its title, author, and rating. The function should return the dictionary for the book with the highest rating.

def highest_rated(books):
    pass
Example Input:

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
Expected Output:

{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}
'''

def highest_rated(books):
    if not books: #Making sure there is at least one entry [EDGE CASE]
        return -1
    tempMaxVal, tempMaxName = None, None

    #The following is attempting to grab the values, not necessary but wanted to practice, 
    #if those values dont exist we return -1
    try:
        tempMaxVal = books[0]["rating"]
        tempMaxDict = books[0]
    except KeyError:
        return -1
    
    for book in books:
        #Could use another try catch block, but for times sake I decided not to
        if book["rating"] > tempMaxVal:
            tempMaxVal = book["rating"]
            tempMaxDict = book
    return tempMaxDict

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))