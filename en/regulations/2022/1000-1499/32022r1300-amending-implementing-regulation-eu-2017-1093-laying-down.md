---
title: "Commission Implementing Regulation (EU) 2022/1300 of 24 March 2022 amending Implementing Regulation (EU) 2017/1093 laying down implementing technical standards with regard to the format of position reports by investment firms and market operators (Text with EEA relevance)"
identifier: "32022R1300"
eli: "http://data.europa.eu/eli/reg_impl/2022/1300/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2022-03-24
entry_into_force: 2022-12-11
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R1300"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2022/1300 of 24 March 2022 amending Implementing Regulation (EU) 2017/1093 laying down implementing technical standards with regard to the format of position reports by investment firms and market operators (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2022/1300**

**of 24 March 2022**

**amending Implementing Regulation (EU) 2017/1093 laying down implementing technical standards with regard to the format of position reports by investment firms and market operators**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Directive 2014/65/EU of the European Parliament and of the Council of 15 May 2014 on markets in financial instruments and amending Directive 2002/92/EC and Directive 2011/61/EU (1), and in particular Article 58(5), third subparagraph, thereof,

Whereas:

(1) Directive (EU) 2021/338 of the European Parliament and of the Council (2) sets out amendments to Article 58 of Directive 2014/65/EU as regards position reporting.

(2) In accordance with those amendments to Article 58 of Directive 2014/65/EU, position reporting is no longer to apply to securities referred to in Article 4(1), point 44, point (c), of that Directive, which relate to a commodity or an underlying as referred to in Section C.10 of Annex I to that Directive. Therefore, references to those categories of derivatives in the implementing technical standards laid down in Commission Implementing Regulation (EU) 2017/1093 (3) should be deleted.

(3) Implementing Regulation (EU) 2017/1093 should therefore be amended accordingly.

(4) This Regulation is based on the draft implementing technical standards submitted to the Commission by the European Securities and Markets Authority.

(5) The European Securities and Markets Authority has conducted open public consultations on the draft implementing technical standards on which this Regulation is based, analysed the potential related costs and benefits and requested the advice of the Securities and Markets Stakeholder Group established in accordance with Article 37 of Regulation (EU) No 1095/2010 of the European Parliament and of the Council (4),

HAS ADOPTED THIS REGULATION:

## Article 1

Annex II to Implementing Regulation (EU) 2017/1093 is amended in accordance with the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 24 March 2022.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 173, 12.6.2014, p. 349.

(2) Directive (EU) 2021/338 of the European Parliament and of the Council of 16 February 2021 amending Directive 2014/65/EU as regards information requirements, product governance and position limits, and Directives 2013/36/EU and (EU) 2019/878 as regards their application to investment firms, to help the recovery from the COVID-19 crisis (OJ L 68, 26.2.2021, p. 14).

(3) Commission Implementing Regulation (EU) 2017/1093 of 20 June 2017 laying down implementing technical standards with regard to the format of position reports by investment firms and market operators (OJ L 158, 21.6.2017, p. 16).

(4) Regulation (EU) No 1095/2010 of the European Parliament and of the Council of 24 November 2010 establishing a European Supervisory Authority (European Securities and Markets Authority), amending Decision No 716/2009/EC and repealing Commission Decision 2009/77/EC (OJ L 331, 15.12.2010, p. 84).

## ANNEX

Table 2 of Annex II to Implementing Regulation (EU) 2017/1093 is replaced by the following:

**‘Table 2**

**Table of fields to be reported for all positions across all maturities of all contracts for the purposes of Article 2**

