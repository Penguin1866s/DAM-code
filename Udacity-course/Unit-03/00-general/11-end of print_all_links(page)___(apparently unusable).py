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

def union(list1 , list2):
    for i in list2:
        if list2.index(i) != 0:
            list1.append(i)
        else:
            continue
    return list1 , list2

#New function01:
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl , print_all_links(get_next_target(page)))
            crawled.append(page)
    return crawled
print(crawl_web(page))
#end new function01
