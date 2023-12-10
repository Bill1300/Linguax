#/bin/bash

#🐍
mkdir ~/.linguax
mv ./executar.py ~/.linguax
touch ~/.linguax/historico.json
touch ~/.linguax/historico.xlsx
echo "data_hora;texto_entrada;texto_saida;idiona_saida;" > ~/.linguax/historico.xlsx
touch ~/.linguax/meta.dados

#🦪
sudo mv ./linguax.sh /bin
sudo chmod 755 /bin/linguax.sh
sudo mv /bin/linguax.sh /bin/linguax #Renomear

echo -e "\e[1;45m Instalado com sucesso! \e[0m"
