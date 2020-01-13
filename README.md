# scRNAseq-tools

**Warning Undergoing Construction!**

Collection of scripts for single cell RNA-seq analysis.

# Environment Setup
# Scripts
## converter.py
Cross compatible single cell object converter for Seurat version 3.1.2, Scanpy version 1.4.4, and SingleCellExperiment (sce) version 1.8.0.

#### Scanpy to Seurat
```
python3 converter.py --input_seurat path/to/rds --output_scanpy path/to/h5ad
```

#### Seurat to Scanpy
```
python3 converter.py --input_scanpy path/to/h5ad --output_seurat path/to/rds```
```

#### Seurat to SingleCellExperiment
```
python3 converter.py --input_seurat path/to/rds --output_sce path/to/Rdata
```

#### SingleCellExperiment to Seurat
```
python3 converter.py --input_sce path/to/Rdata --output_seurat path/to/rds
```

#### SingleCellExperiment to Scanpy
```
python3 converer.py --input_sce path/to/Rdata --output_scanpy path/to/h5ad
```

Acknowledgments and thanks extend to the [Theis](https://github.com/theislab/anndata2ri) and [Satija](https://satijalab.org/seurat/v3.1/conversion_vignette.html) laboratories for supporting interoperability between single-cell object formats.
