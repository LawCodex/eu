---
title: "Commission Implementing Regulation (EU) 2022/79 of 19 January 2022 laying down rules for the application of Regulation (EU) 2021/1139 of the European Parliament and of the Council as regards the recording, transmission and presentation of operation-level implementation data"
identifier: "32022R0079"
eli: "http://data.europa.eu/eli/reg_impl/2022/79/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2022-01-19
entry_into_force: 2022-11-10
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0079"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2022/79 of 19 January 2022 laying down rules for the application of Regulation (EU) 2021/1139 of the European Parliament and of the Council as regards the recording, transmission and presentation of operation-level implementation data

**COMMISSION IMPLEMENTING REGULATION (EU) 2022/79**

**of 19 January 2022**

**laying down rules for the application of Regulation (EU) 2021/1139 of the European Parliament and of the Council as regards the recording, transmission and presentation of operation-level implementation data**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2021/1139 of the European Parliament and of the Council of 7 July 2021 establishing the European Maritime, Fisheries and Aquaculture Fund and amending Regulation (EU) 2017/1004 (1), in particular Article 46(4) thereof,

Whereas:

(1) Article 46(3) of Regulation (EU) 2021/1139 (‘the EMFAF Regulation’) establishes a framework for shared management by requiring the Member States’ managing authorities to provide the Commission with relevant operation-level implementation data. This data should include the key characteristics of each beneficiary and each operation supported by the EMFAF under shared management. This requirement complements that established in Article 42 of Regulation (EU) 2021/1060 of the European Parliament and of the Council (2) concerning the transmission of cumulative data for each programme.

(2) In order to ensure consistency and completeness of the data, for both managing authorities and for the Commission, it is necessary to provide a common format as well as common technical specifications and rules for the presentation of that data.

(3) The measures provided for in this Regulation should apply promptly, to facilitate consistent recording of data from the beginning of programme implementation.

(4) The measures provided for in this Regulation are in accordance with the opinion of the Committee for the European Maritime, Fisheries and Aquaculture Fund,

HAS ADOPTED THIS REGULATION:

## Article 1 — Subject matter

This Regulation sets out rules for the recording, transmission and presentation of the operation-level implementation data referred to in Article 46(3) of Regulation (EU) 2021/1139 (‘implementation data’).

## Article 2 — Recording and transmission of implementation data

Managing Authorities shall record and provide the Commission with implementation data for each operation supported under shared management in line with the format set out in Annex I.

## Article 3 — Presentation of data

Managing Authorities shall present the implementation data referred to in Article 2 in accordance with the specifications provided for in the tables set out in Annex II.

## Article 4 — Entry into force

This Regulation shall enter into force on the day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 19 January 2022.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 247, 13.7.2021, p. 1.

(2) Regulation (EU) 2021/1060 of the European Parliament and of the Council of 24 June 2021 laying down common provisions on the European Regional Development Fund, the European Social Fund Plus, the Cohesion Fund, the Just Transition Fund and the European Maritime, Fisheries and Aquaculture Fund and financial rules for those and for the Asylum, Migration and Integration Fund, the Internal Security Fund and the Instrument for Financial Support for Border Management and Visa Policy (OJ L 231, 30.6.2021, p. 159).

## ANNEX I — FORMAT FOR THE TRANSMISSION OF DATA

**Table 1**

**Operation description**

