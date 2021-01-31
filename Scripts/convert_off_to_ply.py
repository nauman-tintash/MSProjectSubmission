import os
import glob
import multiprocessing as mp
from multiprocessing import Pool
import trimesh

#INPUT_PATH = '/mnt/DeepLearningResearch/ldif/data/ShapeNet/*/04256520/'
INPUT_PATH = '/mnt/DeepLearningResearch/occupancy_networks/data/ShapeNet.build/*/4_watertight_scaled/'
def to_ply(path):

    input_file  = path
    filepath = os.path.splitext(path)[0]
    output_file = filepath + '.ply'

    if os.path.exists(output_file):
        return

    # cmd = 'meshlabserver -i {} -o {}'.format(input_file,output_file)
    # if you run this script on a server: comment out above line and uncomment the next line
    cmd = 'xvfb-run -a -s "-screen 0 800x600x24" meshlabserver -i {} -o {}'.format(input_file,output_file)
    os.system(cmd)

def delete_file(path):
    os.remove(path)

p = Pool(mp.cpu_count())
p.map(to_ply, glob.glob( INPUT_PATH + '*.off'))
#p.map(delete_file, glob.glob( INPUT_PATH + '*.off'))
