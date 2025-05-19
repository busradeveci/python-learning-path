from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Rastgele veri oluştur
np.random.seed(42)
X = np.random.rand(100, 2)

# K-Means kümeleme uygula
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Sonuçları görselleştir
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
plt.title("K-Means Kümeleme")
plt.show()