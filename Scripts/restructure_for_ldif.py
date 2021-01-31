import pickle
import os
import glob
import multiprocessing as mp
from multiprocessing import Pool
import trimesh
from functools import partial

#source dataset_shapenet/config.sh

#INPUT_PATH = '/mnt/DeepLearningResearch/occupancy_networks/data/ShapeNet.build/04256520/4_watertight_scaled/'
OUTPUT_PATH = '/mnt/DeepLearningResearch/ldif/data/ShapeNet/'

INPUT_PATH = '/mnt/DeepLearningResearch/occupancy_networks/data/ShapeNet.build/'

def copy_to_ldif(input_path, output_path, filename):
    input_file  = input_path + filename
    output_file = output_path + filename

    # cmd = 'meshlabserver -i {} -o {}'.format(input_file,output_file)
    # if you run this script on a server: comment out above line and uncomment the next line
    cmd = 'cp -u {} {}'.format(input_file,output_file)
    os.system(cmd)

#p = Pool(mp.cpu_count())


#f = pickle.load(INPUT_PATH + "test.lst")
#f = open(INPUT_PATH + "train.lst", "r")

#lines = f.read().splitlines()

#print(lines)

#p.map(copy_to_ldif, lines)

splits = ['train', 'test', 'val']
classes = ['03001627','02958343', '04256520','02691156','03636649','04401088','04530566','03691459','02933112','04379243','03211117','02828884','04090263']
for split in splits:
    os.mkdir(OUTPUT_PATH + split)
    print("COPYING " + split)
    for c in classes:
        print("COPYING " + c)

        INPUT_PATH_C=INPUT_PATH + c
        FILE_LIST_PATH=INPUT_PATH_C + '/' + split + '.lst' 
        OUTPUT_PATH_C = OUTPUT_PATH + split + "/" + c

        os.mkdir(OUTPUT_PATH_C)
        
        p = Pool(mp.cpu_count())
        f = open(FILE_LIST_PATH, "r")

        lines = f.read().splitlines()
        p.map(partial(copy_to_ldif, INPUT_PATH_C + "/4_watertight_scaled/",OUTPUT_PATH_C + "/"), lines)
