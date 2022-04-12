import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.load_dataset()
data=np.random.rand(100,5)
plt.boxplot(data)
plt.show()