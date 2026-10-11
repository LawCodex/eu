---
title: "Commission Implementing Regulation (EU) 2019/363 of 13 December 2018 laying down implementing technical standards with regard to the format and frequency of reports on the details of securities financing transactions (SFTs) to trade repositories in accordance with Regulation (EU) 2015/2365 of the European Parliament and of the Council and amending Commission Implementing Regulation (EU) No 1247/2012 with regard to the use of reporting codes in the reporting of derivative contracts (Text with EEA relevance.)"
identifier: "32019R0363"
eli: "http://data.europa.eu/eli/reg_impl/2019/363/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2018-12-13
entry_into_force: 2019-12-14
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R0363"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2019/363 of 13 December 2018 laying down implementing technical standards with regard to the format and frequency of reports on the details of securities financing transactions (SFTs) to trade repositories in accordance with Regulation (EU) 2015/2365 of the European Parliament and of the Council and amending Commission Implementing Regulation (EU) No 1247/2012 with regard to the use of reporting codes in the reporting of derivative contracts (Text with EEA relevance.)

**COMMISSION IMPLEMENTING REGULATION (EU) 2019/363**

**of 13 December 2018**

**laying down implementing technical standards with regard to the format and frequency of reports on the details of securities financing transactions (SFTs) to trade repositories in accordance with Regulation (EU) 2015/2365 of the European Parliament and of the Council and amending Commission Implementing Regulation (EU) No 1247/2012 with regard to the use of reporting codes in the reporting of derivative contracts**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to Regulation (EU) 2015/2365 of the European Parliament and of the Council of 25 November 2015 on transparency of securities financing transactions and of reuse and amending Regulation (EU) No 648/2012 (1), and in particular Article 4(10) thereof,

Having regard to Regulation (EU) No 648/2012 of the European Parliament and of the Council of 4 July 2012 on OTC derivatives, central counterparties and trade repositories (2) and in particular Article 9(6) thereof,

Whereas:

(1) The details reported by securities financing transaction (‘SFT’) counterparties to trade repositories or the European Securities and Markets Authority (‘ESMA’) should be submitted in a harmonised format in order to facilitate data collection, aggregation and comparison across trade repositories. To minimise costs for the reporting counterparties, the reporting format for SFTs should be consistent, to the extent feasible, with that prescribed for the reporting of derivatives contracts under Article 9 of Regulation (EU) No 648/2012 of the European Parliament and of the Council. This Regulation therefore prescribes the format for each of the fields to be reported and standardises a report by reference to an ISO standard that is widely used in the financial industry.

(2) The global legal entity identifier (‘LEI’) system has now been fully implemented and each counterparty to an SFT should therefore only use that system to identify a legal entity in a report. For the counterparty's use of the LEI system to be effective, that counterparty should ensure that the reference data related to its LEI are renewed in accordance with the terms of an accredited LEI issuer (Local Operating Unit). An extension of the global LEI system to identify branches of legal entities is currently being developed. Until such time as that extension is finalised and considered suitable for the purposes of reporting SFTs, and this Regulation is amended accordingly, the ISO code of the country where the branch is located should be used to identify that branch where an SFT is concluded through a branch office of a counterparty.

(3) A global unique trader identifier (‘UTI’) system for identifying SFTs is also being developed. Until such time as that global UTI system is finalised and considered suitable for the purposes of reporting SFTs, and this Regulation is amended accordingly, a UTI agreed by the counterparties should be used to identify a SFT.

(4) Article 4a of Commission Implementing Regulation (EU) No 1247/2012 (3) contains a procedure to determine the entity responsible for generating a UTI in respect of the reporting of derivatives contracts for those situations where counterparties fail to agree on the entity responsible for generating the UTI. To ensure consistency between the reporting of derivatives contracts and of SFTs, a similar procedure should be set up for counterparties reporting SFTs.

(5) Currently, there is no common market practice for determining the counterparty side in an SFT. Therefore, specific rules should be established to ensure the accurate and consistent identification of the collateral provider and of the collateral taker in an SFT.

(6) A number of reports may be submitted for a single SFT, for example if successive modifications are made to that SFT. In order to ensure that each report relating to an SFT, and each SFT as a whole, is properly understood, reports should be submitted in the chronological sequence in which the reported events occurred.

(7) To lessen the burden of reporting the modification of certain values, and in particular the details of collateral value, of margin posted or received and of collateral reuse, those details should be reported as they stand at the end of each day only if they vary from previously reported details.

(8) The details of an outstanding margin loan should be reported as they stand at the end of each day, where there is a net cash debit in base currency or where a counterparty's short market value is positive.

(9) The market value of securities lent or borrowed should be reported as it stands at the end of each day. Similarly, when the counterparties report the market value of collateral, they should do so as it stands at the end of each day.

(10) This Regulation is based on the draft implementing technical standards submitted by ESMA to the Commission, pursuant to the procedure in Article 15 of Regulation (EU) No 1095/2010 of the European Parliament and of the Council of 24 November 2010 establishing a European Supervisory Authority (European Securities and Markets Authority) (4).

(11) ESMA has conducted open public consultations on these draft implementing technical standards, analysed the potential related costs and benefits and requested the opinion of the Securities and Markets Stakeholder Group established in accordance with Article 37 of Regulation (EU) No 1095/2010,

(12) As it is the case for the reporting of SFTs, certain identifiers and codes to be used for the reporting of derivative contracts are still being developed. Until such time as those identifiers and codes are available, considered suitable for the purposes of reporting and Implementing Regulation (EU) No 1247/2012 has been amended accordingly, that Regulation provides for the use of an ISO 10692 CFI code to classify derivatives for which an ISO 6166 ISIN code or an AII code are not available, and for the use of a unique trade identifier agreed by the counterparties to identify a derivative report. To ensure legal certainty as regards the appropriate procedure to amend the requirements applicable to the reporting of derivatives contracts, and the required degree of consistency between the reporting of derivatives and of SFTs, Implementing Regulation (EU) No 1247/2012 should only refer to the requirements currently applicable to that reporting.

(13) Implementing Regulation (EU) No 1247/2012 should therefore be amended accordingly,

HAS ADOPTED THIS REGULATION:

## Article 1 — Data standards and formats for SFT reports

The details of an SFT in a report to be submitted pursuant to Article 4(1) of Regulation (EU) 2015/2365 shall be provided in accordance with the standards and formats specified in Tables 1 to 5 of Annex I. That report shall be provided in a common electronic and machine-readable form and in a common XML template in accordance with the ISO 20022 methodology.

## Article 2 — Identification of counterparties and other entities

1\. The report referred to in Article 1 shall use an ISO 17442 legal entity identifier (‘LEI’) code to identify the following:

(a) a beneficiary which is a legal entity;

(b) a broking entity;

(c) a central counterparty (‘CCP’) authorised in accordance with Regulation (EU) No 648/2012;

(d) a clearing member;

(e) an agent lender;

(f) a central securities depository (‘CSD’) participant;

(g) a counterparty which is a legal entity;

(h) a tri-party agent;

(i) a report submitting entity;

(j) an issuer of a security which was lent, borrowed or provided as collateral in a SFT.

2\. A counterparty to an SFT shall ensure that the reference data related to its ISO 17442 LEI code is renewed in accordance with the terms of any of the accredited Local Operating Units of the Global LEI System.

3\. Where an SFT is concluded through a branch of a counterparty, the report referred to in Article 1 shall use the code specified in Field 7 and in Field 8 of Table 1 of Annex I to identify that branch of a counterparty.

## Article 3 — Unique Trade Identifier

1\. A report shall be identified through a unique trade identifier (‘UTI’) agreed by the counterparties in accordance with the format specified in Field 1 of Table 2 of Annex I.

2\. Where counterparties fail to agree on the entity responsible for generating UTI to be assigned to the report, the counterparties shall determine the entity responsible for generating a UTI in accordance with the following:

(a) for centrally-executed and cleared SFTs, the UTI shall be generated at the point of clearing by the CCP for the clearing member. Another UTI shall be generated by the clearing member for its counterparty;

(b) for centrally-executed but not centrally-cleared SFTs, the UTI shall be generated by the trading venue of execution for its member;

(c) for centrally-confirmed and cleared SFTs, the UTI shall be generated by the CCP for the clearing member at the point of clearing. Another UTI shall be generated by the clearing member for its counterparty;

(d) for SFTs that were centrally-confirmed by electronic means but were not centrally-cleared, the UTI shall be generated by the trade confirmation platform at the point of confirmation;

(e) for all SFTs other than those referred to in points (a) to (d), the following shall apply:

(i) where financial counterparties conclude an SFT with non-financial counterparties, the financial counterparties shall generate the UTI;

(ii) for all securities lending or borrowing transactions other than those referred to in point (i), the collateral provider as referred to in Article 4 shall generate the UTI;

(iii) for all SFTs other than those referred to in points (i) and (ii), the collateral taker as referred to in Article 4 shall generate the UTI.

3\. The counterparty generating the UTI shall communicate that UTI to the other counterparty in a timely manner so that the latter is able to meet its reporting obligation.

## Article 4 — Counterparty side

1\. The counterparty side to the SFT referred to in Field 9 of Table 1 of Annex I shall be identified in accordance with paragraphs 2 to 4.

2\. In the case of repurchase transactions, buy-sell back transactions and sell-buy back transactions, the counterparty that buys securities, commodities, or guaranteed rights relating to title to securities or commodities in the opening or spot leg of the trade and agrees to sell them at a specified price on a future date in the closing or forward leg of the trade, shall be identified as the collateral taker in Field 9 of Table 1 of Annex I. The counterparty that sells those securities, commodities, or guaranteed rights shall be identified as the collateral provider in Field 9 of Table 1 of Annex I.

