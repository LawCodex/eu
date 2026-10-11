---
title: "Commission Implementing Regulation (EU) No 1249/2012 of 19 December 2012 laying down implementing technical standards with regard to the format of the records to be maintained by central counterparties according to Regulation (EU) No 648/2012 of the European Parliament and of the Council on OTC derivatives, central counterparties and trade repositories Text with EEA relevance"
identifier: "32012R1249"
eli: "http://data.europa.eu/eli/reg_impl/2012/1249/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2012-12-19
entry_into_force: 2012-04-16
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32012R1249"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) No 1249/2012 of 19 December 2012 laying down implementing technical standards with regard to the format of the records to be maintained by central counterparties according to Regulation (EU) No 648/2012 of the European Parliament and of the Council on OTC derivatives, central counterparties and trade repositories Text with EEA relevance

**COMMISSION IMPLEMENTING REGULATION (EU) No 1249/2012**

**of 19 December 2012**

**laying down implementing technical standards with regard to the format of the records to be maintained by central counterparties according to Regulation (EU) No 648/2012 of the European Parliament and of the Council on OTC derivatives, central counterparties and trade repositories**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to the opinion of the European Central Bank (1),

Having regard to Regulation (EU) No 648/2012 of the European Parliament and of the Council of 4 July 2012 on OTC derivatives, central counterparties and trade repositories (2), and in particular Article 29(5) thereof,

Whereas:

(1) In accordance with Article 29(4) of Regulation (EU) No 648/2012, Articles 13, 14 and 15 of the delegated act with regard to regulatory technical standards specifying the details of the records and information to be kept by central counterparties (CCPs) adopted pursuant to Article 29(4) of Regulation (EU) No 648/2012, rules should also be laid down to specify the format of the record and information kept in accordance those Articles.

(2) To carry out their duties effectively and consistently, the relevant authorities should be provided with data that are comparable among CCPs. The use of common formats also facilitates the reconciliation of data between CCPs.

(3) A CCP should be required to retain data for record keeping purposes in a format compatible with the format in which data is retained by trade repositories, taking into account that in certain circumstances CCPs and trade repositories are required to maintain or report the same information. The use of a common format across different financial market infrastructures facilitates the greater use of these formats by a wide variety of market participants, thus promoting standardisation.

(4) To facilitate straight through processing and reduction of costs to market participants, it is important to use standardised procedures and data formats across CCPs as much as possible.

(5) The underlying should be identified by using a single identifier, however there is currently no market wide standardised code to identify the underlyings within a basket. CCPs should therefore indicate at least that the underlying is a basket and use International Securities Identification numbers (ISINs) for standardised indices where possible.

(6) This Regulation is based on the draft implementing technical standards submitted by the European Securities and Markets Authority (ESMA) to the Commission.

(7) In accordance with Article 15 of Regulation (EU) No 1095/2010 of the European Parliament and of the Council of 24 November 2010 establishing a European Supervisory Authority (European Securities and Markets Authority) (3), ESMA has conducted an open public consultation before submitting the draft implementing technical standards on which this Regulation is based, analysed the potential related costs and benefits and requested the opinion of the Securities and Markets Stakeholder Group established in accordance with Article 37 of Regulation (EU) No 1095/2010,

HAS ADOPTED THIS REGULATION:

## Article 1 — Formats of records

1\. A CCP shall retain the records specified in Article 20 of the delegated act with regard to regulatory technical standards on requirements specifying the details of the records and information to be kept by central counterparties (CCPs) adopted pursuant to Article 29(4) of Regulation (EU) No 648/2012 for each contract processed in the format set out in Table 1 in the Annex.

2\. A CCP shall retain the records specified in Article 21 of the delegated act with regard to regulatory technical standards on requirements specifying the details of the records and information to be kept by central counterparties (CCPs) adopted pursuant to Article 29(4) of Regulation (EU) No 648/2012 for each position in the format set out in Table 2 in the Annex.

3\. A CCP shall retain the records specified in Article 22 of the delegated act with regard to regulatory technical standards on requirements specifying the details of the records and information to be kept by central counterparties (CCPs) adopted pursuant to Article 29(4) of Regulation (EU) No 648/2012 for activities related to its business and internal organisation in the format set out in Table 3 in the Annex.

4\. A CCP shall provide the competent authority the records and information under paragraphs 1, 2 and 3 in a format that allows a direct data feed between the CCP and the competent authority. A CCP shall establish such data feed within six months after the request of the competent authority.

## Article 2 — Entry into force

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 19 December 2012.

For the Commission

The President

José Manuel BARROSO