<table>
<tbody><tr><td>Field</td><td>Content of field</td><td>Field Type</td><td>Field Length</td><td>Storage Format</td><td>Comment</td><td>Link with Annex VII of CPR</td></tr>
<tr><td>01</td><td>CCI</td><td>text</td><td>15 </td><td></td><td>Common code of identification of the programme. Not applicable for direct and indirect management. </td><td></td></tr>
<tr><td>02</td><td>Unique Identifier of the Operation (ID)</td><td>text</td><td>255 </td><td></td><td>Required for all operations supported by the EMFAF.</td><td>Table 1, field 13. Table 4, field 6. Table 5, fields 11, 12. </td></tr>
<tr><td>03</td><td>Description of the operation</td><td>text</td><td>255 </td><td></td><td>Required for all operations supported by the EMFAF.</td><td></td></tr>
<tr><td>04</td><td>Common fleet register (CFR) number</td><td>long text</td><td>63 999 </td><td></td><td>Where relevant. Common fleet register (CFR) number as per Commission Implementing Regulation (EU) 2017/218 (1) <table><tbody><tr><td>—</td><td>one vessel per operation: CFR number</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>more than one vessel per operation: CFR numbers as CSV (Character Separated Values). Semicolon “;” shall be used as separator.</td></tr>
</tbody>
</table>
 No blanks, no quotation marks. </td><td></td></tr>
