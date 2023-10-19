ddd_page ='''page = '<html><body><a href="https://www.google.com">Google</a><a href="https://www.youtube.com">YouTube</a><a href="https://www.github.com">GitHub</a><a href="https://www.stackoverflow.com">Stack Overflow</a><a href="https://www.amazon.com">Amazon</a></body></html>'''

def get_next_tarjet (page):
    start_link = page.find('<a href=')
    if start_link == - 1:
        return None , 0
#        url = None
#        end_quote = 0
    else:
        start_quote = page.find('"' , start_link)
        end_quote = page.find('">' , start_quote + 1)
        url = page[start_quote : end_quote + 1]
    return url , end_quote

#page = page[end_quote + 1 : ]
url , endpost = get_next_tarjet('yeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesssssssssss sssssssss s s  ssssss')
print(url)
print(endpost)

if url:#Verify if url has a value / that the value of url is not None.
    print("Here!")
else:
    print("Not here!")

print('\n')

url , endpost = get_next_tarjet('''page = '<html><body><a href="https://www.google.com">Google</a><a href="https://www.youtube.com">YouTube</a><a href="https://www.github.com">GitHub</a><a href="https://www.stackoverflow.com">Stack Overflow</a><a href="https://www.amazon.com">Amazon</a></body></html>''')
print(url)
print(endpost)

if url:#Verify if url has a value / that the value of url is not None.
    print("Here!")
else:
    print("Not here!")

print('\n\n\n\n\nQuiz print_all_links:')
page = '''<html><body><a href="https://www.google.com">Google</a><a href="https://www.youtube.com">YouTube</a><a href="https://www.github.com">GitHub</a><a href="https://www.stackoverflow.com">Stack Overflow</a><a href="https://www.amazon.com">Amazon</a></body></html>'''

def get_next_tarjet(page):
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

def print_all_links(page):
    while True:
        url , endpost = get_next_tarjet(page)
        if url:
            print(url)
            page = page[endpost]
        else:
            break
print(print_all_links(page))