3\. In the case of securities or commodities borrowing transactions and securities or commodities lending transactions, the counterparty that lends the securities or commodities on condition that the borrower will return equivalent securities or commodities on a future date or at the request of the transferor, shall be identified as the collateral taker in Field 9 of Table 1 of Annex I. The counterparty that borrows those securities or commodities shall be identified as the collateral provider in Field 9 of Table 1 of Annex I.

4\. In the case of margin lending transactions, the borrower, that is the counterparty to which credit is extended in exchange for collateral, shall be identified as the collateral provider in Field 9 of Table 1 of Annex I. The lender, that is the counterparty that provides the credit in exchange for collateral, shall be identified as the collateral taker in Field 9 of Table 1 of Annex I.

## Article 5 — Frequency of SFT reports

1\. All reports of the details of an SFT specified under Article 1(2) of Commission Delegated Regulation (EU) 2019/356 (5) be provided in the chronological order in which the reported events occurred.

2\. A counterparty to a margin lending transaction shall report the details of the outstanding margin loan as they stand at the end of each day, where there is a net cash debit in base currency or where a counterparty's short market value is positive.

3\. A counterparty to an outstanding SFT shall report any modification of the details relating to the collateral data in Fields 75 to 94 of Table 2 of Annex I with action type ‘Collateral update’. The counterparty shall report those modified details as they stand at the end of each day until it reports the termination of the SFT, or it reports the SFT with action type ‘Error’, or until the SFT reaches its maturity date, whichever is the earlier.

4\. A counterparty to an outstanding SFT shall report any modification of the end-of-day market value of the securities lent or borrowed in Field 57 of Table 2 of Annex I with action type ‘Valuation update’. The counterparty shall report that modified market value as it stands at the end of each day until it reports the termination of the SFT, or it reports the SFT with action type ‘Error’, or until the SFT reaches its maturity date.

5\. A counterparty shall report any modification of the total amount of margin posted or received for all cleared SFTs as it stands at the end of the day in Fields 8 to 19 of Table 3 of Annex I with action type ‘Margin update’ after it has first reported the total amount of margin posted or received with action type ‘New’.

6\. A counterparty shall report any modification of the value of reused collateral, reinvested cash and the funding sources with action type ‘Reuse update’ as it stands at the end of the day in Fields 8 to 14 of Table 4 of Annex I after it has reported the relevant values with action type ‘New’.

## Article 6 — Amendments to Implementing Regulation (EU) No 1247/2012

Implementing Regulation (EU) No 1247/2012 is amended as follows:

(1) Article 4 is amended as follows:

(a) paragraph 7 is replaced by the following:

‘The derivative shall be classified in Field 4 of Table 2 of the Annex using an ISO 10692 Classification of Financial Instrument (CFI) code.’;

(b) paragraphs 8 and 9 are deleted.

(2) In Article 4a, paragraph 1 is replaced by the following:

‘1. A report shall be identified through a unique trade identifier agreed by the counterparties.’;

(3) The Annex is replaced by the text set out in Annex II to this Regulation.

## Article 7 — Entry into force

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 13 December 2018.

For the Commission

The President

Jean-Claude JUNCKER

(1) OJ L 337, 23.12.2015, p. 1.

(2) OJ L 201, 27.7.2012, p. 1.

(3) Commission Implementing Regulation (EU) No 1247/2012 of 19 December 2012 laying down implementing technical standards with regard to the format and frequency of trade reports to trade repositories according to Regulation (EU) No 648/2012 of the European Parliament and of the Council on OTC derivatives, central counterparties and trade repositories (OJ L 352, 21.12.2012, p. 20).

(4) OJ L 331, 15.12.2010, p. 84.

(5) Commission Delegated Regulation (EU) 2019/356 of 13 December 2018 supplementing Regulation (EU) 2015/2365 of the European Parliament and of the Council with regard to regulatory technical standards specifying the details of securities financing transactions (SFTs) to be reported to trade repositories (See page 1 of this Official Journal).

## ANNEX I

**Formats to be used for reports on the details of securities financing transactions, as referred to in Article 4(1) and (5) of Regulation (EU) 2015/2365**

**Table 1**

**Counterparty Data**

| No | Field | Format |
| --- | --- | --- |
| 1 | Reporting timestamp | ISO 8601 date in the format and Coordinated Universal Time (UTC) time format, i.e. YYYY-MM-DDThh:mm:ssZ |
| 2 | Report submitting entity | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 3 | Reporting counterparty | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 4 | Nature of the reporting counterparty | ‘F’ - Financial counterparty ‘N’ - Non-financial counterparty |
| 5 | Sector of the reporting counterparty | Taxonomy for Financial Counterparties: ‘CDTI’ - Credit institution authorised in accordance with Directive 2013/36/EU of the European Parliament and of the Council (1) or Council Regulation (EU) No 1024/2013 (2) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘INVF’ - Investment firm authorized in accordance with Directive 2014/65/EU of the European Parliament and of the Council (3) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘INUN’ - Insurance undertaking authorized in accordance with Directive 2009/138/EC of the European Parliament and of the Council (4) (Solvency II) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘AIFD’ - AIF managed by AIFMs authorized or registered in accordance with Directive 2011/61/EU of the European Parliament and of the Council (5) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘ORPI’ - Institution for occupational retirement provision authorized or registered in accordance with Directive 2003/41/EC of the European Parliament and of the Council (6) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘CCPS’ - Central counterparty authorized in accordance with Regulation (EU) No 648/2012 of the European Parliament and of the Council (7) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘REIN’ - Reinsurance undertaking authorized in accordance with Solvency II or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘CSDS’ - Central securities depository authorized in accordance with Regulation (EU) No 909/2014 of the European Parliament and of the Council (8) or a third-country entity which would require authorisation or registration in accordance with that legislative act ‘UCIT’ - UCITS and its management company, authorized in accordance with Directive 2009/65/EC of the European Parliament and of the Council (9) or a third-country entity which would require authorisation or registration in accordance with that legislative act Taxonomy for Non-Financial Counterparties. The categories below correspond to the main sections of NACE classification as defined in Regulation (EC) No 1893/2006 of the European Parliament and of the Council (10) ‘A’ - Agriculture, forestry and fishing ‘B’ - Mining and quarrying ‘C’ - Manufacturing ‘D’ - Electricity, gas, steam and air conditioning supply ‘E’ - Water supply, sewerage, waste management and remediation activities ‘F’ - Construction ‘G’ - Wholesale and retail trade, repair of motor vehicles and motorcycles ‘H’ - Transportation and storage ‘I’ - Accommodation and food service activities ‘J’ - Information and communication ‘K’ - Financial and insurance activities ‘L’ - Real estate activities ‘M’ - Professional, scientific and technical activities ‘N’ - Administrative and support service activities ‘O’ - Public administration and defence; compulsory social security ‘P’ - Education ‘Q’ - Human health and social work activities ‘R’ - Arts, entertainment and recreation ‘S’ - Other service activities ‘T’ - Activities of households as employers; undifferentiated goods – and services –producing activities of households for own use ‘U’ - Activities of extraterritorial organizations and bodies |
| 6 | Additional sector classification | ‘ETFT’ - ETF ‘MMFT’ - MMF ‘REIT’ - REIT ‘OTHR’ – Other |
| 7 | Branch of the reporting counterparty | ISO 3166-1 alpha-2 country code 2 alphabetic characters. |
| 8 | Branch of the other counterparty | ISO 3166-1 alpha-2 country code 2 alphabetic characters. |
| 9 | Counterparty side | ‘TAKE’ - Collateral taker ‘GIVE’ - Collateral provider |
| 10 | Entity responsible for the report | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 11 | Other counterparty | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. Client code (up to 50 alphanumeric characters). |
| 12 | Country of the other Counterparty | ISO 3166-1 alpha-2 country code 2 alphabetic characters. |
| 13 | Beneficiary | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. Client code (up to 50 alphanumeric characters). |
| 14 | Tri-party agent | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 15 | Broker | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 16 | Clearing member | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 17 | Central Securities Depository (‘CSD’) participant or indirect participant | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 18 | Agent lender | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |

**Table 2**

**Loan and Collateral Data**

