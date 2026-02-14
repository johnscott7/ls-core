# Sort the following list of dictionaries based on the yera of publication of each book
# from earliest to most recent

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def published_year(book_dict):
    return int(book_dict['published'])

books.sort(key = published_year)
print(books)