import xml.etree.ElementTree as ET
import glob


arquivos = glob.glob("*.xml")
textoXML = open('arqTextoXML.txt','w')
tags     = open('arqTags.txt','r')
#conteudoTags = tags.read()

for arq in arquivos:
  tree = ET.parse(arq)
  root = tree.getroot()
  for child in root.iter():
    tag = child.tag.split('}')[-1]
    if len(child) == 0 and tag == 'tpLograd' or 'dscLograd' or 'nrLograd' or 'bairro' or 'cep' or 'codMunic' or 'uf' or 'defFisica' or 'defVisual' or 'defAuditiva' or 'defMental' or 'defIntelectual' or 'reabReadap' or 'infoCota' or 'tpDep' or 'nmDep' or 'dtNascto3' or 'cpfDep' or 'depIRRF' or 'depSF' or 'incTrab' or 'matricula' or 'tpRegTrab' or 'tpRegPrev' or 'cadIni' or 'dtAdm' or 'tpAdmissao' or 'indAdmissao' or 'tpRegJor' or 'natAtividade' or 'dtBase' or 'cnpjSindCategProf' or 'nmCargo' or 'CBOCargo' or 'codCateg' or 'vrSalFx' or 'undSalFixo' or 'tpContr' or 'tpInsc4' or 'nrInsc5' or 'qtdHrsSem' or 'tpJornada' or 'tmpParc' or 'horNoturno' or 'dscJorn':
      textoXML.write(str(child.text)+'|')
  textoXML.write('\n')

textoXML.close()