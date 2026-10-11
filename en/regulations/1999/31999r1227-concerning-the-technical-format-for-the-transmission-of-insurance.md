---
title: "Commission Regulation (EC) No 1227/1999 of 28 May 1999 concerning the technical format for the transmission of insurance services statistics (Text with EEA relevance)"
identifier: "31999R1227"
eli: "http://data.europa.eu/eli/reg/1999/1227/oj"
type: regulation
jurisdiction: eu
language: en
date: 1999-05-28
entry_into_force: 1999-05-27
last_amended: 2007-01-01
consolidated_version: "01999R1227-20070101"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01999R1227-20070101"
retrieved: 2026-10-11
---

# Commission Regulation (EC) No 1227/1999 of 28 May 1999 concerning the technical format for the transmission of insurance services statistics (Text with EEA relevance)

**COMMISSION REGULATION (EC) NO 1227/1999**

**of 28 May 1999**

**concerning the technical format for the transmission of insurance services statistics**

**(Text with EEA relevance)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION REGULATION (EC) No 1792/2006 of 23 October 2006 </td><td> L 362</td><td>1</td><td>20.12.2006</td></tr>
</table>

|  | ACT concerning the conditions of accession of the Czech Republic, the Republic of Estonia, the Republic of Cyprus, the Republic of Latvia, the Republic of Lithuania, the Republic of Hungary, the Republic of Malta, the Republic of Poland, the Republic of Slovenia and the Slovak Republic and the adjustments to the Treaties on which the European Union is founded | L 236 | 33 | 23.9.2003 |
| --- | --- | --- | --- | --- |

**COMMISSION REGULATION (EC) NO 1227/1999**

**of 28 May 1999**

**concerning the technical format for the transmission of insurance services statistics**

**(Text with EEA relevance)**

## Article 1

The technical format referred to in Article 9 of Regulation (EC, Euratom) No 58/97 is defined in the Annex to this Regulation.

## Article 2

Member States shall apply this format for the data concerning the 1996 reference year and subsequent years.

## Article 3

This Regulation shall enter into force on the 20th day following its publication in the Official Journal of the European Communities.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

## ANNEX — TECHNICAL FORMAT

**1\. The form of the data**

The data is sent as a set of records of which a large part describes the characteristics of the data (country, year, economic activity, etc.). The data itself is a number which can be linked to flags and explanatory footnotes used for example to describe aggregations of NACE codes. Confidential data should be sent with the true value being recorded in the value field and a flag indicating the nature of the confidential data being added to the record.

In order to be precise about the nature of the data, it is necessary to distinguish the following special cases:

— data equal to zero (coded ‘0’) : real values of zero only,

— confidential data (coded ‘x’) : indicates data which the Member State does not transmit to Eurostat because the data is confidential,

— missing data (coded ‘m’) : this is data which is currently missing but the Member State intends to supply when available,

— data not available : this is data which is not collected in a Member State. In this case the corresponding record is not sent.

By default, if an entire dimension (a variable, a NUTS code, a NACE code, etc.) is not collected then the corresponding records will not exist except for those which are missing because they form part of a regrouping of NACE codes. This is why it is important to distinguish data which is really missing by supplying a record (one per missing item) in which the data value is coded as ‘m’, and data which is really equal to zero by supplying the corresponding records in which the data value is set to 0.

**2\. Record structure**