<table>
<tbody><tr><td>No</td><td>Field</td><td>Format</td></tr>
<tr><td>1</td><td>Unique Trade Identifier (UTI)</td><td>Up to 52 alphanumeric character code including four special characters: Only upper-case alphabetic characters A–Z and the digits 0–9, inclusive in both cases, are allowed. </td></tr>
<tr><td>2</td><td>Report tracking number</td><td>Up to 52 alphanumeric character code including four special characters: Only upper-case alphabetic characters A–Z and the digits 0–9, inclusive in both cases, are allowed. </td></tr>
<tr><td>3</td><td>Event date</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>4</td><td>Type of SFT</td><td>‘SLEB’ - securities or commodities lending or securities or commodities borrowing ‘SBSC’ - buy-sell back transaction or sell-buy back transaction  ‘REPO’ - repurchase transaction  ‘MGLD’ - margin lending transaction </td></tr>
<tr><td>5</td><td>Cleared</td><td>‘true’ ‘false’ </td></tr>
<tr><td>6</td><td>Clearing timestamp</td><td>ISO 8601 date in the format and Coordinated Universal Time (UTC) time format, i.e. YYYY-MM-DDThh:mm:ssZ</td></tr>
<tr><td>7</td><td>CCP</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td>8</td><td>Trading venue</td><td>ISO 10383 Market Identifier Code (MIC), 4 alphanumeric characters. Where segmental MICs exist for a trading venue, the segmental MIC shall be used. </td></tr>
<tr><td>9</td><td>Master agreement type</td><td>‘MRAA’ - MRA ‘GMRA’ – GMRA  ‘MSLA’ - MSLA  ‘GMSL’ - GMSLA  ‘ISDA’ - ISDA  ‘DERP’ - Deutscher Rahmenvertrag für Wertpapierpensionsgeschäfte  ‘CNBR’ - China Bond Repurchase Master Agreement,  ‘KRRA’ - Korea Financial Investment Association (KOFIA) Standard Repurchase Agreement  ‘CARA’ - Investment Industry Regulatory Organization of Canada (IIROC) Repurchase/Reverse Repurchase Transaction Agreement  ‘FRFB’ - Convention-Cadre Relative aux Operations de Pensions Livrees,  ‘CHRA’ -Swiss Master Repurchase Agreement  ‘DEMA’ - German Master Agreement  ‘JPBR’ - Japanese Master Agreement on the Transaction with Repurchase Agreement of the Bonds  ‘ESRA’ - Contrato Marco de compraventa y Reporto de valores  ‘OSLA’ - Overseas Securities Lending Agreement (OSLA)  ‘MEFI’ - Master Equity and Fixed Interest Stock Lending Agreement (MEFISLA)  ‘GESL’ - Gilt Edged Stock Lending Agreement (GESLA)  ‘KRSL’ - Korean Securities Lending Agreement (KOSLA)  ‘DERD’ - Deutscher Rahmenvertrag für Wertpapierdarlehen  ‘AUSL’ - Australian Masters Securities Lending Agreement (AMSLA)  ‘JPBL’ - Japanese Master Agreement on Lending Transaction of Bonds  ‘JPSL’ - Japanese Master Agreement on the Borrowing and Lending Transactions of Share Certificates  ‘BIAG’ - bilateral agreement  ‘CSDA’ - CSD bilateral agreement  Or ‘OTHR’ if the master agreement type is not included in the above list </td></tr>
<tr><td>10</td><td>Other master agreement type</td><td>Up to 50 alphanumeric characters.</td></tr>
<tr><td>11</td><td>Master agreement version</td><td>ISO 8601 date in the format YYYY</td></tr>
<tr><td>12</td><td>Execution timestamp</td><td>ISO 8601 date in the format and Coordinated Universal Time (UTC) time format, i.e. YYYY-MM-DDThh:mm:ssZ</td></tr>
<tr><td>13</td><td>Value date (Start date)</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>14</td><td>Maturity date (End date)</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>15</td><td>Termination date</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>16</td><td>Minimum notice period</td><td>Integer field up to 3 digits.</td></tr>
<tr><td>17</td><td>Earliest call-back date</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>18</td><td>General collateral Indicator</td><td>‘SPEC’ - specific collateral ‘GENE’ - general collateral </td></tr>
<tr><td>19</td><td>Delivery By Value (‘DBV’) indicator</td><td>‘true’ ‘false’ </td></tr>
<tr><td>20</td><td>Method used to provide collateral</td><td>‘TTCA’- title transfer collateral arrangement ‘SICA’- securities financial collateral arrangement  ‘SIUR’- securities financial collateral arrangement with the right of use </td></tr>
<tr><td>21</td><td>Open term</td><td>‘true’ ‘false’ </td></tr>
<tr><td>22</td><td>Termination optionality</td><td>‘EGRN’ - evergreen ‘ETSB’ - extendable  ‘NOAP’ - non applicable </td></tr>
<tr><td colspan="3">In the case of margin lending, the attributes listed in fields 23-34 shall be repeated and completed for each currency used in the margin loan.</td></tr>
<tr><td>23</td><td>Fixed rate</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>24</td><td>Day count convention</td><td>The code representing day count convention: ‘A001’ - IC30360ISDAor30360AmericanBasicRule  ‘A002’ - IC30365  ‘A003’ - IC30Actual  ‘A004’ - Actual360  ‘A005’ - Actual365Fixed  ‘A006’ - ActualActualICMA  ‘A007’ - IC30E360orEuroBondBasismodel1  ‘A008’ - ActualActualISDA  ‘A009’ - Actual365LorActuActubasisRule  ‘A010’ - ActualActualAFB  ‘A011’ - IC30360ICMAor30360basicrule  ‘A012’ - IC30E2360orEurobondbasismodel2  ‘A013’ - IC30E3360orEurobondbasismodel3  ‘A014’ - Actual365NL  Or up to 35 alphanumeric characters if the day count convention is not included in the above list. </td></tr>
<tr><td>25</td><td>Floating rate</td><td>The code representing the floating rate index ‘EONA’ - EONIA  ‘EONS’ - EONIA SWAP  ‘EURI’ - EURIBOR  ‘EUUS’ - EURODOLLAR  ‘EUCH’ - EuroSwiss  ‘GCFR’ - GCF REPO  ‘ISDA’ - ISDAFIX  ‘LIBI’ - LIBID  ‘LIBO’ - LIBOR  ‘MAAA’ - Muni AAA  ‘PFAN’ - Pfandbriefe  ‘TIBO’ - TIBOR  ‘STBO’ - STIBOR  ‘BBSW’ - BBSW  ‘JIBA’ - JIBAR  ‘BUBO’ - BUBOR  ‘CDOR’ - CDOR  ‘CIBO’ - CIBOR  ‘MOSP’ - MOSPRIM  ‘NIBO’ - NIBOR  ‘PRBO’ - PRIBOR  ‘TLBO’ - TELBOR  ‘WIBO’ - WIBOR  ‘TREA’ - Treasury  ‘SWAP’ - SWAP  ‘FUSW’ - Future SWAP  Or up to 25 alphanumeric characters if the reference rate is not included in the above list. </td></tr>
<tr><td>26</td><td>Floating rate reference period — time period</td><td>Time period describing reference period, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>27</td><td>Floating rate reference period — multiplier</td><td>Integer multiplier of the time period describing reference period of the floating rate. Up to 3 numeric characters. </td></tr>
<tr><td>28</td><td>Floating rate payment frequency — time period</td><td>Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>29</td><td>Floating rate payment frequency — multiplier</td><td>Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numeric characters. </td></tr>
<tr><td>30</td><td>Floating rate reset frequency — time period</td><td>Time period describing how often the counterparties reset the floating repo rate, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>31</td><td>Floating rate reset frequency — multiplier</td><td>Integer multiplier of the time period describing how often the counterparties reset the floating repo rate. Up to 3 numeric characters. </td></tr>
<tr><td>32</td><td>Spread</td><td>Up to 5 numeric characters.</td></tr>
<tr><td>33</td><td>Margin lending currency amount</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>34</td><td>Margin lending currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td colspan="3">Fields 35-36 shall be repeated and completed for each floating rate adjustment.</td></tr>
<tr><td>35</td><td>Adjusted rate</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>36</td><td>Rate date</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>37</td><td>Principal amount on the value date</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>38</td><td>Principal amount on the maturity date</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>39</td><td>Principal amount currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>40</td><td>Type of asset</td><td>‘SECU’ - Securities ‘COMM’ - Commodities </td></tr>
<tr><td>41</td><td>Security identifier</td><td>ISO 6166 ISIN 12 character alphanumeric code.</td></tr>
<tr><td>42</td><td>Classification of a security</td><td>ISO 10692 CFI, 6 characters alphabetical code.</td></tr>
<tr><td colspan="3">Where a commodity was lent or borrowed, the classification of that commodity shall be specified in fields 43, 44 and 45.</td></tr>
<tr><td>43</td><td>Base product</td><td>Only values in the ‘Base product’ column of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>44</td><td>Sub — product</td><td>Only values in the ‘Sub — product’ column of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>45</td><td>Further sub — product</td><td>Only values in the ‘Further sub — product’ of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>46</td><td>Quantity or nominal amount</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>47</td><td>Unit of measure</td><td>‘KILO’ - Kilogram, ‘PIEC’ - Piece, ‘TONS’ - Ton, ‘METR’ - Metre, ‘INCH’ - Inch, ‘YARD’ - Yard, ‘GBGA’ - GBGallon, ‘GRAM’ - Gram, ‘CMET’ - Centimetre, ‘SMET’ - SquareMetre, ‘FOOT’ - Foot, ‘MILE’ - Mile, ‘SQIN’ - SquareInch, ‘SQFO’ - SquareFoot, ‘SQMI’ - SquareMile, ‘GBOU’ - GBOunce, ‘USOU’ - USOunce, ‘GBPI’ - GBPint, ‘USPI’ - USPint, ‘GBQA’ - GBQuart, ‘USQA’ - USQuart, ‘USGA’ - USGallon, ‘MMET’ - Millimetre, ‘KMET’ - Kilometre, ‘SQYA’ - SquareYard, ‘ACRE’ - Acre, ‘ARES’ - Are, ‘SMIL’ - SquareMillimetre, ‘SCMT’ - SquareCentimetre, ‘HECT’ - Hectare, ‘SQKI’ - SquareKilometre, ‘MILI’ - MilliLitre, ‘CELI’ - Centilitre, ‘LITR’ - Litre, ‘PUND’ - Pound, ‘ALOW’ - Allowances, ‘ACCY’ - AmountOfCurrency, ‘BARL’ - Barrels, ‘BCUF’ - BillionCubicFeet, ‘BDFT’ - BoardFeet, ‘BUSL’ - Bushels, ‘CEER’ - CertifiedEmissionsReduction, ‘CLRT’ - ClimateReserveTonnes, ‘CBME’ - CubicMeters, ‘DAYS’ - Days, ‘DMET’ - DryMetricTons, ‘ENVC’ - EnvironmentalCredit, ‘ENVO’ - EnvironmentalOffset, ‘HUWG’ - Hundredweight, ‘KWDC’ - KilowattDayCapacity, ‘KWHO’ - KilowattHours, ‘KWHC’ - KilowattHoursCapacity, ‘KMOC’ - KilowattMinuteCapacity, ‘KWMC’ - KilowattMonthCapacity, ‘KWYC’ - KilowattYearCapacity, ‘MWDC’ - MegawattDayCapacity, ‘MWHO’ - MegawattHours, ‘MWHC’ - MegawattHoursCapacity, ‘MWMC’ - MegawattMinuteCapacity, ‘MMOC’ - MegawattMonthCapacity, ‘MWYC’ - MegawattYearCapacity, ‘TONE’ - MetricTons, ‘MIBA’ - MillionBarrels, ‘MBTU’ - OneMillionBTU, ‘OZTR’ - TroyOunces, ‘UCWT’ - USHundredweight, ‘IPNT’ - IndexPoint, ‘PWRD’ - PrincipalWithRelationToDebtInstrument, ‘DGEU’ - DieselGallonEquivalent, ‘GGEU’ - GasolineGallonEquivalent, ‘TOCD’ - TonsOfCarbonDioxide.</td></tr>
<tr><td>48</td><td>Currency of nominal amount</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>49</td><td>Security or commodity price</td><td>Up to 18 numeric characters including up to 5 decimals in case the price is expressed units. Up to 11 numeric characters including up to 10 decimals in case the price is expressed as percentage or yield.  The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>50</td><td>Price currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>51</td><td>Security quality</td><td>‘INVG’ - Investment grade ‘NIVG’ - Non-investment grade  ‘NOTR’ - Non-rated  ‘NOAP’ - Not applicable </td></tr>
<tr><td>52</td><td>Maturity of the security</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>53</td><td>Jurisdiction of the issuer</td><td>ISO 3166-1 alpha-2 country code, 2 alphabetic characters.</td></tr>
<tr><td>54</td><td>LEI of the issuer</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td>55</td><td>Security type</td><td>‘GOVS’ - Government securities ‘SUNS’ - Supra-nationals and agencies securities  ‘FIDE’ - Debt securities (including covered bonds) issued by banks and other financial institutions  ‘NFID’ - Corporate debt securities (including covered bonds) issued by non-financial institutions  ‘SEPR’ - Securitized products (including CDO, CMBS, ABCP)  ‘MEQU’ - Main index equities (including convertible bonds)  ‘OEQU’ - Other equities (including convertible bonds)  ‘OTHR’- Other assets (including shares in mutual funds) </td></tr>
<tr><td>56</td><td>Loan value</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>57</td><td>Market value</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>58</td><td>Fixed rebate rate</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’. The negative symbol, if populated, shall not be counted as a numerical character. </td></tr>
<tr><td>59</td><td>Floating rebate rate</td><td>The code representing the floating rate index ‘EONA’ - EONIA  ‘EONS’ - EONIA SWAP  ‘EURI’ - EURIBOR  ‘EUUS’ - EURODOLLAR  ‘EUCH’ - EuroSwiss  ‘GCFR’ - GCF REPO  ‘ISDA’ - ISDAFIX  ‘LIBI’ - LIBID  ‘LIBO’ - LIBOR  ‘MAAA’ - Muni AAA  ‘PFAN’ - Pfandbriefe  ‘TIBO’ - TIBOR  ‘STBO’ - STIBOR  ‘BBSW’ - BBSW  ‘JIBA’ - JIBAR  ‘BUBO’ - BUBOR  ‘CDOR’ - CDOR  ‘CIBO’ - CIBOR  ‘MOSP’ - MOSPRIM  ‘NIBO’ - NIBOR  ‘PRBO’ - PRIBOR  ‘TLBO’ - TELBOR  ‘WIBO’ - WIBOR  ‘TREA’ - Treasury  ‘SWAP’ - SWAP  ‘FUSW’ - Future SWAP  Or up to 25 alphanumeric characters if the reference rate is not included in the above list </td></tr>
<tr><td>60</td><td>Floating rebate rate reference period — time period</td><td>Time period describing reference period, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>61</td><td>Floating rebate rate reference period — multiplier</td><td>Integer multiplier of the time period describing reference period of the floating rebate rate. Up to 3 numeric characters. </td></tr>
<tr><td>62</td><td>Floating rebate rate payment frequency — time period</td><td>Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>63</td><td>Floating rebate rate payment frequency — multiplier</td><td>Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numeric characters. </td></tr>
<tr><td>64</td><td>Floating rebate rate reset frequency — time period</td><td>Time period describing how often the counterparties reset the floating rebate rate, whereby the following abbreviations apply: ‘YEAR’ - Year  ‘MNTH’ - Month  ‘WEEK’ - Week  ‘DAYS’ - Day </td></tr>
<tr><td>65</td><td>Floating rebate rate reset frequency — multiplier</td><td>Integer multiplier of the time period describing how often the counterparties reset the floating rebate rate. Up to 3 numeric characters. </td></tr>
<tr><td>66</td><td>Spread of the rebate rate</td><td>Up to 5 numeric characters.</td></tr>
<tr><td>67</td><td>Lending fee</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’.</td></tr>
<tr><td>68</td><td>Exclusive arrangements</td><td>‘true’ ‘false’ </td></tr>
<tr><td>69</td><td>Outstanding margin loan</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>70</td><td>Base currency of outstanding margin loan</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>71</td><td>Short market value</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td colspan="3">Collateral data</td></tr>
<tr><td>72</td><td>Uncollateralised Securities Lending (‘SL’) flag</td><td>‘true’ ‘false’ </td></tr>
<tr><td>73</td><td>Collateralisation of net exposure</td><td>‘true’ ‘false’ </td></tr>
<tr><td>74</td><td>Value date of the collateral</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td colspan="3">Where specific collateral was used, fields 75 to 94 shall be repeated and completed for each component of collateral, where applicable.</td></tr>
<tr><td>75</td><td>Type of collateral component</td><td>‘SECU’ - Securities ‘COMM’ - Commodities (only for repos, securities and commodities lending and borrowing and buy-sell backs)  ‘CASH’ - Cash </td></tr>
<tr><td colspan="3">Where cash was used as collateral, this shall be specified in fields 76 and 77.</td></tr>
<tr><td>76</td><td>Cash collateral amount</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>77</td><td>Cash collateral currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>78</td><td>Identification of a security used as collateral</td><td>ISO 6166 ISIN 12 character alphanumeric code.</td></tr>
<tr><td>79</td><td>Classification of a security used as collateral</td><td>ISO 10692 CFI, 6 characters alphabetical code.</td></tr>
<tr><td colspan="3">Where a commodity was used as collateral, the classification of that commodity shall be specified in fields 80, 81 and 82.</td></tr>
<tr><td>80</td><td>Base product</td><td>Only values in the ‘Base product’ column of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>81</td><td>Sub — product</td><td>Only values in the ‘Sub — product’ column of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>82</td><td>Further sub — product</td><td>Only values in the ‘Further sub — product’ of the classification of commodities derivatives table are allowed.</td></tr>
<tr><td>83</td><td>Collateral quantity or nominal amount</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>84</td><td>Collateral unit of measure</td><td>‘KILO’ - Kilogram, ‘PIEC’ - Piece, ‘TONS’ - Ton, ‘METR’ - Metre, ‘INCH’ - Inch, ‘YARD’ - Yard, ‘GBGA’ - GBGallon, ‘GRAM’ - Gram, ‘CMET’ - Centimetre, ‘SMET’ - SquareMetre, ‘FOOT’ - Foot, ‘MILE’ - Mile, ‘SQIN’ - SquareInch, ‘SQFO’ - SquareFoot, ‘SQMI’ - SquareMile, ‘GBOU’ - GBOunce, ‘USOU’ - USOunce, ‘GBPI’ - GBPint, ‘USPI’ - USPint, ‘GBQA’ - GBQuart, ‘USQA’ - USQuart, ‘USGA’ - USGallon, ‘MMET’ - Millimetre, ‘KMET’ - Kilometre, ‘SQYA’ - SquareYard, ‘ACRE’ - Acre, ‘ARES’ - Are, ‘SMIL’ - SquareMillimetre, ‘SCMT’ - SquareCentimetre, ‘HECT’ - Hectare, ‘SQKI’ - SquareKilometre, ‘MILI’ - MilliLitre, ‘CELI’ - Centilitre, ‘LITR’ - Litre, ‘PUND’ - Pound, ‘ALOW’ - Allowances, ‘ACCY’ - AmountOfCurrency, ‘BARL’ - Barrels, ‘BCUF’ - BillionCubicFeet, ‘BDFT’ - BoardFeet, ‘BUSL’ - Bushels, ‘CEER’ - CertifiedEmissionsReduction, ‘CLRT’ - ClimateReserveTonnes, ‘CBME’ - CubicMeters, ‘DAYS’ - Days, ‘DMET’ - DryMetricTons, ‘ENVC’ - EnvironmentalCredit, ‘ENVO’ - EnvironmentalOffset, ‘HUWG’ - Hundredweight, ‘KWDC’ - KilowattDayCapacity, ‘KWHO’ - KilowattHours, ‘KWHC’ - KilowattHoursCapacity, ‘KMOC’ - KilowattMinuteCapacity, ‘KWMC’ - KilowattMonthCapacity, ‘KWYC’ - KilowattYearCapacity, ‘MWDC’ - MegawattDayCapacity, ‘MWHO’ - MegawattHours, ‘MWHC’ - MegawattHoursCapacity, ‘MWMC’ - MegawattMinuteCapacity, ‘MMOC’ - MegawattMonthCapacity, ‘MWYC’ - MegawattYearCapacity, ‘TONE’ - MetricTons, ‘MIBA’ - MillionBarrels, ‘MBTU’ - OneMillionBTU, ‘OZTR’ - TroyOunces, ‘UCWT’ - USHundredweight, ‘IPNT’ - IndexPoint, ‘PWRD’ - PrincipalWithRelationToDebtInstrument, ‘DGEU’ - DieselGallonEquivalent, ‘GGEU’ - GasolineGallonEquivalent, ‘TOCD’ - TonsOfCarbonDioxide.</td></tr>
<tr><td>85</td><td>Currency of collateral nominal amount</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>86</td><td>Price currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>87</td><td>Price per unit</td><td>Up to 18 numeric characters including up to 5 decimals in case the price is expressed in units. Up to 11 numeric characters including up to 10 decimals in case the price is expressed as percentage or yield.  The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>88</td><td>Collateral market value</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>89</td><td>Haircut or margin</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>90</td><td>Collateral quality</td><td>‘INVG’ - Investment grade ‘NIVG’ - Non-investment grade  ‘NOTR’ - Non-rated  ‘NOAP’ - Not applicable </td></tr>
<tr><td>91</td><td>Maturity date of the security</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>92</td><td>Jurisdiction of the issuer</td><td>ISO 3166-1 alpha-2 country code, 2 alphabetic characters.</td></tr>
<tr><td>93</td><td>LEI of the issuer</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td>94</td><td>Collateral type</td><td>‘GOVS’ - Government securities ‘SUNS’ - Supra-nationals and agencies securities  ‘FIDE’ - Debt securities (including covered bonds) issued by banks and other financial institutions  ‘NFID’ - Corporate debt securities (including covered bonds) issued by non-financial institutions  ‘SEPR’ - Securitized products (including CDO, CMBS, ABCP)  ‘MEQU’ - Main index equities (including convertible bonds)  ‘OEQU’ - Other equities (including convertible bonds)  ‘OTHR’- Other assets (including shares in mutual funds) </td></tr>
<tr><td>95</td><td>Availability for collateral reuse</td><td>‘true’ ‘false’ </td></tr>
<tr><td colspan="3">Field 96 shall be specified in the case where a collateral basket was used. The detailed allocation of collateral for SFTs transacted against a collateral pool shall be specified in fields 75 to 94 when available.</td></tr>
<tr><td>96</td><td>Collateral basket identifier</td><td>ISO 6166 ISIN 12 character alphanumeric code, or ‘NTAV’ </td></tr>
<tr><td>97</td><td>Portfolio code</td><td>52 alphanumeric character code including four special characters: .- _.  Special characters are not allowed at the beginning and at the end of the code. No space allowed. </td></tr>
<tr><td>98</td><td>Action type</td><td>‘NEWT’ - New ‘MODI’ - Modification  ‘VALU’ - Valuation  ‘COLU’ - Collateral update  ‘EROR’ - Error  ‘CORR’ - Correction  ‘ETRM’ - Termination/Early Termination  ‘POSC’ - Position component </td></tr>
<tr><td>99</td><td>Level</td><td>‘TCTN’ - Transaction ‘PSTN’ - Position </td></tr>
</tbody>
</table>

