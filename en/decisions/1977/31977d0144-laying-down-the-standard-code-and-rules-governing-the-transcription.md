---
title: "77/144/EEC: Commission Decision of 22 December 1976 laying down the standard code and rules governing the transcription into a machine-readable form of the data of the surveys of plantations of certain species of fruit trees, and laying down the boundaries of the production areas for these surveys"
identifier: "31977D0144"
eli: "http://data.europa.eu/eli/dec/1977/144/oj"
type: decision
subtype: addressed
jurisdiction: eu
language: en
date: 1976-12-22
entry_into_force: 1977-09-27
last_amended: 1996-11-26
consolidated_version: "01977D0144-19961126"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01977D0144-19961126"
retrieved: 2026-10-11
---

# 77/144/EEC: Commission Decision of 22 December 1976 laying down the standard code and rules governing the transcription into a machine-readable form of the data of the surveys of plantations of certain species of fruit trees, and laying down the boundaries of the production areas for these surveys

1977D0144 — EN — 26.11.1996 — 007.001

This document is meant purely as a documentation tool and the institutions do not assume any liability for its contents

COMMISSION DECISION

of 22 December 1976

laying down the standard code and rules governing the transcription into a machine-readable form of the data of the surveys of plantations of certain species of fruit trees, and laying down the boundaries of the production areas for these surveys

(77/144/EEC)

(OJ L 047, 18.2.1977, p.52)

Amended by:

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td> M1</td><td>Commission Decision of 7 May 1981</td><td> L 167</td><td>12</td><td>24.6.1981</td></tr>
<tr><td> M2</td><td>Commission Decision of 13 December 1985</td><td> L 373</td><td>59</td><td>31.12.1985</td></tr>
<tr><td> M3</td><td>Commission Decision of 16 March 1987</td><td> L 94</td><td>32</td><td>8.4.1987</td></tr>
<tr><td></td><td>Commission Decision of 18 November 1991</td><td> L 333</td><td>23</td><td>4.12.1991</td></tr>
<tr><td></td><td>Commission Decision of 29 November 1995</td><td> L 302</td><td>37</td><td>15.12.1995</td></tr>
<tr><td></td><td>Commission Decision of 25 November 1996</td><td> L 318</td><td>14</td><td>7.12.1996</td></tr>
</table>

COMMISSION DECISION

of 22 December 1976

laying down the standard code and rules governing the transcription into a machine-readable form of the data of the surveys of plantations of certain species of fruit trees, and laying down the boundaries of the production areas for these surveys

(77/144/EEC)

THE COMMISSION OF THE EUROPEAN COMMUNITIES,

Having regard to the Treaty establishing the European Economic Community,

Having regard to Council Directive 76/625/EEC of 20 July 1976 concerning the statistical surveys to be carried out by the Member States in order to determine the production potential of plantations of certain species of fruit trees, and in particular Article 4 (2) and (4) thereof,

Whereas the equipment which the Commission has available for analyzing the results of the surveys of plantations of certain species of fruit trees and the need for its rational use require that the machine-readable forms compatible with the equipment be specified and that a standard format be prescribed for the transcription of the data into a machine-readable form;

Whereas within certain production areas homogeneous climatic and agronomic conditions exist which are associated with more or less uniform yields of fruit per hectare; whereas the use of survey results for each production area improves the accuracy of medium-term estimates of production; whereas the boundaries of such production areas shall be fixed;

Whereas the measures provided for in this Decision are in accordance with the opinion of the Standing Committee for Agricultural Statistics,

HAS ADOPTED THIS DECISION:

## Article 1

The machine-readable forms for submission of the data provided for in Article 2 of Directive 76/625/EEC by those Member States which process their survey information electronically shall be either magnetic tape or 80-column punch cards.

## Article 2

The standard format, codes and rules governing transcription on to magnetic tape or 80-column punch cards of the data provided for in Article 2 of Directive 76/625/EEC and the administrative procedure governing the transmission of the magnetic tape files to the SOEC shall be as set out in the Annexes hereto.

## Article 3

The boundaries of the production areas to be adopted shall be as set out in the Annexes hereto.

## Article 4

This Decision is addressed to the Member States.

## ANNEX I

Tape specification for the delivery to the SOEC of the results of the statistical surveys of plantations of certain species of fruit trees to be carried out in Member States

(Directive 76/625/EEC)

GENERAL PROVISIONS

I. The information recorded in accordance with the characteristics referred to in Article 2 of Directive 76/625/EEC is to be delivered to the SOEC in the following form by those Member States which process their survey information electronically:

1\. On nine-track magnetic tape 1600 BPI (630 bytes/cm) IBM standard label or no label.

2\. The information shall refer to summaries of holdings if the survey is exhaustive (or to raised summaries of holdings if the survey is based on random sampling), and not to individual holdings.

3\. The information shall be of fixed record length and shall be recorded in the following FORTRAN format:

I2, I2, I2, I3, I1, 6F7.0 (beginning in position 1).

4\. The first five fields of each record shall contain information to permit identification (country, production area, variety and density class). The codes for these fields are specified in the detailed provisions and in Annex II. The following six fields, each of seven digits, shall contain the information about the area in ares within each of the six age classes of the record. The age classes are defined in the detailed provisions. The information shall be entered right justified in each field.

