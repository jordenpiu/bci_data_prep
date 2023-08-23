import mne 
import os 
from utils import *

def fif_read(root,file_name):
    raw_path = os.path.join(root,file_name)
    raw = mne.io.read_raw(raw_path)
    raw.load_data()
    raw.filter(l_freq=4,h_freq=40)

    events, event_id = mne.events_from_annotations(raw)
    print(events)
    # tmin= 0 
    # tmax = 1
    # baseline = (None, 0)
    # epochs_ica = mne.Epochs(raw,
    #                         events = events,)

files = os.listdir(fif_dir)
i=0
for f in files:
    fif_read(fif_dir, f)
    print(i)
    i=i+1