**Table 3**

**Margin Data**

| No | Field | Format |
| --- | --- | --- |
| 1 | Reporting timestamp | ISO 8601 date in the format and Coordinated Universal Time (UTC) time format, i.e. YYYY-MM-DDThh:mm:ssZ |
| 2 | Event date | ISO 8601 date in the format YYYY-MM-DD |
| 3 | Report submitting entity | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 4 | Reporting Counterparty | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 5 | Entity responsible for the report | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 6 | Other counterparty | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code. |
| 7 | Portfolio code | 52 alphanumeric character code including four special characters: .- _. Special characters are not allowed at the beginning and at the end of the code. No space allowed. |
| 8 | Initial margin posted | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 9 | Currency of the initial margin posted | ISO 4217 Currency Code, 3 alphabetic characters. |
| 10 | Variation margin posted | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 11 | Currency of the variation margin posted | ISO 4217 Currency Code, 3 alphabetic characters. |
| 12 | Initial margin received | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 13 | Currency of the initial margin received | ISO 4217 Currency Code, 3 alphabetic characters. |
| 14 | Variation margin received | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 15 | Currency of the variation margin received | ISO 4217 Currency Code, 3 alphabetic characters. |
| 16 | Excess collateral posted | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 17 | Currency of the excess collateral posted | ISO 4217 Currency Code, 3 alphabetic characters. |
| 18 | Excess collateral received | Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. |
| 19 | Currency of the excess collateral received | ISO 4217 Currency Code, 3 alphabetic characters. |
| 20 | Action type | ‘NEWT’ - New ‘MARU’ - Margin update ‘EROR’ - Error ‘CORR’ - Correction |

