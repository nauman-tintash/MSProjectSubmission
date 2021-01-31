import trimesh
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
import glob
import os
import argparse

def create_voxel_off(path):

    pc_path = path + 'pointcloud.npz'   
    off_path = path + 'exported_mesh.off' 

    pc = np.load(pc_path)

    points = pc['points']
    normals = pc['normals']

    trimesh.Trimesh(vertices = points, vertex_normals = normals , faces = []).export(off_path)
    print('Finished: {}'.format(path))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create off visualization from point cloud.'
    )

    parser.add_argument('-res', type=int)
    parser.add_argument('-num_points', type=int)

    args = parser.parse_args()

    ROOT = '/mnt/DeepLearningResearch/occupancy_networks/data/ShapeNet/03001627'

    p = Pool(mp.cpu_count())
    p.map(create_voxel_off, glob.glob(ROOT + '/*/'))
