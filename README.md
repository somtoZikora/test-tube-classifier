# test-tube-classifier

## Setup

### Download assets

Please download photo assets from this [bucket](https://mega.nz/file/IHJFlKLI#a0pndJtsIqhAPLK1KWXpXO5JQSZqTNFib05w1lcKlxQ).

### Install dependencies

Please follow the instructions [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to install the conda package manager if you don't have it yet, then run the following on the command line

```
conda create -n ttc python=3.5

conda activate ttc

pip install tensorflow==1.14.0rc0 keras opencv-python imageai Pillow
```

## Working on the project

Unzip the photo assets, then add the `train` and `test` folders to the folder `test_tubes`.

Run the file `augment.py` to increase the number of test and train photos to 1020 per class. This is the minimum required by ImageAI.
**Note that this requires at least 65GB free storage on your hard drive**.

Refer to the ImageAI docs to create and test models. `model.py` is a nice example :) .