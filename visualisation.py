import matplotlib as plt
from SOMMERECURSSION import TableConditionnement3,tablePourcentage3
from SOMMETRIPAIRE import TableConditionnement4,tablePourcentage4
from SOMMEINSERTION import TableConditionnement5,tablePourcentage5
from SOMMETRIECROISSANT import TableConditionnement1,tablePourcentage1
from SOMMETRIEDECROISSANT import TableConditionnement2,tablePourcentage2



plt.plot(TableConditionnement1,tablePourcentage1,label="Ordre Croissant")
# plt.plot(TableConditionnement2,tablePourcentage2,label="Ordre décroissant ")
plt.plot(TableConditionnement3,tablePourcentage3,label="Recurssive ") 
plt.plot(TableConditionnement4,tablePourcentage4,label="SommationPair")
plt.plot(TableConditionnement5,tablePourcentage5,label="SommationInsertion")  
plt.xlabel('Conditionnement')
plt.ylabel('erreur directe ')
plt.title(' graphe de comparaison')
  
plt.legend()
plt.show()