# precision = hit set/test set
# recall = hit set/ number of recommandations
# f1 measures = weighted avg of precision and recall, 2*[(precision*recall)/(precision+recall)]

import matplotlib.pyplot as plt

plt.plot([6/7, 11/14, 16/21, 22/28, 27/35])

plt.xlabel('num_recommendation vs recall')
plt.axis([0, 5, 0, 1])
plt.show()