# h5 Gitar Hero

## x)
#### Pro Git, 2ed & 1.3 Getting Started - What is Git?
- Gitin toiminta perustuu siihen, että se talentaa dataa snapshotteina. Teoriassa siis tämä tarkoittaa, että Git ottaa aina commitin yhteydessä kuvan  tiedostoista.
- Yksi Gitille ominaispiirteitä on, että lähes jokainen toiminta on paikallista. Se tarkoittaa, että Git vaatii toimiakseen vain paikalliset tiedostot toimiakseen eli verkkoyhteyttä ei vaadita. Tämä toimii, koska koko historia on omalla koneella.
- Toinen Gitille tyypillinen piirre on eheys eli kaikki muutokset ovat Gitin huomattavissa ja turvattu, niin ettei mitään voi muuttua huomaamatta.
- Lisäksi kolmas tyypillenen ominaisuus on, että yleisesti Git lisää vain dataa. Eli toimintaperiaate perusttuu siihen, että toiminnot mahdollistavat jatkuvan tiedon lisäämisen.
- Gitin kolme tilaa
  1. Modified: tässä muutoksia tehdään ja niitä ei ole vielä commitattu
  2. Staged: tässä muutokset ovat lisätty seuraavaa committia varten
  3. Commited: tässä data on jo tallentunut paikallisesti toimivaan tietokantaan
- Kysymys: Millaisia ongelmia Gitin kanssa tulee tuotantoympäristössä tyypillisesti ja ovatko ne suuria?


#### Termit
- git add --all; lisää Gittiinn kaikki muutokset, jotka voidaan myöhemmin committaa ja sitten puskea.
- git commit; tallentaa kaikki git add --all komennon muutokset tietokantaan.
- git pull; vetää ulos muiden repositoryn käyttäjien tekemät muutokset, joita he ovat jo puskeneet läpi.
- git push; puskee kaikki commitatut muutokset repositoryyn, josta ne voi seuraava vetää pull komennolla itselle tai jos kukaan muu ei ole repositoryssä, niin tällöin muutokset tulevatvain omaan Gittiin näkyviin itselleen.
- &&; avulla voidaan yhdistää komento, jolloin se suorittaa ne molemmat.
- Kysymys: Onko muita tapoja yhdistää komentoja kuin tämä && ?

## a) Online
Aloitin valitsemalla GitHubin oikeasta yläkulmasta ”New repository”
<img width="1004" height="217" alt="image" src="https://github.com/user-attachments/assets/5ad1e476-1e79-4190-b673-b6c3d56aecf4" />


Seuraavaksi avautuvassa näkymässä päästään syöttämään repositorylle nimi, kuvaus ja muut olennaiset konfiguraatiot. Annoin repositorylleni nimeksi ”Sunshine-exercise”. Descriptioniksi annoin ” This exercise is even flashier than sunshine.”. Konfiguraatioihin määritin repositoryn julkiseksi eli kuka vain voi katsoa sitä, mutta vain minulla on commit oikeudet. Näitä commit-oikeuksia voi lisätä myöhemmin, mikäli niin tarvitsee tehdä. Lisäsin README tiedoston oletuksena mukaan. Sitä voidaan käyttöö suuremmissa projekteissa projektin kuvaukseen ja se luo selkeän pohjan repositorysta. ”Add .gitignore” kohtaan en tehnyt muutoksia ja jätin sen kohtaan”No .gitignore”. Lisenssiksi valitsin ”GNU General Public License v3.0”. Tämä lisenssi varmistaa, että projektini pysyy avoimena ja suojaa patenttiongelmilta. Tämä lisenssi on tunnettu ja laajasti monissa tapauksissa käytössä. Lopuksi painoin ”Create repositorya”
<img width="774" height="678" alt="image" src="https://github.com/user-attachments/assets/7ab1c67d-cdb8-4925-b112-3941b7fa7541" />


Näin voimme todeta, että meillä on luomamme repository toiminnassa.
<img width="1004" height="726" alt="image" src="https://github.com/user-attachments/assets/a6314ced-a46b-48a6-ba75-0e3bada7464e" />


