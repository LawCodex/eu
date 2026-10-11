---
title: "Commission Regulation (EC) No 332/2007 of 27 March 2007 on the technical arrangements for the transmission of railway transport statistics (Text with EEA relevance )"
identifier: "32007R0332"
eli: "http://data.europa.eu/eli/reg/2007/332/oj"
type: regulation
jurisdiction: eu
language: en
date: 2007-03-27
entry_into_force: 2007-07-11
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32007R0332"
retrieved: 2026-10-11
---

# Commission Regulation (EC) No 332/2007 of 27 March 2007 on the technical arrangements for the transmission of railway transport statistics (Text with EEA relevance )

**COMMISSION REGULATION (EC) No 332/2007**

**of 27 March 2007**

**on the technical arrangements for the transmission of railway transport statistics**

**(Text with EEA relevance)**

THE COMMISSION OF THE EUROPEAN COMMUNITIES,

Having regard to the Treaty establishing the European Community,

Having regard to Regulation (EC) No 91/2003 of the European Parliament and of the Council of 16 December 2002 on rail transport statistics (1), and in particular Article 6(2) thereof,

Whereas:

(1) It is necessary to specify the format in which rail transport data are to be transmitted to the Commission (Eurostat) in sufficient detail to ensure that the data can be processed rapidly and in a cost-effective way.

(2) The measures provided for in this Regulation are in accordance with the opinion of the Statistical Programme Committee, set up by Decision 89/382/EEC, Euratom (2),

HAS ADOPTED THIS REGULATION:

## Article 1

The technical format for the transmission of data to the Commission (Eurostat) shall be as set out in the Annex.

Member States shall use this format for the data concerning reference year 2007 and subsequent years.

## Article 2

The data and metadata supplied pursuant to Regulation (EC) No 91/2003 shall be transmitted in electronic format to the single entry point for data at the Commission (Eurostat) by any organisation designated by the national authorities. Transmission shall conform to an appropriate interchange standard specified by Eurostat.

## Article 3

This Regulation shall enter into force on the 20th day following its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 27 March 2007.

For the Commission

Joaquín ALMUNIA

Member of the Commission

(1) OJ L 14, 21.1.2003, p. 1. Regulation as amended by Commission Regulation (EC) No 1192/2003 (OJ L 167, 4.7.2003, p. 13).

(2) OJ L 181, 28.6.1989, p. 47.

## ANNEX

**TECHNICAL FORMAT FOR DATA TRANSMISSION**

**1\. DATA STRUCTURE**

The individual data records to be sent to Eurostat for each quarter, year or period of five years, comprise 9 datasets, each corresponding to an annex of Regulation (EC) No 91/2003. These datasets thus contain the following data:

— annual statistics on goods transport — detailed reporting (Annex A),

— annual statistics on goods transport — simplified reporting (Annex B),

— annual statistics on passenger transport — detailed reporting (Annex C),

— annual statistics on passenger transport — simplified reporting (Annex D),

— quarterly statistics on goods and passenger transport (Annex E),

— quinquennial regional statistics on goods and passenger transport (Annex F),

— quinquennial statistics on traffic flows on the rail network (Annex G),

— statistics on accidents (Annex H),

— a list of the railway undertakings for which statistics are provided (Annex I).

Annexes B and D set out simplified reporting requirements that may be used by Member States as an alternative to the normal detailed reporting set out in Annexes A and C, for undertakings below the thresholds laid down in Article 4(2) of Regulation (EC) No 91/2003.

**2\. LIST OF FIELDS**

Pursuant to Regulation (EC) No 91/2003, one dataset has to be provided for each annex in the form of a flat file using the semi-colon ‘;’ as a field separator. Each dataset, except dataset C, must contain data for all mandatory tables required by the annex. For each dataset, the number of fields in each record is fixed. In other words, all fields must be present even if they are empty (two successive field separators indicate an empty field).

The individual fields are described below as follows:

— Field number: this identifies the position of the field in the record,

— Field name: this either refers to a variable in Regulation (EC) No 91/2003, or to an internal identifier used to identify the record,

— Description: short description of the contents of the field,

