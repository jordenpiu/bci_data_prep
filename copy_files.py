import os 
import shutil
drive = "/media/pankhi/Seagate Backup Plus Drive/Poulami/Compressed/EEG_ConvertedData/EEG_ConvertedData"
files = os.listdir(drive)
dst = "/media/pankhi/57A77BEF00BB01D2/DATA/BCI/multigrasp_realMove"
i=0

for file in files:
    if "multigrasp_realMove" in file:
        
        shutil.copy(os.path.join(drive,file),dst)
        print(i)
        i=i+1