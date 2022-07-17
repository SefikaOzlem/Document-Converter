# Document-Converter
The tool takes command line arguments according to the formats you want to convert
between them. A typical command line usage is as follows:
python <filename> <input file> <output file/xsd file> <type>
● The first argument, <filename> is the python file for conversion operations, <input
file> refers to the source filename which will be converted and the third one,
<output file>, refer to the target filename, or XSD file. The last argument,
<type>, defines conversion type (1=CSV to XML, 2=XML to CSV, 3=XML to JSON,
4=JSON to XML, 5=CSV to JSON, 6=JSON to CSV,7=XML validates with XSD)
● The sample command line usage converting from XML to JSON as follows::
python student_id.py test.xml test.json 3
● For XML operations, you should use xml.etree.ElementTree and for JSON
operations you should use json library of python. XSD validation should be
implemented using etree library under lxml.Any other libraries for file types other
than these are not allowed.
