# Pizza fantasia

## x)

### 4.12.1 Size and Complexity of Some DSLs
- DSL:t voivat kasvaa erittäin suuriksi ja niistä voi tulla monimutkaisia. 
- Salt-niminen hallinta ohjelma sisältää state-funktioita ja dokumentaatio tälle on peräti yli 75 000 sanaa pitkä. 
- Salt generoi koodia Jinja2 hyödyntäen.
- Puppet on huomattavasti pienempi, koska se sisältää vain 113 funktiota. 
- Yleiset ohjelmointikielet esittävät toiston funktiona, mutta Puppetilla on oma menetelmä ja siinä toiston tilalla käytetään virtuaaliresursseja.
- Kysymys: Millaisissa ympäristöissä kumpikin on parempi?

### 4.12.2 Use of DSL Functions in Case Configuration
- CM-työkaluissa on satoja eri funktioita, mutta vain pientä osaa niistä käytetään.
- Yleisimpiä on case, file, package ja exec.
- Eli vaikka tarjolla on suuri määrä funktioita, niin silti pieni joukko funkioita riittää suurimman osan käytttö tarpeista.
- Kysymys: Millaisissa tilanteissa näitä muita funktioita käytetään.

### 4.12.3 Dependencies Between Main Functions
- Avain funktiot: package, file, servicem user, group, directory ja symlink.
- Kaksi tärkeintä perustoimintoa ovat exec ja file.
- Näiden kahden päälle rakentuvat muut funktiot
- Järjestelmä on impotentti eli tekee muutoksia vain jos tila ei ole jo sille oikea.
- Huomio: Mielenkiintoinen rakenne, jossa execin ja filen päälle rakentuu muut tärkeätkin funktiot, kuten package, service, user ja group.

## a)
Aloitin päivittämällä järjestelmäni komenolla sudo apt update.
<img width="1004" height="235" alt="image" src="https://github.com/user-attachments/assets/ebf8052e-23c4-4356-b1c6-3fcc11dbda8f" />

Sitten asensin Caddy nimisen verkkopalvelimen komennolla sudo apt install caddy.
<img width="1004" height="525" alt="image" src="https://github.com/user-attachments/assets/b0c33625-5b29-4f0f-9f0f-1cebd2ed7dab" />

Koska minulla oli apache2 päällä ja se kuunteli porttia 80, niin en pystynyt saamaan aluksi Caddy:a päällä, mutta lopetin apache2 palvelun komennolla sudo systemctl stop apache2. Tämän jälkeen kun ajoin komennon sudo systemctl start caddy ja sen perään sudo systemctl status caddy niin huomasin, että se toimii.
<img width="1004" height="403" alt="image" src="https://github.com/user-attachments/assets/5c112402-597c-49d8-9238-87ee79567149" />

Varmistin vielä tämän menemällä selaimeen ja ottamalla yhteyden omaan localhostiin eli http://localhost ja sain onnistuneen tuloksen.
<img width="1004" height="523" alt="image" src="https://github.com/user-attachments/assets/b5ea4727-204d-4936-9dab-999a3c0c479f" />

## b)
Loin kansiot Caddylle jokaiseen osioon (tasks, handlers, files).
- mkdir /roles/caddy/files/ -p
- mkdir /roles/caddy/handlers/ -p
- mkdir /roles/caddy/tasks/ -p
<img width="1004" height="104" alt="image" src="https://github.com/user-attachments/assets/23963816-f7a6-4f8b-8f79-e41b9676c7c4" />


<img width="691" height="344" alt="image" src="https://github.com/user-attachments/assets/01c47138-6a02-41d7-ac5b-f2a161cbfac7" />


Alla näkyy roles/caddy/handlers/main.yml sisältö.
<img width="606" height="257" alt="image" src="https://github.com/user-attachments/assets/dadf4641-5faf-42a1-8b5b-06e8b5ac39d8" />


Alla näkyy roles/caddy/tasks/main.yml sisältö.
<img width="628" height="512" alt="image" src="https://github.com/user-attachments/assets/7d4de718-300d-466b-a87b-854ab7be892e" />


Alla näkyy site.yml sisältö.
<img width="597" height="494" alt="image" src="https://github.com/user-attachments/assets/bd6759ce-b638-43b4-88d9-f98d422cf5ec" />


