# HMoTP
High-speed milling of thin-walled parts (HMoTP) dataset 2024 released by Prof. Qinghua Song's Lab from Shandong University.
This is a dataset for high-performance machining of titanium alloy thin-walled parts containing milling force, milling bending moment, workpiece vibration, and tool wear data that can be used for tool wear monitoring and chatter detection researches.
## Paper
This is a dataset for our accepted paper 'R. Wang, Q. Song, Y. Peng, et al. Toward digital twins for high-performance manufacturing: Tool wear monitoring in high-speed milling of thin-walled parts using domain knowledge, Robot Comput-Integr Manuf 2024;88:102723 https://doi.org/10.1016/j.rcim.2024.102723'.
If this dataset is useful for your research, please cite our paper:
## Dataset structure
Data of Each cutting in the dataset is stored as an independent CSV file. 
The cutting data of the three tools are stored in folders named CuttingsignalsT01/CuttingsignalsT02/CuttingsignalsT03 respectively. 
Each cutting tool has 100 sets of cutting data. Taking the T1 tool as an example, its cutting data is saved in 100 CSV files named T01_001.CSV to T01_100.CSV.
Each CSV file of cutting data contains data for 7 channels: Fx, Fy, Fz, Mz, Ax, Ay, and Az.
Each cutting data corresponds to a tool wear value, and the wear values of all tools are saved in files named ToolWeaT01.csv/ToolWeaT02.csv/ToolWeaT03.csv.
# Download
All the data can be downloaded from one of the following links 
1. Baidu Netdisk: https://pan.baidu.com/s/1PFtNowJL_QUmHMtoHvRHJA Extraction code: sdum
2. Google Drive: https://drive.google.com/drive/folders/1eBhTSXMd8jVITfQoJifC50fE_NIFqb89?usp=sharing
# Contact infor
Please contact Runqiong Wang (wangrunqiong@163.com), the first author of the paper, if you encounter any problems in using it.