— Coding: in tables A2 and A4 certain fields are to be coded according to Annexes J to K of Regulation (EC) No 91/2003. Additional coding rules are noted here. Further explanations and recommendations on coding are provided by Eurostat in the Guidelines for the implementation of Regulation (EC) No 91/2003,

— Field type: indicates whether the field contains a numeric quantity or a text string, all numeric quantities are to be provided as integers,

— Maximum length: the maximum expected length of the data for a particular field. Data that are too long cannot be loaded,

— Confidentiality flag (FlagC) indicates if the record is considered confidential by the Member State (Council Regulations (EC) No 322/97 (1), Article 13(1) and (Euratom, EEC) No 1588/90 (2), Article 2),

— Flag of authorisation for dissemination of confidential data (FlagD) indicates if confidential data provided by the Member States can be disseminated (Council Regulations (EC) No 322/97, Article 13(2) and (Euratom, EEC) No 1588/90, Article 5(4)). Hence, the Commission is legally permitted to change the Member State’s judgment in well-defined cases. This is done by changing FlagD=1 to FlagD=0 when FlagC=1.

**Dataset for Annex A: Annual statistics on goods transport — detailed reporting**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>A1 to A9</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>A0</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>TransID</td><td>Type of transport</td><td><table><tbody><tr><td>0</td><td>:</td><td>total transport</td></tr>
<tr><td>1</td><td>:</td><td>national transport</td></tr>
<tr><td>2</td><td>:</td><td>international transport — total</td></tr>
<tr><td>3</td><td>:</td><td>international transport — outgoing</td></tr>
<tr><td>4</td><td>:</td><td>international transport — incoming</td></tr>
<tr><td>5</td><td>:</td><td>transit transport</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>6</td><td>Goods</td><td>Type of goods</td><td>annex J of the Regulation</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>7</td><td>DGoods</td><td>Type of dangerous goods</td><td>annex K of the Regulation</td><td>Text</td><td>3 </td><td></td></tr>
<tr><td>8</td><td>LDG</td><td>Country of loading</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td>XX</td></tr>
<tr><td>9</td><td>UNL</td><td>Country of unloading</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td>XX</td></tr>
<tr><td>10</td><td>Consgmt</td><td>Type of consignment</td><td><table><tbody><tr><td>1</td><td>:</td><td>full trainloads</td></tr>
<tr><td>2</td><td>:</td><td>full wagonloads</td></tr>
<tr><td>3</td><td>:</td><td>other</td></tr>
<tr><td>9</td><td>:</td><td>unknown</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>11</td><td>TTU</td><td>Type of transport Unit</td><td><table><tbody><tr><td>1</td><td>:</td><td>containers and swap bodies</td></tr>
<tr><td>2</td><td>:</td><td>semi-trailers (unaccompanied)</td></tr>
<tr><td>3</td><td>:</td><td>road vehicles (accompanied)</td></tr>
<tr><td>9</td><td>:</td><td>unknown</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>12</td><td>Tonnes</td><td>Total goods transport</td><td>Tonnes</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>13</td><td>Tkm</td><td>Total goods transport in 1 000 tonne-kilometres</td><td>1 000 Tonnes-km</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>14</td><td>NbrITU</td><td>Number of Intermodal transport unit</td><td>Number of ITU</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>15</td><td>TeuITU</td><td>Intermodal transport units carried in TEU</td><td>TEU</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>16</td><td>TrainKM</td><td>Goods train movement in 1 000 km</td><td>1 000 Train-km</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>17</td><td>FlagC</td><td>Confidentiality flag</td><td><table><tbody><tr><td>1</td><td>:</td><td>confidential</td></tr>
<tr><td>0</td><td>:</td><td>not confidential</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>18</td><td>FlagD</td><td>Flag of authorisation for dissemination</td><td><table><tbody><tr><td>1</td><td>:</td><td>dissemination not authorised</td></tr>
<tr><td>0</td><td>:</td><td>dissemination authorised</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex A, each record comprises 18 fields. The following table shows in grey the fields that have to be provided for the different tables of Annex A. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