<table>
<tbody><tr><td>  </td><td>Field</td><td>Type</td><td>Maximum length</td><td>Values</td></tr>
<tr><td>1</td><td>Series</td><td>A</td><td>2</td><td>5A, 5B, 5C, etc. Alphanumeric code of the series (see list below)</td></tr>
<tr><td>2</td><td>Year</td><td>A</td><td>4</td><td>Year in four characters, e. g. 1996</td></tr>
<tr><td>3</td><td>Territorial unit</td><td>A</td><td>2</td><td>Corresponds to the country code. NUTS 95 is the new nomenclature put in place in June 95</td></tr>
<tr><td>4</td><td>Economic activity</td><td>A</td><td>4</td><td>NACE Rev. 1 code</td></tr>
<tr><td>5</td><td>Measurement</td><td>A</td><td>3</td><td>Variable — type of measurement</td></tr>
<tr><td>6</td><td>Unit</td><td>A</td><td>4</td><td>Unit</td></tr>
<tr><td>7</td><td>Variable</td><td>A</td><td>5</td><td>Variable code. The codes laid down in Annex 5 to the SBS Regulation have 5 characters (see list below)</td></tr>
<tr><td>8</td><td>Type of insurance enterprise/business</td><td>A</td><td>1</td><td>Code for the type of insurance enterprise or insurance business (see list below)</td></tr>
<tr><td rowspan="2">9</td><td>Size class</td><td>A</td><td>4</td><td>Code for the size class (see list below)</td></tr>
<tr><td>Residence of parent enterprise</td><td>A</td><td>4</td><td>Code for the country of residence of the parent enterprise (see list below)</td></tr>
<tr><td>10</td><td>Breakdown of products</td><td>A</td><td>6</td><td>Corresponds to the classification of products according to activities code (see list below)</td></tr>
<tr><td rowspan="2">11</td><td>Legal status</td><td>A</td><td>4</td><td>Code for the legal status of the enterprise (see list below)</td></tr>
<tr><td>Geographical breakdown</td><td>A</td><td>4</td><td>Code for the geographical breakdown of the partner countries (see list below)</td></tr>
<tr><td>12</td><td>Data value</td><td>A</td><td>12</td><td>Numeric value of the data (negative values are preceded by a minus sign) expressed as a whole number without decimal places. An ‘x’ should be used if the data is not sent to Eurostat because the data is confidential and an ‘m’ should be used if the data is not sent because it is missing</td></tr>
<tr><td>13</td><td>Quality flag</td><td>A</td><td>1</td><td>R: revised data, M: updated data P: provisional data</td></tr>
<tr><td>14</td><td>Confidentiality flag</td><td>A</td><td>1</td><td>A, B, C, D: indicates that the data is confidential and the reason for that confidentiality (see list below). A blank space indicates non-confidential data</td></tr>
<tr><td>15</td><td>Dominance</td><td>N</td><td>3</td><td>A numeric value less than or equal to 100. This indicates the percentage dominance of one or two enterprises which dominate the data and make it confidential. The value is rounded to the nearest whole number: e.g 90,3 becomes 90, 94,50 becomes 95. This field is blank for non-confidential data. This field is only used when the confidentiality flags B or C are used in the previous field</td></tr>
<tr><td>16</td><td>List</td><td>A</td><td>1</td><td>Code corresponding to the list to which the variable — characteristic — belongs</td></tr>
<tr><td>17</td><td>Footnote</td><td>A</td><td>250</td><td>Free note on the data</td></tr>
<tr><td colspan="5">NB: A = Alphanumeric, N = Numeric. </td></tr>
</tbody>
</table>

This format may be converted into a fixed format by using the maximum length of each field and right justifying the contents of each field preceded by blanks.

**3\. Description of the fields**

**3.1. Series**

| Series type | Code |
| --- | --- |
| Annual enterprise statistics | 5A |
| Annual enterprise statistics broken down by legal status | 5B |
| Annual enterprise statistics broken down according to the country of residence of the parent enterprise | 5C |
| Annual enterprise statistics broken down by size class | 5D |
| Annual enterprise statistics broken down by product | 5E |
| Annual enterprise statistics by geographical breakdown | 5F |

**3.2. Year**

**3.3. Territorial unit**

This code corresponds to the country for national series

Country name Code

Belgium BE

Bulgaria BG

Czech Republic CZ

Denmark DK

Germany DE

Estonia EE

Greece GR

Spain ES

France FR

Ireland IE

Italy IT

Cyprus CY

Latvia LV

Lithuania LT

Luxembourg LU

Hungary HU

Malta MT

Netherlands NL

Austria AT

Poland PL

Portugal PT

Romania RO

Slovenia SI

Slovakia SK

Finland FI

Sweden SE

United Kingdom UK

Iceland IS

Liechtenstein LI

Norway NO

Switzerland CH

**3.4. Economic activity**

| Economic activity title — Nace Rev.1 | Code |
| --- | --- |
| Life insurance | 66.01 |
| Non-life insurance | 66.03 |
| Reinsurance | 66.04 |

**3.5. Measurement**

