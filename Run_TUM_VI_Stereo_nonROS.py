# This script is to run all the experiments in one program

import os
import subprocess
import time
import signal


# SeqNameList = ['room1_512_16', 'not_exist'];
SeqNameList = ['room1_512_16', 'room2_512_16', 'room3_512_16', 'room4_512_16', 'room5_512_16', 'room6_512_16', 'not_exist'];

Result_root = '/mnt/DATA/tmp/TUM_VI/OKVIS_Stereo_Baseline_redo/'

Number_GF_List = [400];
Num_Repeating = 10 # 1 # 
# SleepTime = 2 # 10 # 25

#----------------------------------------------------------------------------------------------------------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ALERT = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for ri, num_gf in enumerate(Number_GF_List):
    
    Experiment_prefix = 'ObsNumber_' + str(int(num_gf))

    for iteration in range(0, Num_Repeating):

        Experiment_dir = Result_root + Experiment_prefix + '_Round' + str(iteration + 1)
        cmd_mkdir = 'mkdir ' + Experiment_dir
        subprocess.call(cmd_mkdir, shell=True)

        for sn, sname in enumerate(SeqNameList):
            
            print bcolors.ALERT + "====================================================================" + bcolors.ENDC

            SeqName = SeqNameList[sn]
            print bcolors.ALERT + "Round: " + str(iteration + 1) + "; Seq: " + SeqName

            File_Setting = '../config/config_okvis_50_20.yaml'
            # File_Setting = '../config/config_fpga_p2_tumvi.yaml'
            Path_Image   = '/mnt/DATA/Datasets/TUM_VI/dataset-' + SeqName + '/mav0/'
            File_traj = Experiment_dir + '/' + SeqName

            cmd_slam   = str('./okvis_app_synchronous ' + File_Setting + ' ' + Path_Image + ' ' + File_traj)
            
            print bcolors.WARNING + "cmd_slam: \n"   + cmd_slam   + bcolors.ENDC

            print bcolors.OKGREEN + "Launching SLAM" + bcolors.ENDC
            # proc_slam = subprocess.Popen(cmd_slam, shell=True)
            proc_slam = subprocess.call(cmd_slam, shell=True)