<table>
<tbody><tr><td colspan="2"></td><td colspan="9">DsetID</td></tr>
<tr><td>Field number</td><td>Field name</td><td>A1</td><td>A2</td><td>A3</td><td>A4</td><td>A5 (3)</td><td>A6</td><td>A7</td><td>A8</td><td>A9</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>TransID</td><td>*</td><td></td><td>*</td><td></td><td></td><td>*</td><td>*</td><td>*</td><td></td></tr>
<tr><td>6</td><td>Goods</td><td></td><td>*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>7</td><td>DGoods</td><td></td><td></td><td></td><td>*</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>8</td><td>LDG</td><td></td><td></td><td>*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>9</td><td>UNL</td><td></td><td></td><td>*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>10</td><td>Consgmt</td><td></td><td></td><td></td><td></td><td>*</td><td></td><td></td><td></td><td></td></tr>
<tr><td>11</td><td>TTU</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>12</td><td>Tonnes</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>13</td><td>Tkm</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>14</td><td>NbrITU</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>15</td><td>TeuITU</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>16</td><td>TrainKM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>17</td><td>FlagC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>18</td><td>FlagD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex B: Annual statistics on goods transport — simplified reporting**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>B1 to B2</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>A0</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>TransID</td><td>Type of transport</td><td><table><tbody><tr><td>0</td><td>:</td><td>total transport</td></tr>
<tr><td>1</td><td>:</td><td>national transport</td></tr>
<tr><td>2</td><td>:</td><td>international transport — total</td></tr>
<tr><td>3</td><td>:</td><td>international transport — outgoing</td></tr>
<tr><td>4</td><td>:</td><td>international transport — incoming</td></tr>
<tr><td>5</td><td>:</td><td>transit transport</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>6</td><td>Tonnes</td><td>Total goods transport</td><td>Tonnes</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>7</td><td>Tkm</td><td>Total goods transport in 1 000 tonne-kilometres</td><td>1 000 Tonnes-km</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>8</td><td>TrainKm</td><td>Goods train movement in 1 000 train-km</td><td>1 000 Train-km</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>9</td><td>FlagC</td><td>Confidentiality flag</td><td><table><tbody><tr><td>1</td><td>:</td><td>confidential</td></tr>
<tr><td>0</td><td>:</td><td>not confidential</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>10</td><td>FlagD</td><td>Flag of authorisation for dissemination</td><td><table><tbody><tr><td>1</td><td>:</td><td>dissemination not authorised</td></tr>
<tr><td>0</td><td>:</td><td>dissemination authorised</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex B, each record comprises 10 fields. The following table shows in grey the fields that have to be provided for each of the two tables of Annex B. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

<table>
<tbody><tr><td colspan="2"></td><td colspan="2">DsetID</td></tr>
<tr><td>Field number</td><td>Field name</td><td>B1</td><td>B2</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>TransID</td><td>*</td><td></td></tr>
<tr><td>6</td><td>Tonnes</td><td></td><td></td></tr>
<tr><td>7</td><td>Tkm</td><td></td><td></td></tr>
<tr><td>8</td><td>TrainKM</td><td></td><td></td></tr>
<tr><td>9</td><td>FlagC</td><td></td><td></td></tr>
<tr><td>10</td><td>FlagD</td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex C: Annual statistics on passenger transport — detailed reporting**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>C1 to C5</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>A0</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>TransID</td><td>Type of transport</td><td><table><tbody><tr><td>1</td><td>:</td><td>national transport</td></tr>
<tr><td>2</td><td>:</td><td>international transport — total</td></tr>
<tr><td>3</td><td>:</td><td>international transport — outgoing</td></tr>
<tr><td>4</td><td>:</td><td>international transport — incoming</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>6</td><td>LDG</td><td>Country of embarkation</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td>XX</td></tr>
<tr><td>7</td><td>UNL</td><td>Country of disembarkation</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td>XX</td></tr>
<tr><td>8</td><td>Pass</td><td>Total passenger transport</td><td>Passengers</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>9</td><td>Passkm</td><td>Total passenger transport in 1 000 passenger-kilometres</td><td>1 000 pkm</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>10</td><td>TrainKm</td><td>Passengers train movements in 1 000 train-km</td><td>1 000 Train-km</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>11</td><td>FlagC</td><td>Confidentiality flag</td><td><table><tbody><tr><td>1</td><td>:</td><td>confidential</td></tr>
<tr><td>0</td><td>:</td><td>not confidential</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>12</td><td>FlagD</td><td>Flag of authorisation for dissemination</td><td><table><tbody><tr><td>1</td><td>:</td><td>dissemination not authorised</td></tr>
<tr><td>0</td><td>:</td><td>dissemination authorised</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex C, each record comprises of 12 fields. The following table shows in grey the fields that have to be provided for the different tables of Annex C. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

