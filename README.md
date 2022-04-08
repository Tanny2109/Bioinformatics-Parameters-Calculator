# solubility-app

Launch the web app (Click on the icon):

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/tanny2109/bioinformatics-parameters-calculator/main/molecular-descriptor-app.py)

With the help of this [awesome discussion over in the Streamlit Discuss board](https://discuss.streamlit.io/t/can-i-add-conda-package-in-requirements-txt/8062/4) and the awesome [GitHub repo from iwatobipen](https://github.com/iwatobipen/chem_streamlit/) for ideas in getting rdkit installed via conda.

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *solubility*
```
conda create -n solubility python=3.8
```
Secondly, we will login to the *solubility* environement
```
conda activate solubility
```
To deactivate the environment
```
conda deactivate
```
### Install prerequisite libraries

Download requirements.txt file

```
wget https://raw.githubusercontent.com/Tanny2109/Bioinformatics-Parameters-Calculator/main/requirements.txt

```

Pip install libraries
```
pip install -r requirements.txt
```
If the above code gives error while downloading and installing certain packages, use following code to install them separately using the same versoin of libraries given in requirements.txt file
```
pip install pandas=1.1.3 
```

Install rdkit
```
conda install -c conda-forge rdkit rdkit
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/Tanny2109/Bioinformatics-Parameters-Calculator/archive/refs/heads/main.zip

###  Launch the app

```
streamlit run app.py
```
# Everytime you need to launch the app, please activate the solubility environment created earlier.
