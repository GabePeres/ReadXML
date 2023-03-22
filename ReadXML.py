import xml.etree.ElementTree as ET
import glob

arquivos  = glob.glob("*.xml")
textoXML  = open('arqTextoXML.txt','w')

for arq in arquivos:
  tree = ET.parse(arq)
  root = tree.getroot()
  
  for child in root.iter():
    tag = child.tag.split('}')[-1]        
    if len(child) == 0:        
        textoXML.write(str(child.text)+'|')
  textoXML.write('\n')

textoXML.close()
#caso os arquivos XMLs forem diferentes existe o potencial das informações ficarem em colunas diferentes.