**Table 4**

**Re-use, Cash Reinvestment and Funding Sources Data**

<table>
<tbody><tr><td>No</td><td>Field</td><td>Format</td></tr>
<tr><td>1</td><td>Reporting timestamp</td><td>ISO 8601 date in the format and UTC time format, i.e. YYYY-MM-DDThh:mm:ssZ</td></tr>
<tr><td>2</td><td>Event date</td><td>ISO 8601 date in the format YYYY-MM-DD</td></tr>
<tr><td>3</td><td>Report submitting entity</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td>4</td><td>Reporting counterparty</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td>5</td><td>Entity responsible for the report</td><td>ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code.</td></tr>
<tr><td colspan="3">Field 6 shall be repeated and completed for each collateral component.</td></tr>
<tr><td>6</td><td>Type of collateral component</td><td>‘SECU’ - Securities ‘CASH’ - Cash </td></tr>
<tr><td colspan="3">Fields 7, 8, 9 and 10 shall be repeated and completed for each security.</td></tr>
<tr><td>7</td><td>Collateral component</td><td>ISO 6166 ISIN 12 character alphanumeric code.</td></tr>
<tr><td>8</td><td>Value of reused collateral</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>9</td><td>Estimated reuse of collateral</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>10</td><td>Reused collateral currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>11</td><td>Reinvestment Rate</td><td>Up to 11 numeric characters including up to 10 decimals expressed as percentage where 100 % is represented as ‘100’.</td></tr>
<tr><td colspan="3">Fields 12, 13 and 14 shall be repeated and completed for each investment where cash collateral has been re-invested and in respect of each currency.</td></tr>
<tr><td>12</td><td>Type of re-invested cash investment</td><td>‘MMFT’ - registered money market fund ‘OCMP’ - any other commingled pool  ‘REPM’ - the repo market  ‘SDPU’ - direct purchase of securities  ‘OTHR’ - other </td></tr>
<tr><td>13</td><td>Re-invested cash amount</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character. If populated, it shall be represented with a dot. </td></tr>
<tr><td>14</td><td>Re-invested cash currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td colspan="3">In the case of margin lending transactions, the counterparty shall repeat and complete fields 15, 16 and 17 for each funding source and shall provide the information in these fields at entity level.</td></tr>
<tr><td>15</td><td>Funding sources</td><td>‘REPO’ - repos or BSB ‘SECL’ - cash collateral from securities lending  ‘FREE’ - free credits  ‘CSHS’ - proceeds from customer short sales  ‘BSHS’ - proceeds from broker short sales  ‘UBOR’ - unsecured borrowing  ‘OTHR’ - other </td></tr>
<tr><td>16</td><td>Market value of the funding sources</td><td>Up to 18 numeric characters including up to 5 decimals. The decimal mark is not counted as a numeric character.  If not possible, pro rata amount. </td></tr>
<tr><td>17</td><td>Funding sources currency</td><td>ISO 4217 Currency Code, 3 alphabetic characters.</td></tr>
<tr><td>18</td><td>Action type</td><td>‘NEWT’ - New ‘REUU’ - reuse update  ‘EROR’ - Error  ‘CORR’ - Correction </td></tr>
</tbody>
</table>

**Table 5**

**Classification of commodities**