Provisional (tables C1 and C2) and final consolidated data (tables C3 and C4) are to be sent at different times following the same structure.

<table>
<tbody><tr><td colspan="2"></td><td colspan="5">DsetID</td></tr>
<tr><td>Field Number</td><td>Field name</td><td>C1 (4)</td><td>C2 (4)</td><td>C3 (5)</td><td>C4 (5)</td><td>C5</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>TransID</td><td>* 1 & 2</td><td>* 3 & 4</td><td>* 1 & 2</td><td>* 3 & 4</td><td></td></tr>
<tr><td>6</td><td>LDG</td><td></td><td>*</td><td></td><td>*</td><td></td></tr>
<tr><td>7</td><td>UNL</td><td></td><td>*</td><td></td><td>*</td><td></td></tr>
<tr><td>8</td><td>Pass</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>9</td><td>Passkm</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>10</td><td>TrainKM</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>11</td><td>FlagC</td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>12</td><td>FlagD</td><td></td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex D: Annual statistics on passenger transport — simplified reporting**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>D1 to D2</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>A0</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>Pass</td><td>Total passenger transport</td><td>Passengers</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>6</td><td>Passkm</td><td>Total passenger transport in 1 000 passenger-kilometres</td><td>1 000 pkm</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>7</td><td>TrainKm</td><td>Passenger train movements in 1 000 train-km</td><td>1 000 Train-km</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>8</td><td>FlagC</td><td>Confidentiality flag</td><td><table><tbody><tr><td>1</td><td>:</td><td>confidential</td></tr>
<tr><td>0</td><td>:</td><td>not confidential</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>9</td><td>FlagD</td><td>Flag of authorisation for dissemination</td><td><table><tbody><tr><td>1</td><td>:</td><td>dissemination not authorised</td></tr>
<tr><td>0</td><td>:</td><td>dissemination authorised</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex D, each record comprises of 9 fields. The following table shows in grey the fields that have to be provided for each of the two tables of Annex D. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

<table>
<tbody><tr><td colspan="2"></td><td colspan="2">DsetID</td></tr>
<tr><td>Field number</td><td>Field name</td><td>D1</td><td>D2</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>Pass</td><td></td><td></td></tr>
<tr><td>6</td><td>Passkm</td><td></td><td></td></tr>
<tr><td>7</td><td>TrainKM</td><td></td><td></td></tr>
<tr><td>8</td><td>FlagC</td><td></td><td></td></tr>
<tr><td>9</td><td>FlagD</td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex E: Quarterly statistics on goods and passenger transport**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>E1 to E2</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>Q1 to Q4</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>Tonnes</td><td>Total goods transport</td><td>Tonnes</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>6</td><td>Tkm</td><td>Total goods transport in 1 000 tonne-kilometres</td><td>1 000 Tonnes-km</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>7</td><td>Pass</td><td>Total passenger transport</td><td>Passengers</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>8</td><td>Passkm</td><td>Total passenger transport in 1 000 passenger-kilometres</td><td>1 000 pkm</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>9</td><td>FlagC</td><td>Confidentiality flag</td><td><table><tbody><tr><td>1</td><td>:</td><td>confidential</td></tr>
<tr><td>0</td><td>:</td><td>not confidential</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>10</td><td>FlagD</td><td>Flag of authorisation for dissemination</td><td><table><tbody><tr><td>1</td><td>:</td><td>dissemination not authorised</td></tr>
<tr><td>0</td><td>:</td><td>dissemination authorised</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex E, each record comprises 10 fields. The following table shows in grey the fields that have to be provided for each of the two tables of Annex E. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

