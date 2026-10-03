# x) Lue ja tiivistä

## SSH public key – Login without password
  - SSH on yleinen ja turvallinen tapa ottaa etäyhteys palvelimelle.
  - Monet ohjelmistotuotteet käyttävät SSH:ta niiden taustalla.
  - SSH perustuu julkiseen ja yksityisen avainparin salaukseen.
  - Julkisen avaimen voi kopioida niin, että SSH käyttää sitä aina automaattisesti.
Huomio: Oivallukseni on, että SSH:n hyödyntämä avainpari on paljon turvallisempi, kuin salasanat.

## Hello Ansible
  - Ansible toimii SSH:n kautta.
  -	Komentoja voidaan ajaa samanaikaisesti monelta koneelta kerrallaan.
  -	Jokaisella roolilla on omat tehtävänsä.
  -	Luo tiedoston kohdekoneelle ja raportoi siitä muutokset, jos sellaisia on.
Kysymys: Kun annoimme Ansiblen ajaa komento ansible all -a ’uptime’ -i hosts.ini, miksi tässä käytämme vain ” ’ ” merkkiä, 
kun puolestaan muutosten jälkeen voimme ajaa helpomman komennon ansible all -a ”uptime”, niin käytämme sanan uptime molemmin puolin merkkiä ” ” ” ?


# a) Asenna SSH-demoni ja testaa se kirjautumalla SSH:lla
Ajoin Debianissa sudo apt-get update, jonka avulla varmistin, että järjestelmä on valmis latausta varten. 
Latauksen suoritin komennolla sudo apt-get install -y ssh. Jotta sain ssh-yhteyden käynnistymään automaattisesti
aina boottauksen yhteydessä, ajoin komennon sudo systemctl enable --now ssh.
Lopuksi testasin vielä yhteyden onnistumisen ssh localhost komennolla.

# b) Automatisoi ssh-kirjautuminen julkisella avaimella
Jotta saan käyttööni julkisen avaimen käyttöön asensin sen komennolla ssh-keygen. Tämä generoi minulle julkisen avaimen. 
Komennolla ssh-copy-id localhost kopion julkisen avaimen omalle palvelimelle (localhost). 
Lopuksi testasin vielä kirjautumisen ssh localhost avulla ja pääsin sisään.

# c) Tee hei maailma ansiblella ja kokeile sitä SSH:n yli
Aloitin suorittamalla perinteisesti päivitykset komennolla sudo apt-get update ja sen jälkeen asensin ansiblen, micro-tekstieditorin,
bash-completionin ja treen komennolla sudo apt-get install ansible micro bash-completion tree. 
Tämän jälkeen loin ansiblelle kansion. Tämän jälkeen kotihakemistooni loin uuden teksti tiedoston hosts.ini. Jotta pystyimme varmistumaan,
että ansible voi käyttää ssh:ta, ajoin komennon ansible all -a ’uptime’ -i hosts.ini. 
Seuraavaksi lisäsin hosts.ini tiedostoon määritelmän, joka estää python valituksen. Sitten loin site.yml,
johon määriteltiin mitkä tietokoneet saavat mitkä oikeudet. 
Tämän jälkeen loin rooleille oman kansion ja micro-tiedoston, johon kirjoitin sisällön. Tämä tulosti sisältöni ja näytti,
että muutos on tapahtunut. Jotta sain varmennettua, että toimii myös ssh:n yli niin testasin sen komennolla ssh localhost ’cat  /tmp/hello-ansible. 
Tarkastelin loppuksi tehtyä suoritusta tree -F komennolla, joka listaa puumaisen rakenteen avulla luomani tiedostot ja hakemistot.
Ajoin vielä kerran komennon ansible.playbook site.yml. Se tulosti hyväksytyn tuloksen ja lisäksi, että muutoksia aiempaan on tehty nolla kappaletta.