<table>
<tbody><tr><td>Base product</td><td>Sub — product</td><td>Further sub — product</td></tr>
<tr><td rowspan="10">‘AGRI’ - Agricultural</td><td>‘GROS’ - Grains Oil Seeds</td><td>‘FWHT’ - Feed Wheat ‘SOYB’ - Soybeans  ‘CORN’ - Maize  ‘RPSD’ – Rapeseed  ‘RICE’ - Rice  ‘OTHR’ - Other </td></tr>
<tr><td>‘SOFT’ - Softs</td><td>‘CCOA’ - Cocoa ‘ROBU’ - Robusta Coffee  ‘WHSG’ - White Sugar  ‘BRWN’ - Raw Sugar  ‘OTHR’ - Other </td></tr>
<tr><td>‘POTA’- Potato</td><td></td></tr>
<tr><td>‘OOLI’- Olive oil</td><td>‘LAMP’ – ‘Lampante’ ‘OTHR’ - Other </td></tr>
<tr><td>‘DIRY’- Dairy</td><td></td></tr>
<tr><td>‘FRST’ - Forestry</td><td></td></tr>
<tr><td>‘SEAF’ - Seafood</td><td></td></tr>
<tr><td>‘LSTK’ - Livestock</td><td></td></tr>
<tr><td>‘GRIN’ - Grain</td><td>‘MWHT’ - Milling Wheat ‘OTHR’ - Other </td></tr>
<tr><td>‘OTHR’ - Other</td><td></td></tr>
<tr><td rowspan="4">‘NRGY’ – ‘Energy</td><td>‘ELEC’ -Electricity</td><td>‘BSLD’ - Base load ‘FITR’ - Financial Transmission Rights  ‘PKLD’ - Peak load  ‘OFFP’ - Off-peak  ‘OTHR’ - Other </td></tr>
<tr><td>‘NGAS’ - Natural Gas</td><td>‘GASP’ - GASPOOL ‘LNGG’ - LNG  ‘NBPG’ - NBP  ‘NCGG’ - NCG  ‘TTFG’ – TTF  ‘OTHR’ - Other </td></tr>
<tr><td>‘OILP’ -Oil</td><td>‘BAKK’ - Bakken ‘BDSL’ - Biodiesel  ‘BRNT’ - Brent  ‘BRNX’ - Brent NX  ‘CNDA’ - Canadian  ‘COND’ - Condensate  ‘DSEL’ - Diesel  ‘DUBA’ - Dubai  ‘ESPO’ - ESPO  ‘ETHA’ - Ethanol  ‘FUEL’ - Fuel  ‘FOIL’ - Fuel Oil  ‘GOIL’ - Gasoil  ‘GSLN’ - Gasoline  ‘HEAT’ - Heating Oil  ‘JTFL’ - Jet Fuel  ‘KERO’ - Kerosene  ‘LLSO’ - Light Louisiana Sweet (LLS)  ‘MARS’ - Mars  ‘NAPH’ - Naptha  ‘NGLO’ - NGL  ‘TAPI’ - Tapis  ‘URAL’ - Urals  ‘WTIO’ – WTI  ‘OTHR’ - Other </td></tr>
<tr><td>‘COAL’- Coal ‘INRG’ - Inter Energy  ‘RNNG’ - Renewable energy  ‘LGHT’ - Light ends  ‘DIST’ – Distillates  ‘OTHR’ - Other </td><td></td></tr>
<tr><td rowspan="2">‘ENVR’ - Environmental</td><td>‘EMIS’ - Emissions</td><td>‘CERE’ - CER ‘ERUE’ - ERU  ‘EUAE’ - EUA  ‘EUAA’ – EUAA  ‘OTHR’-Other </td></tr>
<tr><td>‘WTHR’ - Weather ‘CRBR’ - Carbon related’  ‘OTHR’ - Other </td><td></td></tr>
<tr><td rowspan="4">‘FRGT’ -‘Freight’</td><td>‘WETF’ - Wet</td><td>‘TNKR’ –Tankers ‘OTHR’ - Other </td></tr>
<tr><td>‘DRYF’ - Dry</td><td>‘DBCR’ - Dry bulk carriers ‘OTHR’ - Other </td></tr>
<tr><td>‘CSHP’ - Containerships</td><td></td></tr>
<tr><td>‘OTHR’ - Other</td><td></td></tr>
<tr><td>‘FRTL’ -‘Fertilizer’</td><td>‘AMMO’ - Ammonia ‘DAPH’ - DAP (Diammonium Phosphate)  ‘PTSH’ - Potash  ‘SLPH’ - Sulphur  ‘UREA’ - Urea  ‘UAAN’ - UAN (urea and ammonium nitrate)  ‘OTHR’ - Other </td><td></td></tr>
<tr><td>‘INDP’ - Industrial products’</td><td>‘CSTR’ - Construction ‘MFTG’ - Manufacturing </td><td></td></tr>
<tr><td rowspan="2">‘METL’ - Metals’</td><td>‘NPRM’ - Non Precious</td><td>‘ALUM’ - Aluminium ‘ALUA’ - Aluminium Alloy  ‘CBLT’ - Cobalt  ‘COPR’ - Copper  ‘IRON’ - Iron ore  ‘LEAD’ - Lead  ‘MOLY’ - Molybdenum  ‘NASC’ - NASAAC  ‘NICK’ - Nickel  ‘STEL’ - Steel  ‘TINN’ - Tin  ‘ZINC’ - Zinc  ‘OTHR’ - Other </td></tr>
<tr><td>‘PRME’ - Precious</td><td>‘GOLD’ - Gold ‘SLVR’ - Silver  ‘PTNM’ - Platinum  ‘PLDM’ - Palladium  ‘OTHR’ - Other </td></tr>
<tr><td>‘MCEX’ - Multi Commodity Exotic’</td><td></td><td></td></tr>
<tr><td>‘PAPR’ - Paper’</td><td>‘CBRD’ - Containerboard ‘NSPT’ - Newsprint  ‘PULP’ - Pulp  ‘RCVP’ - Recovered paper  ‘OTHR’ - Other </td><td></td></tr>
<tr><td>‘POLY’ - Polypropylene’</td><td>‘PLST’ – Plastic ‘OTHR’ - Other </td><td></td></tr>
<tr><td>‘INFL’ - Inflation’</td><td></td><td></td></tr>
<tr><td>‘OEST’ - Official economic statistics’</td><td></td><td></td></tr>
<tr><td>‘OTHC’ - Other C10 ‘as defined in Table 10.1 Section 10 of Annex III to Commission Delegated Regulation (EU) 2017/583 (11)</td><td></td><td></td></tr>
<tr><td>‘OTHR’ - Other</td><td></td><td></td></tr>
</tbody>
</table>

(1) Directive 2013/36/EU of the European Parliament and of the Council of 26 June 2013 on access to the activity of credit institutions and the prudential supervision of credit institutions and investment firms (OJ L 176, 27.6.2013, p. 338).

(2) Council Regulation (EU) No 1024/2013 of 15 October 2013 conferring specific tasks on the European Central Bank concerning policies relating to the prudential supervision of credit institutions (OJ L 287, 29.10.2013, p. 63).

(3) Directive 2014/65/EU of the European Parliament and of the Council of 15 May 2014 on markets in financial instruments (OJ L 173, 12.6.2014, p. 349).

(4) Directive 2009/138/EC of the European Parliament and of the Council of 25 November 2009 on the taking-up and pursuit of the business of Insurance and Reinsurance (Solvency II) (OJ L 335, 17.12.2009, p. 1).

(5) Directive 2011/61/EU of the European Parliament and of the Council of 8 June 2011 on Alternative Investment Fund Managers (OJ L 174, 1.7.2011, p. 1).

(6) Directive 2003/41/EC of the European Parliament and of the Council of 3 June 2003 on the activities and supervision of institutions for occupational retirement provision (OJ L 235, 23.9.2003, p. 10).

(7) Regulation (EU) No 648/2012 of the European Parliament and of the Council of 4 July 2012 on OTC derivatives, central counterparties and trade repositories (OJ L 201, 27.7.2012, p. 1).

(8) Regulation (EU) No 909/2014 of the European Parliament and of the Council of 23 July 2014 on improving securities settlement in the European Union and on central securities depositories (OJ L 257, 28.8.2014, p. 1).

(9) Directive 2009/65/EC of the European Parliament and of the Council of 13 July 2009 on the coordination of laws, regulations and administrative provisions relating to undertakings for collective investment in transferable securities (UCITS) (OJ L 302, 17.11.2009, p. 32)

(10) Regulation (EC) No 1893/2006 of the European Parliament and of the Council of 20 December 2006 establishing the statistical classification of economic activities NACE Revision 2 (OJ L 393, 30.12.2006, p. 1).

(11) Commission Delegated Regulation (EU) 2017/583 of 14 July 2016 supplementing Regulation (EU) No 600/2014 of the European Parliament and of the Council on markets in financial instruments with regard to regulatory technical standards on transparency requirements for trading venues and investment firms in respect of bonds, structured finance products, emission allowances and derivatives (OJ L 87, 31.3.2017, p. 229)

## ANNEX II

The Annex to Implementing Regulation (EU) No 1247/2012 is replaced by the text below.

**‘ANNEX**

**Table 1**

**Counterparty Data**

