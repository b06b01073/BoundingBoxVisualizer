# Folder structure

```
.
├── VideoMaker.py
├── __pycache__
│   └── VideoMaker.cpython-39.pyc
├── makeVideo.py
├── readme.md
└── train
    ├── images
    │   ├── 0902_150000_151900
    │   ├── 0902_190000_191900
    │   ├── 0903_150000_151900
    │   ├── 0903_190000_191900
    │   ├── 0924_150000_151900
    │   ├── 0924_190000_191900
    │   ├── 0925_150000_151900
    │   ├── 0925_190000_191900
    │   ├── 1015_150000_151900
    │   ├── 1015_190000_191900
    │   ├── 1016_150000_151900
    │   └── 1016_190000_191900
    └── labels
        ├── 0902_150000_151900
        ├── 0902_190000_191900
        ├── 0903_150000_151900
        ├── 0903_190000_191900
        ├── 0924_150000_151900
        ├── 0924_190000_191900
        ├── 0925_150000_151900
        ├── 0925_190000_191900
        ├── 1015_150000_151900
        ├── 1015_190000_191900
        ├── 1016_150000_151900
        └── 1016_190000_191900
```

# How to run this repo
Install the packages in `requirements.txt` first.

```
# Example: 
# This will read the images from train/images/0902_150000_151900/ and the labels from train/labels/0902_150000_151900/
# The result will be stored in video directory.
$ python makeVideo.py -i=train/images/0902_150000_151900/ -l=train/labels/0902_150000_151900/ -s=video
```