| Measurement | Code |
| --- | --- |
| National currency | NC |
| Euro | EUR |
| Number | NBR |

**3.6. Unit**

Unit Code

Unit UNIT

1000 1000

Mio MIO

Bio BIO

**3.7. Variable**

<table>
<tbody><tr><td>Variable title</td><td>Code</td></tr>
<tr><td>Number of enterprises</td><td>11 11 0</td></tr>
<tr><td>Number of enterprises broken down by legal status</td><td>11 11 1</td></tr>
<tr><td>Number of enterprises broken down by size class of gross premiums written</td><td>11 11 2</td></tr>
<tr><td>Number of enterprises broken down by size class of gross technical provisions</td><td>11 11 3</td></tr>
<tr><td>Number of enterprises broken down by country of residence of the parent enterprise</td><td>11 11 5</td></tr>
<tr><td>Total number and location of branches in other countries</td><td>11 41 0</td></tr>
<tr><td colspan="2">Technical part of the profit and loss account</td></tr>
<tr><td>Gross premiums written</td><td>12 11 0</td></tr>
<tr><td>Gross direct premiums written</td><td>12 11 1</td></tr>
<tr><td>Gross reinsurance accepted, written premiums</td><td>12 11 2</td></tr>
<tr><td>Gross direct premiums written, individual premiums</td><td>12 11 3</td></tr>
<tr><td>Gross direct premiums written, premiums under group contracts</td><td>12 11 4</td></tr>
<tr><td>Gross direct premiums written, periodic premiums</td><td>12 11 5</td></tr>
<tr><td>Gross direct premiums written, single premiums</td><td>12 11 6</td></tr>
<tr><td>Gross direct premiums written, premiums from non-bonus contracts</td><td>12 11 7</td></tr>
<tr><td>Gross direct premiums written, premiums from bonus contracts</td><td>12 11 8</td></tr>
<tr><td>Gross direct premiums written, premiums from contracts where the investment risk is borne by policyholders</td><td>12 11 9</td></tr>
<tr><td>Investment income</td><td>32 22 0</td></tr>
<tr><td>Unrealised gains on investments</td><td>32 23 0</td></tr>
<tr><td>Gross change in life insurance provision</td><td>32 25 0</td></tr>
<tr><td>Investment charges</td><td>32 27 0</td></tr>
<tr><td>Unrealised losses on investments</td><td>32 28 0</td></tr>
<tr><td>Allocated investment return transferred to the non-technical account</td><td>32 29 0</td></tr>
<tr><td>Gross change in the provision for unearned premiums</td><td>32 11 2</td></tr>
<tr><td>Gross premiums written broken down by legal status</td><td>32 11 4</td></tr>
<tr><td>Gross direct premiums written broken down according to the country of residence of the parent enterprise</td><td>32 11 5</td></tr>
<tr><td>Gross reinsurance premiums accepted, written premiums broken down according to the country of residence of the parent enterprise</td><td>32 11 6</td></tr>
<tr><td>Allocated investment return transferred from the non-technical account</td><td>32 12 0</td></tr>
<tr><td>Gross claims payments</td><td>32 13 1</td></tr>
<tr><td>Gross payments in respect of claims incurred in the current accounting year</td><td>32 13 2</td></tr>
<tr><td>Gross change in the provision for outstanding claims</td><td>32 13 4</td></tr>
<tr><td>Gross operating expenses</td><td>32 14 0</td></tr>
<tr><td>Change in the equalisation provision</td><td>32 15 0</td></tr>
<tr><td>Other items in the technical account, gross amount</td><td>32 16 0</td></tr>
<tr><td>Other technical income, net amount</td><td>32 16 1</td></tr>
<tr><td>Net changes in other technical provisions, not shown under other headings</td><td>32 16 2</td></tr>
<tr><td>Bonuses and rebates, net amount</td><td>32 16 3</td></tr>
<tr><td>Other technical charges, net amount</td><td>32 16 4</td></tr>
<tr><td>Sub-total I (= gross balance of the technical account)</td><td>32 17 0</td></tr>
<tr><td>Reinsurance balance</td><td>32 18 0</td></tr>
<tr><td>Reinsurers share of gross premiums written</td><td>32 18 1</td></tr>
<tr><td>Reinsurers share of gross premiums written broken down according to the residence of the parent enterprise</td><td>32 18 2</td></tr>
<tr><td>Reinsurers share of the gross change in the provision for unearned premiums</td><td>32 18 3</td></tr>
<tr><td>Reinsurers share of gross claims payments</td><td>32 18 5</td></tr>
<tr><td>Reinsurers share of gross change in the provision for outstanding claims</td><td>32 18 6</td></tr>
<tr><td>Reinsurance commissions and profit participations</td><td>32 18 7</td></tr>
<tr><td>Reinsurers share of the gross amount of other items in the technical account</td><td>32 18 8</td></tr>
<tr><td>Reinsurers share of gross change in life insurance provision</td><td>32 33 4</td></tr>
<tr><td>Sub-total II (= net balance of the technical account)</td><td>32 19 0</td></tr>
<tr><td colspan="2">Non-technical part of the profit and loss account</td></tr>
<tr><td>Investment income</td><td>32 42 0</td></tr>
<tr><td>Allocated investment return transferred from the life-assurance technical account</td><td>32 43 0</td></tr>
<tr><td>Investment charges</td><td>32 44 0</td></tr>
<tr><td>Allocated investment return transferred to the non-life insurance technical account</td><td>32 45 0</td></tr>
<tr><td>Other income</td><td>32 46 0</td></tr>
<tr><td>Other charges, including value adjustments</td><td>32 47 0</td></tr>
<tr><td>Profit or loss on ordinary activities</td><td>32 48 0</td></tr>
<tr><td>Extraordinary profit or loss</td><td>32 49 0</td></tr>
<tr><td>All taxes (tax on profit or loss on ordinary activities, tax on extraordinary profit or loss, other taxes)</td><td>32 50 0</td></tr>
<tr><td>Profit or loss for the financial year</td><td>32 51 0</td></tr>
<tr><td colspan="2">Additional variables relating to the profit and loss account</td></tr>
<tr><td>Commissions for total insurance business</td><td>32 61 1</td></tr>
<tr><td>Commissions for direct insurance business</td><td>32 61 2</td></tr>
<tr><td>External expenses on goods and services</td><td>32 61 4</td></tr>
<tr><td>Personnel costs</td><td>13 31 0</td></tr>
<tr><td>External and internal claims management expenses</td><td>32 61 5</td></tr>
<tr><td>Acquisition costs</td><td>32 61 6</td></tr>
<tr><td>Administrative expenses</td><td>32 61 7</td></tr>
<tr><td>Gross other technical charges</td><td>32 61 8</td></tr>
<tr><td>Investment management charges</td><td>32 61 9</td></tr>
<tr><td>Income from participating interests</td><td>32 71 1</td></tr>
<tr><td>Income from land and buildings</td><td>32 71 3</td></tr>
<tr><td>Income from other investments</td><td>32 71 4</td></tr>
<tr><td>Value re-adjustments on investments</td><td>32 71 5</td></tr>
<tr><td>Gains on the realisation on investments</td><td>32 71 6</td></tr>
<tr><td>Investment management charges, including interest</td><td>32 72 1</td></tr>
<tr><td>Value adjustments on investments</td><td>32 72 2</td></tr>
<tr><td>Losses on the realisation on investments</td><td>32 72 3</td></tr>
<tr><td>Gross premiums written in direct business by (sub)categories of the CPA (5-digit level and subcategories 66.03.21 and 66.03.22)</td><td>33 11 1</td></tr>
<tr><td>Reinsurers share of gross direct premiums written by (sub)categories of the CPA (5-digit level and subcategories 66.03.21 and 66.03.22)</td><td>33 12 1</td></tr>
<tr><td>Gross claims incurred, direct business by (sub)categories of the CPA (5-digit level and subcategories 66.03.21 and 66.03.22)</td><td>33 13 1</td></tr>
<tr><td>Gross operating expenses, direct business by (sub)categories of the CPA (5-digit level and subcategories 66.03.21 and 66.03.22)</td><td>33 14 1</td></tr>
<tr><td>Reinsurance balance, direct business by (sub)categories of the CPA (5-digit level and subcategories 66.03.21 and 66.03.22)</td><td>33 15 1</td></tr>
<tr><td>Geographical breakdown — in general — of gross direct premiums written</td><td>34 11 0</td></tr>
<tr><td>Geographical breakdown — in general — of gross reinsurance premiums accepted, premiums written</td><td>34 12 0</td></tr>
<tr><td>Geographical breakdown of reinsurers share of gross premiums written</td><td>34 13 0</td></tr>
<tr><td>Gross direct premiums written by CPA category (5-digit level) and by Member State, geographical breakdown of the business written under the right of establishment</td><td>34 31 1</td></tr>
<tr><td>Gross direct premiums written by CPA category (5-digit level) and by Member State, geographical breakdown of business written under the right of freedom to provide services</td><td>34 32 1</td></tr>
<tr><td>Number of persons employed</td><td>16 11 0</td></tr>
<tr><td>Land and buildings</td><td>36 11 0</td></tr>
<tr><td>Land and buildings occupied by an insurance enterprise for its own activities</td><td>36 11 1</td></tr>
<tr><td>Land and buildings (current value)</td><td>36 11 2</td></tr>
<tr><td>Investments in affiliated enterprises and participating interests</td><td>36 12 0</td></tr>
<tr><td>Shares in affiliated enterprises and participating interest</td><td>36 12 1</td></tr>
<tr><td>Debt securities issued by, and loans to, affiliated enterprises and to enterprises with which an insurance enterprise is linked by the virtue of a participating interest</td><td>36 12 2</td></tr>
<tr><td>Investments in affiliated enterprises and participating interests (current value)</td><td>36 12 3</td></tr>
<tr><td>Other financial investments</td><td>36 13 0</td></tr>
<tr><td>Shares and other variable-yield securities and units in unit trusts</td><td>36 13 1</td></tr>
<tr><td>Debt securities and other fixed-income securities</td><td>36 13 2</td></tr>
<tr><td>Participation in investment pools</td><td>36 13 3</td></tr>
<tr><td>Loans guaranteed by mortgages</td><td>36 13 4</td></tr>
<tr><td>Other loans</td><td>36 13 5</td></tr>
<tr><td>Other (including deposits with credit institutions)</td><td>36 13 6</td></tr>
<tr><td>Other financial investments (current value)</td><td>36 13 8</td></tr>
<tr><td>Deposits with ceding enterprises</td><td>36 14 0</td></tr>
<tr><td>Investments for the benefit of life-assurance policyholders who bear the investment risk</td><td>36 20 0</td></tr>
<tr><td>Investments for the benefit of life-assurance policyholders who bear the investment risk — land and buildings</td><td>36 21 0</td></tr>
<tr><td>Investments for the benefit of life-assurance policyholders who bear the investment risk — other financial investments</td><td>36 22 0</td></tr>
<tr><td>Balance sheet total</td><td>36 30 0</td></tr>
<tr><td>Total capital and reserves</td><td>37 10 0</td></tr>
<tr><td>Total capital and reserves, broken down by legal status</td><td>37 10 1</td></tr>
<tr><td>Subscribed capital or equivalent funds</td><td>37 11 0</td></tr>
<tr><td>Share premium account, revaluation reserve, reserve</td><td>37 12 0</td></tr>
<tr><td>Subordinated liabilities</td><td>37 20 0</td></tr>
<tr><td>Total net technical provisions</td><td>37 30 1</td></tr>
<tr><td>Gross provision for unearned premiums</td><td>37 31 0</td></tr>
<tr><td>Gross life assurance provision</td><td>37 32 0</td></tr>
<tr><td>Gross provision for outstanding claims</td><td>37 33 0</td></tr>
<tr><td>Gross provision for outstanding claims, related to direct business</td><td>37 33 1</td></tr>
<tr><td>Gross provision for outstanding claims related to direct business, by (sub)category of the CPA (5-digit level) and subcategories 66.03.21 and 66.03.22)</td><td>37 33 3</td></tr>
<tr><td>Gross provision for bonuses and rebates</td><td>37 34 0</td></tr>
<tr><td>Equalisation provision</td><td>37 35 0</td></tr>
<tr><td>Gross other technical provisions</td><td>37 36 0</td></tr>
<tr><td>Gross technical provisions for life-assurance policies where the investment risk is borne by the policyholders</td><td>37 37 0</td></tr>
<tr><td>Debenture loans</td><td>37 41 0</td></tr>
<tr><td>Amounts owed to credit institutions</td><td>37 42 0</td></tr>
<tr><td>Number of contracts outstanding at the end of the accounting year, relating to direct business for all individual life insurance contracts and for the following subcategories of the CPA: 66.01.1, 66.03.1, 66.03.4 and 66.03.5</td><td>39 10 0</td></tr>
<tr><td>Number of insured persons at the end of the accounting year, relating to direct business for all group life insurance contracts and for the following subcategory of the CPA: 66.03.1</td><td>39 20 0</td></tr>
<tr><td>Number of insured vehicles at the end of the accounting year, relating to direct business, for the following subcategory of the CPA: 66.03.2</td><td>39 30 0</td></tr>
<tr><td>Gross insured sum at the end of the accounting year, relating to direct business, for the following subcategories of the CPA: 66.01.1 and 66.01.4</td><td>39 40 0</td></tr>
<tr><td>Number of claims incurred during the accounting year, relating to direct business, for the following subcategory of the CPA: 66.03.2</td><td>39 50 0</td></tr>
</tbody>
</table>

