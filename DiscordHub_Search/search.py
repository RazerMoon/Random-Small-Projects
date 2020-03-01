from requests_html import HTMLSession
import sys

class hubSearch():
    def getUsers(self, query, page):
        r = session.get(f'https://discordhub.com/user/search?user_search_bar={query}&page={page}')
        
        about = r.html.find('a', containing='#')
        
        for element in about:
            print(element.text)
    
    def __init__(self, query, maxpage):
        for page in range(1,maxpage+1):
            self.getUsers(query, page)

if __name__ == "__main__":
    session = HTMLSession()

    if len(sys.argv) - 1 == 2:
        hubSearch(sys.argv[1], int(sys.argv[2]))
    elif len(sys.argv) - 1 == 1 and sys.argv[1] == "--help":
        print("""Please pass in your query and the last page you want to check.

        For example: "python search.py test 1"
        will return the first page of results for the name "test"
        """)
    else:
        print('Wrong number of arguments! Check "--help" for usage')
