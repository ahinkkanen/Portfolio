# Hermes: paikallisesti ajettava tekoälyagentti

Hermes on tekoälyagentti, jonka olen asentanut omalle työpöytäkoneelleni. Sen käyttämä kielimalli pyörii paikallisesti LM Studion kautta, joten tekoäly toimii kokonaan omalla laitteistollani ilman ulkopuolista pilvipalvelua.

## Johdanto

Halusin ymmärtää, miten tekoälyagentti toimii käytännössä ja kokeilla, millaista on ajaa kielimallia omalla koneella. Useimmat tekoälypalvelut toimivat pilvessä verkon yli, jolloin kaikki syötteeni kulkevat palveluntarjoajan palvelimien kautta. Paikallisessa ratkaisussa data pysyy omalla koneellani, ja käyttökustannuksia ei synny. Tämä sopii hyvin yksityisyyttä painottavaan kotilaboratorio ekosysteemiin

<img width="1684" height="989" alt="image" src="https://github.com/user-attachments/assets/7d1b48a2-30e1-4f8a-8e68-a806a5602fc7" />

## Toteutus
Alusta: Bazzite-Linux-työpöytäkoneeni, jossa agentti on asennettu.
Kielimalli: hermes-2-pro-mistral-7b, jota ajetaan LM Studiolla. LM Studio huolehtii mallin lataamisesta ja ajamisesta paikallisesti ja agentti käyttää sitä omana "aivonaan".
Paikallisuus: mikään ei vaadi ulkoista tekoälypalvelua, joten päättely tapahtuu kokonaan omalla koneella.

<img width="1635" height="1020" alt="image" src="https://github.com/user-attachments/assets/ae866b5f-e9ed-4ce9-8d17-f9627e101e41" />

## Mitä opin
- Kielimallin asentaminen ja ajaminen omalla koneella
- Mallien valinta ja ajaminen paikallisesti ja se miten oma laitteisto rajaa sitä, millaisia malleja voi käyttää
- Tekoälyagentin ja sen käyttämän kielimallin erottaminen toisistaan: agentti on ohjelma, malli on sen käyttämä osa
- Paikallisen ratkaisun hyödyt (yksityisyys, hallinta) ja kompromissit (laitteiston rajat)

## Tila

Hermes on asennettu työpöytäkoneelle ja hermes-2-pro-mistral-7b kielimalli pyörii LM Studiossa. Projekti on kokeiluvaiheessa ja kehitän sitä opintojen ja oman oppimisen mukana.