**3.8. Type of insurance enterprise or insurance business**

| Type of insurance enterprise or insurance business | Code |
| --- | --- |
| Life insurance enterprises | 1 |
| Non-life insurance enterprises | 2 |
| Composite insurance enterprises | 3 |
| Specialist reinsurance enterprises | 4 |
| Life business of composite insurance enterprises | 5 |
| Non-life business of composite insurance enterprises (including business accepted) | 6 |

**3.9. Size classes / Residence of parent enterprise**

| Size class by gross premiums written (million EUR) | Code |
| --- | --- |
| < 5 | SC11 |
| 5 - 50 | SC12 |
| 51 - 250 | SC13 |
| 251 - 500 | SC14 |
| 501 - 1 000 | SC15 |
| 1 000 + | SC16 |

| Size class by gross technical provisions written (million EUR) | Code |
| --- | --- |
| < 50 | SC21 |
| 50 - 500 | SC22 |
| 501 - 2 500 | SC23 |
| 2 501 - 5 000 | SC24 |
| 5 001 - 10 000 | SC25 |
| 10 000 + | SC26 |

| Country of residence of the parent enterprise | Code |
| --- | --- |
| Parent enterprise situated in the home Member State | RE01 |
| Parent enterprise situated in other countries | RE02 |

**3.10. Breakdown of products**

