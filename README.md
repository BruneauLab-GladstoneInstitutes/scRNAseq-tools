# scRNAseq-tools

**Warning Undergoing Construction!**

Collection of scripts for single cell RNA-seq analysis.

# Environment Setup
# Scripts
## converter.py
Cross compatible single cell object converter for Seurat version 3.1.2 file extension '.rds', Scanpy version 1.4.4 file extension '.h5ad', and SingleCellExperiment (sce) version 1.8.0 file extension '.Rdata'. The first and second arguments must be the absolute paths for the input and desired output file type.

#### Seurat to Scanpy
```
python3 converter.py data.rds data.h5ad
```

#### Scanpy to Seurat
```
python3 converter.py data.h5ad data.rds
```

#### Seurat to SingleCellExperiment
```
python3 converter.py data.rds data.Rdata
```

#### SingleCellExperiment to Seurat
```
python3 converter.py data.rds data.Rdata
```

Acknowledgments and thanks extend to the [Theis](https://github.com/theislab/anndata2ri) and [Satija](https://satijalab.org/seurat/v3.1/conversion_vignette.html) laboratories for supporting interoperability between single-cell object formats.
