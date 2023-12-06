cat ../UD_Finnish-TDT/*.conllu | grep -Pe '^[0-9]+' | awk -F'\t' '{print $3 "\t" $2 "\t" $4}' | sort | uniq | grep -Pv ' ' > source_data.txt
mkdir -p fi_FI-spell
java -jar ../hunspell-builder/target/hunspell-builder-0.2-jar-with-dependencies.jar source_data.txt fi_FI-spell/fi_FI
