---
title: "Commission Implementing Regulation (EU) 2021/1179 of 16 July 2021 amending Implementing Regulation (EU) No 1051/2011 as regards the aggregate tables and micro-data files for the transmission of the data (Text with EEA relevance)"
identifier: "32021R1179"
eli: "http://data.europa.eu/eli/reg_impl/2021/1179/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2021-07-16
entry_into_force: 2021-11-23
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R1179"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2021/1179 of 16 July 2021 amending Implementing Regulation (EU) No 1051/2011 as regards the aggregate tables and micro-data files for the transmission of the data (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2021/1179**

**of 16 July 2021**

**amending Implementing Regulation (EU) No 1051/2011 as regards the aggregate tables and micro-data files for the transmission of the data**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) No 692/2011 of the European Parliament and of the Council of 6 July 2011 concerning European statistics on tourism and repealing Council Directive 95/57/EC (1), and in particular Article 9(2) and (3) thereof,

Whereas:

(1) Commission Implementing Regulation (EU) No 1051/2011 (2) lays down the exchange standard for aggregate tables and micro-data files.

(2) Following the entry into force of Commission Delegated Regulation (EU) 2019/1681 (3) laying down technical changes to the transmission format for annual data to be transmitted to the Commission, it is necessary to adapt Annexes II and III to Implementing Regulation (EU) No 1051/2011 as regards the aggregate tables and micro-data files for transmission of data.

(3) Implementing Regulation (EU) No 1051/2011 should therefore be amended accordingly.

(4) The measures provided for in this Regulation are in accordance with the opinion of the European Statistical System Committee, established by Article 7 of Regulation (EC) No 223/2009 of the European Parliament and of the Council (4),

HAS ADOPTED THIS REGULATION:

## Article 1

Implementing Regulation (EU) No 1051/2011 is amended as follows:

(1) Annex II is amended as follows:

under ‘Header’, the datasets listed in the third indent are amended as follows:

(1) ‘int_cap_annual’ is replaced by ‘TOUR_CAP_A’;

(2) ‘int_occ_annual’ is replaced by ‘TOUR_OCC_A’;

(3) ‘int_occ_mnight’ is replaced by ‘TOUR_NIGHTS_M’;

(4) ‘int_occ_marrno’ is replaced by ‘TOUR_ARRNOCC_M’;

(5) ‘int_non_rented’ is replaced by ‘TOUR_NONRENT_A’;

(6) ‘nat_dem_partic’ is replaced by ‘TOUR_PARTIC_A’;

(7) ‘nat_dem_sdvout’ is replaced by ‘TOUR_SDVOUT_Q’;

(8) ‘nat_dem_sdvdom’ is replaced by ‘TOUR_SDVDOM_Q’;

(2) Annex III is replaced by the text in the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 16 July 2021.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 192, 22.7.2011, p. 17.

(2) Commission Implementing Regulation (EU) No 1051/2011 of 20 October 2011 implementing Regulation (EU) No 692/2011 of the European Parliament and of the Council concerning European statistics on tourism, as regards the structure of the quality reports and the transmission of the data (OJ L 276, 21.10.2011, p. 13).

(3) Commission Delegated Regulation (EU) 2019/1681 of 1 August 2019 amending Regulation (EU) No 692/2011 of the European Parliament and of the Council concerning European statistics on tourism, as regards the transmission deadlines and adaptation of Annexes I and II (OJ L 258, 9.10.2019, p. 1).

(4) Regulation (EC) No 223/2009 of the European Parliament and of the Council of 11 March 2009 on European statistics and repealing Regulation (EC, Euratom) No 1101/2008 of the European Parliament and of the Council on the transmission of data subject to statistical confidentiality to the Statistical Office of the European Communities, Council Regulation (EC) No 322/97 on Community Statistics, and Council Decision 89/382/EEC, Euratom establishing a Committee on the Statistical Programmes of the European Communities (OJ L 87, 31.3.2009, p. 164).

## ANNEX — ‘ANNEX III

**Micro-data files for the transmission of data listed in Section 2 of Annex II to Regulation (EU) No 692/2011**

**File structure and codification: practical arrangements**

Each observed trip shall be an individual record in the transmitted micro-data file. This micro-data file shall be fully checked, edited and, where necessary, imputed, and shall follow the file structure and codification described in the table below. The Commission (Eurostat) will supply additional guidance on the format for transmission.