<table>
<tbody><tr><td colspan="2"></td><td colspan="2">DsetID</td></tr>
<tr><td>Field number</td><td>Field name</td><td>E1</td><td>E2</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>Tonnes</td><td></td><td></td></tr>
<tr><td>6</td><td>Tkm</td><td></td><td></td></tr>
<tr><td>7</td><td>Pass</td><td></td><td></td></tr>
<tr><td>8</td><td>Passkm</td><td></td><td></td></tr>
<tr><td>9</td><td>FlagC</td><td></td><td></td></tr>
<tr><td>10</td><td>FlagD</td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex H: Statistics on accidents**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>H1 to H4</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>Period</td><td>Reference period</td><td>A0</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>5</td><td>AccID</td><td>Type of accident</td><td><table><tbody><tr><td>1</td><td>:</td><td>Collisions</td></tr>
<tr><td>2</td><td>:</td><td>Derailments</td></tr>
<tr><td>3</td><td>:</td><td>Accidents involving level crossings</td></tr>
<tr><td>4</td><td>:</td><td>Accidents to persons caused by rolling stock in motion</td></tr>
<tr><td>5</td><td>:</td><td>Fire in rolling stock</td></tr>
<tr><td>6</td><td>:</td><td>Others</td></tr>
<tr><td>7</td><td>:</td><td>Total</td></tr>
<tr><td>9</td><td>:</td><td>Unknown</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>6</td><td>PersID</td><td>Category of person</td><td><table><tbody><tr><td>1</td><td>:</td><td>Passengers</td></tr>
<tr><td>2</td><td>:</td><td>Employees</td></tr>
<tr><td>3</td><td>:</td><td>Others</td></tr>
<tr><td>4</td><td>:</td><td>Total</td></tr>
</tbody>
</table>
 [5: Level-crossing users] <table><tbody><tr><td>[6:</td><td>Unauthorised persons on railway premises]</td></tr>
</tbody>
</table>
<table><tbody><tr><td>9</td><td>:</td><td>Unknown</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>7</td><td>NbAccSign</td><td>Number of significant accidents</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>8</td><td>NbAccInj</td><td>Number of serious injury accidents</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>9</td><td>NbAccDGIn</td><td>Number of accident involving the transport of dangerous goods</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>10</td><td>NbAccDGRe</td><td>Number of accident releasing dangerous goods</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>11</td><td>NbPersK</td><td>Number of persons killed</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
<tr><td>12</td><td>NbPersI</td><td>Number of persons seriously injured</td><td>Number</td><td>Numeric</td><td>8 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex H, each record comprises 12 fields. The following table shows in grey the fields that have to be provided for each table of Annex H. The white cells correspond to blank fields in the record. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

The table contains two further categories of persons that may be required in future: ‘5: Level-crossing users’; and: ‘6: Unauthorised persons on railway premises’.

<table>
<tbody><tr><td colspan="2"></td><td colspan="4">DsetID</td></tr>
<tr><td>Field number</td><td>Field name</td><td>H1</td><td>H2</td><td>H3</td><td>H4</td></tr>
<tr><td>1</td><td>RCount</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>2</td><td>DsetID</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>3</td><td>Year</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>4</td><td>Period</td><td>*</td><td>*</td><td>*</td><td>*</td></tr>
<tr><td>5</td><td>AccID</td><td>*</td><td></td><td>*</td><td>*</td></tr>
<tr><td>6</td><td>PersID</td><td></td><td></td><td>*</td><td>*</td></tr>
<tr><td>7</td><td>NbAccSign</td><td></td><td></td><td></td><td></td></tr>
<tr><td>8</td><td>NbAccInj (6)</td><td></td><td></td><td></td><td></td></tr>
<tr><td>9</td><td>NbAccDGIn</td><td></td><td></td><td></td><td></td></tr>
<tr><td>10</td><td>NbAccDGRe</td><td></td><td></td><td></td><td></td></tr>
<tr><td>11</td><td>NbPersK</td><td></td><td></td><td></td><td></td></tr>
<tr><td>12</td><td>NbPersI</td><td></td><td></td><td></td><td></td></tr>
</tbody>
</table>

