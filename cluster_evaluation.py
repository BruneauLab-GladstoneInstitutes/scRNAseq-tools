import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_mutual_info_score

def _create_df(meta_table):
    meta_df = pd.read_csv(meta_table)
    nmi_df = pd.DataFrame([cluster for cluster in list(meta_df) if cluster.split('_')[0] == 'integrated'], columns=['res'])
    nmi_df['x'] = [cleanup.split('_')[-1] for cleanup in nmi_df['res']]
    return meta_df, nmi_df

def _run_nmi(meta_table, nmi_df, feature_list):
    for feature in feature_list:
        nmi_df[feature] = [normalized_mutual_info_score(meta_table[feature], meta_table[res]) for res in nmi_df['res']]
    return nmi_df

def _create_line_plot(nmi_df, figure_name):
    with PdfPages(figure_name) as pdf:
        for data in list(nmi_df):
            if data not in ['res', 'x']:
                fig = plt.figure()
                plt.title(data)
                plt.plot(nmi_df['x'], nmi_df[data], '-o')
                plt.xticks(rotation=45)
                plt.ylabel('NMI')
                plt.xlabel('louvain resolution')
                pdf.savefig(fig)


def _cli():
    cli = argparse.ArgumentParser()
    cli.add_argument("--meta_table", type=str, help="Path to meta table.")
    cli.add_argument("--feature_list", nargs = "*", type=str, default=[])
    cli.add_argument("--figure_name", type=str, default='nmi_louvain_res.pdf')
    args = cli.parse_args()
    return args.meta_table, args.feature_list, args.figure_name

def main():
    meta_table, feature_list, figure_name = _cli()
    meta_df, nmi_df = _create_df(meta_table)
    nmi_df = _run_nmi(meta_df, nmi_df, feature_list)
    _create_line_plot(nmi_df, figure_name)
    
if __name__ == '__main__':
    main()
    