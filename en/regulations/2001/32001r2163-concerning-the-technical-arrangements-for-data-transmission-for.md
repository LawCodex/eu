---
title: "Commission Regulation (EC) No 2163/2001 of 7 November 2001 concerning the technical arrangements for data transmission for statistics on the carriage of goods by road (Text with EEA relevance)"
identifier: "32001R2163"
eli: "http://data.europa.eu/eli/reg/2001/2163/oj"
type: regulation
jurisdiction: eu
language: en
date: 2001-11-07
entry_into_force: 2001-03-14
last_amended: 2008-01-01
consolidated_version: "02001R2163-20080101"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02001R2163-20080101"
retrieved: 2026-10-11
---

# Commission Regulation (EC) No 2163/2001 of 7 November 2001 concerning the technical arrangements for data transmission for statistics on the carriage of goods by road (Text with EEA relevance)

**COMMISSION REGULATION (EC) No 2163/2001**

**of 7 November 2001**

**concerning the technical arrangements for data transmission for statistics on the carriage of goods by road**

**(Text with EEA relevance)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td>COMMISSION REGULATION (EC) No 973/2007 of 20 August 2007</td><td> L 216</td><td>10</td><td>21.8.2007</td></tr>
</table>

**COMMISSION REGULATION (EC) No 2163/2001**

**of 7 November 2001**

**concerning the technical arrangements for data transmission for statistics on the carriage of goods by road**

**(Text with EEA relevance)**

THE COMMISSION OF THE EUROPEAN COMMUNITIES,

Having regard to the Treaty establishing the European Community,

Having regard to Council Regulation (EC) No 1172/98 of 25 May 1998 on statistical returns in respect of the carriage of goods by road ( 1 ), as amended by Commission Regulation (EC) No 2691/1999 ( 2 ), and in particular Article 5(2) and Article 9 thereof,

Whereas:

(1) In accordance with Article 5(2) of Regulation (EC) No 1172/98, the Commission shall determine the arrangements for the transmission of data by the Member States.

(2) It is necessary to specify the format in which the data are to be transmitted to Eurostat in sufficient detail to ensure that the data can be processed rapidly and in a cost effective way.

(3) This Regulation does not change the status of the variables which are declared optional in Regulation (EC) No 1172/98.

(4) The measures provided for in this Regulation are in accordance with the opinion of the Statistical Programme Committee, set up by Council Decision 89/382/EEC, Euratom ( 3 ),

HAS ADOPTED THIS REGULATION:

## Article 1

The technical format for the transmission of data to the Commission (Eurostat) is defined in the Annex to this Regulation.

Member States shall use this format for the data concerning the 2002 reference year and subsequent years.

## Article 2

Member States shall transmit to the Commission (Eurostat) the data and metadata required by this Regulation in electronic form, in conformity with an interchange standard proposed by the Commission (Eurostat).

## Article 3

This Regulation shall enter into force on the 20th day following its publication in the Official Journal of the European Communities.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

## ANNEX — TECHNICAL FORMAT FOR DATA TRANSMISSION

**1\. DATA STRUCTURE**

The individual data records for each quarter, which are to be sent to Eurostat, shall consist of three linked data sets covering:

A1 vehicle-related variables

A2 journey-related variables

A3 goods-related variables (in the basic transport operation).

Each A1 ‘vehicle record’ is linked to 1-n ‘journey records’ (A2 data set) which contain data on the journeys made by that vehicle during the survey period (normally one week). Each journey record is in turn linked to 0-m ‘goods records’ (A3 data set) which contain data on the basic transport operations which make up that journey.

Figure 1 illustrates the structure of the data.