5\. Member States shall have a choice as to blocking factor; the SOEC must be told which blocking factor has been used.

6\. Member States shall specify on the documents accompanying the transmission the number of species and the number of varieties within each species.

7\. The records shall be sorted according to species, variety, area or territory and density of plantation.

II. The following pages give for the various items of a record:

(a) the codes which are to be used;

(b) the number of digits required for the item of question;

(c) the consecutive numbering of the positions for the various items.

DETAILED PROVISIONS

<table>
<tbody><tr><td>  </td><td>  </td><td>Code</td><td>Digits</td><td>Byte number on tape</td></tr>
<tr><td colspan="2"> 1. Country </td><td>  </td><td>2</td><td>1,2</td></tr>
<tr><td colspan="2">Germany</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">France</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Italy</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Netherlands</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Belgium</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Luxembourg</td><td>06</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">United Kingdom</td><td>07</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Ireland</td><td>08</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Denmark</td><td>09</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Greece</td><td>10</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Spain</td><td>11</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Portugal</td><td>12</td><td>  </td><td>  </td></tr>
<tr><td colspan="5"></td></tr>
<tr><td colspan="2">Austria</td><td>13</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Finland</td><td>14</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Sweden</td><td>15</td><td>  </td><td>  </td></tr>
<tr><td colspan="5"></td></tr>
<tr><td colspan="2"> 2. Production area </td><td>  </td><td>2</td><td>3,4</td></tr>
<tr><td colspan="2">Germany</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Norden</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Mitte</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Süden</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Ost</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">France</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Sud-ouest</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Sud-est</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Loire</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Reste</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Italy</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Apples, pears)</td></tr>
<tr><td colspan="2">Val Padana</td><td>11</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Trentino-Alto Adige</td><td>21</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Piemonte and Valle d'Aosta</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Centrale</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Meridionale</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Peaches and apricots)</td></tr>
<tr><td colspan="2">Val Padana and Trentino-Alto Adige</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Piemonte and Valle d'Aosta</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Centrale</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Meridionale</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Oranges, lemons and small-fruited citrus)</td></tr>
<tr><td colspan="2">Sicilia</td><td>14</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Calabria</td><td>24</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Puglia and Basilicata</td><td>34</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Altre zone</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Netherlands</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Belgium</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Luxembourg</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">United Kingdom</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Ireland</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Denmark</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="5"></td></tr>
<tr><td colspan="2">Austria</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Finland</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Sweden</td><td>00</td><td>  </td><td>  </td></tr>
<tr><td colspan="5"></td></tr>
<tr><td colspan="2">Greece</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Apples)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Macedonia</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Thessaly</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>96</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Pears)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Macedonia</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Thessaly</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Crete</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>97</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Peaches)</td></tr>
<tr><td colspan="2">Macedonia</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Thessaly</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>92</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Apricots)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Macedonia</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>95</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Oranges)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Crete</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Epirus</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>99</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Lemons)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Central Greece and Euboea</td><td>06</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>94</td><td>  </td><td>  </td></tr>
<tr><td colspan="5">(Small-fruited citrus)</td></tr>
<tr><td colspan="2">Peloponnesus</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Crete</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Aegean Islands</td><td>07</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Other areas</td><td>93</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Spain</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Galicia</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Principado de Asturias</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Cantabria</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">País Vasco</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Navarra</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">La Rioja</td><td>06</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Aragón</td><td>07</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Cataluña</td><td>08</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Baleares</td><td>09</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Castilla y León</td><td>10</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Madrid</td><td>11</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Castilla-La Mancha</td><td>12</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Comunidad Valenciana</td><td>13</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Región de Murcia</td><td>14</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Extremadura</td><td>15</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Andalucía</td><td>16</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Canarias</td><td>17</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Portugal</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Norte</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Centro</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Lisboa and Vale do Tejo</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Alentejo</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Algarve</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Região Autónoma dos Açores</td><td>06</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Região Autónoma da Madeira</td><td>07</td><td>  </td><td>  </td></tr>
<tr><td colspan="2"> 3. Species </td><td>  </td><td>2</td><td>5-6</td></tr>
<tr><td rowspan="2">Apples:</td><td>dessert</td><td>01</td><td>  </td><td>  </td></tr>
<tr><td>others</td><td>02</td><td>  </td><td>  </td></tr>
<tr><td rowspan="2">Pears:</td><td>dessert</td><td>03</td><td>  </td><td>  </td></tr>
<tr><td>others</td><td>04</td><td>  </td><td>  </td></tr>
<tr><td rowspan="3">Peaches:</td><td>white flesh</td><td>05</td><td>  </td><td>  </td></tr>
<tr><td>yellow flesh</td><td>06</td><td>  </td><td>  </td></tr>
<tr><td>colour not specified</td><td>07</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Apricots</td><td>08</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Oranges</td><td>09</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Lemons</td><td>10</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Small-fruited citrus</td><td>11</td><td>  </td><td>  </td></tr>
<tr><td colspan="2"> 4. Variety </td><td>  </td><td>3</td><td>7-9</td></tr>
<tr><td colspan="2">Codes for specified varieties of each species are given in Annex II.</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2"> 5. Density of plantation  (Trees per hectare) </td><td>  </td><td>1</td><td>10</td></tr>
<tr><td colspan="2">Apples and pears:</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Under 400</td><td>1</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">400 - 799</td><td>2</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">800 - 1 599</td><td>3</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">1 600 and over</td><td>4</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Total</td><td>9</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Peaches and apricots:</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Under 300</td><td>1</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">300 - 399</td><td>2</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">400 - 599</td><td>3</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">600 - 799</td><td>4</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">800 and over</td><td>5</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Total</td><td>9</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Oranges, lemons and small-fruited citrus:</td><td>  </td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Under 250</td><td>1</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">250 - 374</td><td>2</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">375 - 499</td><td>3</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">500 - 624</td><td>4</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">625 - 749</td><td>5</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">750 and over</td><td>6</td><td>  </td><td>  </td></tr>
<tr><td colspan="2">Total</td><td>9</td><td>  </td><td>  </td></tr>
<tr><td colspan="5"> 6. Age of trees (1) </td></tr>
<tr><td rowspan="6">Age class</td><td>1</td><td>  </td><td>7</td><td>11-17</td></tr>
<tr><td>2</td><td>  </td><td>7</td><td>18-24</td></tr>
<tr><td>3</td><td>  </td><td>7</td><td>25-31</td></tr>
<tr><td>4</td><td>  </td><td>7</td><td>32-38</td></tr>
<tr><td>5</td><td>  </td><td>7</td><td>39-45</td></tr>
<tr><td>6</td><td>  </td><td>7</td><td>46-52</td></tr>
<tr><td colspan="5"> (1) The area for each age class is given in ares. </td></tr>
</tbody>
</table>

