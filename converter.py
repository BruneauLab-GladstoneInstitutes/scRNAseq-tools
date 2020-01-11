#!/usr/bin/python

"""
Program: converter.py
Author: Andrew Blair
Email: andrew.blair@gladstone.ucsf.edu

Cross compatible single cell object converter for Seurat version 3.1.2, Scanpy version 1.4.4, and SingleCellExperiment (sce) version 1.8.0. The first and second arguments must be the absolute paths for the input and desired output file type.

Example:

python3 converter.py

# Seurat to Scanpy
python3 converter.py

# Scanpy to Seurat
python3 converter.py

# Seurat to SingleCellExperiment
python3 converter.py

# SingleCellExperiment to Seurat
python3 converter.py


Notes:
* Using subprocess module because sourcing Seurat using rpy2 causes segmentation fault.
"""
import os
import argparse
import itertools
import subprocess
import pandas as pd
import scanpy as sc
import anndata2ri
import rpy2.robjects as robjects
anndata2ri.activate()

def scanpy_to_seurat(input_scanpy, output_seurat, meta_export='no'):
    '''
    Convert a Seurat object to a Scanpy object
    
    :param input_scanpy: str, Scanpy object file path
    :param output_seurat: str, Seurat object file path
    return: None
    '''
    subprocess.call('Rscript utils/converter.R -i ' + input_scanpy + ' -o ' + output_seurat + ' -m ' + meta_export, shell=True)

def seurat_to_scanpy(input_seurat, output_scanpy):
    '''
    Convert a Seurat object to a Scanpy object
    
    :param input_seurat: str, Seurat object file path
    :param output_scanpy: str, SingleCellExperiment object file path
    return: None
    '''
    seurat_to_sce(input_seurat, 'sce.rds', meta_export='yes')
    meta_df = pd.read_csv('meta.csv')
    os.remove('meta.csv')
    sce_to_scanpy('sce.rds', output_scanpy, meta_df = meta_df)
    
def seurat_to_sce(input_seurat, output_sce, meta_export='no'):
    '''
    Convert a Seurat object to a SingleCellExperiment object
    
    :param input_seurat: str, Seurat object file path
    :param output_sce: str, SingleCellExperiment object file path
    return: None
    '''
    subprocess.call('Rscript utils/converter.R -i ' + input_seurat + ' -o ' + output_sce + ' -m ' + meta_export, shell=True)

def sce_to_scanpy(input_sce, output_scanpy, meta_df=None):
    '''
    Convert a SingleCellExperiment object to a Scanpy object
    
    :param input_sce: str, SingleCellExperiment object file path
    :param output_scanpy: str, Scanpy object file path
    return: None
    '''
    readRDS = robjects.r['readRDS']
    adata = readRDS(input_sce)
    if meta_df:
        adata.obs = meta_df
    adata.write(output_scanpy)

def main(input_scanpy, input_seurat, input_sce, output_scanpy, output_seurat, output_sce):
    '''
    Convert single cell object file type
    
    return: None
    '''
    # Scanpy to Seurat
    if None not in [input_scanpy, output_seurat]:
        scanpy_to_seurat(input_scanpy, output_seurat)
    
    # Seurat to Scanpy
    if None not in [input_seurat, output_scanpy]:
        seurat_to_scanpy(input_seurat, output_scanpy)
    
    # Seurat to SingleCellExperiment
    if None not in [input_seurat, output_sce]:
        seurat_to_sce(input_seurat, output_sce)
    
    # SingleCellExperiment to Seurat
    if None not in [input_sce, output_seurat]:
        sce_to_seurat(input_sce, output_seurat)
    
    # SingleCellExperiment to Scanpy
    if None not in [input_sce, output_scanpy]:
        sce_to_scanpy(input_sce, output_scanpy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a single cell file format.')
    
    # Inputs
    parser.add_argument('--input_scanpy', metavar='path', required=False,
                        help='Input Scanpy object file path.')
    parser.add_argument('--input_seurat', metavar='path', required=False,
                        help='Input Seurat object file path.')
    parser.add_argument('--input_sce', metavar='path', required=False,
                        help='Input SingleCellExperiment object file path.')
    
    # Output
    parser.add_argument('--output_scanpy', metavar='path', required=False,
                        help='Desired output object file path.')
    parser.add_argument('--output_seurat', metavar='path', required=False,
                        help='Desired output object file path.')
    parser.add_argument('--output_sce', metavar='path', required=False,
                        help='Desired output object file path.')
                        
    args = parser.parse_args()
    main(input_scanpy=args.input_scanpy, input_seurat=args.input_seurat, input_sce=args.input_sce, output_scanpy=args.output_scanpy, output_seurat=args.output_seurat, output_sce=args.output_sce)