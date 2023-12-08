cd data-prep
zcat counts_min_3.raw.txt.gz | tqdm | python3 filter.py | gzip > filtered_counts.txt.gz
zcat filtered_counts.txt.gz | tqdm | python3 prep_input.py > input.fi.txt
cd ..
java -jar hunspell-builder/target/hunspell-builder-0.2-jar-with-dependencies.jar data-prep/input.fi.txt spell-plugin/dictionaries/fi_FI
