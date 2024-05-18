def reverseSortedUserViews(user_views)
    reversedDict = {}
    for key in sorted_user_views:
    	val = sorted_user_views[key]
    	reversedDict[val] = key
    return reversedDict

n = int(input())
empty_dict = {}
for i in range(n):
	user, views = input().split()
	views = int(views)
	if user not in empty_dict:
		empty_dict[user] = views
	else:
	    empty_dict[user] += views
sorted_user_views = dict(sorted(empty_dict.items(), key=lambda x: x[1]))

reversedDict = reverseSortedUserViews(sorted_user_views)
max_key = max(reversedDict)
print(reversedDict[max_key])