Age classes are defined as follows:

<table>
<tbody><tr><td colspan="4">(years)</td></tr>
<tr><td>  </td><td>Apples and pears</td><td>Peaches and apricots</td><td>Oranges, lemons and small-fruited citrus</td></tr>
<tr><td>1</td><td>0- 4</td><td>0- 4</td><td>0- 4</td></tr>
<tr><td>2</td><td>5- 9</td><td>5- 9</td><td>5- 9</td></tr>
<tr><td>3</td><td>10-14</td><td>10-14</td><td>10-14</td></tr>
<tr><td>4</td><td>15-24</td><td>15-19</td><td>15-24</td></tr>
<tr><td>5</td><td>25 and over</td><td>20 and over</td><td>25-39</td></tr>
<tr><td>6 (1)</td><td>—</td><td>—</td><td>40 and over</td></tr>
<tr><td colspan="4"> (1) In the case of apples, pears, peaches and apricots, the information for class 6 is seven zeros. </td></tr>
</tbody>
</table>

## ANNEX II

Codes for specified varieties of each species for delivery to the Statistic Office of the European Communities of the results of the statistical surveys of plantations of certain species of fruit trees to be carried out in Member States

(Directive 76/625/EEC)

<table>
<tbody><tr><td>Varieties</td><td>Code</td></tr>
<tr><td colspan="2"> 1. Apple trees </td></tr>
<tr><td colspan="2">Apple trees giving dessert apples</td></tr>
<tr><td>Cardinal</td><td>001</td></tr>
<tr><td>Discovery</td><td>002</td></tr>
<tr><td>Gravenstein/Gråsten</td><td>003</td></tr>
<tr><td>James Grieve</td><td>005</td></tr>
<tr><td>Worcester Pearmain</td><td>006</td></tr>
<tr><td>Reine des Reinettes/Goldparmäne</td><td>007</td></tr>
<tr><td>Ingrid Marie</td><td>008</td></tr>
<tr><td>McIntosh</td><td>009</td></tr>
<tr><td>Jonathan</td><td>010</td></tr>
<tr><td>Red Delicious, etc. (group) and Starking Delicious</td><td>011</td></tr>
<tr><td>Golden Delicious and Golden Spur</td><td>012</td></tr>
<tr><td>Spartan</td><td>013</td></tr>
<tr><td>Reinette du Canada</td><td>014</td></tr>
<tr><td>Cox's Orange Pippin</td><td>015</td></tr>
<tr><td>Boskoop</td><td>016</td></tr>
<tr><td>Morgenduft (Imperatore) and Rome Beauty</td><td>017</td></tr>
<tr><td>Rambour d'hiver</td><td>018</td></tr>
<tr><td>Granny Smith</td><td>019</td></tr>
<tr><td>Reinette du Mans</td><td>020</td></tr>
<tr><td>Annurca</td><td>021</td></tr>
<tr><td>Stayman</td><td>022</td></tr>
<tr><td>Glockenapfel</td><td>023</td></tr>
<tr><td>Abbondanza</td><td>026</td></tr>
<tr><td>Holsteiner Cox</td><td>027</td></tr>
<tr><td>Reinette Clochard</td><td>028</td></tr>
<tr><td>Gloster</td><td>031</td></tr>
<tr><td>Crispin/Mutzu</td><td>033</td></tr>
<tr><td>Melrose</td><td>034</td></tr>
<tr><td>Egremont Russet</td><td>035</td></tr>
<tr><td>Lobo</td><td>036</td></tr>
<tr><td>Luxembourg Triumpf</td><td>038</td></tr>
<tr><td>Luxembourg Reinette</td><td>039</td></tr>
<tr><td>Fyriki</td><td>042</td></tr>
<tr><td>Delicious Pilafa</td><td>043</td></tr>
<tr><td>Jonagold</td><td>044</td></tr>
<tr><td>Katy</td><td>045</td></tr>
<tr><td>Idared</td><td>046</td></tr>
<tr><td>Elstar</td><td>047</td></tr>
<tr><td>Reinette Parda</td><td>050</td></tr>
<tr><td>Starkimson and clones (Coopers)</td><td>051</td></tr>
<tr><td>Verde doncella</td><td>052</td></tr>
<tr><td>Fiesta</td><td>053</td></tr>
<tr><td>Groupe Gala</td><td>054</td></tr>
<tr><td>Braeburn</td><td>055</td></tr>
<tr><td>Prima</td><td>056</td></tr>
<tr><td>Akane</td><td>057</td></tr>
<tr><td>Top Red Delicious</td><td>058</td></tr>
<tr><td>Alkmine</td><td>059</td></tr>
<tr><td>Varieties</td><td>Code</td></tr>
<tr><td>Jumba</td><td>060</td></tr>
<tr><td>Casa Nova de Alcobaça</td><td>061</td></tr>
<tr><td>Aroma</td><td>062</td></tr>
<tr><td>Limoncella</td><td>063</td></tr>
<tr><td>Andre Reinettes</td><td>064</td></tr>
<tr><td>Jersey Mac</td><td>065</td></tr>
<tr><td>Belepsch</td><td>066</td></tr>
<tr><td>Ontario</td><td>067</td></tr>
<tr><td>Fuji No 1</td><td>068</td></tr>
<tr><td>Kronprinz Rudolf</td><td>069</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2">Apple trees exclusively producing apples intended for uses other than as dessert apples (optional)</td></tr>
<tr><td>Bramley's Seedling</td><td>001</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 2. Pear trees </td></tr>
<tr><td colspan="2">Pear trees giving dessert pears</td></tr>
<tr><td>Gentile Bianca</td><td>001</td></tr>
<tr><td>Coscia</td><td>002</td></tr>
<tr><td>Butirra Precoce Morettini</td><td>003</td></tr>
<tr><td>Spadoncina</td><td>004</td></tr>
<tr><td>Jules Guyot/Limonera</td><td>005</td></tr>
<tr><td>Santa Maria Morettini</td><td>006</td></tr>
<tr><td>Spadona d'Estate</td><td>007</td></tr>
<tr><td>William's</td><td>008</td></tr>
<tr><td>Clara Frijs</td><td>009</td></tr>
<tr><td>Clapp's Favourite</td><td>010</td></tr>
<tr><td>Triomphe de Vienne</td><td>012</td></tr>
<tr><td>Alexandrine Douillard</td><td>013</td></tr>
<tr><td>Beurré Hardy</td><td>014</td></tr>
<tr><td>Durondeau</td><td>015</td></tr>
<tr><td>Légipont/Charneu</td><td>016</td></tr>
<tr><td>Louise Bonne d'Avranches</td><td>017</td></tr>
<tr><td>Abate Fetel</td><td>018</td></tr>
<tr><td>Conférence</td><td>019</td></tr>
<tr><td>Kaiser Alexander</td><td>021</td></tr>
<tr><td>Doyenné du Cornice</td><td>022</td></tr>
<tr><td>Passe Crassane</td><td>023</td></tr>
<tr><td>Alexandra Lucas</td><td>024</td></tr>
<tr><td>Decana d'Inverno</td><td>025</td></tr>
<tr><td>Packam's Triumph</td><td>026</td></tr>
<tr><td>Épine du Mas</td><td>027</td></tr>
<tr><td>Madernassa</td><td>028</td></tr>
<tr><td>Butirra d'Estate</td><td>029</td></tr>
<tr><td>Curé</td><td>030</td></tr>
<tr><td>William's rouge</td><td>031</td></tr>
<tr><td>Krystalli</td><td>034</td></tr>
<tr><td>Blanquilla</td><td>035</td></tr>
<tr><td>M. P. Morettini</td><td>036</td></tr>
<tr><td>Ercolini</td><td>037</td></tr>
<tr><td>Rocha</td><td>038</td></tr>
<tr><td>Kontoula</td><td>039</td></tr>
<tr><td>Général Leclerc</td><td>040</td></tr>
<tr><td>Roma</td><td>041</td></tr>
<tr><td>Concorde</td><td>042</td></tr>
<tr><td>Varieties</td><td>Code</td></tr>
<tr><td>Castell</td><td>043</td></tr>
<tr><td>Max red Bartlett</td><td>044</td></tr>
<tr><td>Flor de invierno</td><td>045</td></tr>
<tr><td>Devoe</td><td>046</td></tr>
<tr><td>Highland</td><td>047</td></tr>
<tr><td>Nashi-group</td><td>048</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2">Pear trees exclusively producing pears intended for uses other than as dessert pears (optional)</td></tr>
<tr><td>Saint Rémy</td><td>001</td></tr>
<tr><td>Gieser Wildman</td><td>002</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 3. Peach trees </td></tr>
<tr><td colspan="2">Peach trees giving fruits with yellow flesh</td></tr>
<tr><td>Maycrest group (early 1 or very early):</td><td>510</td></tr>
<tr><td>Maycrest</td><td>511</td></tr>
<tr><td>Armgold</td><td>512</td></tr>
<tr><td>Others</td><td>519</td></tr>
<tr><td>Springcrest group (early 2 or early):</td><td>520</td></tr>
<tr><td>Springcrest</td><td>521</td></tr>
<tr><td>Spring Lady</td><td>522</td></tr>
<tr><td>Others</td><td>529</td></tr>
<tr><td>Cardinal group (early 3 or early):</td><td>530</td></tr>
<tr><td>Cardinal</td><td>531</td></tr>
<tr><td>Dixired</td><td>532</td></tr>
<tr><td>June Gold</td><td>533</td></tr>
<tr><td>Others</td><td>539</td></tr>
<tr><td>Redhaven group (early 4 or seasonal):</td><td>540</td></tr>
<tr><td>Redhaven</td><td>541</td></tr>
<tr><td>Sudanell</td><td>542</td></tr>
<tr><td>Maruja</td><td>543</td></tr>
<tr><td>Others</td><td>549</td></tr>
<tr><td>Glohaven group (early 5 or seasonal):</td><td>560</td></tr>
<tr><td>Glohaven</td><td>561</td></tr>
<tr><td>Redtop</td><td>562</td></tr>
<tr><td>Fairhaven</td><td>563</td></tr>
<tr><td>Others</td><td>569</td></tr>
<tr><td>Cresthaven group (early 6 and 7 or late):</td><td>570</td></tr>
<tr><td>Cresthaven</td><td>571</td></tr>
<tr><td>Andros</td><td>572</td></tr>
<tr><td>Loadel</td><td>573</td></tr>
<tr><td>Suncrest</td><td>574</td></tr>
<tr><td>Vivian</td><td>575</td></tr>
<tr><td>Merril Franciscan</td><td>576</td></tr>
<tr><td>Loring</td><td>577</td></tr>
<tr><td>Dixon</td><td>578</td></tr>
<tr><td>Others</td><td>579</td></tr>
<tr><td>J. H. Hale group (early 8, 9 and 10 or very late):</td><td>580</td></tr>
<tr><td>J. H. Hale</td><td>581</td></tr>
<tr><td>Tardio de Calanda</td><td>582</td></tr>
<tr><td>Elberta</td><td>583</td></tr>
<tr><td>Fayette</td><td>584</td></tr>
<tr><td>Roubidoux</td><td>585</td></tr>
<tr><td>Others</td><td>589</td></tr>
<tr><td>Varieties</td><td>Code</td></tr>
<tr><td>Pavie/Percoche group:</td><td>600</td></tr>
<tr><td>Fortuna</td><td>601</td></tr>
<tr><td>Klamt</td><td>602</td></tr>
<tr><td>Caroline</td><td>603</td></tr>
<tr><td>Vesuvio</td><td>604</td></tr>
<tr><td>Babygold 5, 6 and 7</td><td>605</td></tr>
<tr><td>Bowen</td><td>606</td></tr>
<tr><td>Katherina</td><td>607</td></tr>
<tr><td>Merriam</td><td>608</td></tr>
<tr><td>Others</td><td>609</td></tr>
<tr><td>Nectarines and brugnons</td><td>700</td></tr>
<tr><td>Armking-Mayred group (early 1 and 2 or very early):</td><td>710</td></tr>
<tr><td>Armking-Mayred</td><td>711</td></tr>
<tr><td>Others</td><td>719</td></tr>
<tr><td>Grimson-Maygrand group (early 3 or early):</td><td>720</td></tr>
<tr><td>Grimson-Maygrand</td><td>721</td></tr>
<tr><td>Others</td><td>729</td></tr>
<tr><td>Stark Red gold group (early 4, 5 and 6 or seasonal):</td><td>730</td></tr>
<tr><td>Stark Red gold</td><td>731</td></tr>
<tr><td>Independance</td><td>732</td></tr>
<tr><td>Nectared</td><td>733</td></tr>
<tr><td>Others</td><td>739</td></tr>
<tr><td>Fantasia group (early 7 and 8 or late):</td><td>740</td></tr>
<tr><td>Fantasia</td><td>741</td></tr>
<tr><td>Others</td><td>749</td></tr>
<tr><td>Fairlane group (early 9 and 10 or very late):</td><td>750</td></tr>
<tr><td>Fairlane</td><td>751</td></tr>
<tr><td>Others</td><td>759</td></tr>
<tr><td>Other yellow flesh varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2">Peach trees giving fruit with white flesh</td></tr>
<tr><td>Springtime group (early 1 or very early):</td><td>510</td></tr>
<tr><td>Springtime</td><td>511</td></tr>
<tr><td>Mayflower</td><td>512</td></tr>
<tr><td>Morettini No 1 and 5/4</td><td>513</td></tr>
<tr><td>Others</td><td>519</td></tr>
<tr><td>Robin group (early 2 and 3 or early):</td><td>530</td></tr>
<tr><td>Robin</td><td>531</td></tr>
<tr><td>Alexandra</td><td>532</td></tr>
<tr><td>Amsden</td><td>533</td></tr>
<tr><td>Others</td><td>539</td></tr>
<tr><td>Maria Bianca group (early 4, 5 and 6 or seasonal):</td><td>540</td></tr>
<tr><td>Maria Bianca</td><td>541</td></tr>
<tr><td>Redwing</td><td>542</td></tr>
<tr><td>Bella di Cesena</td><td>543</td></tr>
<tr><td>Others</td><td>549</td></tr>
<tr><td>Michelini group (early 7 and 8 or late):</td><td>550</td></tr>
<tr><td>Michelini and Impero</td><td>551</td></tr>
<tr><td>Honey dew Hale</td><td>552</td></tr>
<tr><td>Pieri 81</td><td>553</td></tr>
<tr><td>Others</td><td>559</td></tr>
<tr><td>Paraguya group (early 9 and 10 or very late):</td><td>560</td></tr>
<tr><td>Paraguya</td><td>561</td></tr>
<tr><td>Others</td><td>569</td></tr>
<tr><td>Nectarines and brugnons</td><td>700</td></tr>
<tr><td>Snow-Queen group (early 2 and 3 or early):</td><td>710</td></tr>
<tr><td>Snow-Queen</td><td>711</td></tr>
<tr><td>Others</td><td>719</td></tr>
<tr><td>Other nectarines and brugnons not specified</td><td>799</td></tr>
<tr><td>Other white flesh varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2">Peach trees giving fruits with flesh other than white or yellow or of unspecified colour</td></tr>
<tr><td>Varieties to be specified by the Member State</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 4. Apricot trees </td></tr>
<tr><td>Polonais</td><td>001</td></tr>
<tr><td>Rouge du Roussillon</td><td>002</td></tr>
<tr><td>Bergeron</td><td>003</td></tr>
<tr><td>Cafona</td><td>004</td></tr>
<tr><td>Boccucia</td><td>005</td></tr>
<tr><td>Monaco Bello</td><td>006</td></tr>
<tr><td>Bebecou</td><td>007</td></tr>
<tr><td>Précoce de Tyrinthe</td><td>009</td></tr>
<tr><td>Bulida</td><td>010</td></tr>
<tr><td>Canino</td><td>011</td></tr>
<tr><td>Moniqui</td><td>012</td></tr>
<tr><td>Currot</td><td>014</td></tr>
<tr><td>Paviot</td><td>015</td></tr>
<tr><td>Real Fino</td><td>016</td></tr>
<tr><td>Précoce d'Imola</td><td>018</td></tr>
<tr><td>5. Castrese</td><td>019</td></tr>
<tr><td>Pepitos</td><td>020</td></tr>
<tr><td>Galta Rocha</td><td>021</td></tr>
<tr><td>Louisette</td><td>022</td></tr>
<tr><td>Tadeo</td><td>023</td></tr>
<tr><td>Rojo del Medio</td><td>024</td></tr>
<tr><td>Palabras</td><td>025</td></tr>
<tr><td>Labertin No 1</td><td>026</td></tr>
<tr><td>Jaubert</td><td>027</td></tr>
<tr><td>Real Fino</td><td>028</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 5. Orange trees </td></tr>
<tr><td colspan="2">Orange trees giving blood oranges</td></tr>
<tr><td>Sanguinello</td><td>001</td></tr>
<tr><td>Moro</td><td>002</td></tr>
<tr><td>Tarocco</td><td>004</td></tr>
<tr><td>Sanguina Comune</td><td>042</td></tr>
<tr><td>Other blood oranges (to be specified by the Member State)</td><td>900-948</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>949</td></tr>
<tr><td colspan="2">Orange trees giving sweet oranges other than blood oranges</td></tr>
<tr><td>Ovale/Calabrese</td><td>003</td></tr>
<tr><td>Belladonna</td><td>006</td></tr>
<tr><td>Shamottti (Jaffa)</td><td>008</td></tr>
<tr><td>Salustiana</td><td>009</td></tr>
<tr><td>De Setúbal</td><td>010</td></tr>
<tr><td>Valencia Late</td><td>015</td></tr>
<tr><td>Bionda Comune</td><td>016</td></tr>
<tr><td>D. João</td><td>023</td></tr>
<tr><td>Espera da Vidigueira</td><td>026</td></tr>
<tr><td>Bionda Apirena</td><td>029</td></tr>
<tr><td>Vaniglia Apirena</td><td>030</td></tr>
<tr><td>Cadenera</td><td>031</td></tr>
<tr><td>Koima</td><td>034</td></tr>
<tr><td>Navels (group):</td><td>050</td></tr>
<tr><td>Merlin or Washinton Navel</td><td>051</td></tr>
<tr><td>Navelina or Dalmau</td><td>052</td></tr>
<tr><td>Navel New Hall</td><td>053</td></tr>
<tr><td>Thonson Navel</td><td>054</td></tr>
<tr><td>Navelate</td><td>055</td></tr>
<tr><td>Lane Late</td><td>056</td></tr>
<tr><td>Other Navels</td><td>059</td></tr>
<tr><td>Other sweet oranges (to be specified by the Member State)</td><td>950-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 6. Lemon trees </td></tr>
<tr><td>Femminello Ovale</td><td>001</td></tr>
<tr><td>Femminello di S. Teresa</td><td>002</td></tr>
<tr><td>Monachello</td><td>003</td></tr>
<tr><td>Inter Donato</td><td>004</td></tr>
<tr><td>Lunario Tondo (Arancino)</td><td>005</td></tr>
<tr><td>Lunario Sfusato (Palermo)</td><td>006</td></tr>
<tr><td>Maglini</td><td>007</td></tr>
<tr><td>Karystini</td><td>008</td></tr>
<tr><td>Adamopoulou</td><td>009</td></tr>
<tr><td>Lisbon</td><td>010</td></tr>
<tr><td>Eureka</td><td>011</td></tr>
<tr><td>Berna group</td><td>012</td></tr>
<tr><td>Mesero group</td><td>013</td></tr>
<tr><td>Lunero (four seasons)</td><td>014</td></tr>
<tr><td>Real</td><td>015</td></tr>
<tr><td>Comune</td><td>016</td></tr>
<tr><td>Siagara bianca</td><td>017</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
<tr><td colspan="2"> 7. Small citrus fruit trees </td></tr>
<tr><td colspan="2">Small citrus fruit trees giving mandarins</td></tr>
<tr><td>Avana</td><td>101</td></tr>
<tr><td>Tardivo o Di Ciaculli</td><td>102</td></tr>
<tr><td>Common</td><td>103</td></tr>
<tr><td>Wilking</td><td>104</td></tr>
<tr><td>Kara</td><td>105</td></tr>
<tr><td>Encore</td><td>107</td></tr>
<tr><td>Setubalense</td><td>109</td></tr>
<tr><td>Carvalhais</td><td>110</td></tr>
<tr><td>Clemenvilla</td><td>111</td></tr>
<tr><td>Fortune</td><td>112</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>190-198</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>199</td></tr>
<tr><td colspan="2">Small citrus fruit trees giving clementines</td></tr>
<tr><td>Clémentine de Corse</td><td>201</td></tr>
<tr><td>Montreal</td><td>202</td></tr>
<tr><td>Comune</td><td>203</td></tr>
<tr><td>Fina</td><td>204</td></tr>
<tr><td>Oroval</td><td>205</td></tr>
<tr><td>Clemenules or Clémentine Di Nules</td><td>206</td></tr>
<tr><td>Clémentine Porou</td><td>208</td></tr>
<tr><td>Hernandina</td><td>209</td></tr>
<tr><td>Marisol</td><td>210</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>290-298</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>299</td></tr>
<tr><td colspan="2">Small citrus fruit trees giving satsumas</td></tr>
<tr><td>Satsuma</td><td>301</td></tr>
<tr><td>Clausellina</td><td>302</td></tr>
<tr><td>Owari</td><td>306</td></tr>
<tr><td>Ohitsu</td><td>308</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>390-398</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>399</td></tr>
<tr><td colspan="2">Other small citrus fruit trees</td></tr>
<tr><td>Tangero</td><td>401</td></tr>
<tr><td>Mandarine clementine o nova</td><td>501</td></tr>
<tr><td>Other varieties (to be specified by the Member State)</td><td>900-998</td></tr>
<tr><td>Varieties not specified elsewhere</td><td>999</td></tr>
</tbody>
</table>