Data that does not respect the exchange standard set out in this Annex will be considered as not having been sent.

**Header**

The purpose of the header is to identify the transmitted data series. It shall consist of four fields:

— Reference period shall consist of seven characters, the first four identifying the year and the last three the period within the year (A00).

— Country code shall consist of two characters, containing the two-character country code of the Member State transmitting the data. Examples: BE (Belgium), BG (Bulgaria), …

— Subject shall consist of the identifier of the dataset: nat_dem_microdata.

— Currency identifies the currency in which expenditure is reported (EUR or NAC). While euro area Member States shall provide data in euro (code EUR), non-euro area Member States can report data either in euro or in their national currency (code NAC). However, all expenditure must be reported in the same currency inside one file.

**Data**

| Column name | Identifier | Description | Filter/remarks |
| --- | --- | --- | --- |
| ID | 000001-999999 | Sequence number of the trip |  |
|  |  | CHARACTERISTICS OF THE TRIP |  |
| Field 1 |  | Month of departure |  |
|  | 01-24 | Number of the month (January of the reference year = 01, December of the reference year = 12; January of the previous calendar year = 13, December of the previous calendar year = 24) |  |
| Field 2 |  | Duration of the trip in number of nights |  |
|  | 001-366 | Number of nights (3 digits maximum) |  |
| Field 3 |  | Duration of the trip: number of nights spent on the domestic territory | Only for outbound trips Triennial variable, in the optional years: code = Blank |
|  | 000-183 | Number of nights (3 digits maximum) |  |
| Field 4 |  | Main country of destination |  |
|  |  | Coding according to the country list in the methodological manual drawn up under Article 10 of Regulation (EU) No 692/2011 |  |
| Field 5 |  | Main purpose of the trip |  |
|  | 1 | Private/personal purpose: leisure, recreation and holidays |  |
|  | 2 | Private/personal purpose: visiting relatives and friends |  |
|  | 3 | Private/personal purpose: other (e.g. health treatment, pilgrimage) |  |
|  | 4 | Professional/business purpose |  |
|  |  | Type of destination | Triennial variable, in the optional years: code = Blank |
| Field 6 | 1 | City = Yes |  |
|  | 2 | City = No |  |
|  | 9 | City = Not applicable (Field 5 = 4) |  |
| Field 7 | 1 | Seaside = Yes |  |
|  | 2 | Seaside = No |  |
|  | 9 | Seaside = Not applicable (Field 5 = 4) |  |
| Field 8 | 1 | Countryside (including lakeside, riverside, etc.) = Yes |  |
|  | 2 | Countryside (including lakeside, riverside, etc.) = No |  |
|  | 9 | Countryside (including lakeside, riverside, etc.) = Not applicable (Field 5 = 4) |  |
| Field 9 | 1 | Cruise ship = Yes |  |
|  | 2 | Cruise ship = No |  |
|  | 9 | Cruise ship = Not applicable (Field 5 = 4) |  |
| Field 10 | 1 | Mountains (highlands, hills, etc.) = Yes |  |
|  | 2 | Mountains (highlands, hills, etc.) = No |  |
|  | 9 | Mountains (highlands, hills, etc.) = Not applicable (Field 5 = 4) |  |
| Field 11 | 1 | Other = Yes |  |
|  | 2 | Other = No |  |
|  | 9 | Other = Not applicable (Field 5 = 4) |  |
| Field 12 |  | Participation of children | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
|  | 9 | Not applicable (Field 5 = 4) |  |
| Field 13 |  | Main means of transport |  |
|  | 1 | Air (flights, scheduled or chartered, or other air services) |  |
|  | 2 | Waterway (passenger lines and ferries, cruises, pleasure boat, rented vessel, etc.) |  |
|  | 3 | Railway |  |
|  | 4 | Bus, coach (regular/scheduled or occasional/non-scheduled) |  |
|  | 5 | Regular/scheduled bus or coach | Optional breakdown |
|  | 6 | Occasional/non-scheduled bus or coach | Optional breakdown |
|  | 7 | Private motor vehicle (owned or leased, including friends/relatives’ car) |  |
|  | 8 | Rented motor vehicle (including ride-sharing or car-sharing platforms) |  |
|  | 9 | Other (e.g. bicycle) |  |
| Field 14 |  | Main means of accommodation |  |
|  | 1 | Rented accommodation: hotels or similar establishments |  |
|  | 2 | Rented accommodation: campsites, caravan or trailer park (non-residential) |  |
|  | 3 | Rented accommodation: such as a house, villa or apartment; rented room(s) in a dwelling |  |
|  | 4 | Rented accommodation: other rented accommodation (such as youth hostels, marinas, health establishments) |  |
|  | 5 | Non-rented accommodation: own holiday home |  |
|  | 6 | Non-rented accommodation: accommodation provided free of charge by relatives or friends |  |
|  | 7 | Non-rented accommodation: other non-rented accommodation |  |
| Field 15 |  | Booking of the trip: internet booking of the main means of accommodation | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
| Field 16 |  | Booking of the trip: booking channel for the main means of accommodation | Triennial variable, in the optional years: code = Blank |
|  | 1 | Directly with the accommodation provider |  |
|  | 2 | Via a travel agency, tour operator, portal or short-term property or holiday letting agency listing multiple accommodation providers |  |
|  | 3 | No booking was needed |  |
| Field 17 |  | Booking of the main means of accommodation via a website or app such as Airbnb, Booking.com, Expedia, HomeAway | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
|  | 9 | Not applicable (Field 14 ≠ 3 or Field 15 ≠ 1 or Field 16 ≠ 2) |  |
| Field 18 |  | Booking of the trip: internet booking of the main means of transport | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
| Field 19 |  | Booking of the trip: booking channel for the main means of transport | Triennial variable, in the optional years: code = Blank |
|  | 1 | Directly with the transport provider |  |
|  | 2 | Via a travel agency, tour operator, portal |  |
|  | 3 | No booking was needed |  |
| Field 20 |  | Booking of the main means of transport via a website or app such as BlaBlaCar | Optional triennial variable, if not transmitted: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
|  | 9 | Not applicable (Field 18 ≠ 1 or Field 19 ≠ 2) |  |
| Field 21 |  | Booking of the trip: package trip | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
| Field 22 |  | Booking of the trip: internet booking of the package | Triennial variable, in the optional years: code = Blank |
|  | 1 | Yes |  |
|  | 2 | No |  |
| Field 23 |  | Expenditure related to the trip by the individual tourist on packages |  |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
| Field 24 |  | Expenditure related to the trip by the individual tourist on transport |  |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
| Field 25 |  | Expenditure related to the trip by the individual tourist on accommodation |  |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
| Field 26 |  | Expenditure related to the trip by the individual tourist on food and drinks in cafés and restaurants | Optional variable, if not transmitted: code = Blank |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
| Field 27 |  | Other expenditure related to the trip by the individual tourist (total other, including durables and valuable goods) |  |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
| Field 28 |  | Durables and valuable goods (subcategory of “Other expenditure related to the trip by the individual tourist”) |  |
|  | 00000000-99999998 | Amount in euro (or in national currency for non-euro area Member States) (8 digits maximum) |  |
|  |  | Profile of the visitor |  |
| Field 29 |  | Gender |  |
|  | 1 | Male |  |
|  | 2 | Female |  |
| Field 30 |  | Age |  |
|  | 000-198 | Number of full years (3 digits) |  |
| Field 31 |  | Country of residence |  |
|  |  | The two-digit country code (Belgium = BE, Bulgaria = BG, ...) |  |
| Field 32 |  | Educational attainment level | Optional variable, if not transmitted: code = Blank |
|  | 1 | At most lower secondary (ISCED 2011 levels 0-2) |  |
|  | 2 | Upper secondary and post-secondary (non-tertiary) (ISCED 2011 levels 3 and 4) |  |
|  | 3 | Tertiary (ISCED 2011 levels 5-8) |  |
| Field 33 |  | Employment situation | Optional variable, if not transmitted: code = Blank |
|  | 1 | Employed (employee or self-employed) |  |
|  | 2 | Unemployed |  |
|  | 3 | Student (or pupil) |  |
|  | 4 | Other not in the labour force |  |
| Field 34 |  | Household income in quartiles | Optional variable, if not transmitted: code = Blank’ |
|  | 1 | 1st quartile |  |
|  | 2 | 2nd quartile |  |
|  | 3 | 3rd quartile |  |
|  | 4 | 4th quartile |  |
|  |  | Grossing-Up factor |  |
|  |  | Grossing-up factor from sample to population |  |
| Field 35 | 000000-999999 | Field 35 contains integers |  |
| Field 36 | 000-999 | Field 36 contains decimal places |  |
