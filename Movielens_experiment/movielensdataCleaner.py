import numpy as np
import csv
import pyfpgrowth

userRatingsDict = {}
MovieIdMap = {}
num_users = 0
num_movie = 0

fileRead = open('/home/pooja/GITHUB/Improving-Diversity-Performance-of-Association-Rule-Based-Recommender-Systems/ml-100k/u.data', 'r')
if fileRead.mode == 'r':
    contents = fileRead.read()
    contents = contents.split('\n')

for frow in contents:
    row = frow.split()
    if row[0] not in userRatingsDict:
        userRatingsDict[row[0]] = []

    if int(row[2]) > 2:
        userRatingsDict[row[0]].append(row[1])

    if int(row[0]) > num_users:
        num_users = int(row[0])

fileRead.close()
#print(userRatingsDict)

#  fileRead = open('C:\\Users\\Navneet\\Desktop\\ml-100k\\u.item', 'r', encoding='utf-8')
#  file = csv.reader(fileRead)

# for row in file:
#      try:
#  #print(row[0], row[1])

#          MovieIdMap[row[0]] = row[1]
#          if int(row[0]) > num_movie:
#             num_movie = int(row[0])
#      except:
#          pass

# #print(MovieIdMap)

# rating_matrix = np.matrix(np.zeros((num_users+1, num_movie+1)), dtype=np.float)
# rating2Dlist = []
# for userId in userRatingsDict.keys():
#     rating2Dlist.append(userRatingsDict[userId])
#     for movies in userRatingsDict[userId]:
#         rating_matrix[int(userId), int(movies)] = 1.0

# converting userRatingDict to 2d list for input to pyfpgrowth.
transactional_data = []
for key in userRatingsDict:
    transactional_data.append(userRatingsDict[key])

# for j in transactional_data:
#     print("\n")
#     print(j)

# print (len(transactional_data))

# # print(rating_matrix)
# # ##print (rating2Dlist)
patterns = pyfpgrowth.find_frequent_patterns(transactional_data, 100)
# #print (patterns)
# # printing patterns in reverse order of support count
# #for key, value in sorted(patterns.items(), key=lambda kv: kv[1], reverse=True):
#    # print(key, ' ', value)
# # #print (patterns)
rules = pyfpgrowth.generate_association_rules(patterns, 0.4)
# #print (rules)
frules = open('rules.txt', 'w')
for key, value in sorted(rules.items(), key=lambda kv: kv[1][1], reverse=True):
    print (' '.join(key) + ' ' + ' '.join(value[0]) + '|' + str(value[1]))
    frules.write(' '.join(key) + ' * ' + ' '.join(value[0]) + '|' + str(value[1]) + '\n')

frules.close()