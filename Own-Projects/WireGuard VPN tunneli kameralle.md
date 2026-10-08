# WireGuard-VPN-tunneli kodin valvontakameralle (työn alla)

Projektin tarkoituksena on päästä turvallisesti katsomaan kodin valvontakameraa kotiverkon ulkopuolelta itse ylläpidetyn WireGuard-VPN:n kautta pilvipalvelun sijaan. Projekti on vielä työn alla.

## Tarkoitus

Useimmat kuluttajakamerat reitittävät videokuvansa valmistajan pilven kautta. Se on kätevää, mutta tarkoittaa, että kameran kuva kulkee palvelimien kautta, joita en hallitse. Haluan päinvastoin: kamera pysyy paikallisessa verkossa, ja yhdistän omaan verkkooni salatun tunnelin kautta vain silloin, kun tarvitsen sitä.

WireGuard on moderni ja kevyt VPN-protokolla. Se sopii hyvin Raspberry Pi:lle ja on mielenkiintoinen myös tietoturvan kannalta. Tavoite on, että kun olen poissa kotoa, puhelimeni yhdistää Pi:hin WireGuardilla, ja tunnelin sisältä pääsen kameraan kuin olisin kotona. Kameraa ei tarvitse avata suoraan internetiin, vaan ulos näkyy vain yksi salattu palvelu.

## Suunnitelma ja osat
- Kamera: Tapo C100, joka on liitetty RTSP-videovirran kautta. RTSP:n avulla yhteensopiva sovellus voi katsoa kameraa paikallisesti ilman valmistajan pilveä.
- VPN-palvelin: WireGuard Raspberry Pi 4:llä, asennettuna PiVPN:llä, joka helpottaa WireGuardin asiakkaiden luomista ja hallintaa.
- Dynaaminen DNS: DuckDNS antaa kotiyhteydelle pysyvän nimen, vaikka operaattorin julkinen IP-osoite voi vaihtua.
- Porttiohjaus: reitittimen pitää ohjata VPN:n UDP-portti Pi:lle, jotta internetistä tulevat yhteydet pääsevät perille.

WireGuard on asennettu PiVPN:llä ja DuckDNS on käytössä. Ongelmaksi on osoittautunut yhteyden saaminen toimimaan ulkoa kotiverkkoon. Epäilen kahta mahdollista syytä:

Mesh-reitittimen porttiohjaus. Verkkoni oli alun perin rakennettu TP-Link Deco -mesh-järjestelmän varaan, jossa porttiohjaus ei välttämättä toimita liikennettä Pi:lle luotettavasti.
Operaattorin toiminta. Jotkin operaattorit rajoittavat saapuvaa UDP-liikennettä ja WireGuard perustuu UDP:hen.

Olen vaihtanut operaattorin päätelaitteen omaan reitittimeeni, jotta kotiverkon asetukset ovat omassa hallinnassani. Seuraavana vuorossa on vianmääritys kerros kerrallaan, kunnes yhteys toimii ulkoa.

## Mitä projekti on opettanut tähän mennessä
- Kerroksittainen vianmääritys. VPN-ongelma voi olla asiakkaassa, palvelimessa, DNS:ssä, reitittimessä tai operaattorilla. Yksi kerros kerrallaan testaaminen on ainoa luotettava tapa.
- Tietoturva suunnittelussa. Yhden hyvin tunnetun, salatun palvelun avaaminen on turvallisempaa kuin kameran avaaminen suoraan internetiin.
- Oman verkon tunteminen. NAT:n, porttiohjauksen ja UDP:n käyttäytymisen ymmärtäminen on tämän projektin keskeinen taito.

## Tila
Työn alla. Tarkoitus ja toteutustapa on suunniteltu, osat on asennettu ja ulkoinen yhteys on vielä selvitettävänä.
