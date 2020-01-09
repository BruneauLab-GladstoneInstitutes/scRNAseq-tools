# scRNAseq-tools

Collection of scripts for single cell RNA-seq analysis.

# Environment Setup
# Scripts
## converter.py
Cross compatible single cell object converter for Seurat version 3.1.2, Scanpy version 1.4.4, and SingleCellExperiment (sce) version 1.8.0. The first and second arguments are the input file type path and the desired output file type path.

```
python3 converter.py --<seurat_obj, scanpy_obj, sce_obj> --<seurat_obj, scanpy_obj, sce_obj>
```

The following file type conversions are supported:

#### Seurat to Scanpy
```
python3 converter.py --seurat_obj data.rds --scanpy_obj data.h5ad
```

#### Scanpy to Seurat
```
python3 converter.py --scanpy_obj data.h5ad --seurat_obj data.rds
```

#### Seurat to SingleCellExperiment
```
python3 converter.py --seurat_obj data.rds --sce_obj data.Rdata
```

#### SingleCellExperiment to Seurat
```
python3 converter.py --seurat_obj data.rds --sce_obj data.Rdata
```

Acknowledgments and thanks extend to the [Theis](https://github.com/theislab/anndata2ri) and [Satija](https://satijalab.org/seurat/v3.1/conversion_vignette.html) laboratories for supporting interoperability between single-cell object formats.
