import mne 
from scipy.io import loadmat 
import os 
from utils import *
import numpy as np

def convert_to_fif(root, file_name):

    data=loadmat(os.path.join(root,file_name))
    sfreq=data['nfo']['fs'][0][0][0][0]
    eegdataa = data['ch1'].T
    nchannels,nsamples = eegdataa.shape
    channel_names = [s[0] for s in data['nfo']['clab'][0][0][0]]
    event_onsets = data['mrk'][0][0][0]
    event_codes = data['mrk'][0][0][1]
    labels = np.zeros((1, nsamples),int)
    labels[0, event_onsets] = event_codes

    cl_lab = [s[0] for s in data['nfo']['className'][0][0][0]]
    cl1 = cl_lab[0]
    cl2 = cl_lab[1]

    nclasses = len(cl_lab)
    nevents=len(event_onsets)

    info = mne.create_info(ch_names = channel_names, sfreq = sfreq, ch_types='eeg')

    raw_data = np.array([data["ch1"],data["ch2"],data["ch3"],data["ch4"],data["ch5"],data["ch6"],
                      data["ch7"],data["ch8"],data["ch9"],data["ch10"],data["ch11"],data["ch12"],
                      data["ch13"],data["ch14"],data["ch15"],data["ch16"],data["ch17"],data["ch18"],
                      data["ch19"],data["ch20"],data["ch21"],data["ch22"],data["ch23"],data["ch24"],
                      data["ch25"],data["ch26"],data["ch27"],data["ch28"],data["ch29"],data["ch30"],
                       data["ch31"],data["ch32"],data["ch33"],data["ch34"],data["ch35"],data["ch36"],
                       data["ch37"],data["ch38"],data["ch39"],data["ch40"],data["ch41"],data["ch42"],
                        data["ch43"],data["ch44"],data["ch45"],data["ch46"],data["ch47"],data["ch48"],
                        data["ch49"],data["ch50"],data["ch51"],data["ch52"],data["ch53"],data["ch54"],
                        data["ch55"],data["ch56"],data["ch57"],data["ch58"],data["ch59"],data["ch60"]])
    
    raw_data = np.reshape(raw_data,(60,len(data['ch1'])))

    raw_data_from_mat = mne.io.RawArray(raw_data, info)

    raw_data_from_mat.save(os.path.join(fif_dir,file_name).replace("mat","fif"),overwrite=True)

files = os.listdir(root)
i=0
for f in files:
    convert_to_fif(root, f)
    print(i)
    i=i+1