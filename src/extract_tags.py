def sanitize(tag_name):
    return tag_name.replace('\'', '_').replace(' ', '-')

if __name__ == '__main__':


    file = open('../Artist_experiment/Datasets/user_taggedartists.dat', 'r')
    userData = (file.read()).split('\n')[1:]
    userData = [i.split() for i in userData]

    tagFile = open('../Artist_experiment/Datasets/tags.dat', 'r', encoding='latin-1')
    tagData = (tagFile.read()).split('\n')[1:]
    tagData = [i.split('\t') for i in tagData]

    print(tagData)
    tagDic = {}
    for i in tagData:
        if len(i) != 2:
            continue
        tagDic[i[0]] = sanitize(i[1])
    print(tagDic)


    artist_info_file = open('../Artist_experiment/artist_tag_info.txt', 'w')
    artistTagDic = {}
    for j in userData:
        if len(j) == 0:
            continue
        if j[1] not in artistTagDic:
            artistTagDic[j[1]] = {}
        if j[2] not in artistTagDic[j[1]]:
            artistTagDic[j[1]][j[2]] = 0

        artistTagDic[j[1]][j[2]] = artistTagDic[j[1]][j[2]] + 1
    
    for (ar_id, ar_info) in artistTagDic.items():
        artist_info_file.write(ar_id + ' : ')
        tag_cnt = 0
        for tag_id, count in sorted(ar_info.items(), key=lambda kv: kv[1], reverse=True):
            tag_cnt += 1
            if tag_cnt > 3:
                break
            artist_info_file.write(tagDic[tag_id] + ' (' + tag_id + ') ')
        artist_info_file.write('\n')

    artist_info_file.close()










