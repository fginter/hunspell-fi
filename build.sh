java -jar hunspell-builder/target/hunspell-builder-0.2-jar-with-dependencies.jar input.fi.txt spell-plugin/fi_FI

cd spell-plugin
zip -r ../fi-spell-0.2.xpi .
cd ..