| Products | Code |
| --- | --- |
| Non-linked life insurance services | 66.01.1 |
| Linked life insurance services | 66.01.2 |
| Tontine insurance services | 66.01.3 |
| Capital redemption insurance services | 66.01.4 |
| Other life insurance services | 66.01.5 |
| Group pension services | 66.02.1 |
| Accident and health insurance services | 66.03.1 |
| Motor vehicle insurance services | 66.03.2 |
| Motor vehicle insurance services, third party liability | 66.03.21 |
| Motor vehicle insurance services, other classes | 66.03.22 |
| Marine, aviation and transport insurance services | 66.03.3 |
| Fire and other damage to property insurance services | 66.03.4 |
| General liability insurance services | 66.03.5 |
| Credit and suretyship insurance services | 66.03.6 |
| Assistance, legal expenses and miscellaneous financial loss insurance services | 66.03.7 |
| Other non-life insurance services | 66.03.8 |

**3.11. Legal status / Geographical breakdown**

| Legal status | Code |
| --- | --- |
| Incorporated enterprises limited by shares | LS01 |
| Mutual enterprises | LS02 |
| Branches of non-EEA enterprises | LS03 |
| Others | LS04 |

<table>
<tbody><tr><td>Countries and groups of countries</td><td>Code</td></tr>
<tr><td>BelgiqueBelgië</td><td>BEL</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>България</td><td>BGR</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Česká republika</td><td>CZE</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Danmark</td><td>DNK</td></tr>
<tr><td>Deutschland</td><td>DEU</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Eesti</td><td>EST</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Ελλάδα</td><td>GRC</td></tr>
<tr><td>España</td><td>ESP</td></tr>
<tr><td>France</td><td>FRA</td></tr>
<tr><td>Ireland</td><td>IRL</td></tr>
<tr><td>Italia</td><td>ITA</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Κύπρος</td><td>CYP</td></tr>
<tr><td>Latvija</td><td>LVA</td></tr>
<tr><td>Lietuva</td><td>LTU</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Luxembourg</td><td>LUX</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Magyarország</td><td>HUN</td></tr>
<tr><td>Malta</td><td>MLT</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Nederland</td><td>NLD</td></tr>
<tr><td>Österreich</td><td>AUT</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Polska</td><td>POL</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Portugal</td><td>PRT</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>România</td><td>ROU</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>Slovenija</td><td>SVN</td></tr>
<tr><td>Slovensko</td><td>SVK</td></tr>
<tr><td colspan="2"></td></tr>
<tr><td>SuomiFinland</td><td>FIN</td></tr>
<tr><td>Sverige</td><td>SWE</td></tr>
<tr><td>United Kingdom</td><td>GBR</td></tr>
<tr><td>Island</td><td>ISL</td></tr>
<tr><td>Liechtenstein</td><td>LI</td></tr>
<tr><td>Norge</td><td>NOR</td></tr>
<tr><td>SchweizSuisseSvizzera</td><td>CHE</td></tr>
<tr><td>USA</td><td>USA</td></tr>
<tr><td>Japan</td><td>JPN</td></tr>
<tr><td>In Member State of head office</td><td>MSHO</td></tr>
<tr><td>In other EU Member State</td><td>OMS</td></tr>
<tr><td>In other EEA countries</td><td>OEEA</td></tr>
<tr><td>In other third countries (rest of the world)</td><td>THCO</td></tr>
</tbody>
</table>

