# h6

## Tekijät Aaro Hinkkanen ja Minttu Hillebrandt

##

Projektin tarkoitus on luoda automatisoitu järjestelmän tilanvalvonta ohjelma, joka tarkastaa paikallisen tietokoneen eri osien kuormitusta. Automatisointi tehdään Ansiblen avulla. Lopputuloksena paikalliselle tietokoneelle on asentunut paketteja ja skriptejä joiden avulla pystytään komentoriviltä tarkastamaan jatkuvasti koneen kuormitus tasoja.

## Kokonaisuuden hahmotelma
Alla näkyvässä kuvassa on hakemistopuu rakenne, joka kuvaa projetkin sisällön.
<img width="1004" height="671" alt="Hakemistopuu terminaalissa." src="https://github.com/user-attachments/assets/1a991763-455f-441e-a9d1-b023b8857498" />

## Ohjeistus
Luodaan hakemisto rakenne "monitoring" Mini-project nimisen kansion sisään
````
mkdir monitoring
cd monitoring/
mkdir files
mkdir handlers
mkdir tasks
cd ~/code/Mini-project/monitoring/files/
micro collect.sh
micro dashboard.sh
micro alert.sh
cd ~/code/Mini-project/monitoring/handlers/
micro main.yml
cd ~/code/Mini-project/monitoring/tasks/
micro main.yml
````

Luodaan Mini-project nimiseen kansioon tiedosto nimeltä inventory
````
micro inventory
````

Luodaan Mini-project nimiseen kansioon site.yml
````
micro site.yml
````

## Tiedostojen sisällöt
### files kansion sisältämät skripti tiedostojen sisällöt
##
````
collect.sh
````
<img width="1747" height="614" alt="collect.sh koodi." src="https://github.com/user-attachments/assets/e307375d-6d45-4a0c-af1c-a5d3fccad25d" />

##
````
dashboard.sh
````
<img width="1239" height="662" alt="dashboard.sh koodi." src="https://github.com/user-attachments/assets/b21bce8f-7320-40a5-a36a-4e63a8d1f1c1" />

##
````
alert.sh
````
<img width="1894" height="1046" alt="alert.sh koodi." src="https://github.com/user-attachments/assets/7248c6a0-5664-4461-9ec8-942fc9e1426e" />

### tasks kansion sisältö
````
main.yml
````
<img width="786" height="1149" alt="tasks kansion sisältö
main.yml koodi." src="https://github.com/user-attachments/assets/e4a83f96-ed6d-45d9-b306-230b13d2f254" />

### handlers kansion sisältö
````
main.yml
````
<img width="399" height="140" alt="handlers kansion sisältö
main.yml koodi." src="https://github.com/user-attachments/assets/700a556f-2e80-4ff0-a99a-e18c827afa21" />

##
### Mini-project kansiossa olevien tiedostojen sisällöt
````
inventory
````
<img width="603" height="50" alt="inventory tiedosto koodi." src="https://github.com/user-attachments/assets/d20e7035-b725-4b0a-a9e5-e824aa120d9c" />

##
````
site.yml
````
<img width="722" height="205" alt="site.yml tiedosto koodi." src="https://github.com/user-attachments/assets/6ef4e4a1-af53-44df-955b-7fa8cf85a1ac" />


## Testit ja playbook ajot
````
Playbook ajo saatiin onnitumaan ja muutokset näkyvät kohdassa "changed"
````
<img width="1004" height="683" alt="Terminaalin playbookajo." src="https://github.com/user-attachments/assets/78c6e41e-c49e-4335-bef0-d0485cee09ad" />

##
````
Playbook ajettiin vielä kerran, jotta saatiin idempotentti aikaiseksi
````
<img width="1004" height="604" alt="Terminaalin playbookajo, idempotentti tila." src="https://github.com/user-attachments/assets/39b5a5bc-97a6-411d-ac1e-fb7e41670a52" />

##
````
Kun playbook ajo onnistuu testasimme terminaalissa avata skriptin kirjoittamalla komentoriville /usr/local/bin/dashboard.sh
````
<img width="1568" height="327" alt="Terminaalista kuva kun /usr/local/bin/dashboard.sh komentoa ei löytynyt." src="https://github.com/user-attachments/assets/fe35fd5a-128c-4bbb-8a1c-0b17fc012e56" />

##


> dashboard.sh ei tuottanut sellaista tulosta kuin olisimme halunneet (kuva alhaalla). Aloimme selvittämään mistä virhe johtuu ja huomasimme virheen olevan skirpti tiedostossa, josta puuttui päättävä lainausmerkki ("). 

<img width="1041" height="150" alt="Terminaalista kuva kun /usr/local/bin/dashboard.sh ei tulostanut mitään, koska koodista oli unohtunut yksi merkki." src="https://github.com/user-attachments/assets/ac2b5d78-a82b-4b21-903f-c12ca6113d9d" />

##
````
Ajoimme komentorivillä uudestaan /usr/local/bin/dashboard.sh ja tulos oli sellainen, mitä halusimmekin.
````
<img width="1004" height="507" alt="Terminaalissa SYSTEM MONITORING laatikko." src="https://github.com/user-attachments/assets/8cdf0214-45f4-4d35-9b56-21d53dd8791d" />

## Koneen prosessorin rasittaminen varoitusta varten alla olevalla komennolla
````
yes /dev/null &
````
<img width="1004" height="153" alt="yes /dev/null & komennolla rasitusta." src="https://github.com/user-attachments/assets/5df9ca8c-ad3f-4ea5-b95e-351044914bdb" />

##

> Komento lisäsi prosessorin kuormitusta merkittävästi ja alert.sh suorittaminen osoitti, että varoitus toimi kun se ylitti raja-arvon.
<img width="1004" height="574" alt="Rasituksen vaikutukset sekä varoitus." src="https://github.com/user-attachments/assets/3c21fa86-7e26-4bdb-8062-689a7051b5d2" />

##

## Yhteenveto
Projektina loimme automatisoitavan valvonta järjestelmän, joka tarkastaa paikkallisen koneen kuormituksen jokaisen minuutin välein. Projektin toisena tärkeänä sivuosana oli oppia versionhallinnan käyttöä ryhmässä. Gitin käyttö sujui meidän välillä erinomaisesti. Meidän välinen viestintä oli erinomaista ja työnjako meni tasan. Vaikka komentorivi kuvissa näkyy Aaron virtuaalikone, molemmat meistä antoivat yhtä suuren työpanoksen projektiin. Olimme jatkuvasti Discordin kautta puhelussa, jossa pohdimme ongelmakohtia yhdessä.

##
<img width="558" height="216" alt="Discord-puhelusta kuva." src="https://github.com/user-attachments/assets/2fa14027-6090-4787-9637-fa36a7c14b21" />


##

## Linkki YouTube Demo-videoon: https://www.youtube.com/watch?v=4JByZLupOuM

## Lähteet: 

- https://terokarvinen.com/palvelinten-hallinta/#h6-miniprojekti 
- https://www.linuxoperatingsystem.net/yes-command-line-in-linux-a-comprehensive-guide/
- https://dohost.us/index.php/2025/08/15/automating-tasks-on-debian-with-cron-and-systemd-timers/#:~:text=This%20guide%20provides%20a%20comprehensive%2C%20step-by-step%20tutorial%20on,and%20systemd%20timers%20for%20task%20automation%20on%20Debian.
- https://phoenixnap.com/kb/linux-date-command