**Dataset for Annex I**

<table>
<tbody><tr><td>Field number</td><td>Field name</td><td>Description</td><td>Coding</td><td>Field type</td><td>Max length</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>2</td><td>DsetID</td><td>Dataset identifier</td><td>I1</td><td>Text</td><td>2 </td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the dataset</td><td>4 digits</td><td>Text</td><td>4 </td><td></td></tr>
<tr><td>4</td><td>UCode</td><td>Undertaking code (constant over years)</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for the United Kingdom + 3-digit number</td><td>Text</td><td>5 </td><td>XX</td></tr>
<tr><td>5</td><td>UName</td><td>Name of undertaking</td><td></td><td>Text</td><td>100 </td><td></td></tr>
<tr><td>6</td><td>CountID</td><td>Country in which undertaking is based</td><td>ISO-3166-alpha2 nomenclature except ‘UK’ for United Kingdom</td><td>Text</td><td>2 </td><td>XX</td></tr>
<tr><td>7</td><td>IntFret</td><td>Freight transport activity: international</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>8</td><td>Natfret</td><td>Freight transport activity: national</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>9</td><td>Intpass</td><td>passenger transport activity: international</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>10</td><td>Natpass</td><td>passenger transport activity: national</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>11</td><td>DsetA</td><td>Data included in Annex A</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>12</td><td>DsetB</td><td>Data included in Annex B</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>13</td><td>DsetC</td><td>Data included in Annex C</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>14</td><td>DsetD</td><td>Data included in Annex D</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>15</td><td>DsetE</td><td>Data included in Annex E</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>16</td><td>DsetF</td><td>Data included in Annex F</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>17</td><td>DsetG</td><td>Data included in Annex G</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>18</td><td>DsetH</td><td>Data included in Annex H</td><td><table><tbody><tr><td>1</td><td>:</td><td>YES</td></tr>
<tr><td>0</td><td>:</td><td>NO</td></tr>
</tbody>
</table>
</td><td>Text</td><td>1 </td><td></td></tr>
<tr><td>19</td><td>Tonnes</td><td>Total freight transport (in tonnes)</td><td>Tonnes</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>20</td><td>Tkm</td><td>Total freight transport (1 000 tkm)</td><td>1 000 Tonne-kilometre</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>21</td><td>Pass</td><td>Total passenger transport (in passenger)</td><td>Number of passengers</td><td>Numeric</td><td>10 </td><td></td></tr>
<tr><td>22</td><td>Passkm</td><td>Total passenger transport (1 000 passenger-km)</td><td>1 000 passenger-km</td><td>Numeric</td><td>10 </td><td></td></tr>
</tbody>
</table>

In the flat file containing the data for Annex I, each record comprises of 22 fields. The following table shows all fields in grey because there is only one table in Annex I. Optional fields may be left empty. An asterisk indicates a key field. The combination of the values of the key fields for a record must constitute a unique key value within the file. If duplicate key values are found, the file will not be loaded correctly.

| Field number | Field name | DsetID I1 |
| --- | --- | --- |
| 1 | RCount | * |
| 2 | DsetID | * |
| 3 | Year | * |
| 4 | UCode | * |
| 5 | UName (7) |  |
| 6 | CountID |  |
| 7 | IntFret |  |
| 8 | Natfret |  |
| 9 | Intpass |  |
| 10 | Natpass |  |
| 11 | DsetA |  |
| 12 | DsetB |  |
| 13 | DsetC |  |
| 14 | DsetD |  |
| 15 | DsetE |  |
| 16 | DsetF |  |
| 17 | DsetG |  |
| 18 | DsetH |  |
| 19 | Tonnes (8) |  |
| 20 | Tkm (9) |  |
| 21 | Pass (10) |  |
| 22 | Passkm (11) |  |

**3\. MISSING VALUES**

For certain fields, Eurostat may recommend the use of specific codes for missing values or other special values (see column ‘specific codes for missing values’).