|  | Field | Format |
| --- | --- | --- |
|  | Parties to the contract |  |
|  |  |  |
| 1 | Reporting timestamp | ISO 8601 date in the format and Coordinated Universal Time (UTC) time format YYYY-MM-DDThh:mm:ssZ |
| 2 | Reporting Counterparty ID | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code. |
| 3 | Type of ID of the other Counterparty | ‘LEI’ for ISO 17442 Legal Entity Identifier (LEI) ‘CLC’ for Client code |
| 4 | ID of the other Counterparty | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code. Client code (up to 50 alphanumerical digits). |
| 5 | Country of the other Counterparty | ISO 3166 – 2 character country code |
| 6 | Corporate sector of the reporting counterparty | Taxonomy for Financial Counterparties: A = Assurance undertaking authorised in accordance with Directive 2009/138/EC of the European Parliament and of the Council (1) C = Credit institution authorised in accordance with Directive 2013/36/EU of the European Parliament and of the Council (2) F = Investment firm authorised in accordance with Directive 2004/39/EC of the European Parliament and of the Council (3) I = Insurance undertaking authorised in accordance with Directive 2009/138/EC L = Alternative investment fund managed by Alternative Investment Fund Managers (AIFMs) authorised or registered in accordance with Directive 2011/61/EU of the European Parliament and of the Council (4) O = Institution for occupational retirement provision within the meaning of Article 6(a) of Directive 2003/41/EC of the European Parliament and of the Council (5) R = Reinsurance undertaking authorised in accordance with Directive 2009/138/EC U = Undertakings for the Collective Investment in Transferable Securities (UCITS)and its management company, authorised in accordance with Directive 2009/65/EC of the European Parliament and of the Council (6) Taxonomy for Non-Financial Counterparties. The following categories correspond to the main sections of Statistical classification of economic activities in the European Community (NACE) as defined in Regulation (EC) No 1893/2006 of the European Parliament and of the Council (7) 1 = Agriculture, forestry and fishing 2 = Mining and quarrying 3 = Manufacturing 4 = Electricity, gas, steam and air conditioning supply 5 = Water supply, sewerage, waste management and remediation activities 6 = Construction 7 = Wholesale and retail trade, repair of motor vehicles and motorcycles 8 = Transportation and storage 9 = Accommodation and food service activities 10 = Information and communication 11 = Financial and insurance activities 12 = Real estate activities 13 = Professional, scientific and technical activities 14 = Administrative and support service activities 15 = Public administration and defence; compulsory social security 16 = Education 17 = Human health and social work activities 18 = Arts, entertainment and recreation 19 = Other service activities 20 = Activities of households as employers; undifferentiated goods – and services –producing activities of households for own use 21 = Activities of extraterritorial organisations and bodies Where more than one activity is reported, list the codes in order of the relative importance of the corresponding activities, separating them with a ‘-’. Leave blank in the case of CCPs and other type of counterparties in accordance with Article 1(5) of Regulation (EU) No 648/2012. |
| 7 | Nature of the reporting counterparty | F = Financial Counterparty N = Non-Financial Counterparty C = Central Counterparty O = Other |
| 8 | Broker ID | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code. |
| 9 | Report submitting entity ID | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code) |
| 10 | Clearing member ID | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code |
| 11 | Type of ID of the Beneficiary | ‘LEI’ for ISO 17442 Legal Entity Identifier (LEI) ‘CLC’ for Client code |
| 12 | Beneficiary ID | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code or up to 50 alphanumerical character client code in the case where the client is not eligible for a Legal Entity Identifier |
| 13 | Trading capacity | P = Principal A = Agent |
| 14 | Counterparty side | B = Buyer S = Seller Populated in accordance with Article 3a |
| 15 | Directly linked to commercial activity or treasury financing | Y = Yes N = No |
| 16 | Clearing threshold | Y = Above the threshold N = Below the threshold |
| 17 | Value of contract | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |
| 18 | Currency of the value | ISO 4217 Currency Code, 3 alphabetical characters |
| 19 | Valuation timestamp | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |
| 20 | Valuation type | M = Mark-to-market O = Mark-to-model C = CCP's valuation. |
| 21 | Collateralisation | U = uncollateralised PC = partially collateralised OC = one way collateralised FC = fully collateralised Populated in accordance with Article 3b |
| 22 | Collateral portfolio | Y = Yes N = No |
| 23 | Collateral portfolio code | Up to 52 alphanumerical characters including four special characters: ‘. - _.’ Special characters are not allowed at the beginning and at the end of the code. No space allowed. |
| 24 | Initial margin posted | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 25 | Currency of the initial margin posted | ISO 4217 Currency Code, 3 alphabetical characters |
| 26 | Variation margin posted | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 27 | Currency of the variation margins posted | ISO 4217 Currency Code, 3 alphabetical characters |
| 28 | Initial margin received | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 29 | Currency of the initial margin received | ISO 4217 Currency Code, 3 alphabetical characters |
| 30 | Variation margin received | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 31 | Currency of the variation margins received | ISO 4217 Currency Code, 3 alphabetical characters |
| 32 | Excess collateral posted | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 33 | Currency of the excess collateral posted | ISO 4217 Currency Code, 3 alphabetical characters |
| 34 | Excess collateral received | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |
| 35 | Currency of the excess collateral received | ISO 4217 Currency Code, 3 alphabetical characters |

**Table 2**

**Common Data**

