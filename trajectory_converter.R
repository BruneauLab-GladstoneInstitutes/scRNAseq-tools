library(Seurat)
library(monocle3)
library(optparse)

#' Seurat to CDS
#' Converts a Scanpy file to CDS file format
#' @param input_scanpy Seurat object file path
#' @param output_seurat CDS object output path
#' @return CDS file with extension .cds
#' @export
seurat_to_cds <- function(input_seurat, output_cds){
    sobj <- readRDS(input_seurat)
    gene_df <- as.data.frame(row.names(sobj@assays$RNA@data))
    colnames(gene_df) <- "gene_short_name"
    rownames(gene_df) <- gene_df$gene_short_name
    cds <- new_cell_data_set(sobj@assays$RNA@counts,
                          cell_metadata = sobj@meta.data,
                          gene_metadata = gene_df)
    saveRDS(cds, file=output_cds)
}

# Command line interface
option_list = list(
    
    make_option(c("--seurat_to_cds"), type="character" , default=NULL, help="Seurat to CDS",
                metavar="character")
);

parser <-OptionParser(option_list=option_list)
arguments <- parse_args (parser, positional_arguments=TRUE)
opt <- arguments$options
output_obj <- arguments$args

# Convert files
if ('seurat_to_cds' %in% names(opt)){
    input_obj <- strsplit(opt$seurat_to_cds, ",")
    seurat_to_cds(input_obj[[1]], output_obj[[1]])
}