<tr><td>05</td><td>Sector the operation is contributing to</td><td>text</td><td>2 </td><td></td><td>See code in Table 1 of Annex II. Only one option can be selected. </td><td></td></tr>
<tr><td>06</td><td>Specific objective</td><td>text</td><td>5 </td><td></td><td>For shared management: see nomenclature in Annex II of the EMFAF Regulation. For direct and indirect management: see nomenclature in the work programme adopted pursuant to Article 10 of the EMFAF Regulation. </td><td></td></tr>
<tr><td>07</td><td>NUTS code</td><td>text</td><td>5 </td><td></td><td>Only NUTS versions valid during the programming period, i.e. NUTS Classification 2021 or later. See Commission Delegated Regulation 2019/1755 of 8 August 2019 or https://ec.europa.eu/eurostat/web/nuts/background. No spaces. NUTS 3 by default, NUTS 2 to national level as appropriate if the operation relates to a larger region or the whole Member State. “TCX1” for operations in third countries. </td><td></td></tr>
<tr><td>08</td><td>Name of beneficiary</td><td>text</td><td>255 </td><td></td><td></td><td></td></tr>
<tr><td>09</td><td>Beneficiary code</td><td>text</td><td>250 </td><td></td><td>Unique code. For shared management: based on the national application system. </td><td></td></tr>
<tr><td>10</td><td>Type of beneficiary</td><td>text</td><td>2 </td><td></td><td>See code in Table 2 of Annex II. Only one option can be selected. </td><td></td></tr>
<tr><td>11</td><td>Gender of beneficiary/natural person</td><td>text</td><td>2 </td><td></td><td>See code in Table 3 of Annex II. Only one option can be selected. </td><td></td></tr>
<tr><td>12</td><td>Number of people directly involved in the operation</td><td>number</td><td></td><td>long integer</td><td>Excludes contractors and people/employees not directly participating in the operation.</td><td></td></tr>
<tr><td>13</td><td>Number of partners involved in the operation</td><td>number</td><td></td><td>long integer</td><td></td><td></td></tr>
<tr><td>14</td><td>Lead partner</td><td>text</td><td>2 </td><td></td><td>See code in Table 4 of Annex II.</td><td></td></tr>
<tr><td>15</td><td>Indication as to whether the operation relates to marine, inland, or both</td><td>text</td><td>2 </td><td></td><td>See code in Table 5 of Annex II.</td><td></td></tr>
<tr><td>16</td><td>State of progress of the operation</td><td>text</td><td>2 </td><td></td><td>See code in Table 6 of Annex II.</td><td>Table 1, field 13. Table 4, field 6. Table 5, fields 11, 12. Table 9, fields 11, 12, 13, 14. </td></tr>
<tr><td>17</td><td>Total eligible cost (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td></td></tr>
<tr><td>18</td><td>Total eligible public cost (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td>Table 1, field 8. Table 4, field 4. </td></tr>
<tr><td>19</td><td>EMFAF support (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td>Table 1, field 9.</td></tr>
<tr><td>20</td><td>Date of approval of application for support</td><td>date</td><td></td><td>dd/mm/yyyy</td><td></td><td></td></tr>
<tr><td>21</td><td>Total eligible expenditure (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td></td></tr>
<tr><td>22</td><td>Total eligible public expenditure (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td>Table 1, field 11. Table 4, field 5. </td></tr>
<tr><td>23</td><td>EMFAF eligible expenditure (EUR)</td><td>number</td><td></td><td>double</td><td>No currency sign.</td><td></td></tr>
<tr><td>24</td><td>Date of final payment to beneficiary</td><td>date</td><td></td><td>dd/mm/yyyy</td><td></td><td></td></tr>
<tr><td>25</td><td>Type of intervention</td><td>text</td><td>2 </td><td></td><td>For shared management: see codes in Annex IV of the EMFAF Regulation. For direct and indirect management: see codes in Table 9 of Annex II. </td><td>Table 4, field 3.</td></tr>
<tr><td>26</td><td>Type of operation</td><td>text</td><td>2 </td><td></td><td>See code in Table 7 of Annex II</td><td></td></tr>
<tr><td>27</td><td>Increase of the gross tonnage of a fishing vessel under Article [19(3)] of the EMFAF Regulation</td><td>number</td><td></td><td>double</td><td>Amount of additional GT. Blank in case operation not related to Article [19(3)]. </td><td></td></tr>
<tr><td>28</td><td>Description of the fleet segment relevant to field 27</td><td>text</td><td>255 </td><td></td><td>If relevant, description of the fleet segment(s) of origin of the gross tonnage allocated to the vessel benefitting from the operation as presented in the annual report foreseen under Article 22(2) of Regulation (EU) No 1380/2013 of the European Parliament and of the Council, in line with Commission guidelines COM(2014)545.</td><td></td></tr>
<tr><td>29</td><td>Operation relevant to small-scale coastal fishing (SSCF)</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>30</td><td>Operation relevant to the landing obligation</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>31</td><td>Operation relevant to climate change</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>32</td><td>Operation relevant to non-discrimination</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>33</td><td>Operation relevant to gender equality</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>34</td><td>Operation relevant to rights of people with disabilities</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
<tr><td>35</td><td>Form of support</td><td>text</td><td>2 </td><td></td><td>See code in Table 8 of Annex II. Only one option can be selected. </td><td></td></tr>
<tr><td>36</td><td>Did the beneficiary previously receive EMFF/EMFAF support?</td><td>text</td><td>2 </td><td></td><td>Only 01 or 02 allowed. See code in Table 4 of Annex II. </td><td></td></tr>
</tbody>
</table>

**Table 2**

**Indicators applicable to the operation**

| Field | Content of field | Type | Length | Format | Comment | Link with Annex VII of CPR: |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CCI | text | 15 |  | Link to table I (key attribute) |  |
| 2 | Unique Identifier of the Operation (ID) | text | 255 |  | Link to table I (key attribute) | Table 1, field 13. Table 4, field 6. Table 5, fields 11, 12. |
| 37 | Common result indicator(s) code(s) applicable to the operation (as many rows as relevant) | text | 6 |  | See codes in Table 10 of Annex II | Table 9, field 5. |
| 38 | Baseline value | number |  | double |  | Table 9, fields 11, 13. |
| 39 | Indicative result expected by the beneficiary (one row per indicator) | number |  | double |  | Table 9, field 12. |
| 40 | Ex-post result (one row per indicator) | number |  | double | The resulting value after the project has been completed. | Table 9, field 14. |

(1) Commission Implementing Regulation (EU) 2017/218 of 6 February 2017 on the Union fishing fleet register (OJ L 34, 9.2.2017, p. 9).

## ANNEX II — PRESENTATION OF IMPLEMENTATION DATA

**Table 1**

**Sector the operation is contributing to (Annex I, Table 1, field 5)**

| Code | Description |
| --- | --- |
| 01 | Fisheries |
| 02 | Aquaculture |
| 03 | Processing |
| 04 | Tourism |
| 05 | Environment |
| 06 | Maritime (except fishing and aquaculture) |
| 07 | Integrated/multisector |
| 08 | Other |

**Table 2**

**Type of beneficiary (1) (Annex I, Table 1, field 10)**

| Code | Description |
| --- | --- |
| 01 | PO – Producer organisation |
| 02 | APO – Association of producer organisations |
| 03 | IBO – Inter-branch organisation |
| 04 | Private enterprise – micro |
| 05 | Private enterprise – SME (Small or medium-sized enterprise) |
| 06 | Private enterprise – large |
| 07 | Public body |
| 08 | Research centre / university / scientists |
| 09 | Non-governmental organisation (NGO) / association |
| 10 | Educational institution |
| 11 | LAG – Local action group |
| 12 | Entity without legal personality |
| 13 | International organisation |
| 14 | Commission bodies and agencies |
| 15 | Natural persons |
| 16 | Other |

**Table 3**

**Gender of beneficiary/natural person (Annex I, Table 1, field 11)**

| Code | Description |
| --- | --- |
| 01 | Natural person – male |
| 02 | Natural person – female |
| 03 | Natural person – non-defined gender |
| 04 | More than one natural person, family |
| 05 | More than one natural person, predominately male |
| 06 | More than one natural person, predominately female |
| 07 | N/A. (in the case of legal persons) |

**Table 4**

**Codes for Yes/No fields (Annex I, Table 1, fields 29-34 and 36)**

| Code | Description |
| --- | --- |
| 01 | Yes |
| 02 | No |

**Table 5**

**Indication as to whether the operation relates to marine, inland, or both (Annex I, Table 1, field 15)**

| Code | Description |
| --- | --- |
| 01 | Marine |
| 02 | Inland |
| 03 | Both |
| 04 | N/A |

**Table 6**

**State of progress of the operation (Annex I, Table 1, field 16)**

| Code | Description |
| --- | --- |
| 00 | Operation selected |
| 01 | Operation interrupted/abandoned following partial implementation |
| 02 | Operation under implementation |
| 03 | Operation fully implemented (but for which all expenses have not necessarily been paid to the beneficiary) |
| 04 | Operation completed |

**Table 7**

**Type of operation (Annex I, Table 1, field 26)**

| Code | Description |
| --- | --- |
| 01 | Investment in reduction of energy use and energy efficiency |
| 02 | Investment in renewable energy systems |
| 03 | Investment in on-board production equipment |
| 04 | Investment on board to improve navigation or engine control |
| 05 | Investment in physical infrastructure at existing fishing ports or at new or existing landing sites |
| 06 | First acquisition of a fishing vessel |
| 07 | Investment to improve traceability |
| 08 | Preparation and implementation of production and marketing plans by producer organisations |
| 09 | Marketing activities |
| 10 | Advisory services |
| 11 | Investments to support business development (strategy development, administration, equipment) |
| 12 | Other business-diversification operations not involving fisheries, aquaculture, or innovation |
| 13 | Insurance schemes |
| 14 | Training to improve skills and develop human capital |
| 15 | Events |
| 16 | Awareness raising, communication to the wider public |
| 17 | Capacity building |
| 18 | Development of marketing innovation |
| 19 | Development of process innovation |
| 20 | Development of product innovation |
| 21 | Studies and research |
| 22 | Knowledge sharing |
| 23 | Cooperation |
| 24 | Restoring ecological continuity of rivers |
| 25 | Restocking of aquatic species |
| 26 | Retrieval and/or disposal of marine litter |
| 27 | Environmental services |
| 28 | Specific investments for improving aquatic habitats and biodiversity |
| 29 | Permanent cessation of fishing activities |
| 30 | Temporary cessation of fishing activities |
| 31 | Compensation |
| 32 | Productive investments for sustainable aquaculture |
| 33 | Gear selectivity to reduce unwanted catches |
| 34 | Gear modification to minimise habitat impacts |
| 35 | Gear selectivity in relation to endangered, threatened and protected species |
| 36 | Use of unwanted catches |
| 37 | Natura 2000 areas management and monitoring (soft operations) |
| 38 | Investments in Natura 2000 areas restoration |
| 39 | Management and monitoring of marine protected areas (soft operations) |
| 40 | Investments in the restoration of marine protected areas |
| 41 | Reduction and prevention of pollution/contamination |
| 42 | Water usage and water quality improvements |
| 43 | Investments for control and enforcement for public authorities |
| 44 | Investments for control and enforcement for private business |
| 45 | Observation coordination |
| 46 | Data collection |
| 47 | Investment in IT – hardware |
| 48 | Investment in IT – software |
| 49 | IT development and maintenance |
| 50 | Data assembly and dissemination |
| 51 | Inspections |
| 52 | Investment in animal welfare |
| 53 | Food quality and hygiene safety |
| 54 | Investments in safety equipment |
| 55 | Investments in working conditions |
| 56 | Pilot projects |
| 57 | Socio-cultural development |
| 58 | Governance |
| 59 | Animation and capacity building |
| 60 | Preparatory actions |
| 61 | Management |
| 62 | Assistance under Direct Management |
| 63 | Evaluation |
| 64 | Other (social) |
| 65 | Other (environmental) |
| 66 | Other (economic) |

**Table 8**

**Form of support (Annex I, Table 1, field 35)**

| Code | Description |
| --- | --- |
| 01 | Grants |
| 02 | Financial instruments |
| 03 | Combination of grants and financial instruments |
| 04 | Prizes |
| 05 | Contracting (Direct management) |

**Table 9**

**Types of intervention for support under direct and indirect management (Annex I. Table 1, field 25)**

| Code | Description |
| --- | --- |
| 17 | International ocean governance |
| 18 | Maritime policy |
| 19 | Scientific advice |
| 20 | Control and enforcement |
| 21 | Voluntary contributions to international organisations |
| 22 | Conservation measures |
| 23 | Advisory councils |
| 24 | Communication |
| 25 | Market intelligence |

**Table 10**

**Common result indicators (Annex I. Table 2, field 37)**

| Code | Description | Measurement unit |
| --- | --- | --- |
| CR01 | New production capacity | tonnes/annum |
| CR02 | Aquaculture production maintained | tonnes/annum |
| CR03 | Businesses created | number of entities |
| CR04 | Businesses with higher turnover | number of entities |
| CR05.1 | Capacity of vessels withdrawn | GT |
| CR05.2 | Capacity of vessels withdrawn | kW |
| CR06 | Jobs created | number of persons |
| CR07 | Jobs maintained | number of persons |
| CR08 | Persons benefitting | number of persons |
| CR09.1 | Area addressed by operations contributing to a good environmental status, protecting, conserving, and restoring biodiversity and ecosystems | km2 |
| CR09.2 | Area addressed by operations contributing to a good environmental status, protecting, conserving, and restoring biodiversity and ecosystems | km2 |
| CR10 | Actions contributing to a good environmental status, including nature restoration, conservation, protection of ecosystems, biodiversity, animal health and welfare | number of actions |
| CR11 | Entities increasing social sustainability | number of entities |
| CR12 | Effectiveness of the system for “collection, management and use of data” | scale: high, medium, low |
| CR13 | Cooperation activities between stakeholders | number of actions |
| CR14 | Innovations enabled | number of new products, services, processes, business models or methods |
| CR15 | Control means installed or improved | number of means |
| CR16 | Entities benefitting from promotion and information activities | number of entities |
| CR17 | Entities improving resource efficiency in production and/or processing | number of entities |
| CR18.1 | Energy consumption leading to CO2 emissions reduction | kWh/tonnes |
| CR18.2 | Energy consumption leading to CO2 emissions reduction | litres/h |
| CR19 | Actions to improve governance capacity | number of actions |
| CR20 | Investment induced | EUR |
| CR21 | Datasets and advice made available | number |
| CR22 | Usage of data and information platforms | number of page views |

(1) The lead partner, if an operation has more than one beneficiary.
