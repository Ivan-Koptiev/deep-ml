import numpy as np

def euclidean_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.sqrt(np.sum((point1 - point2)**2))

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = list(initial_centroids)

    for i in range(max_iterations):

        clusters = {str(j): [] for j in range(k)}

        for pt_index in range(len(points)):
            current_dist = float('inf')
            closest_cluster_index = 0
            for j in range(len(centroids)):
                dist = euclidean_distance(points[pt_index], centroids[j])
                if dist < current_dist:
                    current_dist = dist
                    closest_cluster_index = j

            clusters[str(closest_cluster_index)].append(points[pt_index])

        new_centroids = []
        for cluster_points in clusters.values():
            if cluster_poi