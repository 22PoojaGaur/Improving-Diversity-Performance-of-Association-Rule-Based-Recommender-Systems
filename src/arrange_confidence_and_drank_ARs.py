# frequent patterns have been found before this file
# association rules have been found before this file
# dranks for association rules have been found before running this file.

# This module takes two files as input one with ARs sorted by confidence
# other one ARs with drank and same order as the first file
# Note that the ARs sorted by confidence has a '*' between X and Y


if __name__ == '__main__':
    arcf = input('Enter file with Ass Rules sorted by confidence -> ')
    ardf = input('Enter file with Ass Rules with dranks -> ')

    rules_with_confidence = open(arcf, 'r').read().split('\n')
    rules_with_drank = open(ardf, 'r').read().split('\n')

    rules_confidences_dict = {}
    rules_dranks_dict = {}
    rules_X = []
    rules_Y = []

    for i in range(0, len(rules_with_confidence)):
        confidence = rules_with_confidence[i].split('|')[1].strip()
        drank = rules_with_drank[i].split('|')[1].strip()
        X = rules_with_confidence[i].split('|')[0].split('*')[0].strip()
        Y = rules_with_confidence[i].split('|')[0].split('*')[1].strip()

        rules_confidences_dict[X + '=>' + Y] = float(confidence)
        rules_dranks_dict[X + '=>' + Y] = float(drank)

    f_conf_out = open('AR_sorted_by_confidence.txt', 'w')
    f_drank_out = open('AR_sorted_by_drank.txt', 'w')

    for key, value in sorted(
            rules_confidences_dict.items(), key=lambda kv: kv[1], reverse=True):
        f_conf_out.write(str(key) + ' | ' + str(value) + '\n')

    for key, value in sorted(
            rules_dranks_dict.items(), key=lambda kv: kv[1], reverse=True):
        f_drank_out.write(str(key) + ' | ' + str(value) + '\n')