**3.12. Data value**

Monetary data is expressed in millions of national currency units except for:

— Italy : data is given in milliards of national currency units.

In order to be precise about the nature of the data, it is necessary to distinguish the following cases:

— data equal to zero (coded ‘0’) : real values of zero only,

— confidential data (coded ‘x’) : indicates data which the Member State does not transmit to Eurostat because the data is confidential. A flag should also be used to indicate that the data is missing due to confidentiality (see 3.14 below),

— missing data (coded ‘m’) : this is data which is currently missing but the Member State intends to supply when available,

— data not available : this is data which is not collected in a Member State. In this case the corresponding record is not sent.

By default, if an entire dimension (a variable, a NUTS code, a NACE code, etc.) is not collected then the corresponding records will not exist except for those which are missing because they form part of a regrouping of NACE codes. This is why it is important to distinguish data which is really missing by supplying a record (one per missing item) in which the data value is coded as ‘m’.

**3.13. Quality flag**

| Data type | Code |
| --- | --- |
| Revised data | R |
| Updated data | M |
| Provisional data | P |

‘Revised data’ refers to data which are sent for a second (or more) time and are corrections of data which has been previously sent.

‘Updated data’ concerns data which was not previously available and was coded as missing in the data value field (see 3.12 above) but has since become available.

