page = '<html><body><a href="https://www.example.com">Click here</a><a href="https://www.google.com">Google</a><a href="https://www.github.com">GitHub</a><a href="https://www.python.org">Python</a><a href="https://www.stackoverflow.com">Stack Overflow</a></body></html>'

start_link = page.find('<a href=')
start_quote = page.find('"' , start_link)
end_quote = page.find('">' , start_link) + 1
url = page[start_quote : end_quote]
print(url)

def get_next_target (S):
    start_link = S.find('<a href=')
    start_quote = S.find('"' , start_link)
    end_quote = S.find('">' , start_link) + 1
    url = S[start_quote : end_quote]
    return url , end_quote

print(get_next_target(page))