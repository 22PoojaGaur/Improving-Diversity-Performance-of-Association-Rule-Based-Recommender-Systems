# the association rule sorted by confidence is created before this file.
# the association rule sorted by drank is created before this file.

# It takes a file containing input pattern and suggests recommendations
# based on that.


def get_recommendation(X, rule_inter):
    result = []
    for i in rule_inter:
        if set(i.split('=>')[0].strip().split(' ')).issubset(set(X)):
            result.append(i)

    recs = set()
    for i in result:
        if len(i.split('=>')[1].strip().split(' ')) == 1:
            # print(i.split('=>')[1].strip())
            recs.add(i.split('=>')[1].strip())
    return (result, list(recs))


if __name__ == '__main__':
    inp = input('enter input file for recommendations -> ')

    Xs = open(inp, 'r').read().split('\n')
    ass_c = open('AR_sorted_by_confidence.txt', 'r').read().split('\n')
    ass_d = open('AR_sorted_by_drank.txt', 'r').read().split('\n')

    # store the intersection of rules of both sorted list
    rule_inter = []

    rule_conf_dict = {}
    rule_drank_dict = {}

    fin_dict = {}
    for i in ass_c:
        rule_conf_dict[i.split('|')[0].strip()] = i.split('|')[1].strip()
    for i in ass_d:
        rule_drank_dict[i.split('|')[0].strip()] = i.split('|')[1].strip()

    sorted_conf_rules = []
    for rule, conf in sorted(rule_conf_dict.items(), key=lambda x: x[1], reverse=True):
        sorted_conf_rules.append(rule)

    sorted_drank_rules = []
    for rule, drank in sorted(rule_drank_dict.items(), key=lambda x: x[1], reverse=True):
        # put threshold for drank here
        thresh= 0.05
        assert thresh != None
        if float(drank) >= thresh:
            sorted_drank_rules.append(rule)

    rule_inter = list(set(sorted_conf_rules) & set(sorted_drank_rules))
    # for rule, conf in rule_conf_dict.items():
    #     fin_dict[rule] = (conf, rule_drank_dict[rule])

    # for key, value in sorted(fin_dict.items(), key=lambda x: x[1], reverse=True):
    #     rule_inter.append(key)
    #print(rule_inter)
    # rule_inter = list(set(rule_conf) & set(rule_drank))

    for x in Xs:
        if x == '':
            continue
        # print(x)
        (rules, recs) = get_recommendation(x.strip().split(' '), rule_inter)
        # print('rules for ' + x + ' -> ' + '\n'.join(rules))
        print('recommendations for HC-HD ' + x + ' -> ' + ' '.join(recs))
        print('\n')

        (rules, recs) = get_recommendation(x.strip().split(' '), rule_conf_dict.keys())
        print('recommendations for HC ' + x + ' -> ' + ' '.join(recs))
        print('\n')