The flag indicating ‘Provisional data’ should be used in order to indicate that it is likely that the data being transmitted may be corrected.

**3.14. Confidentiality**

Member States are asked to clearly indicate confidential data using the flags listed below:

Countries which cannot send confidential data are asked to set the value to ‘x’ (see 3.12 above) and to indicate using a flag that the data is missing due to confidentiality.

| Reason for confidentiality | Flag |
| --- | --- |
| Too few enterprises | A |
| One enterprise dominates the data | B |
| Two enterprises dominate the data | C |
| Confidential data due to secondary confidentiality | D |

**3.15. Dominance**

A numeric value less than or equal to 100. This indicates the percentage dominance of one or two enterprises which dominate the data and make it confidential. The value is rounded to the nearest whole number: e.g. 90,3 becomes 90, 94, 50 becomes 95. This field is blank for non-confidential data. This field is only used when the confidentiality flags B or C are used in the previous field.

**3.16. List**

The variables — characteristics — are presented in Regulation (EC) No 410/98 in two different lists: A and B. The first year of reference for which they shall be compiled differs. Three variables are optional.

List Flag

List A A

List B B

Optional O

**4\. Examples of records**

**Example 1**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5A | 1996 | BE | 6603 | NBR | UNIT | 11110 | 2 |  |  |  | 95 |  |  |  | A |

