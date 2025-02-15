#!/usr/bin/env python
from pca.PCAprint import PCAprint
# from PCAprint import PCAprint
#from PCA import PCA
#from PCAprep import MyPCAprep
#from PCAinit import PCAinit
from pca.KeywordInit import Keyword
# import numpy as np

if __name__ == '__main__':
    
    inpt = 'convert_inpt'
    
    kw = Keyword(inpt)
    pca = PCAprint(kw)
    
#     pca.DirectoryCheck()
#     kw.FileCheck('config_space.npy')
    pca.BasisCheck()
    pca.ShapeCheck()
    pca.ReadMinimaIndex()
    pca.ReadConfigurationSpace()
#    print pca.kw.beta
    if pca.kw.beta:
        pca.ReadMinimaEnergies()   
        pca.FindGM()
        pca.CalculateWeighting()
#    pca.basis = 'dihedral'
    # Convert config_space to selected basis set
    if pca.kw.basis == 'cartesian':

        pca.ReshapeCartesian1D3D()

        pca.LstSqrStructureFit()
        pca.ReshapeCartesian3D2D()

    if pca.kw.basis == 'dihedral':
        print 'Converting to Internal Dihedrals'
        pca.ReshapeDihedral()
        print 'Done'
        

    pca.SaveConfigSpace(kw.conv_fname)
