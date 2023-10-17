def find_last (search_string , target_string):
    firstSearch = search_string.find(target_string)
    result = search_string.find(target_string[-3] , firstSearch)
    return result + 2

print(find_last('This is reallly uncomfortable for me' , 'uncomfortable'))

#In the video-tutorial, I don't undertand the solution.##Don't understand-03