Belgium declares in the series 5A — annual enterprise statistics — for the reference year 1996, in NACE Rev.1 class 66.03: 95 non-life insurance enterprises. The data is non confidential and in List A.

5A; 1996; BE; 6603; NBR; UNIT; 11110; 2;;;; 95;;;; A

**Example 2**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5B | 1996 | DK | 6601 | NBR | UNIT | 11111 | 1 |  |  | LS01 | 49 |  |  |  | A |

Denmark declares in the series 5B — annual enterprise statistics broken down by legal status — for the reference year 1996, in NACE Rev.1 class 66.01: 49 life insurance enterprises which are incorporated enterprises limited by shares. The data is non confidential and in List A.

5B; 1996; DK; 6601; NBR; UNIT; 11111; 1;;; LS01; 49;;;; A

**Example 3**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5C | 1996 | PT | 6601 | NBR | UNIT | 11115 | 1 | RE02 |  |  | 47 |  |  |  | A |

Portugal declares in the series 5C — annual enterprise statistics broken down by country of residence of the parent enterprise — for the reference year 1996, in NACE Rev.1 class 66.01: 47 life insurance enterprises whose parent enterprises are situated in other countries. The data is non confidential and in list A.

5C; 1996; PT; 6601; NBR; UNIT; 11115; 1; RE02;;; 47;;;; A

**Example 4**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5D | 1996 | FI | 6603 | NBR | UNIT | 11112 | 2 | SC14 |  |  | 7 |  |  |  | A |

Finland declares in the series 5D — annual enterprise statistics broken down by size classes — for the reference year 1996, in NACE Rev.1 class 66.03: 7 non-life insurance enterprises whose turnover is falling between EUR 251 and 500 million. The data is non confidential and in List A.

5D; 1996; FI; 6603; NBR; UNIT; 11112; 2; SC14;;; 7;;;; A

**Example 5**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List | Footnoote |
| 5E | 1996 | ES | 6601 | NC | MIO | 33111 | 1 |  | 66011 |  | 1410692 |  |  |  | A | Including life business of composite enterprises |

Spain declares in the series 5E — annual enterprise statistics broken down by product — for the reference year 1996, in NACE Rev.1 class 66.01: ESP 1 410 692 million of gross direct premiums written in non-linked insurance services by life insurance enterprises. This data is non confidential and in List A.

5E; 1996; ES; 6601; NC; MIO; 33111; 1;; 66011;; 1410692;;;; A

**Example 6**

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5F | 1996 | CH | 6601 | NC | MIO | 34311 | 1 |  | 66021 | NLD | 302 |  |  |  | A |

Switzerland declares in the series 5F — geographical breakdown of annual enterprise statistics — for the reference year 1996, in NACE Rev.1 class 66.01: CHF 302 million of gross direct premiums written via branches in the Netherlands by life insurance enterprises in the product group pension services. This data is non confidential and in List A.

5F; 1996; CH; 6601; NC; MIO; 34311; 1;; 66021; NLD; 302;;;; A

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Series | Year | Territorial Unit | Economic activity | Measurment | Unit | Variable | Type of enterprise | Size class/Residence | Products | Legal status, geographical breakdown | Data value | Quality flag | Confidentiality flag | Dominance | List |
| 5F | 2000 | ES | 6604 | NC | MIO | 34120 | 4 |  |  | OMS | M |  |  |  | B |

Spain declares in the series 5F — geographical breakdown of annual enterprise statistics — for the reference year 2000, in NACE Rev.1 class 66.04: ESP million missing data of gross reinsurance premiums accepted, written by specialist reinsurance enterprises in other Member States. This data is non confidential ans in List B.

5F; 2000; ES; 6604; NC; MIO; 34120; 4;;; OMS; M;;;; B

**5\. Type of magnetic media**

In order to facilitate reading the data, the data must be supplied on 3,5″ diskette.

**6\. Other methods**

Member States are encouraged to send the data sets via Gesmes.

Upon written request Eurostat can provide Member States with electronic questionnaires using Microsoft Excel. The request should be made well in advance of the planned date of data delivery.

( 1 ) OJ L 14, 17.1.1997, p. 1.

( 2 ) OJ L 52, 21.2.1998, p. 1.
