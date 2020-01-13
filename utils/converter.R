# Program: converter.R
# Author: Andrew Blair
# Email: andrew.blair@gladstone.ucsf.edu
#
# Description: Cross compatible single cell object converter for Seurat version 3.1.2, Scanpy version 1.4.4, and
# SingleCellExperiment (sce) version 1.8.0. The first and second arguments must be the absolute paths for the input and desired
# output file type.
#
# Example:
# 
# Scanpy to Seurat
# Rscript converter.R --scanpy_to_seurat <path to h5ad> <path to rds>
# 
# Seurat to SingleCellExperiment
# Rscript converter.R --seurat_to_sce <path to rds> <path to Rdata>
# 
# SingleCellExperiment to Seurat
# Rscript converter.R --sce_to_seurat <path to Rdata> <path to rds>
#
# Notes
# * This script is a secondary interface to converter.py, however, users may be run it independently.

library(Seurat)
library(optparse)

#' Scanpy to Seurat
#' Converts a Scanpy file to Seurat file format
#' @param input_scanpy Scanpy object file path
#' @param output_seurat Seurat object output path
#' @return Seurat file with extension .Rdata
#' @export
scanpy_to_seurat <- function(input_scanpy, output_seurat){
    sobj <- ReadH5AD(input_scanpy)
    saveRDS(sobj, file=output_seurat)
}

#' Seurat to SingleCellExperiment
#' Converts a Seurat file to SingleCellExperiment file format
#' @param input_seurat Seurat object file path
#' @param output_sce SingleCellExperiment output path
#' @return SingleCellExperiment file with file extension .Rdata
#' @export
seurat_to_sce <- function(input_seurat, output_sce, meta){
    sobj <- readRDS(input_seurat)
    if (meta == 'yes'){write.csv(sobj@meta.data, 'meta.csv')}
    sce <- as.SingleCellExperiment(sobj)
    saveRDS(sce, file=output_sce)
    
}

#' SingleCellExperiment to Seurat
#' Converts a Seurat file to SingleCellExperiment file format
#' @param input_sce SingleCellExperiment object file path
#' @param output_seurat Seurat object file path
#' @return SingleCellExperiment file with file extension .Rdata
#' @export
sce_to_seurat <- function(input_sce, output_seurat){
    sce <- readRDS(input_sce)
    sobj <- as.Seurat(sce)
    saveRDS(sobj, file=output_seurat)
}

# Command line interface
option_list = list(
    
    make_option(c("--scanpy_to_seurat"), type="character" , default=NULL, help="Seurat to Scanpy",
                metavar="character"),
    
    make_option(c("--seurat_to_sce"), type="character" , default=NULL, help="Seurat to SingleCellExperiment",
                metavar="character"),
    
    make_option(c("--sce_to_seurat"), type="character" , default=NULL, help="Seurat to Scanpy",
                metavar="character"),
    
    make_option(c("--meta"), type="character", default="no", help="Export Seurat meta data", metavar="character") 
);

parser <-OptionParser(option_list=option_list)
arguments <- parse_args (parser, positional_arguments=TRUE)
opt <- arguments$options
output_obj <- arguments$args

# Convert files
if ('scanpy_to_seurat' %in% names(opt)){
    input_obj <- strsplit(opt$scanpy_to_seurat, ",")
    scanpy_to_seurat(input_obj[[1]], output_obj[[1]])
}

if ('seurat_to_sce' %in% names(opt)){
    input_obj <- strsplit(opt$seurat_to_sce, ",")
    seurat_to_sce(input_obj[[1]], output_obj[[1]], opt$meta)
}

if ('sce_to_seurat' %in% names(opt)){
    input_obj <- strsplit(opt$sce_to_seurat, ",")
    sce_to_seurat(input_obj[[1]], output_obj[[1]])
}


