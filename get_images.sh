if [ -d  "images" ]; then
  rm images/*.*
else
  mkdir images
fi

if [ ! -d "backup"]; then
  mkdir labels
fi

wget http://cvcl.mit.edu/scenedatabase/highway.zip
unzip highway.zip
cp highway/*.* images/.
rm -r highway
rm highway.zip

wget http://cvcl.mit.edu/scenedatabase/opencountry.zip
unzip opencountry.zip
cp Opencountry/*.* images/.
rm -r Opencountry
rm opencountry.zip

wget http://cvcl.mit.edu/scenedatabase/street.zip
unzip street.zip
cp street/*.* images/.
rm -r street
rm street.zip

wget http://cvcl.mit.edu/scenedatabase/inside_city.zip
unzip inside_city.zip
cp inside_city/*.* images/.
rm -r inside_city
rm inside_city.zip

rm images/*.db
