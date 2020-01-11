library(Seurat)
library(optparse)

#' Seurat to SingleCellExperiment
#' Converts a Seurat file to SingleCellExperiment file format
#' @param sobj Seurat object
#' @param sce_output SingleCellExperiment output path
#' @return SingleCellExperiment file with file extension .Rdata
#' @export
seurat_to_sce <- function(seurat_obj, sce_output){
    sce <- as.SingleCellExperiment(sobj)
    saveRDS(sce, sce_output)
}

#' Scanpy to Seurat
#' Converts a Scanpy file to Seurat file format
#' @param scanpy_obj Scanpy object file path
#' @param seurat_obj 
#' @return Seurat file with extension .Rdata
#' @export
scanpy_to_seurat <- function(scanpy_obj, seurat_obj){
    sobj <- ReadH5AD(scanpy_obj)
    saveRDS(sobj, file=seurat_obj)
}
            
option_list = list(
    make_option(c("-i", "--seurat_obj"), type="character", default=NULL, 
                help="Seurat object file path.", metavar="character"),
    make_option(c("-o", "--sce_output"), type="character", default=NULL, 
              help="Single cell experiment object output file path.", metavar="character"),
    make_option(c("-m", "--meta"), type="character", default="no", 
              help="Single cell experiment object output file path.", metavar="character"),
    make_option(c("-s", "--scanpy_obj"), type="character", default=NULL, 
              help="Single cell experiment object output file path.", metavar="character")

);

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

sce_output <- opt$sce_output
sobj <- readRDS(opt$seurat_obj)

# Export sce file
seurat_to_sce(sobj, sce_output)

# Export sce and seurat metadata dataframe
if (opt$meta == 'yes'){
    write.csv(sobj@meta.data, 'meta.csv')
    seurat2sce(sobj, opt$sce_output)
}

if (length(opt$scanpy_obj)){
    scanpy_to_seurat(opt$scanpy_obj, opt$)
}