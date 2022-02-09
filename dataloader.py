import numpy as np
from scipy.spatial import cKDTree

# load a scan
data = np.load("scan.npz")
points = data["points"]
sensors = data["sensor_position"]
assert(points.shape==sensors.shape)

# compute the mean neighborhood distance of the point cloud
tree = cKDTree(points)
d = tree.query(points, k=2)[0][:, 1].mean()

# compute the unit vectors from points to sensors
sensor_vectors = points - sensors
sensor_vectors = sensor_vectors / np.linalg.norm(sensor_vectors, axis=1)[:, np.newaxis]

# compute the auxiliary points and append them to the input point cloud
p_before = points + d * sensor_vectors
p_after = points - d * sensor_vectors
points = np.vstack((points, p_before, p_after))

# make the point type identifiers
points_ident = np.zeros(shape=(sensors.shape[0], 2))
p_before_ident = points_ident + [1, 0]
p_after_ident = points_ident + [0, 1]
ident = np.vstack((points_ident, p_before_ident, p_after_ident))

# assemble the visibility augmented point cloud with auxiliary points and sensor vectors
visibility_augmented_pointcloud = np.hstack((points, ident, np.tile(sensor_vectors, (3,1))))