Additional information is provided in the Guidelines for the implementation of Regulation (EC) No 91/2003.

**4\. ALTERNATIVE STANDARD FORMATS**

Member States may use other standard formats which support the abovementioned data structures, where these are proposed by Eurostat.

**5\. VALIDATION OF DATA BY EUROSTAT**

Eurostat will apply some validation checks to the data transmitted by Member States, before the data are loaded into the production database. Where a significant number of records fail these checks, Eurostat will notify the Member State of the records in error and indicate the reasons for non-acceptance. The Member State will be requested to rectify the errors noted and then to re-submit the complete dataset (not just the records that were in error). This procedure is necessary in order to guarantee the correctness of the data within and between different datasets.

**6\. NAMING OF DATASET FILE**

The following file naming convention must be used:

‘ RAIL_annex_frequency_CC_YYYY_period[_OptionalField].format ’ where:

<table>
<tbody><tr><td>RAIL</td><td>For RAIL data</td></tr>
<tr><td>Annex</td><td>Dataset identification (i.e. Annex of the Regulation):<table><tbody><tr><td>A</td><td>:</td><td>Annual statistics on goods transport — detailed reporting</td></tr>
<tr><td>B</td><td>:</td><td>Annual statistics on goods transport — simplified reporting</td></tr>
<tr><td>C</td><td>:</td><td>Annual statistics on passenger transport — detailed reporting</td></tr>
<tr><td>D</td><td>:</td><td>Annual statistics on passenger transport — simplified reporting</td></tr>
<tr><td>E</td><td>:</td><td>Quarterly statistics on goods and passenger transport</td></tr>
<tr><td>F</td><td>:</td><td>Regional statistics on goods and passenger transport</td></tr>
<tr><td>G</td><td>:</td><td>Statistics on traffic flows on the rail network</td></tr>
<tr><td>H</td><td>:</td><td>Statistics on accidents</td></tr>
<tr><td>I</td><td>:</td><td>List of Railway undertakings</td></tr>
</tbody>
</table>
</td></tr>
<tr><td>Frequency</td><td>A for Annual Q for Quarterly  5 for every five years </td></tr>
<tr><td>CC</td><td>Reporting country: use ISO3166-alpha2 except ‘UK’ for United Kingdom</td></tr>
<tr><td>YYYY</td><td>Year of reference (e.g. 2004)</td></tr>
<tr><td>Period</td><td>‘0000’ for Annual ‘0001’ for the first quarter  ‘0002’ for the second quarter  ‘0003’ for the third quarter  ‘0004’ for the fourth quarter  ‘0005’ for quinquennial </td></tr>
<tr><td>[_OptionalField]</td><td>Can contain any chain of 1 to 220 characters (only ‘A’ to ‘Z’, ‘0’ to ‘9’ or ‘_’ are allowed). This field is not interpreted by Eurostat tools.</td></tr>
<tr><td>.format</td><td>File format: ( e.g. ‘CSV’ for Comma Separated Value, ‘GES’ for GESMES)</td></tr>
</tbody>
</table>

One file has to be sent for each annex of the Regulation and period.

Example:

The file ‘RAIL_E_Q_FR_2004_0002.csv’ is the data file that contains the data from France for Annex E of the Regulation, covering the second quarter of the year 2004.

**7\. TRANSMISSION METHOD**

Data shall be transmitted or uploaded by electronic means to the single entry point for data at Eurostat. This method assures the secure transmission of confidential data.

(1) OJ L 52, 22.2.1997, p. 1.

(2) OJ L 151, 15.6.1990, p. 1.

(3) Table A5 is an optional table.

(4) Provisional data.

(5) Final consolidated data.

(6) Number of serious injury accidents (NbAccInj) is an optional variable in table H1.

(7) Name of undertaking (UName) is an optional variable.

(8) Total freight transport (in tonnes) is an optional variable.

(9) Total freight transport (in 1 000 tkm) (Tkm) is an optional variable.

(10) Total passenger transport (in passengers) (Pass) is an optional variable.

(11) Total passenger transport (in 1 000 pkm) (Passkm) is an optional variable.
