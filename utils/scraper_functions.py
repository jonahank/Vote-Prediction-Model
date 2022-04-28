import requests
from bs4 import BeautifulSoup
import re


def get_vote_links(current_page):
    """Finds the vote page links on the main folktingspage.

    Args:
        main_page_soup (_type_): Takes in the main page with all the vote subpages as a soap object

    Returns:
        _type_: Returns a list of soap Objects with the links to the respective subpages
    """
    prefix = 'https://www.ft.dk/'
    a = current_page.find_all(attrs={'class':'column-documents__link'})
    
    a = [prefix+x['href'] for x in a]  
    return a


def get_soup_page(url_page):
    """Converts URL into a BeautifulSoup object.

    Args:
        url_page (_type_): takes a URL page as input parsed as a string.

    Returns:
        _type_: returns a BeautifulSoup object.
    """
    response = requests.get(url_page)
    page = BeautifulSoup(response.content, 'html.parser')
    return page


def get_votes_by_party(vote_page) -> dict: 
    """ Takes a BeautifulSoup object and retrieves the votes by party
        section, then strips it and modifies it so that it is returned in a fixed sized
        dictionary containing parties, For, Against, Neutral counts.

    Args:
        vote_page (_type_): URL for the folketings vote_page 
        (e.g., https://www.ft.dk/samling/20042/afstemning/64.htm)

    Returns:
        dict: fixed sized dictionary containing parties, For, Against, Neutral, absent counts for each party
    """
    
    table = vote_page.find("div", {"id":"tingdok_accordion_vote-2"})
    dict = {'parties': [], 'For': [], 'Against':[], 'Neutral':[], 'Absent':[]}
    regex_party = re.compile(r"\w* \(\w+\)")
    regex_vote_num = re.compile(r"\d+")

    for child in table.table.tbody.children:
        if re.search(regex_party, child.text.strip()):
            lst = child.text.strip().split("\r\n")
            votes = []
            for i in lst:
                i = i.strip()
                if re.search(regex_party,i): 
                    party = i 
                    dict['parties'].append(party)
                    
                elif re.search(regex_vote_num, i):
                    votes.append(i)
                    
                    
            dict['For'].append(votes[0])
            dict['Against'].append(votes[1])
            dict['Neutral'].append(votes[2])
            dict['Absent'].append(votes[3])
            
    return dict

def get_votes(vote_page):

    vote_section = vote_page.find("div", {"id": "tingdok_accordion_vote-3"})

    votes = {
        'politician': [],
        'party': [],
        'vote': []
    }

    for child in vote_section.tbody.children:
        lst = child.text.strip().split("\n\r")
        if len(lst) == 3:
            person, party, vote = [x.strip() for x in lst]
            votes['politician'].append(person)
            votes['party'].append(party)
            votes['vote'].append(vote)
    
    return votes


def get_description_page(vote_page):
    description_link = vote_page.find("a", {"class":"tingdok-backarrow"})
    prefix = 'https://www.ft.dk/'
    response = requests.get(prefix + description_link['href'])    
    description_page = BeautifulSoup(response.content, 'html.parser')
    
    return description_page


def get_vote_info(description_page):
    description_texts = description_page.find('div', {"class":"tingdok__caseinfospot-a__container"}).text.strip().splitlines()
    info = []
    for line in description_texts:
        if line.strip() != "":
            info.append(line.strip())
    return info
    

def get_vote_id(vote_page):
    return vote_page.h2.text


def get_title(description_page):
    top_header = description_page.find("div", {"class":"tingdok__caseinfotopspot-a__container"})
    return top_header.h1.text.strip()


def get_vote_caller(description_page):
    top_header = description_page.find("div", {"class":"tingdok__caseinfotopspot-a__container"})
    hosts_section = top_header.find("div", {"class":"tingdok-normal"})
    
    meeting_hosts = []
    
    for line in hosts_section:
        clean_line = line.text.strip()
        if len(clean_line)>5:
            meeting_hosts.append(clean_line)
            
    return meeting_hosts

def get_next_page(current_page):
    next_page_url = current_page.find("a", {"title":"Næste"})['href']
    prefix = "https://www.ft.dk/dokumenter/dokumentlister/afstemninger"
    np_response = requests.get(prefix + next_page_url)
    return BeautifulSoup(np_response.content, 'html.parser')

def exists_next_page(current_page):
    if current_page.find("a", {"title":"Næste"})['href'] != None:
            return True
    else:
        False