|  | Field | Format | Applicable types of derivative contracts |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  | Section 2a – Contract type |  | All contracts |
| 1 | Contract type | CD = Financial contracts for difference FR = Forward rate agreements FU = Futures FW = Forwards OP = Option SB = Spreadbet SW = Swap ST = Swaption OT = Other |  |
| 2 | Asset class | CO = Commodity and emission allowances CR = Credit CU = Currency EQ = Equity IR = Interest Rate |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2b – Contract information |  | All contracts |
| 3 | Product classification type | C = CFI |  |
| 4 | Product classification | ISO 10692 CFI, 6 characters alphabetical code |  |
| 5 | Product identification type | Specify the applicable identification: I = ISIN A = AII |  |
| 6 | Product identification | For product identifier type I: ISO 6166 ISIN 12 character alphanumerical code For product identifier type A: Complete AII code |  |
| 7 | Underlying identification type | I = ISIN A = AII B = Basket X = Index |  |
| 8 | Underlying identification | For underlying identification type I: ISO 6166 ISIN 12 character alphanumerical code For underlying identification type A: complete AII code For underlying identification type B: all individual components identification through ISO 6166 ISIN or complete AII code. Identifiers of individual components shall be separated with a dash ‘-’. For underlying identification type X: ISO 6166 ISIN if available, otherwise full name of the index as assigned by the index provider |  |
| 9 | Notional currency 1 | ISO 4217 Currency Code, 3 alphabetical characters |  |
| 10 | Notional currency 2 | ISO 4217 Currency Code, 3 alphabetical characters |  |
| 11 | Deliverable currency | ISO 4217 Currency Code, 3 alphabetical characters |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2c – Details on the transaction |  | All contracts |
| 12 | Trade ID | Up to 52 alphanumerical character code including four special characters:‘. - _.’ Special characters are not allowed at the beginning and at the end of the code. No space allowed. |  |
| 13 | Report tracking number | An alphanumeric field up to 52 characters |  |
| 14 | Complex trade component ID | An alphanumeric field up to 35 characters |  |
| 15 | Venue of execution | ISO 10383 Market Identifier Code (MIC), 4 alphanumerical characters, in accordance with Article 4(b). |  |
| 16 | Compression | Y = contract results from compression N = contract does not result from compression |  |
| 17 | Price/rate | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. In case the price is reported in percent values, it should be expressed as percentage where 100 % is represented as ‘100’ |  |
| 18 | Price notation | U = Units P = Percentage Y = Yield |  |
| 19 | Currency of price | ISO 4217 Currency Code, 3 alphabetic characters |  |
| 20 | Notional | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 21 | Price multiplier | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |  |
| 22 | Quantity | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |  |
| 23 | Up-front payment | Up to 20 numerical characters including decimals. The negative symbol to be used to indicate that the payment was made, not received. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 24 | Delivery type | C = Cash P = Physical O = Optional for counterparty or when determined by a third party |  |
| 25 | Execution timestamp | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |  |
| 26 | Effective date | ISO 8601 date in the format YYYY-MM-DD |  |
| 27 | Maturity date | ISO 8601 date in the format YYYY-MM-DD |  |
| 28 | Termination date | ISO 8601 date in the format YYYY-MM-DD |  |
| 29 | Settlement date | ISO 8601 date in the format YYYY-MM-DD |  |
| 30 | Master Agreement type | Free Text, field of up to 50 characters, identifying the name of the Master Agreement used, if any |  |
| 31 | Master Agreement version | ISO 8601 date in the format YYYY |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2d – Risk mitigation/Reporting |  | All contracts |
| 32 | Confirmation timestamp | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |  |
| 33 | Confirmation means | Y = Non-electronically confirmed N = Non-confirmed E = Electronically confirmed |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2e – Clearing |  | All contracts |
| 34 | Clearing obligation | Y = Yes N = No |  |
| 35 | Cleared | Y = Yes N = No |  |
| 36 | Clearing timestamp | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |  |
| 37 | CCP | ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code |  |
| 38 | Intragroup | Y = Yes N = No |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2f – Interest Rates |  | Interest rate derivatives |
| 39 | Fixed rate of leg 1 | Up to 10 numerical characters including decimals expressed as percentage where 100 % is represented as ‘100’. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 40 | Fixed rate of leg 2 | Up to 10 numerical characters including decimals expressed as percentage where 100 % is represented as ‘100’. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 41 | Fixed rate day count leg 1 | Numerator/Denominator where both Numerator and Denominator are numerical characters or alphabetic expression ‘Actual’, e.g. 30/360 or Actual/365 |  |
| 42 | Fixed rate day count leg 2 | Numerator/Denominator where both Numerator and Denominator are numerical characters or alphabetic expression ‘Actual’, e.g. 30/360 or Actual/365 |  |
| 43 | Fixed rate payment frequency leg 1 –time period | Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 44 | Fixed rate payment frequency leg 1 – multiplier | Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numerical characters. |  |
| 45 | Fixed rate payment frequency leg 2 – time period | Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 46 | Fixed rate payment frequency leg 2 – multiplier | Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numerical characters. |  |
| 47 | Floating rate payment frequency leg 1 – time period | Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 48 | Floating rate payment frequency leg 1 – multiplier | Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numerical characters. |  |
| 49 | Floating rate payment frequency leg 2 – time period | Time period describing how often the counterparties exchange payments, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 50 | Floating rate payment frequency leg 2 – multiplier | Integer multiplier of the time period describing how often the counterparties exchange payments. Up to 3 numerical characters. |  |
| 51 | Floating rate reset frequency leg 1 – time period | Time period describing how often the counterparties reset the floating rate, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 52 | Floating rate reset frequency leg 1 – multiplier | Integer multiplier of the time period describing how often the counterparties reset the floating rate. Up to 3 numerical characters. |  |
| 53 | Floating rate reset frequency leg 2 – time period | Time period describing how often the counterparties reset the floating rate, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 54 | Floating rate reset frequency leg 2 – multiplier | Integer multiplier of the time period describing how often the counterparties reset the floating rate. Up to 3 numerical characters. |  |
| 55 | Floating rate of leg 1 | The name of the floating rate index ‘EONA’ – EONIA ‘EONS’ – EONIA SWAP ‘EURI’ – EURIBOR ‘EUUS’ – EURODOLLAR ‘EUCH’ – EuroSwiss ‘GCFR’ – GCF REPO ‘ISDA’ – ISDAFIX ‘LIBI’ – LIBID ‘LIBO’ – LIBOR ‘MAAA’ – Muni AAA ‘PFAN’ – Pfandbriefe ‘TIBO’ – TIBOR ‘STBO’ – STIBOR ‘BBSW’ – BBSW ‘JIBA’ – JIBAR ‘BUBO’ – BUBOR ‘CDOR’ – CDOR ‘CIBO’ – CIBOR ‘MOSP’ – MOSPRIM ‘NIBO’ – NIBOR ‘PRBO’ – PRIBOR ‘TLBO’ – TELBOR ‘WIBO’ – WIBOR ‘TREA’ – Treasury ‘SWAP’ – SWAP ‘FUSW’ – Future SWAP Or up to 25 alphanumerical characters if the reference rate is not included in the above list |  |
| 56 | Floating rate reference period leg 1 – time period | Time period describing reference period, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 57 | Floating rate reference period leg 1 – multiplier | Integer multiplier of the time period describing the reference period. Up to 3 numerical characters. |  |
| 58 | Floating rate of leg 2 | The name of the floating rate index ‘EONA’ – EONIA ‘EONS’ – EONIA SWAP ‘EURI’ – EURIBOR ‘EUUS’ – EURODOLLAR ‘EUCH’ – EuroSwiss ‘GCFR’ – GCF REPO ‘ISDA’ – ISDAFIX ‘LIBI’ – LIBID ‘LIBO’ – LIBOR ‘MAAA’ – Muni AAA ‘PFAN’ – Pfandbriefe ‘TIBO’ – TIBOR ‘STBO’ – STIBOR ‘BBSW’ – BBSW ‘JIBA’ – JIBAR ‘BUBO’ – BUBOR ‘CDOR’ – CDOR ‘CIBO’ – CIBOR ‘MOSP’ – MOSPRIM ‘NIBO’ – NIBOR ‘PRBO’ – PRIBOR ‘TLBO’ – TELBOR ‘WIBO’ – WIBOR ‘TREA’ – Treasury ‘SWAP’ – SWAP ‘FUSW’ – Future SWAP Or up to 25 alphanumerical characters if the reference rate is not included in the above list |  |
| 59 | Floating rate reference period leg 2 – time period | Time period describing reference period, whereby the following abbreviations apply: Y = Year M = Month W = Week D = Day |  |
| 60 | Floating rate reference period leg 2 – multiplier | Integer multiplier of the time period describing the reference period. Up to 3 numerical characters. |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2g – Foreign Exchange |  | Currency derivatives |
| 61 | Delivery currency 2 | ISO 4217 Currency Code, 3 alphabetical character code |  |
| 62 | Exchange rate 1 | Up to 10 numerical digits including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 63 | Forward exchange rate | Up to 10 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 64 | Exchange rate basis | Two ISO 4217 currency codes separated by ‘/’. First currency code shall indicate the base currency, and the second currency code shall indicate the quote currency. |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2h – Commodities and emission allowances |  | Commodity and emission allowance derivatives |
|  | General |  |  |
|  |  |  |  |
| 65 | Commodity base | AG = Agricultural EN = Energy FR = Freights ME = Metals IN = Index EV = Environmental EX = Exotic OT = Other |  |
| 66 | Commodity details | Agricultural GO = Grains oilseeds DA = Dairy LI = Livestock FO = Forestry SO = Softs SF = Seafood OT = Other Energy OI = Oil NG = Natural gas CO = Coal EL = Electricity IE = Inter-energy OT = Other Freights DR = Dry WT = Wet OT = Other Metals PR = Precious NP = Non-precious Environmental WE = Weather EM = Emissions OT = Other |  |
|  | Energy |  |  |
|  |  |  |  |
| 67 | Delivery point or zone | EIC code, 16 character alphanumeric code Repeatable field. |  |
| 68 | Interconnection Point | EIC code, 16 character alphanumeric code |  |
| 69 | Load type | BL = Base Load PL = Peak Load OP = Off-Peak BH = Hour/Block Hours SH = Shaped GD = Gas Day OT = Other |  |
|  |  |  |  |
|  |  |  |  |
|  | Repeatable section of fields 70 – 77 |  |  |
| 70 | Load delivery intervals | hh:mmZ |  |
| 71 | Delivery start date and time | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |  |
| 72 | Delivery end date and time | ISO 8601 date in the UTC time format YYYY-MM-DDThh:mm:ssZ |  |
| 73 | Duration | N = Minutes H = Hour D = Day W = Week M = Month Q = Quarter S = Season Y = Annual O = Other |  |
| 74 | Days of the week | WD = Weekdays WN = Weekend MO = Monday TU = Tuesday WE = Wednesday TH = Thursday FR = Friday SA = Saturday SU = Sunday Multiple values separated by ‘/’ are permitted |  |
| 75 | Delivery capacity | Up to 20 numerical digits including decimals The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
| 76 | Quantity Unit | KW KWh/h KWh/d MW MWh/h MWh/d GW GWh/h GWh/d Therm/d KTherm/d MTherm/d cm/d mcm/d |  |
| 77 | Price/time interval quantities | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2i – Options |  | Contracts that contain an option |
| 78 | Option type | P = Put C = Call O = where it cannot be determined whether it is a call or a put |  |
| 79 | Option exercise style | A = American B = Bermudan E = European S = Asian More than one value is allowed |  |
| 80 | Strike price (cap/floor rate) | Up to 20 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. The negative symbol, if populated, is not counted as a numerical character. Where the strike price is reported in percent values, it should be expressed as percentage where 100 % is represented as ‘100’ |  |
| 81 | Strike price notation | U = Units P = Percentage Y = Yield |  |
| 82 | Maturity date of the underlying | ISO 8601 date in the format YYYY-MM-DD |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2j – Credit derivatives |  |  |
| 83 | Seniority | SNDB = Senior, such as Senior Unsecured Debt (Corporate/Financial), Foreign Currency Sovereign Debt (Government), SBOD = Subordinated, such as Subordinated or Lower Tier 2 Debt (Banks), Junior Subordinated or Upper Tier 2 Debt (Banks), OTHR = Other, such as Preference Shares or Tier 1 Capital (Banks) or other credit derivatives |  |
| 84 | Reference entity | ISO 3166 – 2 character country code or ISO 3166-2 – 2 character country code followed by dash ‘-’ and up to 3 alphanumeric character country subdivision code or ISO 17442 Legal Entity Identifier (LEI) 20 alphanumerical character code |  |
| 85 | Frequency of payment | MNTH = Monthly QURT = Quarterly MIAN = Semi-annually YEAR = Yearly |  |
| 86 | The calculation basis | Numerator/Denominator where both, Numerator and Denominator are numerical characters or alphabetic expression ‘Actual’, e.g. 30/360 or Actual/365 |  |
| 87 | Series | Integer field up to 5 characters |  |
| 88 | Version | Integer field up to 5 characters |  |
| 89 | Index factor | Up to 10 numerical characters including decimals. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |  |
| 90 | Tranche | T = Tranched U = Untranched |  |
| 91 | Attachment point | Up to 10 numerical characters including decimals expressed as a decimal fraction between 0 and 1. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |  |
| 92 | Detachment point | Up to 10 numerical characters including decimals expressed as a decimal fraction between 0 and 1. The decimal mark is not counted as a numerical character. If populated, it shall be represented by a dot. |  |
|  |  |  |  |
|  |  |  |  |
|  | Section 2k – Modifications to the contract |  |  |
| 93 | Action type | N = New M = Modify E = Error C = Early Termination R = Correction Z = Compression V = Valuation update P = Position component |  |
| 94 | Level | T = Trade P = Position |  |

’

(1) Directive 2009/138/EC of the European Parliament and of the Council of 25 November 2009 on the taking-up and pursuit of the business of Insurance and Reinsurance (Solvency II) (OJ L 335, 17.12.2009, p. 1).

(2) Directive 2013/36/EU of the European Parliament and of the Council of 26 June 2013 on access to the activity of credit institutions and the prudential supervision of credit institutions and investment firms, amending Directive 2002/87/EC and repealing Directives 2006/48/EC and 2006/49/EC (OJ L 176, 27.6.2013, p. 338).

(3) Directive 2004/39/EC of the European Parliament and of the Council of 21 April 2004 on markets in financial instruments amending Council Directives 85/611/EEC and 93/6/EEC and Directive 2000/12/EC of the European Parliament and of the Council and repealing Council Directive 93/22/EEC (OJ L 145, 30.4.2004, p. 1).

(4) Directive 2011/61/EU of the European Parliament and of the Council of 8 June 2011 on Alternative Investment Fund Managers and amending Directives 2003/41/EC and 2009/65/EC and Regulations (EC) No 1060/2009 and (EU) No 1095/2010 (OJ L 174, 1.7.2011, p. 1).

(5) Directive 2003/41/EC of the European Parliament and of the Council of 3 June 2003 on the activities and supervision of institutions for occupational retirement provision (OJ L 235, 23.9.2003, p. 10).

(6) Directive 2009/65/EC of the European Parliament and of the Council of 13 July 2009 on the coordination of laws, regulations and administrative provisions relating to undertakings for collective investment in transferable securities (UCITS) (OJ L 302, 17.11.2009, p. 32).

(7) Regulation (EC) No 1893/2006 of the European Parliament and of the Council of 20 December 2006 establishing the statistical classification of economic activities NACE Revision 2 and amending Council Regulation (EEC) No 3037/90 as well as certain EC Regulations on specific statistical domains (OJ L 393, 30.12.2006, p. 1).