## b) Dolly
Jotta voimme suorittaa virtuaalikoneeltamme komentoja suoraan repositoryyn, niin täytyy kloonata GitHub repository koneellemme. Teemme sen SSH-avaimen avulla. Tämä on turvallinen ja yksinkertainen tapa. 
Valitsemme vihreästä ”Code” napista nuolen alaspäin, josta avautuu valikko ”Local”, josta valitsemme ”SSH” kohdan. Minulla oli entuudestaan jo lisättynä virtuaalikoneeni julkinen SSH-avain, mutta jos sitä ei olisi, niin se tulisi etsiä koneelta. Sen löytää komentoriviltä komennolla cd .ssh ja sieltä löytyy id_ed25519.pub tiedosto, joka sisältää avaimen ja tämän liität GitHubiin.
<img width="1004" height="738" alt="image" src="https://github.com/user-attachments/assets/d14c2afb-9fee-4629-a353-b6139170ea40" />


Nyt voimme komento riviltä kloonata repositoryn komennolla git clone git@github.com:aarohinkkanen/Sunshine-exercise.git
<img width="1004" height="270" alt="image" src="https://github.com/user-attachments/assets/b39d7756-fa8a-4687-a70e-8a407f9f7e73" />


Nyt pystymme suorittamaan komentoja joilla voimme esimerkiksi vetää, puskea ja luoda tiedostoja. 
Kloonasin repositoryn kotihakemistooni, mutta siirsin sen code nimiseen kansioon, jotta hallitseminen olisi helpompaa ja selkeämpää. Tein tämän siirron komennolla mv Sunshine-exercise code .
<img width="1004" height="257" alt="image" src="https://github.com/user-attachments/assets/4542cba4-e9b5-47b4-8175-58030690e5e5" />


Nyt kun repository on haluamassani kansiossa voin alkaa tekemään muutoksia repositoryyn ja puskea niitä julki. Kun tiedän, että repositoryssani ei ole muita minun ei tarvitse käyttää git pull komentoa, joka vetäisi tehdyt muutokset. Tilanteessa, jossa muut tekisivät myös muutoksia niin se olisi ehdottoman tärkeää.
Loin hakemistoon /code/Sunshine-exercise/ tiedoston nimeltä testi.txt.
<img width="1004" height="336" alt="image" src="https://github.com/user-attachments/assets/62ed5aaa-97ee-421e-8ad6-38f81490e771" />


Seuraavaksi komennolla git add --all lisään nämä muutokset GitHubiin. Sen jälkeen suoritan komennon git commit, joka tallentaa projektin Githubiin ja tässä kohtaa pääsee tekemään viestin tehdyistä muutoksista. Viimeiseksi komennolla git push pusken muutokset läpi niin, että ne tulevat näkyviin verkkoon kaikille.
<img width="1004" height="462" alt="image" src="https://github.com/user-attachments/assets/cd930b64-47c2-437f-a0dc-57f5c8d78b65" />


Nyt kun kaikki menivät läpi muutokset tulisi näkyä myös itse GitHubissa.
<img width="848" height="201" alt="image" src="https://github.com/user-attachments/assets/021ce0ae-8faf-4c78-a71d-0b2599ff92f1" />


Myös muutoksia ja lokeja voi tarkastella komentoriviltä komennolla git log --patch. 
Vastaavia tiedostoja voisi tehdä samalla kaavalla repositoryyn monia.
<img width="599" height="422" alt="image" src="https://github.com/user-attachments/assets/d53301a8-1dfb-4b48-9890-a3864b292be2" />


## c) Doh!
Tässä tein harjoitus mielessä turha.txt tekstitiedoston, joka sisälsi tekstiä. Ajoin komennon git add --all, mutta en ikinä git commit komentoa. Kun ajoin sitten lisäyksen jälkeen komennon git reset --hard niin se poisi turha.txt, jota ei ikinä commitattu GitHubiin. 
<img width="1004" height="281" alt="image" src="https://github.com/user-attachments/assets/c37cdcd1-20e1-43ec-870b-9e6979e255e0" />