<table>
<tbody><tr><td>FIELD</td><td>DETAILS TO BE REPORTED</td><td>FORMAT FOR REPORTING</td></tr>
<tr><td>Date and time of report submission</td><td>Field to be populated with the date and time on which the report is submitted.</td><td>{DATE_TIME_FORMAT}</td></tr>
<tr><td>Report reference number</td><td>Field to be populated with the unique identifier given by the submitter unambiguously identifying the report to both submitter and receiving competent authority.</td><td>{ALPHANUM-52}</td></tr>
<tr><td>Date of the trading day of the reported position</td><td>Field to be populated with the date on which the reported position is held at the close of the trading day on the relevant trading venue.</td><td>{DATEFORMAT}</td></tr>
<tr><td>Report status</td><td>Indication as to whether the report is new or a previously submitted report is cancelled or amended. Where a previously submitted report is cancelled or amended, a report which contains all the details of the original report and using the original Report Reference Number should be sent and the “Report status” should be flagged as “CANC”.  For amendments a new report that contains all the details of the original report and using the original Report Reference Number with all necessary details amended should be sent and the “Report status” should be flagged as “AMND”. </td><td>“NEWT” – New “CANC” – Cancellation  “AMND” – Amendment </td></tr>
<tr><td>Reporting entity ID</td><td>The identifier of the reporting investment firm. Field to be populated with the Legal Entity Identifier code (LEI) for legal entities or {NATIONAL_ID} for natural persons not having an LEI.</td><td>{LEI} or  {NATIONAL_ID} – Natural persons </td></tr>
<tr><td>Position holder ID</td><td>Field to be populated with the Legal Entity Identifier code (LEI) for legal entities or {NATIONAL_ID} for natural persons not having an LEI. (Note: if the position is held as a proprietary position of the reporting firm, this field shall be identical to field “Reporting entity ID”).</td><td>{LEI} or  {NATIONAL_ID} – Natural persons </td></tr>
<tr><td>Email address of position holder</td><td>Email address for notifications of position-related matters.</td><td>{ALPHANUM-256}</td></tr>
<tr><td>Ultimate parent entity ID</td><td>Field to be populated with the Legal Entity Identifier code (LEI) for legal entities or {NATIONAL_ID} for natural persons not having an LEI. Note: this field may be identical to field “Reporting entity ID” or “Position holder ID” if the ultimate parent entity holds its own positions, or makes its own reports.</td><td>{LEI} or  {NATIONAL_ID} – Natural persons </td></tr>
<tr><td>Email address of ultimate parent entity</td><td>Email address for correspondence in relation to aggregated positions.</td><td>{ALPHANUM-256}</td></tr>
<tr><td>Parent of collective investment scheme status</td><td>Field to report on whether the position holder is a collective investment undertaking that makes investment decisions independently from its parent as set out by Article 4(2) of Commission Delegated Regulation (EU) 2022/1301 (*1).</td><td>“TRUE” – the position holder is a collective investment undertaking that makes independent investment decisions “FALSE” – the position holder is not a collective investment undertaking that makes independent investment decisions </td></tr>
<tr><td>Identification code of contract traded on trading venues</td><td>Identifier of the commodity derivative, emission allowance or derivative thereof. See field “Trading venue identifier” for treatment of OTC contracts that are economically equivalent to contracts that are traded on trading venues.</td><td>{ISIN}</td></tr>
<tr><td>Venue product code</td><td>Field to be populated with a unique and unambiguous alphanumeric identifier utilised by the trading venue grouping together contracts with different maturities and strike prices in the same product.</td><td>{ALPHANUM-12}</td></tr>
<tr><td rowspan="2">Trading venue identifier</td><td>Field to be populated with the ISO 10383 segment MIC for positions reported in respect of on-venue contracts. Where the segment MIC does not exist, use the operating MIC.</td><td>{MIC}</td></tr>
<tr><td>Use MIC code “XXXX” for off-venue positions in economically equivalent OTC contracts. Use MIC code “XOFF” for listed derivatives or emission allowances traded off-exchange. </td><td></td></tr>
<tr><td>Position type</td><td>Field to report whether the position is in either futures, options, emission allowances or derivatives thereof or any other contract type.</td><td>“OPTN” – Options, including separately tradable options on FUTR or OTHR types, excluding products where the optionality is only an embedded element “FUTR” – Futures  “EMIS” – Emission allowances and derivatives thereof  “OTHR” – any other contract type </td></tr>
<tr><td>Position maturity</td><td>Indication of whether the maturity of the contract comprising the reported position relates to the spot month or to all other months. Note: separate reports are required for spot months and all other months.</td><td>“SPOT” – spot month, including all positions in position types EMIS “OTHR” – all other months </td></tr>
<tr><td>Position quantity</td><td>Field to be populated with the net position quantity held in the commodity derivative, emission allowances or derivatives thereof expressed either in lots, when the position limits are expressed in lots, or units of the underlying. This field should be populated with a positive number for long positions and a negative number for short positions. </td><td>{DECIMAL-15/2}</td></tr>
<tr><td>Notation of the position quantity</td><td>This field shall be populated with the units used to report the position quantity.</td><td>“LOTS” – if the position quantity is expressed in lots {ALPHANUM-25} – a description of the units used if the position quantity is expressed in units of the underlying  “UNIT” – if the position quantity is expressed in units </td></tr>
<tr><td>Delta equivalent position quantity</td><td>If the Position Type is “OPTN” or an option on “EMIS”, then this field shall contain the delta-equivalent quantity of the position reported in the “Position Quantity” field. This field should be populated with a positive number for long calls and short puts and a negative number for long puts and short calls. </td><td>{DECIMAL-15/2}</td></tr>
<tr><td>Indicator of whether the position is risk reducing in relation to commercial activity</td><td>Field to report whether the position is risk reducing in accordance with Article 7 of Delegated Regulation (EU) 2022/1301.</td><td>“TRUE” – the position is risk reducing “FALSE” – the position is not risk reducing </td></tr>
</tbody>
</table>

(*1) Commission Delegated Regulation (EU) 2022/1301 of 31 March 2022 amending the regulatory technical standards laid down in Delegated Regulation (EU) 2020/1226 as regards the information to be provided in accordance with the STS notification requirements for on-balance-sheet synthetic securitisations (OJ L 197, xx.xx.2022, p. 10).’
