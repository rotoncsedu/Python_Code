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

def greet_users(usernames):
    for username in usernames:
        print(f"Hello {username.title()}! Welcome to the Python world")
usernames = ['samiul','sabbir','sadiq']
greet_users(usernames)
'''

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}.")
        completed_models.append(current_design)
def show_all_models(uprinted_designs,completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    print("\nThe following models are in Unprinted Designs:")
    for unprinted_design in unprinted_designs:
        print(unprinted_design)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_all_models(unprinted_designs,completed_models)
'''    
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}.")
        completed_models.append(current_design)
def show_all_models(uprinted_designs,completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    print("\nThe following models are in Unprinted Designs:")
    for unprinted_design in unprinted_designs:
        print(unprinted_design)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_all_models(unprinted_designs,completed_models)

#8-9.
def show_message(message):
    print("\nThe following messages are printed:")
    for msg in message:
        print(msg)
messages = ['Hello Everyone','Welcome','Thank you']
show_message(messages)
#8-10.
def send_message(msg_request,sent_msg):
    loc = 0
    while msg_request:
        current_msg = msg_request.pop(loc)
        print(f"Sending message: {current_msg}")
        sent_msg.append(current_msg)
        loc
def show_sent_messages(sent_msg, msg_request = 'Null'):
    print("\nThe following message are sent: ")
    for msg_sent in sent_msg:
        print(msg_sent)
    if msg_request != 'Null':
        print("\nThe following messages are in sent Archive: ")
        for msg_request in msg_request:
            print(msg_request)
    else:
        print("\nNo message in request")
msg_request = ['Hello Everyone','Welcome','Thank you']
sent_msg = []  
send_message(msg_request[:],sent_msg)
show_sent_messages(sent_msg,msg_request)