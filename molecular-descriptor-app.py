######################
# Import libraries
######################
import numpy as np
import pandas as pd
import streamlit as st
import pickle
from PIL import Image
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors

######################
# Custom function
######################
## Calculate molecular descriptors
def AromaticProportion(m):
  aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
  aa_count = []
  for i in aromatic_atoms:
    if i==True:
      aa_count.append(1)
  AromaticAtom = sum(aa_count)
  HeavyAtom = Descriptors.HeavyAtomCount(m)
  AR = AromaticAtom/HeavyAtom
  return AR

def generate(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem)
        moldata.append(mol)

    baseData= np.arange(1,1)
    i=0
    for mol in moldata:

        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotatableBonds = Descriptors.NumRotatableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)

        row = np.array([desc_MolLogP,
                        desc_MolWt,
                        desc_NumRotatableBonds,
                        desc_AromaticProportion])

        if(i==0):
            baseData=row
        else:
            baseData=np.vstack([baseData, row])
        i=i+1

    columnNames=["MolLogP","MolWt","NumRotatableBonds","AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData,columns=columnNames)

    return descriptors

##############################################################################################
#Own Code
descriptor_names = list(rdMolDescriptors.Properties.GetAvailableProperties())
get_descriptors = rdMolDescriptors.Properties(descriptor_names)

def generate2(smiles, verbose=False):

    moldata= []
    for elem in smiles:
        mol=Chem.MolFromSmiles(elem)
        moldata.append(mol)

    bD = np.arange(1,1)
    i=0
    for mol in moldata:

        row2 = np.array(get_descriptors.ComputeProperties(mol))

        if(i==0):
            bD = row2
        else:
            bD=np.vstack([bD, row2])
        i=i+1

    colNames2 = descriptor_names
    descriptors2 = pd.DataFrame(data=bD, columns=colNames2)

    return descriptors2
####################
######################
# Page Title
######################

image = Image.open('WebApp-Logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# Molecular Descriptors Calculator Web App

This app calculates the descriptors of molecules as well as predicts its logS value!

""")


######################
# Input molecules (Side Panel)
######################

st.sidebar.header('User Input Features')

## Read SMILES input
SMILES_input = "NCCCC\nCCC\nCN"

SMILES = st.sidebar.text_area("SMILES input", SMILES_input)
SMILES = "C\n" + SMILES #Adds C as a dummy, first item
SMILES = SMILES.split('\n')

st.header('Input SMILES')
SMILES[1:] # Skips the dummy first item

#Common Descriptors
st.header('Basic Descriptors')
X = generate(SMILES)
X[1:]
#Calculating my own descriptors
st.header('Computed molecular descriptors')
Y = generate2(SMILES)
Y[1:]
######################
# Pre-built model
######################

# Reads in saved model
load_model = pickle.load(open('solubility_model.pkl', 'rb'))

# Apply model to make predictions
prediction = load_model.predict(X)
#prediction_proba = load_model.predict_proba(X)

st.header('Predicted LogS values')
prediction[1:] # Skips the dummy first item