Ajoin ansible-playbook site.yml -K yhden kerran.
<img width="1004" height="206" alt="image" src="https://github.com/user-attachments/assets/22b48b10-cc88-4ce0-b2e5-9f2d4cd62d91" />


Ajoin ansible-playbook site.yml -K toisen kerran.
<img width="1004" height="200" alt="image" src="https://github.com/user-attachments/assets/6e763723-058b-4391-a37e-7b771f53f751" />


## c)
Aloitin etsimällä tiedoston johon muutokset tulisi tehdä. Se löytyi etc/ hakemistosta polulla etc/caddy/Caddyfile. Tänne tein muutoksen respond ”Testi, toimiiko?”, jonka tarkoitus oli ilmentyä localhostissa pyörivään weppi palvelimelleni kun tallennan muutokset. 
<img width="1004" height="592" alt="image" src="https://github.com/user-attachments/assets/853bf6ea-40b9-41b9-b122-1782205ad41e" />


Kun ajoin ansible-playbookin kaikki muu meni läpi, mutta viimeinen kohta epäonnistui, koska minulla ei ollut roles/caddy/files hakemistossa mitään ja olin asettanut sen poluksi, josta ansible sitä etsii. Niimpä kopion Caddyfile tiedoston komennolla cp /etc/caddy/Caddyfile roles/caddy/files/Caddyfile.
<img width="1004" height="371" alt="image" src="https://github.com/user-attachments/assets/f9f78c8e-45ff-4025-96b7-7b82c87546a4" />


<img width="1004" height="33" alt="image" src="https://github.com/user-attachments/assets/925666e4-8f0d-4d4a-86db-e18e7946f308" />


Varmistin vielä copy osion roles/caddy/tasks/main.yml oikeellisuuden.
<img width="1004" height="454" alt="image" src="https://github.com/user-attachments/assets/6cffbd80-5879-41ed-98ef-9cb16a1a1a50" />


Nyt kun ajoin ansible-playbookin uudestaan kaikki meni läpi onnistuneesti.
<img width="1004" height="170" alt="image" src="https://github.com/user-attachments/assets/65cb875d-0f58-49e5-b73a-8cb271f003e4" />


## d)
Ajan komennon sudo apt-get purge caddy, joka siis poistaa caddy verkkopalvelimen koneeltani.  Tämän jälkeen tarkoitus oli todentaa, että ajamalla ansible-playbookin saan caddyn takaisin ja niin, että se lähtee käyntiin samantien.
<img width="1004" height="489" alt="image" src="https://github.com/user-attachments/assets/cafb288b-1373-4764-9aae-44c149823e32" />


Ajoin ansible-playbookin ja se meni läpi. Muutokset näkyvät.
<img width="1004" height="322" alt="image" src="https://github.com/user-attachments/assets/72363b52-dc1d-4608-b505-22aef9d393ec" />


Testasin vielä varmuudeksi, että caddy on päällä komennolla sudo systemctl status caddy. Näin sain varmuuden, että kaikki on mennyt juuri niin kuin pitikin.
<img width="1004" height="308" alt="image" src="https://github.com/user-attachments/assets/73e948aa-110e-459e-afe9-330afd7a3ea1" />


Testiksi avasin vielä localhostin selaimessa ja se näytti oikealta.
<img width="1004" height="254" alt="image" src="https://github.com/user-attachments/assets/d5b732ef-2e97-4669-8e64-40519088179d" />


## e)
Idempotentti todennus onnistui kun ajoin uudestaan ansible-playbookin.
<img width="1004" height="269" alt="image" src="https://github.com/user-attachments/assets/946d92ce-451d-4407-b281-d003ea330d40" />


## Lähteet
- Karvinen, T. 2026. Apache installed with Ansible - quick notes. Luettavissa: https://terokarvinen.com/apache-ansible/. Luettu: 21.4.2026
- Karvinen, T. 2023. Configuration Management of Distributed Systems over Unreliable and Hostile Networks. Sivut 112-117. Luettavissa: https://westminsterresearch.westminster.ac.uk/download/4cc417566aa9af60fe3826d690719e390abdb7a3c8672f3d51b1eb4ca75e7624/1427236/karvinen-2023-configuration-management-of-distributed-systems.pdf. Luettu: 21.4.2026
- Tehtävässä on hyödynnetty virheilmoituksien tutkimisessa Copilot Smart -kielimallia. Syötteenä käytettiin "Auta tunnistamaan tekemäni virhe virheilmoituksesta".





