page = '''<html><body><a href="https://www.google.com">Google</a><a href="https://www.youtube.com">YouTube</a><a href="https://www.github.com">GitHub</a><a href="https://www.stackoverflow.com">Stack Overflow</a><a href="https://www.amazon.com">Amazon</a></body></html>'''


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == - 1:
        return None , 0
#        url = None
#        end_quote = 0
    else:
        start_quote = page.find('"' , start_link)
        end_quote = page.find('"' , start_quote + 1)
        url = page[start_quote : end_quote +1]
    return url , end_quote
#The part that it was updated:
'''
def print_all_links(page):
    while True:
        url , endpost = get_next_tarjet(page)
        if url:
            print(url)
            page = page[endpost]
        else:
            break'''


#changes Quiz:
def print_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos : ]
        else:
            break
    return links
print(print_all_links(page))
