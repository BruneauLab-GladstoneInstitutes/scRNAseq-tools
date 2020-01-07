library(Seurat)
library(optparse)

option_list = list(
  make_option(c("-i", "--seurat_obj"), type="character", default=NULL, 
              help="Seurat object file path.", metavar="character"),
  
  make_option(c("-o", "--sce_output"), type="character", default=NULL, 
              help="Single cell experiment object output file path.", metavar="character")
); 


opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);

sobj <- readRDS(opt$seurat_obj)
se <- as.SingleCellExperiment(sobj)

write.csv(sobj@meta.data, 'meta.csv')
saveRDS(se, opt$sce_output)