(1) Not yet published in the Official Journal.

(2) OJ L 201. 27.7.2012, p. 1.

(3) OJ L 331, 15.12.2010, p. 84.

## ANNEX

**Tables of fields to be recorded as referred to in Article 1**

**Table 1**

**Records of transactions processed**

<table>
<tbody><tr><td></td><td>Field</td><td>Format</td><td>Description</td></tr>
<tr><td>1</td><td>Reporting timestamp</td><td>ISO 8601 date format / UTC time format.</td><td>Date and time of reporting.</td></tr>
<tr><td>2</td><td>Price/rate</td><td>Up to 20 numerical digits in the format xxxx,yyyyy.</td><td>The price per security or derivative contract excluding commission and (where relevant) accrued interest. In the case of a debt instrument, the price may be expressed either in terms of currency or as a percentage.</td></tr>
<tr><td>2a</td><td>Price notation</td><td>E.g. ISO 4217 Currency Code, 3 alphabetical digits, percentage.</td><td>The manner in which the price is expressed.</td></tr>
<tr><td>3</td><td>Notional Currency</td><td>ISO 4217 Currency Code, 3 alphabetical digits.</td><td>The currency in which the price is expressed. If, in the case of a bond or other form of securitised debt, the price is expressed as a percentage, that percentage shall be included.</td></tr>
<tr><td>3a</td><td>Deliverable currency</td><td>ISO 4217 Currency Code, 3 alphabetical digits.</td><td>The currency to be delivered.</td></tr>
<tr><td>4</td><td>Quantity</td><td>Up to 10 numerical digits.</td><td>The number of units of the financial instruments, the nominal value of bonds, or the number of derivative contracts included in the transaction.</td></tr>
<tr><td>5</td><td>Quantity notation</td><td>Up to 10 numerical digits.</td><td>An indication as to whether the quantity is the number of units of financial instruments, the nominal value of bonds or the number of derivative contracts.</td></tr>
<tr><td>6</td><td>CCP side</td><td>B=Buyer / S=Seller.</td><td></td></tr>
<tr><td>7</td><td>Product ID</td><td>Interim taxonomy in accordance with the information in Article 4 of Regulation (EC) xx/2012 [draft ITS on format and frequency of trade reports to trade repositories], ISIN or a unique product identifier (UPI).</td><td>The contract shall be identified by using a product identifier, where available.</td></tr>
<tr><td>8</td><td>Clearing member ID</td><td>Legal Entity Identifier (LEI) (20 alphanumerical digits), interim entity identifier (20 alphanumerical digits), BIC (11 alphanumerical digits) or client code (50 alphanumerical digits).</td><td>In case the reporting counterparty is not a clearing member, its clearing member shall be identified in this field by a unique code. In case of an individual, a client code, as assigned by the CCP, shall be used.</td></tr>
<tr><td>9</td><td>Beneficiary ID</td><td>Legal Entity Identifier (LEI) (20 alphanumerical digits), interim entity identifier (20 alphanumerical digits), BIC (11 alphanumerical digits) or client code (50 alphanumerical digits).</td><td>If the beneficiary of the contract is not a C/P to this contract it has to be identified by a unique code or, in case of individuals, by a client code as assigned by the legal entity used by the individual.</td></tr>
<tr><td>10</td><td>Party that transferred the contract (in case of give-up)</td><td>Legal Entity Identifier (LEI) (20 alphanumerical digits), interim entity identifier (20 alphanumerical digits), BIC (11 alphanumerical digits) or client code (50 alphanumerical digits).</td><td></td></tr>
<tr><td>11</td><td>Venue of execution</td><td>ISO 10383 Market Identifier Code (MIC) where relevant, XOFF for listed derivatives that are traded off-exchange or XXXX for OTC derivatives.</td><td>Identification of the venue where the transaction was executed. In case of a contract concluded OTC, it has to be identified whether the respective instrument is admitted to trading but traded OTC or not admitted to trading and traded OTC.</td></tr>
<tr><td>12</td><td>Date of interposition</td><td>ISO 8601 date format.</td><td>The day on which the interposition of the CCP in the contract was executed.</td></tr>
<tr><td>13</td><td>Time of interposition</td><td>UTC time format.</td><td>The time at which the interposition of the CCP in the contract was executed, reported in the local time of the competent authority to which the transaction will be reported, and the basis in which the transaction is reported expressed as Coordinated Universal Time (UTC) +/- hours.</td></tr>
<tr><td>14</td><td>Date of termination of the contract</td><td>ISO 8601 date format.</td><td>The day on which the termination of the contract occurred.</td></tr>
<tr><td>15</td><td>Time of termination of the contract</td><td>UTC time format.</td><td>The time at which the termination of the contract occurred, reported in the local time of the competent authority to which the transaction will be reported, and the basis in which the transaction is reported expressed as Coordinated Universal Time (UTC) +/- hours.</td></tr>
<tr><td>16</td><td>Delivery type</td><td>C = cash, P = physical, O = optional for counterparty.</td><td>Whether the contract is settled physically or in cash.</td></tr>
<tr><td>17</td><td>Settlement date</td><td>ISO 8601 date format.</td><td>The day on which the settlement or the buy-in of the contract is executed. If more than one, further fields may be identified.</td></tr>
<tr><td>18</td><td>Time of settlement or of buy-in in the contract</td><td>UTC time format.</td><td>The time at which the settlement or the buy-in of the contract is executed, reported in the local time of the competent authority to which the transaction will be reported, and the basis in which the transaction is reported expressed as Coordinated Universal Time (UTC) +/- hours.</td></tr>
<tr><td colspan="4">Details on the original terms of the contracts cleared, to be provided to the extent they are applicable</td></tr>
<tr></tr>
<tr><td>19</td><td>Date</td><td>ISO 8601 date format.</td><td>The day on which the contract was originally concluded.</td></tr>
<tr><td>20</td><td>Time</td><td>UTC time format.</td><td>The time at which the original contract was originally concluded, reported in the local time of the competent authority to which the transaction will be reported, and the basis in which the transaction is reported expressed as Coordinated Universal Time (UTC) +/- hours.</td></tr>
<tr><td>21</td><td>Product ID</td><td>Interim taxonomy in accordance with the information in Article 4 of Regulation (EC) xx/2012 [draft ITS on format and frequency of trade reports to trade repositories], ISIN or a unique product identifier (UPI).</td><td>The contract shall be identified by using a unique product identifier where available.</td></tr>
<tr><td>22</td><td>Underlying</td><td>A unique product identifier, ISIN (12 alphanumerical digits and CFI (6 alphanumerical digits). Legal Entity Identifier (LEI) (20 alphanumerical digits), interim entity identifier (20 alphanumerical digits), B= Basket, or I=Index.</td><td>The instrument identification applicable to the security that is the underlying asset in a derivative contract as well as the transferable security falling within Article 4(1)(18)(c) of Directive 2004/39/EC.</td></tr>
<tr><td>23</td><td>Derivative type (in case of derivative contract)</td><td>The harmonised description of the derivative type should be done according to one of the top level categories as provided by a uniform internationally accepted standard for financial instrument classification.</td><td></td></tr>
<tr><td>24</td><td>Inclusion of the instrument in the ESMA register of contracts subject to the clearing obligation (in case of derivative contract)</td><td>Y=Yes / N=No.</td><td></td></tr>
<tr><td colspan="4">Other information to be provided to the extent they are applicable</td></tr>
<tr></tr>
<tr><td>25</td><td>Identification of the interoperable CCP clearing one leg of the transaction</td><td>Legal Entity Identifier (LEI) (20 alphanumerical digits), interim entity identifier (20 alphanumerical digits), BIC (11 alphanumerical digits) or client code (50 alphanumerical digits).</td><td></td></tr>
</tbody>
</table>

**Table 2**

**Position records**

|  | Field | Format |
| --- | --- | --- |
| 1 | Clearing member ID | Legal Entity Identifier (LEI), interim entity identifier or BIC |
| 2 | Beneficiary ID | Legal Entity Identifier (LEI), interim entity identifier, BIC or Client Code |
| 3 | Interoperable CCP maintaining the position | Legal Entity Identifier (LEI), interim entity identifier, BIC or Client Code |
| 4 | Sign of the position | B=Buyer / S=Seller |
| 5 | Value of the position | Up to 10 numerical digits (xxxx,yy). |
| 6 | Price at which the contracts are valued | Up to 10 numerical digits (xxxx,yy). |
| 7 | Currency | ISO Currency Code. |
| 8 | Other relevant information | Free Text |
| 9 | Amount of margins called by the CCP | Up to 10 numerical digits (xxxx,yy). |
| 10 | Amount of default fund contributions called by the CCP | Up to 10 numerical digits (xxxx,yy). |
| 11 | Amount of other financial resources called by the CCP | Up to 10 numerical digits (xxxx,yy). |
| 12A | Amount of margins posted by the Clearing Member with reference to client account A | Up to 10 numerical digits (xxxx,yy). |
| 13A | Amount of default fund contributions posted by the Clearing Member with reference to client account A | Up to 10 numerical digits (xxxx,yy). |
| 14A | Amount of other financial resources posted by the Clearing Member with reference to client account A | Up to 10 numerical digits (xxxx,yy). |
| 15B | Amount of margins posted by the Clearing Member with reference to client account B | Up to 10 numerical digits (xxxx,yy). |
| 16B | Amount of default fund contributions posted by the Clearing Member with reference to client account B | Up to 10 numerical digits (xxxx,yy). |
| 17B | Amount of other financial resources posted by the Clearing Member with reference to client account B | Up to 10 numerical digits (xxxx,yy). |

**Table 3**

**Business records**

<table>
<tbody><tr><td></td><td>Field</td><td>Format</td><td>Description</td></tr>
<tr><td>1</td><td>Organisational charts</td><td>Free text</td><td>Board and relevant committees, clearing unit, risk management unit, and all other relevant units or divisions.</td></tr>
<tr><td colspan="4">Shareholders or members that have qualifying holdings (fields to be added for each of the relevant shareholder/member)</td></tr>
<tr></tr>
<tr><td>2</td><td>Type</td><td>S=Shareholder / M=member.</td><td></td></tr>
<tr><td>3</td><td>Type of qualified holding</td><td>D=direct / I=indirect.</td><td></td></tr>
<tr><td>4</td><td>Type of entity</td><td>N=natural person / L=legal person.</td><td></td></tr>
<tr><td>5</td><td>Amount of the holding</td><td>Up to 10 numerical digits (xxxx,yyyyy).</td><td></td></tr>
<tr><td colspan="4">Other documents</td></tr>
<tr></tr>
<tr><td>6</td><td>Policies, procedures, processes required under organisational requirements</td><td>Documents</td><td></td></tr>
<tr><td>7</td><td>Minutes of Board meetings, meeting of sub-committees (if applicable) and of Senior Management Committees (if applicable)</td><td>Documents</td><td></td></tr>
<tr><td>8</td><td>Minutes of meetings of the risk committee</td><td>Documents</td><td></td></tr>
<tr><td>9</td><td>Minutes of consultation group with clearing members and clients (if any)</td><td>Documents</td><td></td></tr>
<tr><td>10</td><td>Reports of internal and external audit, risk management, compliance and consultant</td><td>Documents</td><td></td></tr>
<tr><td>11</td><td>Business continuity policy and disaster recovery plan</td><td>Documents</td><td></td></tr>
<tr><td>12</td><td>Liquidity plan and daily liquidity reports</td><td>Documents</td><td></td></tr>
<tr><td>13</td><td>Documents reflecting all assets and liabilities and capital accounts</td><td>Documents</td><td></td></tr>
<tr><td>14</td><td>Complaints received</td><td>Free text</td><td>For each complaint: information on complaint’s name, address and account number; date of receiving the complaint; names of all persons identified in the complaint; description of the nature of the complaint; disposition of the complaint; date at which the complaint was resolved.</td></tr>
<tr><td>15</td><td>Information on interruption of services or dysfunction</td><td>Free text</td><td>Information on any interruption of services or dysfunction, including a detailed report on the timing, effects and remedial actions.</td></tr>
<tr><td>16</td><td>Results of back and stress test performed</td><td>Free text</td><td></td></tr>
<tr><td>17</td><td>Written communications with competent Authorities, ESMA and the relevant members of the ESCB</td><td>Documents</td><td></td></tr>
<tr><td>18</td><td>Legal opinions received in accordance with organisational requirements</td><td>Documents</td><td></td></tr>
<tr><td>19</td><td>Interoperability arrangements with other CCPs (where applicable)</td><td>Documents</td><td></td></tr>
<tr><td>20</td><td>List of all clearing members (Article 17 of Regulation (EU) No XXX/2012)</td><td>Free text / Document</td><td>List in accordance with Article 17 of Regulation (EU) No XXX/2012.</td></tr>
<tr><td>21</td><td>Information required by Article 17 of Regulation (EU) No XXX/2012</td><td>Free text / Documents</td><td>Law and Rules governing (i) the access to the CCP, (ii) the contracts concluded by the CCP with clearing members and, where practicable, clients, (iii) the contracts that the CCP accepts for clearing, (iv) any interoperability arrangements, (v) the use of collateral and default fund contributions, including the liquidation of positions and collateral and the extent to which collateral is protected against third party claims (level of segregation).</td></tr>
<tr><td>22</td><td>Development on new initiative processes</td><td>Free text</td><td>In case of the provision of new services.</td></tr>
</tbody>
</table>
