# H3 Demoni

## x)
### Karvinen 2026
-	Apache2 on verkkopalvelin
-	Apache2 voidaan myös asentaa ja konfiguroida ansiblen avulla
-	Kaikki konfiguraatiohin tehdyt muutokset tulee voimaan vasta, kun käynnistää palvelun uudelleen
-	Roolin hakemistorakenne muodostuu seuraavasti: tasks/, handlers/, files/
- Kysymys: onko Apache2 tuotannossa enitenkäytetty verkkopalvelin?

### Ansible Community Documentation: Handlers: running operations on change
Handlers – Johdanto
-	Handlerit ovat tehtäviä, jotka suoritetaan vain jos jokin muu tehtävä ilmoittaa muutoksesta
-	Halutaan suorittaa palvelun uudelleenkäynnistys konfiguraatiotiedoston muuttuessa
-	Huomio: handlereiden käyttö nopeuttaa toimenpiteitä.

Notifying handlers
-	Tehtävä voi kutsua yhden tai useita handlereita
-	Voi olla lista useista handlereista tai yksi merkkijono
-	Handleri suoritetaan vain jos tehtävä muuttuu
  
  
Ansible-doc service
-	Tarkoitus on hallita palveluiden tilaa
-	Enabled määrittää käynnistyykö palvelu automaattisesti bootin yhteydessä eli se ei vaikuta sen hetkiseen tilaan.
-	Name määrittää palvelun nimen esim. apache2
-	State määrittää palvelun tilan esim, started, stopped, restarted, reloaded
  
EXAMPLE
````
-	Service:
    name: apache2
    state: started
    enabled: yes
````

## a)
Aloitin Apache2 asentamisen samalla tavalla, kuin minkän muun asentamisen eli päivitän järjestelmän "sudo apt-get update" komennolla. Sen jälkeen asensin Apache2 verkkopalvelun komennolla "sudo apt-get install apache2". Loin Apache2 varten kotihakemistooni kansion publicsite ja sinne tein index.html nimisen tiedoston. Index.html tiedostoon kirjoitin yksinkertaisen html koodin ````<h1> Testisivut </h1>````. 

Seuraavaksi loin uuden konfiguraatiotiedoston Apache2 varten. Tänne lisäsin mallin mukaisen konfiguraation, johon tein muutokset, jotka ovat välttämättömiä, jotta se löytää minun hakemistopolkuni.
<img width="1004" height="473" alt="image" src="https://github.com/user-attachments/assets/16acaea7-2ed2-48d9-83c8-8b4991dd2f65" />

Sitten loin linkin "sites-available/example.com.conf" ja "sites-enabled/example.com.conf" välillä, jotta se ottaa sivuston käyttöön. Linkin loin komennolla ````ln -s /etc/apache2/sites-available/example.com.conf /etc/apache2/sites-enabled/example.com.conf````.

Lopuksi vielä ennenkuin testasin sivuni toimivuutta määritin ohjeiden mukaiset oikeudet sivuston kansioille. 
````
- chmod ugo+x /home/aaro/
- chmod ugo+x /home/aaro/publicsite/
- chmod ugo+r /home/aaro/publicsite/index.html
````

Testasin Apache2 configuraation toimivuutta komennolla ````sudo apache2ctl configtest````.
<img width="1004" height="112" alt="image" src="https://github.com/user-attachments/assets/3c2bf31c-6cc9-4bdd-95da-58c5c8b115e4" />

Kun syntaksi oli OK, sitten käynnistin Apache2 uudestaan komennolla ````sudo systemctl restart apache2````. Sitten testasin sivua nettiselaimessa ja se toimi.
<img width="1004" height="398" alt="image" src="https://github.com/user-attachments/assets/b33e3de6-a633-48ad-be8c-fa722b117f32" />


