# x) Tiivistä

## Karvinen 2026
Komennoilla sudo adduser antero saadaan luotua ympäristöömme uusi käyttäjä nimeltä antero. Komento sudo groupadd sudoless luo sudoless nimisen ryhmän, jota tarvitaan harjoituksessa. Komennolla sudo adduser antero sudoless siirtää käyttäjän ryhmään sudoless. Jotta voimme määrittää asetuksen, että kaikki sudoless rymään kuuluvat käyttäjät voivat käyttää sudoa ilman, että se kysyy aina salasanaa tulee muokkaus tehdä tiedostoon. Tänne lisäämme rivin %sudoless ALL = (ALL) NOPASSWD: ALL. Tämä mahdollistaa salasanattoman sudon käytön. Sitten sitä voi testata ottamalla ssh yhteyden luomaan käyttäjään ja suorittaa sudo komennon. 
Kysymys: Onko turvallista, että sudoa voi käyttää ilman salasanaa?

## Munroe 2006
Tämä sarjakuva/meemi on ytimekäs kuvaus sudon toimintaperiaatteesta. Aluksi henkilö pyytää toista muuttamaan hänet voileiväksi, mutta toinen kyseenalaistaa sen. Seuraavaksi hän lisää alkuun sudo, niin tällöin toinen puoli ei enään kysele vaan suorittaa. Tämä viittaa linuxissa sudoon, jonka avulla voidaan ajaa komentoja ylläpitäjän oikeuksin.
Yhteenvetona sudo avulla voidaan ajaa mitä vain.

## Karvinen 2026
Ansiblella pystyy sudon automatisoidan kokonaan ilman salasanaa ja tämän mahdollistaa SSH avain. Määritykset laitetaan hakemistopolkuun roles/antero/tasks/main.yml. Sinne tekstitiedostoon tulee määritykset ja sen lisäksi site.yml tiedostoon lisäys become: true. Kaikki nämä ja muut määritykset ovat elin tärkeitä. Myös oikeuksien määrittäminen ja niissä pitää tietää, mitä tekee, jotta ei anna vääriä oikeuksia. Niillä voi olla merkittäviä seuraamuksia.
Huomio: Oikeuksia määritellessä tulee tiedostaa tarkkaan mitä oikeuksia antaa ja toiminta logiikka on ymmärrettävä.

## Ansible dokumentaatio

### Ansible-doc copy 

Tarkoituksena on kopioda tiedostoja tai hakemistoja koneelta toiselle.

- content: Tiedoston sisältö
- dest: Lähde hakemisto
- src: Lähettäjän hakemisto
- owner: Tiedoston omistaja
- group: Ryhmät
- mode: Oikeudet

Malli:

name: Kopioidaan tiedoston konfiguraatio ja asetetaan oikeudet

Ansible.builtin.copy:

  src: files/app.ini
  
  dest: /opt/myapp/app.ini
  
  owner: Teppo
  
  group: worker
  
  mode: "0644"



### Ansible-doc apt

Hallinnoi paketteja apt-järjestelmän avulla.

- name: Paketin nimi
- state: Paketin sen hetkinen tila
- update_cache: Päivittää pakettivaraston

Malli:

name: Curl asennus ja pakettivaraston päivitys

ansible.builtin.apt:

  name: curl
  
  state: latest
  
  update_cache: yes



### Ansible-doc file

Tiedostojen ja hakemistojen hallinta

- path: Tiedoston tai hakemiston polku
- recurse: Oikeuksien rekursiivinen asettaminen
- src: Linkin lähde
- state: Tiedoston tila
- owner: Omistaja
- group: Ryhmä
- mode: Oikeudet

Malli:

name: Luodaan hakemisto lokitiedostoille

ansible.builtin.file:

  path: /var/log/customapp
  
  state: directory
  
  owner: aaro
  
  group: leaders
  
  mode: "0750"



### Ansible-doc user

Voi lisätä, muokata tai poistaa käyttäjiä.

- name: Käyttäjän nimi
- create_home: Tekee kotihakemiston
- comment: Käyttäjän kuvaus ja määritelmä
- groups: Ryhmät
- shell: Käyttäjän komentotulkki
- state: Käyttäjän tila
- system: Luo järjestelmäkäyttäjän

Malli:

name: Tehdään palvelukäyttäjä ilman kotihakemistoa

ansible.builtin.user:

  name: kayttaja1
  
  system: yes
  
  shell: /usr/sbin/nologin
  
  stete: present



### Ansible-doc authorized_key