## d) Tukki
Repositoryn lokeja voi tarkastella helposti komennolla git log --patch . Siinä näkee selkeästi eri tietoja. Jokainen commit tulee näkyviin lokeihin ja tiedot päivittyvät aina niiden mukaisiksi, mitä muutokset sisältävät. Alla eroteltu lokistani malliksi.

-	Siinä näkee tekijän, joka tässä tapauksessa olin minä itse eli Aaro Hinkkanen aaro.hinkkanen@gmail.com. 
-	Päiväyksen näkee: torstai 23.4.2026 klo 21:27:58 +0300
-	Viestin, jonka kirjoitin muutoksen kuvaukseksi eli nyt ”First changes for this repo!”
-	Mitä konkreettisesti muutokset sisältävät. Tässä tapauksessa seitsemän riviä samaa tekstiä TESTI!!!


<img width="1004" height="1159" alt="image" src="https://github.com/user-attachments/assets/ea9f6987-9117-4540-bd96-c0127bdc0340" />


En osannut sanoa, miksi osa commiteista tapahtui koulutehtäviin tarkoitetulla tilillä ja osa omalta tililtä. Muokkasin kuitenkin tähän repositoryyn tulevat muutokset tulevan koulutehtäviin tarkoitetulta tililtä. Alla näkyy miten tein muutoksen.
<img width="1004" height="142" alt="image" src="https://github.com/user-attachments/assets/d332a557-b712-4866-84a7-d5e56c765a86" />


Tein muutoksia (uuden tiedoston nimeltä testi2.txt) ja tarkastin tuliko sähköposti oikeaksi ja kyllä tuli. Alla näkyy muutokset.
<img width="1004" height="429" alt="image" src="https://github.com/user-attachments/assets/aef77dfc-b05f-4b86-9440-5c53ba71c438" />
<img width="1004" height="295" alt="image" src="https://github.com/user-attachments/assets/0944c3cc-7c59-4484-a3a5-df81ce9bf07e" />


## e) Gitanbile
Tässä kohdassa siirsin ansible kansion kotihakemistosta minun Sunshine-exercise kansioon, joka on kloonattu Githubiin. Tämän jälkeen ajoin komennot git add --all , git commit , ja git push. Sitten ansible kansio siirtyi versionhallintaani. 
<img width="880" height="198" alt="image" src="https://github.com/user-attachments/assets/ee59d819-c0bf-4c5e-8adc-653b33151184" />


Tämän jälkeen siirsin site.yml tiedoston ansible kansioon ja saman tein roles kansiolle. Sitten tein rooleihin uuden käyttäjän nimeltä ansible. Sille loin tasks kansion, johon kirjoitin oman main.yml tiedoston, joka oli tarkoitus ajaa playbookin avulla. Lisäsin vielä käyttäjän ansible site.yml tiedostoon ja ajoin playbookin lopulta. 
<img width="1004" height="269" alt="image" src="https://github.com/user-attachments/assets/3686280b-d1d0-4b1e-aa35-e4bf3c082b36" />


Playbookin ajo onnistui ja sen jälkeen suoritin terminaalissa komennot git add roles/ansible/tasks, koska muuten se olisi listannut koko roolit, jotka olen määrittänyt. Sen jälkeen ajoin komennon git commit ja git push. Tämän jälkeen kävin päivittämässä Githubini ja sinen oli ilmestynyt playbookin ajama roles/ansible/tasks ja sen sisällä oleva main.yml tiedosto. 
<img width="1004" height="214" alt="image" src="https://github.com/user-attachments/assets/ecf1398f-3ef3-44d3-a683-6924856fa820" />
<img width="1004" height="328" alt="image" src="https://github.com/user-attachments/assets/7ed7b56d-b337-4226-815e-2c7da7ead3eb" />


## f) 
Pari hankittu!


## Lähteet
- Chacon, S. Straub, B. 2014. Pro Git 2nd Edition. Apross. New York City. Luku 1.3. Luettavissa: https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F. Luettu: 23.4.2026.





















