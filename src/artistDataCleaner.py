import pyfpgrowth


if __name__ == '__main__':
    
    file = open('../Artist_experiment/Datasets/user_artists.dat', 'r')
    userData = (file.read()).split('\n')[1:]
    userData = [i.split() for i in userData]
    outputFile = open('../Artist_experiment/Datasets/userTransaction.txt', 'w')
    # Frequent_patterns = open('../Artist_experiment/Datasets/Frequent_patterns.txt', 'w')

    UserDic = {}
    wtThreshold = 333
    for j in userData:
        if len(j) == 0:
            continue
        if j[0] in UserDic:
            if int(j[2]) > wtThreshold:
                UserDic[j[0]].append(j[1])
        else:
            UserDic[j[0]]= []


    transactional_data = []
    for k in UserDic:
        outputFile.write(' '.join(UserDic[k]))
        outputFile.write('\n')
        transactional_data.append(UserDic[k])

    file.close()
    outputFile.close()

    # rest left for testing

    freq_artists = open('../Artist_experiment/Datasets/freq_artists.txt', 'w')
    f_artists = set()
    patterns = pyfpgrowth.find_frequent_patterns(transactional_data[0:-100], 50)
    pattern_keys = patterns.keys()


    # for printing all frequent patterns
    # for k in patterns:
    #     Frequent_patterns.write(' '.join(k)+'=')
    #     Frequent_patterns.write(str(patterns[k]))
    #     Frequent_patterns.write('\n')

    for p in patterns.keys():
        f_artists = f_artists | set([i for i in p])
        if len(f_artists) > 50:
            break
    freq_artists.write(' '.join(f_artists))



    rules = pyfpgrowth.generate_association_rules(patterns, 0.1)

    frules = open('rules.txt', 'w')
    for key, value in sorted(rules.items(), key=lambda kv: kv[1][1], reverse=True):
        #frules.write(' '.join(key) + ' ' + ' '.join(value[0]) + '|' + str(value[1]) + '\n')
        frules.write(' '.join(key) + ' * ' + ' '.join(value[0]) + '|' + str(value[1]) + '\n')

    frules.close()