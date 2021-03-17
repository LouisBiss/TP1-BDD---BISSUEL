# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:15:29 2021

@author: louis
"""


Excercice 1 

-	Création un Namespace nommé "elections" :
    
cqlsh>CREATE KEYSPACE elections with replication={‘class’:’SimpleStrategie’,’replication_factor’:1} AND durable_writes=’true’;

-	Créer table aministré:
    
cqlsh>use elections;
cqlsh:elections> CREATE TABLE administre (numero_id_nationale int PRIMARY KEY, name text, surname text, addresse text);

-	Créer une table candidat 

cqlsh> CREATE TABLE candidat (name text PRIMARY KEY, surname text, parti_politique text);

- Ajouter des administrés dans le tableau des adminitrés:
    
cqlsh :election> INSERT INTO administre (numero_id_nationale, name, surname, adresse) VALUES (1453, ‘Lulu’, ‘LEZEUB’); 
Cqlsh :election> INSERT INTO administre (numero_id_nationale, name, surname, adresse) VALUES (1453, ‘Loulou’, ‘LEGANG’,'ReimsZoo'); 
Cqlsh :election> INSERT INTO administre (numero_id_nationale, name, surname, adresse) VALUES (1453, ‘Tom’, ‘Lesteph’,'Banlieue de Lyon'); 

-Ajouter des candidats dans le tableau des candidats:

cqlsh :election> INSERT INTO candidat (name, surname, parti_politique) VALUES (‘Philou’,’Poutou’,’A’); 
cqlsh :election> INSERT INTO candidat (name, surname, parti_politique) VALUES (‘Natou’,’Arthou’,’B’); 
cqlsh :election> INSERT INTO candidat (name, surname, parti_politique) VALUES (‘JeanLou’,’Meluch’,’C’);     


- Allouer les voix à chaque candidats, mais d'abord il faut d'abord ajouter une nouvelle colonne pour rentrer le nombre de voix:
    
ALTER TABLE candidat ADD nb_voix int ;

- Maintenant il faut mettre à jour les données du tableau:

Update candidat set nb_voix=34, surname=’Poutou’ WHERE name=’Philou’ ;
Update candidat set nb_voix=34, surname=‘Natou’ WHERE name=‘Natou’ ;
Update candidat set nb_voix=34, surname=‘JeanLou’ WHERE name=’Meluch’ ;

1.	Quel est le parti ayant le réuni le plus de voix ?

- Pour déterminer le parti politique ayant réuni le plus de voix il faut additioner les voix recut par les candidats du même:
    
SELECT SUM(nb_voix) from candidat WHERE parti_politique='A';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='B';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='C';

2.	Quel candidat a gagné les élections ?

Pour le déterminer il faut qu on trouve le maximum dans la colonne nb_voix:
    
SELECT name,surname, MAX(nb_voix) FROM candidat;

3.	Le candidat ayant gagné les élections vient-il du parti politique ayant eu la majorité des voix ?

Oui

Exercice 2

1.	Quel est le parti politique ayant eu le plus de voix ?

SELECT SUM(nb_voix) from candidat WHERE parti_politique='A';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='B';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='C';


2.	Quel est le parti politique ayant eu le moins de voix ?


SELECT SUM(nb_voix) from candidat WHERE parti_politique='A';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='B';
SELECT SUM(nb_voix) from candidat WHERE parti_politique='C';






