import numpy as np

camera_matrix = np.array( [[392.18866393 ,  0.      ,   336.96515295],
 [  0.      ,   393.34217754, 224.67147043],
 [  0.      ,     0.        ,   1.        ]])

distortion_coeff = np.array( [[-0.1552758 ,  0.69717213, -0.00807311 ,-0.01116689 ,-0.73045846]])

np.save('camera_matrix2.npy',camera_matrix)
np.save('distortion_coef2.npy',distortion_coeff)