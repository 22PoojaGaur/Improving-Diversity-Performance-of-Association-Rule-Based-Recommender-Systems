# precision = hit set/test set
# recall = hit set/ number of recommandations
# f1 measures = weighted avg of precision and recall, 2*[(precision*recall)/(precision+recall)]

import matplotlib.pyplot as plt

# recall values
#plt.plot([3/10, 6/20, 9/30, 12/40, 15/50, 17/60, 19/70]) # HC-HD
#plt.plot([5/10, 10/20, 13/30, 19/40, 23/50, 26/60, 27/70], 'r') # HC

# precision values
# plt.plot([3/89, 6/89, 9/89, 12/89, 15/89, 17/89, 19/89])
# plt.plot([5/89, 10/89, 13/89, 19/89, 23/89, 26/89, 27/89])
# plt.xlabel('num_recommendation vs precision for artist dataset')
# plt.axis([0, 5, 0, 0.5])
# plt.show()

# diversity  values
plt.plot([1, -0.125, 0.125, 0.1249, 0.078, 0.087]) # HC-HD
plt.plot([1, -0.805, -0.513, -0.467, -0.511, -0.499]) # HC
plt.xlabel('num_recommendation vs diversity for artist dataset')
plt.axis([0, 5, -1, 1])
plt.show()