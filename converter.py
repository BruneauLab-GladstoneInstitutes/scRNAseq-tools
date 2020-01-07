#!/usr/bin/python
import argparse
import subprocess
import scanpy as sc
import anndata2ri

anndata2ri.activate()
# %load_ext rpy2.ipython
import rpy2

# Command line arguments
# @click.command()
# @click.option('--seurat_obj', type=click.STRING, default=False, nargs=1, help='Seurat object file path.')
# @click.option('--scanpy_obj', type=click.STRING, default=False, nargs=1, help='Scanpy object file path.')

def seurat_to_single_cell_experiment(seurat_obj):
    subprocess.call('Rscript seurat2sce.R -i ' + seurat_obj + ' -o sce.rds', shell=True) 

# def seurat_to_scanpy(seurat_obj):
#     %%R -o se
#     se <- readRDS('testrds')
# #     output_scanpy(se)
    
# def output_scanpy(se):
#     se.write('test.h5ad')

def main(seurat_obj, scanpy_obj):
    seurat_to_single_cell_experiment(seurat_obj)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    parser.add_argument('--seurat_obj', metavar='path', required=True,
                        help='Seurat object file path.')
    parser.add_argument('--scanpy_obj', metavar='path', required=True,
                        help='Scanpy object file path.')
    args = parser.parse_args()
    main(seurat_obj=args.seurat_obj, scanpy_obj=args.scanpy_obj)