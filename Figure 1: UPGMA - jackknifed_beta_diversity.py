Last login: Wed Apr 12 22:16:21 on ttys002
Raeenas-MacBook-Air:bioc3301_data raeenahirve$ source activate qiime1
(qiime1) Raeenas-MacBook-Air:bioc3301_data raeenahirve$ cd
(qiime1) Raeenas-MacBook-Air:~ raeenahirve$ cd bioc3301_data
(qiime1) Raeenas-MacBook-Air:bioc3301_data raeenahirve$ ls
2016					corediversityresults
2016_cr_join_no_golay.sh		coreotus
2016_stdout				jack
2017					merge_otu_tables.sh
2017_cr_nojoin_no_golay.sh		merged_otu_table.biom
2017_stdout				merged_otu_table_qual_summary.txt
Acido					merged_otu_table_summary.txt
Filtered OTU				procrustes_results
README.md				rich_sparse_otu_table_summary.txt
comparealphadiversity			taxa_summary
(qiime1) Raeenas-MacBook-Air:bioc3301_data raeenahirve$ jackknifed_beta_diversity.py -i merged_otu_table.biom -o bdiv_jk3700000 -e 300000 -m 2016/map/map.tsv_corrected.txt -t 2016/otus/97_otus.tree