It should be noted that there may not be multiple goods records for each journey record. ![image](http://publications.europa.eu/resource/celex/02001R2163-20080101.ENG.xhtml.L_2001291EN.01001402.tif.jpg) For laden journeys, depending on the method used to record journeys, and/or on the type of journey, there may be only one goods record linked to each journey record. For unladen journeys, there shall normally be no linked goods records (although the existence of linked goods records for empty journeys is permitted).

The ‘Methodological appendix’ in Annex A to Regulation (EC) No 1172/98 provides further information.

**2\. LIST OF FIELDS**

The following information is provided for each field:

— field number: this identifies the position of the field in the record,

— variable: this is either the reference to the variable in Regulation (EC) No 1172/98, or an internal identifier,

— description: short description of the contents of the field,

— coding: variables are to be coded according to Annexes A to G of Regulation (EC) No 1172/98. Additional coding rules are noted here. Further explanations and recommendations on coding may be provided by Eurostat in the reference manual for the implementation of Regulation (EC) No 1172/98,

— field type: indicates whether field contains a numeric quantity or a text string,

— except for variable A1.9, all numeric fields are to be provided as integers,

— variable A1.9 shall have a comma (‘,’) as the decimal separator,

— optional variable: a flag for variables which are optional according to Annex A to Regulation (EC) No 1172/98,

— maximum length: the maximum expected length of the data for this field. Data which are too long cannot be loaded,

— key field: the combination of the values of the key fields for a data set must constitute a unique key value within that data set. If duplicate key values are found, the loading of the data set and its linked data sets is blocked, since the vehicle, journey and goods records cannot be correctly linked.

**Data Set A1: Vehicle-related variables**

<table>
<tbody><tr><td>Field number</td><td>Variable</td><td>Description</td><td>Coding</td><td>Field type</td><td>* = optional variable</td><td>Maximum length</td><td>* = key field</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>(1)</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>2</td><td>DSetID</td><td>Data set identifier</td><td>A1</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the data set</td><td>4 digits</td><td>Text</td><td></td><td>4</td><td>*</td><td></td></tr>
<tr><td>4</td><td>Quarter</td><td>Quarter of the data set</td><td>Q1, Q2, Q3 or Q4</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>5</td><td>QuestN</td><td>Questionnaire identifier</td><td></td><td>Text</td><td></td><td>9</td><td>*</td><td></td></tr>
<tr><td>6</td><td>A1.1</td><td>Possibility of using vehicle for combined transport</td><td>To be developed</td><td>Text</td><td>*</td><td>1</td><td></td><td></td></tr>
<tr><td>7</td><td>A1.3</td><td>Age of the road motor vehicle (lorry or road tractor)</td><td>Years from first registration</td><td>Numeric</td><td></td><td>2</td><td></td><td>99</td></tr>
<tr><td>8</td><td>A1.6</td><td> NACE Rev. 2   activity class of the vehicle operator</td><td>NACE 4-digit level</td><td>Text</td><td>*</td><td>5</td><td></td><td></td></tr>
<tr><td>9</td><td>A1.8.1</td><td>Total vehicle kilometres during the survey period — loaded</td><td>km</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>10</td><td>A1.8.2</td><td>Total vehicle kilometres during the survey period — empty (including road tractor journeys without semi-trailer)</td><td>km</td><td>Numeric</td><td>*</td><td>4</td><td></td><td></td></tr>
<tr><td>11</td><td>A1.9</td><td>Vehicle weighting to be used to get full results from individual data, if the collection of data is carried out from a sample</td><td></td><td>Numeric</td><td></td><td>8</td><td></td><td></td></tr>
<tr><td>12</td><td>Stratum</td><td>Stratum identifier of sample in which vehicle appears</td><td></td><td>Text</td><td></td><td>7</td><td></td><td></td></tr>
<tr><td>13</td><td>A2 link</td><td>Number of linked A2 records</td><td>Numeric</td><td>Numeric</td><td></td><td>5</td><td></td><td></td></tr>
<tr><td colspan="9">(1) This variable shall be coded using the country codes in Annex G to Regulation (EC) No 1172/98.</td></tr>
</tbody>
</table>

**Data set A2: Journey-related variables**

<table>
<tbody><tr><td>Field number</td><td>Variable</td><td>Description</td><td>Coding</td><td>Field type</td><td>* = optional variable</td><td>Maximum length</td><td>* = key field</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>(1)</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>2</td><td>DSetID</td><td>Data set identifier</td><td>A2</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the data set</td><td>4 digits</td><td>Text</td><td></td><td>4</td><td>*</td><td></td></tr>
<tr><td>4</td><td>Quarter</td><td>Quarter of the data set</td><td>Q1, Q2, Q3 or Q4</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>5</td><td>QuestN</td><td>Questionnaire identifier</td><td></td><td>Text</td><td></td><td>9</td><td>*</td><td></td></tr>
<tr><td>6</td><td>JournN</td><td>Journey identifier</td><td></td><td>Text</td><td></td><td>5</td><td>*</td><td></td></tr>
<tr><td>7</td><td>A1.2</td><td>Axle configuration</td><td>Annex B Regulation (EC) No 1172/98</td><td>Text</td><td>*</td><td>3</td><td></td><td></td></tr>
<tr><td>8</td><td>A1.4</td><td>Maximum permissible laden weight</td><td>100 kg</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>9</td><td>A1.5</td><td>Load capacity</td><td>100 kg</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>10</td><td>A1.7</td><td>Type of transport</td><td>Annex A to Regulation (EC) No 1172/98</td><td>Text</td><td></td><td>1</td><td></td><td>9</td></tr>
<tr><td>11</td><td>A2.1</td><td>Type of journey</td><td>Annex C Regulation (EC) No 1172/98</td><td>Text</td><td></td><td>1</td><td></td><td></td></tr>
<tr><td>12</td><td>A2.2</td><td>Weight of goods</td><td>Gross weight in 100 kg</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>13</td><td>A2.3</td><td>Place of loading (of the goods road motor vehicle, for a laden journey)</td><td>(2)</td><td>Text</td><td></td><td>5</td><td></td><td>XX</td></tr>
<tr><td>14</td><td>A2.4</td><td>Place of unloading (of the goods road motor vehicle, for a laden journey)</td><td>(2)</td><td>Text</td><td></td><td>5</td><td></td><td>XX</td></tr>
<tr><td>15</td><td>A2.5</td><td>Distance travelled: actual distance excluding the distance covered by the goods road motor vehicle while being transported by another means of transport</td><td>km</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>16</td><td>A2.6</td><td>Tonnes x km effected during the journey</td><td>tonne/km</td><td>Numeric</td><td></td><td>8</td><td></td><td></td></tr>
<tr><td>17</td><td>A2.7</td><td>Countries crossed in transit (not more than 5)</td><td>(2)</td><td>Text</td><td></td><td>10</td><td></td><td></td></tr>
<tr><td>18</td><td>A2.8</td><td>Place of loading, if any, of the goods road motor vehicle on another means of transport</td><td>(2)</td><td>Text</td><td>*</td><td>5</td><td></td><td>XX</td></tr>
<tr><td>19</td><td>A2.9</td><td>Place of unloading, if any, of the goods road motor vehicle from another means of transport</td><td>(2)</td><td>Text</td><td>*</td><td>5</td><td></td><td>XX</td></tr>
<tr><td>20</td><td>A2.10</td><td>Degree of loading of vehicle (in terms of maximum volume of space used during the journey)</td><td></td><td>Text</td><td>*</td><td>1</td><td></td><td>9</td></tr>
<tr><td>21</td><td>A3 link</td><td>Number of linked A3 records</td><td></td><td>Numeric</td><td></td><td>8</td><td></td><td></td></tr>
<tr><td colspan="9">(1) This variable shall be coded using the country codes in Annex G to Regulation (EC) No 1172/98. (2) This variable shall be coded according to the rules set out in Annex G to Regulation (EC) No 1172/98. </td></tr>
</tbody>
</table>

**Data set A3: Goods-related variables (in the basic transport operation)**

<table>
<tbody><tr><td>Field number</td><td>Variable</td><td>Description</td><td>Coding</td><td>Field type</td><td>* = optional variable</td><td>Maximum length</td><td>* = key field</td><td>Specific codes for missing values</td></tr>
<tr><td>1</td><td>RCount</td><td>Reporting country</td><td>(1)</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>2</td><td>DSetID</td><td>Data set identifier</td><td>A3</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>3</td><td>Year</td><td>Year of the data set</td><td>4 digits</td><td>Text</td><td></td><td>4</td><td>*</td><td></td></tr>
<tr><td>4</td><td>Quarter</td><td>Quarter of the data set</td><td>Q1, Q2, Q3 or Q4</td><td>Text</td><td></td><td>2</td><td>*</td><td></td></tr>
<tr><td>5</td><td>QuestN</td><td>Questionnaire identifier</td><td></td><td>Text</td><td></td><td>9</td><td>*</td><td></td></tr>
<tr><td>6</td><td>JournN</td><td>Journey identifier</td><td></td><td>Text</td><td></td><td>4</td><td>*</td><td></td></tr>
<tr><td>7</td><td>GoodsN</td><td>Goods operation identifier</td><td></td><td>Text</td><td></td><td>6</td><td>*</td><td></td></tr>
<tr><td>8</td><td>A3.1</td><td>Type of goods, according to the groups referring to an appropriate classification</td><td>Annex D to Regulation (EC) No 1172/98 (NST/R)</td><td>Text</td><td></td><td>2</td><td></td><td></td></tr>
<tr><td>9</td><td>A3.2</td><td>Weight of goods</td><td>Gross weight in 100 kg</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td>10</td><td>A3.3</td><td>Classification of dangerous goods</td><td>Annex E to Regulation (EC) No 1172/98 (main categories of Directive 94/55/EC)</td><td>Text</td><td></td><td>3</td><td></td><td></td></tr>
<tr><td>11</td><td>A3.4</td><td>Type of cargo</td><td>Annex F to Regulation (EC) No 1172/98 (1-digit level of UN Recommendation No 21)</td><td>Text</td><td>*</td><td>1</td><td></td><td></td></tr>
<tr><td>12</td><td>A3.5</td><td>Place of loading of the goods</td><td>(2)</td><td>Text</td><td></td><td>5</td><td></td><td>XX</td></tr>
<tr><td>13</td><td>A3.6</td><td>Place of unloading of the goods</td><td>(2)</td><td>Text</td><td></td><td>5</td><td></td><td>XX</td></tr>
<tr><td>14</td><td>A3.7</td><td>Distance travelled, actual distance excluding the distance covered with the goods road motor vehicle while being transported by another means of transport</td><td>km</td><td>Numeric</td><td></td><td>4</td><td></td><td></td></tr>
<tr><td colspan="9">(1) This variable shall be coded using the country codes in Annex G to Regulation (EC) No 1172/98. (2) This variable shall be coded according to the rules set out in Annex G to Regulation (EC) No 1172/98. </td></tr>
</tbody>
</table>

**3\. MISSING VALUES**

By default, missing values in data records shall be coded as an empty field (no data between two successive field separators). For certain fields, Eurostat may recommend the use of specific codes for missing values or other special values (see column ‘specific codes for missing values’).

Additional information is provided in the reference manual for the implementation of Regulation (EC) No 1172/98 on statistics on the carriage of goods by road.

**4\. CHANGE IN CONFIGURATION OR TYPE OF TRANSPORT**

Annex A to Regulation (EC) No 1172/98 noted that during a survey period a vehicle might be subject to a change in configuration (addition of a trailer giving rise to a change in axle configuration and load capacity) or the type of transport might vary between journeys. These changes should be recorded, although this is not obligatory.

In order to permit the transmission of these data within the normal data structures described here, the variables A1.2, A1.4, A1.5 and A1.7 shall be transmitted as part of the A2 data set (journey-related variables).

**5\. VALIDATION OF DATA BY EUROSTAT**

Eurostat shall apply some validation checks to the data transmitted by Member States, before the data are loaded into the production database. Where a significant number of records fails these checks, Eurostat shall notify the Member State of the records in error and provide an indication of the reasons for non-acceptance. The Member State shall be requested to rectify the errors noted and then to re-submit the complete set of three data sets for that quarter (not just the records that were in error). This procedure is necessary in order to guarantee the correctness of the weighting factors and the coherence between the vehicle, journey and goods records.

Where the number of records containing errors is very small and the likely effect on any analysis insignificant, Eurostat shall load those records that pass the verification checks and to discard the records in error. In such a case a Member State shall be informed of the records not passing the checks and the reasons. The Member State shall be invited, if it wished, to correct the errors found and to resubmit the complete set of three data sets for that quarter (not just the records that were in error). Where a re-submission is made, Eurostat shall load the revised data but if no re-submission is made, Eurostat shall use the date already accepted for the preparation of aggregated tables.

**6\. NAMING OF DATA SETS**

Names of data sets shall be, according to the Stadium requirements, in the form ‘CCYYQnROADAx.ZZZ’ where:

CC Reporting country

YY 2 last digits of the year (e.g. ‘01’ for year 2001)

Qn Quarter: n = 1 to 4

ROADAx Data set identification:

A1: vehicle data set

A2: journey data set

A3: goods data set

.ZZZ data set type:

.dat: individual data sets

.zip: compressed data set in Pkzip or WinZip format

Examples:

1\. The data set ‘ES99Q2ROADA1.zip’ is a compressed ‘zip’ data set containing the A1 data set for Spain, year 1999 and quarter 2 (‘ES99Q2ROADA1.dat’).

2\. The data set ‘UK99Q3ROADA2.dat’ is the data set that contains for United Kingdom, year 1999, quarter 3, the data set A2.

The above specified data set name has to appear in the subject line of the electronic mail.

**7\. TRANSMISSION MEDIA**

The preferred transmission support is Stadium, sent to an address to be notified by Eurostat. Note that electronic mail is subject to maximum size limits which may exclude its use for large data sets.

**8\. TRANSITIONAL PERIOD**

In a transitional period, the data may also be sent in ASCII data sets with variable-length fields. The semi-colon (‘;’) is used as the field separator.

All fields must be present even if they are empty (that is, two successive field separators).

Additional spaces in the data fields shall be ignored, unless the specific instructions for a field prohibit the presence of additional spaces.

Furthermore during this transitional period Eurostat shall also support the reception of data by post on diskettes or recordable compact disks (CD-R). Data shall not be accepted on magnetic tapes or on paper.

Where data are to be sent by electronic mail, the following rules shall apply in a transitional period:

— data shall be sent in the form of attached data sets,

— only one data set at a time can be attached to each message,

— the name of the data set shall be used as the subject of the message,

— comments on data (such as methodological notes, remarks on the quality of the data, etc.) can be entered as plain text in the body of the message to which a data data set is attached. Formatted text shall not be used,

— comments on data may also be sent as a separate plain text message (without an attached data data set) using the subject field: ‘CCYYQnROADAx.rem’. Formatted text shall not be used,

— corrections: to correct a data file previously transmitted to Eurostat, the corrected data set shall be sent with the same data set name, together with an explanatory note in plain text format in the body of the e-mail.

( 1 ) OJ L 163, 6.6.1998, p. 1.

( 2 ) OJ L 326, 18.12.1999, p. 39.

( 3 ) OJ L 181, 28.6.1989, p. 47.
