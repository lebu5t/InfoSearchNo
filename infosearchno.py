"""This is a script that will search for info in various norwegian sites and open the website with the results.
It makes searching for a  person a bit easier and you don't have to remember all the sites.
To start a search, just run infosearchno.py"""

import webbrowser
from art import *

name = ''
search = 0
search_ok = False
phone_sites = []
prof_sites = []

type_of_search = ['Phone number - Searching for phone numbers and addresses',
                  'Professional - Searching for companies or if a person has connections to companies',
                  'All - Search for all',
                  ]


def welcome():
    global name, type_of_search, search, search_ok, phone_sites, prof_sites
    welcome_message()
    for x in range(len(type_of_search)):
        print(x, '. ', type_of_search[x])
    print('\n')
    print('Please select the type of search you want to execute (0 - ',len(type_of_search) - 1,')')
    while not search_ok:
        search = int(input())
        if search < len(type_of_search) and search >= 0:
            search_ok =True
            break
        else:
            print('Not a valid choice')
            print('Please try again: ')
    name = input('Enter the name you want to search for with "-" replacing spaces: ')
    print('Searching for ', name, ' in various places...')
    print('Opening new tabs...')

    phone_sites = ['https://www.180.no/search/all?w=' + name,
                    'https://www.1881.no/?query=' + name,
                    'https://www.gulesider.no/' + name + '/personer',
                    'https://1890.no/?query=' + name,
                    ]

    prof_sites = ['https://www.proff.no/rolles%C3%B8k?q=' + name,
                  'https://w2.brreg.no/enhet/sok/treffliste.jsp?navn=' + name + '&orgform=0&fylke=0&kommune=0',
                  'http://www.nettkatalogen.no/bransjelist/' + name,
              ]




def phone_number(name):
    global phone_sites
    for site in phone_sites:
        webbrowser.open_new_tab(site)

def prof_search(name):
    global prof_sites
    for site in prof_sites:
        webbrowser.open_new_tab(site)

def begin_search(search,name):
    if search == 0:
        phone_number(name)
    elif search == 1:
        prof_search(name)
    elif search == 2:
        phone_number(name)
        prof_search(name)
    else:
        print("Sorry, cannot find the requested search")

def welcome_message():

    tprint('InfoSearchNO\n')


welcome()
begin_search(search,name)


