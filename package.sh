rm -f ../fi-spell-0.2.xpi
rm -f ../fi-hunspell-dictionaries-0.2.zip

cd spell-plugin
zip -r ../fi-spell-0.2.xpi .
zip -r ../fi-hunspell-dictionaries-0.2.zip dictionaries/fi_FI

cd ..