Poistaa tai lisää käyttäjien julkisia SSH-avaimia.

- user: Käyttäjä, jonka avain-tiedostoa muokataan
- key: Itse julkinen SSH-avain

Malli:

name: Luodaan ylläpitäjän julkinen avain

ansible.posix.authorized_key:

  user: aaro
  
  state: present
  
  key: "{{ lookup('file', 'keys/admin_id_ed25519.pub') }}"
  

# a)
Aluksi loin uuden käyttäjän ansaar ja tämän jälkeen lisäsin sen ryhmiin sudoless, sudo ja adm. Sain myös tulostettua echo komenolla tekstiä ilman, että sudo kysyy salasanaa. Tämä tapahtui, kun olin ottanut ssh yhteyden ansaar käyttäjälle. Tämä onnistui koska käyttäjä lisätiin ryhmiin, jotka eivät vaadi sudoa. 
<img width="1004" height="564" alt="image" src="https://github.com/user-attachments/assets/0a18e99c-cf7d-4f55-9c3a-051a9131e2e9" />
<img width="1004" height="554" alt="image" src="https://github.com/user-attachments/assets/768c8426-f47f-4c50-b601-9eb664eb1eda" />
<img width="1004" height="416" alt="image" src="https://github.com/user-attachments/assets/e1f6ce58-7fd7-422e-b912-b6fd506d2b7a" />

# b)
Loin taas uuden käyttäjän anaaro, jolle annoin tismalleen samat oikeudet, kuin ansaar nimiselle käyttäjälle. Sain tehtyä tälle käyttäjälle salasanattoman ssh kirjautumisen tehtyä. Nyt pystyn käyttämään sudoa ilman jatkuvaa salasanan syöttöä.
<img width="1004" height="452" alt="image" src="https://github.com/user-attachments/assets/86dae7eb-6844-417e-908e-4fc02aa9c3d7" />
<img width="1004" height="329" alt="image" src="https://github.com/user-attachments/assets/e96fc18a-d761-4b26-8039-ed0c9e5827d6" />

# c)
Asensin kaksi pakettia. Toinen oli curl ja toinen htop. Alla on kuva, missä näkyy main.yml sisältö joka playbookkia ajaessa asentaa molemmat paketit. Paketit löysin Arch Linuxille tehdystä paketti galleriasta.

<img width="635" height="311" alt="image" src="https://github.com/user-attachments/assets/2b6da917-6c7c-46ff-94ef-d9b8bdd2dc77" />
<img width="1004" height="509" alt="image" src="https://github.com/user-attachments/assets/8bffd69a-c9fe-48d4-9244-a02152f60e32" />

# d)
Tässä loin tiedoston yhdelle käyttäjistä. Tämä ilmestyi playbook ajon jälkeen käyttäjän anaaro kotihakmistoon polkuun /home/anaaro/testi.txt. Kävin vielä varmistamassa asian ottamalla ssh yhteyden anaaro@localhostiin. Se piti käydä tarkistamassa sieltä, koska määritin oikeuksiksi 0600 eli vain omistajalla on luku- ja kirjoitusoikeudet. Oikeudet olisivat symbolisessa muodossa näin ”-rw-------.”
<img width="1004" height="413" alt="image" src="https://github.com/user-attachments/assets/b954a72d-1b47-4800-a38d-e3d92a876a11" />
<img width="1004" height="240" alt="image" src="https://github.com/user-attachments/assets/5923654b-73c7-4afb-a6ea-62772ed6550a" />

# e)
Testasin ”service”  käskyä. Sen avulla loin automaattisen SSH-palvelun käynnistymisen aina bootin yhteydessä.
<img width="592" height="248" alt="image" src="https://github.com/user-attachments/assets/607da9ae-dfe6-4574-8cad-42a229d41274" />
<img width="1004" height="164" alt="image" src="https://github.com/user-attachments/assets/ab493d71-1b2a-4ff0-9946-0b1ccad3a311" />

# Lähteet
- Ansible Community Documentation. Luettavissa: https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/index.html. Luettu: 7.4.2026
- Judd Vinet, Aaron Griffin & Levente Polyak 2002. Package Search. Luettavissa: https://archlinux.org/packages/. Luettu: 7.4.2026
- Karvinen, Tero 2026. Passwordless Sudo with Ansible. Luettavissa: https://terokarvinen.com/passwordless-sudo-with-ansible/. Luettu: 7.4.2026
- Karvinen, Tero 2026. Sudo without password. Luettavissa: https://terokarvinen.com/passwordless-sudo/. Luettu: 7.4.2026
