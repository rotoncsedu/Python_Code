def display_message():
    print("We learn Function of Python in this chapter")
display_message()

def favourite_book(book_name):
    print(f"One of your favourite book is {book_name}")
favourite_book('A Golden Age')


def make_shirt(size,print_msg):
    print(f"Your ordered shirt size is : {size}")
    print(f"\'{print_msg}\' will printed on your shirt")

make_shirt(42,'Hello Everyone')
make_shirt(print_msg='My life my rules',size=38)

def make_shirt(size,print_msg = 'I love Python'):
    print(f"Your ordered shirt size is : {size}")
    print(f"\'{print_msg}\' will printed on your shirt")
make_shirt(42)
make_shirt(print_msg='My life my rules',size=38)

def describe_city(city_name,country_name = 'USA'):
    print(f"{city_name.title()} is in {country_name.upper()}")
describe_city('New York')
describe_city('washington','USA')
describe_city(country_name='Bangladesh', city_name= 'Dhaka')


def city_country(city_name,country_name):
    format_name = f"\"{city_name.title()}, {country_name.title()}\""
    return format_name
output = city_country('santiago','chile')
print(output)
output = city_country('delhi','india')
print(output)
output = city_country('islamabad','pakistan')
print(output)

def make_album(artist_name,album_title,number_of_songs = 'None'):
    album_dictionary = {'artist_name':artist_name.capitalize(),'number_of_songs':number_of_songs,'album_title':album_title.title()}
    return album_dictionary
album_details = make_album('james','Sunnota')
print(album_details)
album_details = make_album('Hasan','Lal Konna',12)
print(album_details)
album_details = make_album(number_of_songs=10,album_title='Oo Priya Tomi kothai',artist_name='asif')
print(album_details)