## ANNEX III

Boundaries of the production areas (where appropriate by species) referred to in Article 3

<table>
<tbody><tr><td colspan="3">BELGIUM:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">DENMARK:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">FEDERAL REPUBLIC OF GERMANY:</td></tr>
<tr><td>  </td><td>1.Nord:</td><td>Schleswig-Holstein, Niedersachsen, Hamburg, Bremen</td></tr>
<tr><td>  </td><td>2.Mitte:</td><td>Nordrhein-Westfalen, Hessen, Rheinland-Pfalz, Saarland</td></tr>
<tr><td>  </td><td>3.Süd:</td><td>Baden-Württemberg, Bayern</td></tr>
<tr><td>  </td><td>4.Ost:</td><td>Brandenburg, Mecklenburg-Vorpommern, Sachsen, Sachsen-Anhalt, Thüringen</td></tr>
<tr><td colspan="3">GREECE:</td></tr>
<tr><td>  </td><td rowspan="4">(Apples)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Macedonia</td></tr>
<tr><td>  </td><td>3.Thessaly</td></tr>
<tr><td>  </td><td>4.Other areas</td></tr>
<tr><td>  </td><td rowspan="5">(Pears)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Macedonia</td></tr>
<tr><td>  </td><td>3.Thessaly</td></tr>
<tr><td>  </td><td>4.Crete</td></tr>
<tr><td>  </td><td>5.Other areas</td></tr>
<tr><td>  </td><td rowspan="3">(Peaches)</td><td>1.Macedonia</td></tr>
<tr><td>  </td><td>2.Thessaly</td></tr>
<tr><td>  </td><td>3.Other areas</td></tr>
<tr><td>  </td><td rowspan="3">(Apricots)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Macedonia</td></tr>
<tr><td>  </td><td>3.Other areas</td></tr>
<tr><td>  </td><td rowspan="4">(Oranges)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Crete</td></tr>
<tr><td>  </td><td>3.Epirus</td></tr>
<tr><td>  </td><td>4.Other areas</td></tr>
<tr><td>  </td><td rowspan="3">(Lemons)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Central Greece and Euboea</td></tr>
<tr><td>  </td><td>3.Other areas</td></tr>
<tr><td>  </td><td rowspan="4">(Small-fruited citrus)</td><td>1.Peloponnesus</td></tr>
<tr><td>  </td><td>2.Crete</td></tr>
<tr><td>  </td><td>3.Aegean Islands</td></tr>
<tr><td>  </td><td>4.Other areas</td></tr>
<tr><td colspan="3">SPAIN:</td></tr>
<tr><td>  </td><td>1.Galicia</td></tr>
<tr><td>  </td><td>2.Principado de Asturias</td></tr>
<tr><td>  </td><td>3.Cantabria</td></tr>
<tr><td>  </td><td>4.País Vasco</td></tr>
<tr><td>  </td><td>5.Navarra</td></tr>
<tr><td>  </td><td>6.La Rioja</td></tr>
<tr><td>  </td><td>7.Aragón</td></tr>
<tr><td>  </td><td>8.Cataluña</td></tr>
<tr><td>  </td><td>9.Baleares</td></tr>
<tr><td>  </td><td>10.Castilla y León</td></tr>
<tr><td>  </td><td>11.Madrid</td></tr>
<tr><td>  </td><td>12.Castilla-La Mancha</td></tr>
<tr><td>  </td><td>13.Comunidad Valenciana</td></tr>
<tr><td>  </td><td>14.Región de Murcia</td></tr>
<tr><td>  </td><td>15.Extremadura</td></tr>
<tr><td>  </td><td>16.Andalucía</td></tr>
<tr><td>  </td><td>17.Canarias</td></tr>
<tr><td colspan="3">FRANCE:</td></tr>
<tr><td>  </td><td>1.Sud-ouest:</td><td>Limousin, Auvergne, Aquitaine, Midi-Pyrénées</td></tr>
<tr><td>  </td><td>2.Sud-est:</td><td>Rhône-Alpes, Languedoc-Roussillon, Provence-Alpes, Côte d'Azur, Corse</td></tr>
<tr><td>  </td><td>3.Loire:</td><td>Pays de Loire, Poitou-Charentes, Centre, Ile de France</td></tr>
<tr><td>  </td><td colspan="2">4.Remainder of France</td></tr>
<tr><td colspan="3">IRELAND:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">ITALY:</td></tr>
<tr><td>  </td><td rowspan="5">(Apples, pears)</td><td>1.Val Padana: Lombardia, Veneto, Friuli-Venezia Giulia, Emilia-Romagna</td></tr>
<tr><td>  </td><td>2.Trentino-Alto Adige</td></tr>
<tr><td>  </td><td>3.Piemonte, Valle d'Aosta</td></tr>
<tr><td>  </td><td>4.Centrale: Liguria, Toscana, Umbria, Marche, Lazio, Abruzzo</td></tr>
<tr><td>  </td><td>5.Meridionale: Campania, Calabria, Molise, Puglia, Basilicata, Sicilia, Sardegna.</td></tr>
<tr><td>  </td><td rowspan="4">(Peaches, apricots)</td><td>1.Val Padana and Trentino-Alto Adige: Lombardia, Veneto, Friuli-Venezia Giulia, Emilia-Romagna, Trentino-Alto Adige</td></tr>
<tr><td>  </td><td>2.Piemonte, Valle d'Aosta</td></tr>
<tr><td>  </td><td>3.Centrale: Liguria, Toscana, Umbria, Marche, Lazio, Abruzzo</td></tr>
<tr><td>  </td><td>4.Meridionale: Campania, Calabria, Molise, Puglia, Basilicata, Sicilia, Sardegna</td></tr>
<tr><td>  </td><td rowspan="4">(Oranges, lemons, small-fruited citrus)</td><td>1.Sicilia</td></tr>
<tr><td>  </td><td>2.Calabria</td></tr>
<tr><td>  </td><td>3.Puglia, Basilicata</td></tr>
<tr><td>  </td><td>4.Remainder of Italy</td></tr>
<tr><td colspan="3">LUXEMBOURG:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">NETHERLANDS:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">PORTUGAL:</td></tr>
<tr><td>  </td><td>  </td><td>1.Norte</td></tr>
<tr><td>  </td><td>  </td><td>2.Centro</td></tr>
<tr><td>  </td><td>  </td><td>3.Lisboa and Vale do Tejo</td></tr>
<tr><td>  </td><td>  </td><td>4.Alentejo</td></tr>
<tr><td>  </td><td>  </td><td>5.Algarve</td></tr>
<tr><td>  </td><td>  </td><td>6.Regiâo autonomas Açores</td></tr>
<tr><td>  </td><td>  </td><td>7.Regiâo autonomas Madeira</td></tr>
<tr><td colspan="3">UNITED KINGDOM:</td></tr>
<tr><td>  </td><td colspan="2">Forms a single production area</td></tr>
<tr><td colspan="3">AUSTRIA:</td></tr>
<tr><td>  </td><td>Forms a single production area</td><td>  </td></tr>
<tr><td colspan="3">FINLAND:</td></tr>
<tr><td>  </td><td>Forms a single production area</td><td>  </td></tr>
<tr><td colspan="3">SWEDEN:</td></tr>
<tr><td>  </td><td>Forms a single production area</td><td>  </td></tr>
</tbody>
</table>