## b)
Tein tismalleen saman alun, kuin Apache2 kanssa eli ajoin päivitykset ja asensin Nginx:n. Aluksi myös lopetin Apache2 istunnon komennolla ````sudo systemctl stop apache2````. Tein tämän siksi, että localhostiin samaan porttiin ei voi kaksi eri palvelua kuunnella samanaikaisesti. 

Tein kaikki muutokset jo aiemmin tehtyyn index.html tiedostoon ja nyt sen koodi näytti seuraavalta --> ````<h1>Testisivut (nginx)</h1>````. Minun piti käydä muokkaamassa Nginx:n omaa konfiguraatioita, missä tein muutoksen, jossa määritin rootin omaan hakemistooni. Sen jälkeen annoin samat oikeudet uudeelleen, kuin Apache2 yhteydessä.

<img width="1004" height="177" alt="image" src="https://github.com/user-attachments/assets/6e7eea4f-b7b2-476a-8e5a-716892410a57" />

````
- chmod ugo+x /home/aaro/
- chmod ugo+x /home/aaro/publicsite/
- chmod ugo+r /home/aaro/publicsite/index.html
````
Testasin samalla tavalla konfiguraation toimivuutta, mutta vain Nginx:n tarkoitetulla komennolla ````sudo nginx -t````. 

<img width="1004" height="79" alt="image" src="https://github.com/user-attachments/assets/75ca6b3f-bcd0-49c6-a5fb-d0a03a1bbd44" />

Tein taas Nginx:n kohdalla uudelleen käynnistyksen komennolla ````sudo systemctl restart nginx````. Sitten testasin nettiselaimella ottaa yhteyden localhostiin. 

<img width="1004" height="424" alt="image" src="https://github.com/user-attachments/assets/62262fdc-dd4d-4b9f-84f5-b7e26609cec8" />


## c)
Aloitin luomalla mallin mukaisen hakemistopuu rakenteen, josta tein muutoksilla Nginx:n automatisointia vastaavan version.
<img width="574" height="262" alt="image" src="https://github.com/user-attachments/assets/0b9265d4-0387-4728-befb-0428080548d7" />

~/roles/nginx/tasks/main.yml sisältö:

<img width="1033" height="414" alt="image" src="https://github.com/user-attachments/assets/abcf1ff5-0b71-4a4a-bca0-17a530455daf" />

~/roles/nginx/handlers/main.yml sisältö:

<img width="1082" height="165" alt="image" src="https://github.com/user-attachments/assets/208bfc73-4aea-475c-92af-49bb1ed161dd" />

~/roles/nginx/files/default sisältö:

<img width="1007" height="473" alt="image" src="https://github.com/user-attachments/assets/c6964b12-3108-48b5-b901-b13a0dac54f2" />

Kun testasin ajaa ansible-playbookia, niin tuli virhe, että roolia ei löytynyt. Tajusin, etten ollut lisännyt site.yml tiedostoon tätä luomaani roolia "nginx". Kun lisäsin ja ajoin niin meni läpi. Ajoin vielä varmistaakseni toisen kerran.

<img width="1004" height="541" alt="image" src="https://github.com/user-attachments/assets/f3347891-db53-4d88-be25-2767152a676f" />

<img width="1004" height="193" alt="image" src="https://github.com/user-attachments/assets/75dd433e-6d56-48c8-9866-c248c692e00f" />

Lopuksi testasin vielä toimiiko sivu playbookin ajon jälkeen ja toimi.

<img width="1004" height="533" alt="image" src="https://github.com/user-attachments/assets/5325db64-602a-4567-a6f5-9fd1bb40e5bc" />


## Lähteet
- Ansible Community Documentation. s.a. Handlers: running operations on change. Luettavissa: https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_handlers.html. Luettu: 13.4.2026
- Karvinen, Tero. 2026. Apache installed with Ansible - quick notes. Luettavissa: https://terokarvinen.com/apache-ansible/. Luettu: 11.4.2026
- Karvinen, Tero 2026. Sudo without password. Luettavissa: https://terokarvinen.com/passwordless-sudo/. Luettu: 11.4.2026
