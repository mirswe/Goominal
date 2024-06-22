import webbrowser
import sys

my_webs = {
    "reddit.com",
    "stackoverflow",
}


url = "https://www.google.com/search?q="

#chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'

#webbrowser.get(chrome_path).open(url)

def create_query():
    query = sys.argv[1:]
    return ' '.join(query)

def create_filter():
    filter = '()'
    for index, website in enumerate(my_webs):
        filter += 'site: ' + website
        if index == len(my_webs) -1:
            filter += ')'
        else:
            filter += ' OR '
    return filter

def create_url():
    if len(sys.argv[1:]) ==0:
        print("Error please enter a valid search")
    else:
        final_url = url + create_query() + create_filter()
        webbrowser.open(final_url)


if __name__ == "__main__":
    create_url()
create_filter()
create_query()