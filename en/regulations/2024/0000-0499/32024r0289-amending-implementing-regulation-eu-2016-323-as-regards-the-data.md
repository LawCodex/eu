---
title: "Commission Implementing Regulation (EU) 2024/289 of 12 January 2024 amending Implementing Regulation (EU) 2016/323 as regards the data required for mutual administrative assistance documents relating to the movements of excise goods to be exported under duty suspension pursuant to Council Regulation (EU) No 389/2012"
identifier: "32024R0289"
eli: "http://data.europa.eu/eli/reg_impl/2024/289/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2024-01-12
entry_into_force: 2024-12-16
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R0289"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2024/289 of 12 January 2024 amending Implementing Regulation (EU) 2016/323 as regards the data required for mutual administrative assistance documents relating to the movements of excise goods to be exported under duty suspension pursuant to Council Regulation (EU) No 389/2012

**COMMISSION IMPLEMENTING REGULATION (EU) 2024/289**

**of 12 January 2024**

**amending Implementing Regulation (EU) 2016/323 as regards the data required for mutual administrative assistance documents relating to the movements of excise goods to be exported under duty suspension pursuant to Council Regulation (EU) No 389/2012**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Council Regulation (EU) No 389/2012 of 2 May 2012 on administrative cooperation in the field of excise duties and repealing Regulation (EC) No 2073/2004 (1), and in particular Article 9(2), Article 15(5) and Article 16(3) thereof,

Whereas:

(1) Council Directive (EU) 2020/262 (2) lays down the procedure to be followed for the movements of excise goods between Member States as well as the procedures for the movement of excise goods that are exported outside the Union, and the monitoring and surveillance of those movements by means of the computerised system referred to in Article 1 of Decision (EU) 2020/263 of the European Parliament and of the Council (3) (‘the computerised system’).

(2) Article 21(5) of Directive (EU) 2020/262 provides that the competent authorities in the Member State of export must notify the competent authorities in the Member State of dispatch by means of the computerised system where the goods are no longer to be taken out of the customs territory of the Union.

(3) Commission Implementing Regulation (EU) 2016/323 (4) sets out the rules on cooperation and exchange of information between Member States regarding the movements of excise goods. In order to take account of changes introduced by Article 21(5) of Directive (EU) 2020/262, it is necessary to amend the data required for mutual administrative assistance documents referred to in Article 9(2), Article 15(5) and Article 16(3) of Regulation (EU) No 389/2012 to allow the exchange of information for the movements of excise goods to be exported under duty suspension, so that competent authorities can control those excise movements as well.

(4) Implementing Regulation (EU) 2016/323 should therefore be amended accordingly.

(5) The computerised system is expected to be interfaced with the EU Automated Export System by 13 February 2024, when the notifications referred to in Article 21(5) of Directive (EU) 2020/262 may no longer be made by means other than the computerised system, as set out in Article 54 of that Directive. As this Regulation concerns procedures for the movement of excise goods under duty suspension that are exported outside the Union, the application of this Regulation should be deferred to that date.

(6) The measures provided for in this Regulation are in accordance with the opinion of the Committee on Excise Duty,

HAS ADOPTED THIS REGULATION:

## Article 1

Annexes I and II to Implementing Regulation (EU) 2016/323 are amended in accordance with the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the third day following that of its publication in the Official Journal of the European Union.

It shall apply from 13 February 2024.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 12 January 2024.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 121, 8.5.2012, p. 1.

(2) Council Directive (EU) 2020/262 of 19 December 2019 laying down the general arrangements for excise duty (OJ L 58, 27.2.2020, p. 4).

(3) Decision (EU) 2020/263 of the European Parliament and of the Council of 15 January 2020 on computerising the movement and surveillance of excise goods (OJ L 58, 27.2.2020, p. 43).

(4) Commission Implementing Regulation (EU) 2016/323 of 24 February 2016 laying down detailed rules on cooperation and exchange of information between Member States regarding excise goods pursuant to Council Regulation (EU) No 389/2012 (OJ L 66, 11.3.2016, p. 1).

## ANNEX

Annexes I and II of Implementing Regulation (EU) 2016/323 are amended as follows:

(1) in Annex I, tables 1 to 16 are replaced by the following:

**‘Table 1**

**(referred to in Article 4)**

**Movement Download Request**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Correlation Identifier</td><td>R</td><td></td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>an..44</td></tr>
<tr><td colspan="2">2</td><td>EXCISE MOVEMENT e-AD/e-SAD</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td>The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>National Movement Information Requested flag</td><td>R</td><td></td><td>The format of Boolean is digital: ‘0’ or ‘1’ (‘0’ = No or False; ‘1’ = Yes or True)</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Status</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>X01 = Accepted</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X02 = Cancelled</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X03 = Delivered</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X04 = Diverted</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X05 = Rejected</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X06 = Replaced</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X07 = e-AD/e-SAD Manually Closed</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X08 = Refused</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X09 = None</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X10 = Partially Refused</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X11 = Exporting</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X12 = Accepted for Export</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X13 = Stopped</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X14 = Accepted Export Declaration</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X15 = e-AD Request Accepted for Export</td></tr>
</tbody>
</table>
</td><td>an3</td></tr>
<tr><td></td><td>e</td><td>Last Received Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>IE801 = E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE803 = NOTIFICATION OF DIVERTED E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE807 = INTERRUPTION OF MOVEMENT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE810 = CANCELLATION OF AN E-AD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE813 = CHANGE OF DESTINATION</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE818 = ACCEPTED OR (PARTIALLY) REFUSED REPORT OF RECEIPT/EXPORT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE819 = ALERT OR REJECTION OF AN E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE829 = NOTIFICATION OF ACCEPTED EXPORT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE836 = EXPORT DECLARATION INVALIDATION NOTIFICATION TO MSA OF DISPATCH/CONSIGNOR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE839 = CUSTOMS REJECTION OF E-AD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE881 = MANUAL CLOSURE RESPONSE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE905 = STATUS RESPONSE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>None = NONE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>Note:</td><td>The IE905 should be included only for historical movements, which were manually closed with an IE905 message.</td></tr>
</tbody>
</table>
</td><td>an..5</td></tr>
<tr><td></td><td>f</td><td>Status Request Message Type</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>1 = Status Synchronisation Request</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Movement History Request</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
</tbody>
</table>

**Table 2**

**(referred to in Article 4)**

**Movement Download Answer**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Correlation Identifier</td><td>R</td><td></td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>an..44</td></tr>
<tr><td colspan="2">2</td><td>EXCISE MOVEMENT e-AD/e-SAD</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td>The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Status</td><td>R</td><td></td><td>The possible values of &lt;Status&gt; are:<table><tbody><tr><td>—</td><td>X01 = Accepted</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X02 = Cancelled</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X03 = Delivered</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X04 = Diverted</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X05 = Rejected</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X06 = Replaced</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X07 = e-AD/e-SAD Manually closed</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X08 = Refused</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X09 = None</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X10 = Partially Refused</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X11 = Exporting</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X12 = Accepted for Export</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X13 = Stopped</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X14 = Accepted Export Declaration</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>X15 = e-AD Request Accepted for Export</td></tr>
</tbody>
</table>
</td><td>an3</td></tr>
<tr><td></td><td>d</td><td>Last Received Message Type</td><td></td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>IE801 = E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE803 = NOTIFICATION OF DIVERTED E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE807 = INTERRUPTION OF MOVEMENT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE810 = CANCELLATION OF AN E-AD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE813 = CHANGE OF DESTINATION</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE818 = ACCEPTED OR (PARTIALLY) REFUSED REPORT OF RECEIPT/EXPORT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE819 = ALERT OR REJECTION OF AN E-AD/E-SAD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE829 = NOTIFICATION OF ACCEPTED EXPORT</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE836 = EXPORT DECLARATION INVALIDATION NOTIFICATION TO MSA OF DISPATCH/CONSIGNOR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE839 = CUSTOMS REJECTION OF E-AD</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE881 = MANUAL CLOSURE RESPONSE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>IE905 = STATUS RESPONSE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>None = NONE</td></tr>
</tbody>
</table>
<table><tbody><tr><td>Note:</td><td>The IE905 should be included only for historical movements, which were manually closed with an IE905 message.</td></tr>
</tbody>
</table>
</td><td>an..5</td></tr>
</tbody>
</table>

**Table 3**

**(referred to in Article 4)**

**History of a movement**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td colspan="3">F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Correlation Identifier</td><td>R</td><td></td><td colspan="3">The value of &lt;Request Correlation Identifier&gt; is unique per Member State</td><td>an..44</td></tr>
<tr><td colspan="2">2</td><td>All validated e-ADs/e-SADs</td><td>R</td><td></td><td colspan="3">The set of all draft electronic (simplified) administrative documents or electronic (simplified) administrative documents relating to the movement, the structure of which is set out in Table 1 of Annex I to Delegated Regulation (EU) 2022/1636</td><td>99x</td></tr>
<tr><td colspan="2">3</td><td>All Reports of Receipt/Export</td><td>O</td><td></td><td colspan="3">The set of all Report of receipt/Report of export messages relating to the movement, the structure of which is set out in Table 6 of Annex I to Delegated Regulation (EU) 2022/1636</td><td>99x</td></tr>
<tr><td colspan="2">4</td><td>Last Notification of Diverted e-AD</td><td>O</td><td></td><td colspan="3">The content of the last Notification of change of destination/Notification of splitting message relating to the movement, the structure of which is set out in Table 4 of Annex I to Delegated Regulation (EU) 2022/1636</td><td>1x</td></tr>
<tr><td colspan="2">5</td><td>All Control Reports</td><td>O</td><td></td><td colspan="3">The set of all Control Report messages relating to the movement, the structure of which is set out in Table 11</td><td>99x</td></tr>
<tr><td colspan="2">6</td><td>All Event Reports</td><td>O</td><td></td><td colspan="3">The set of all Event Report messages relating to the movement, the structure of which is set out in Table 12</td><td>99x</td></tr>
<tr><td colspan="2">7</td><td>All explanations of delay for delivery</td><td>O</td><td></td><td colspan="3">The set of all Explanation on delay for delivery messages relating to the movement</td><td>99x</td></tr>
<tr><td colspan="2">7.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Role</td><td>R</td><td></td><td colspan="3">The possible values are:<table><tbody><tr><td>—</td><td>1 = Explanation on delay for sending the report of receipt/export</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Explanation on delay for giving destination</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Validation of Explanation on Delay</td><td>C</td><td>-‘R’ after successful validation - Does not apply otherwise </td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td></td><td>c</td><td>Submitter Type</td><td>R</td><td></td><td colspan="3">The possible values are :<table><tbody><tr><td>—</td><td>1 = Consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Consignee</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Submitter Identification</td><td>R</td><td></td><td colspan="3">The &lt;Submitter Identification&gt; is a valid trader excise number. (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>e</td><td>Explanation Code</td><td>R</td><td></td><td colspan="3">(see Code list 7 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Explanation Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ Otherwise</td></tr>
</tbody>
</table>
 (see Explanation Code in box 7.1e) </td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">7.2</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">8</td><td>All Notifications of Accepted Export</td><td>O</td><td></td><td colspan="3">The set of all Notification of accepted export messages relating to the movement</td><td>99x</td></tr>
<tr><td colspan="2">8.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date and Time of Issuance</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td colspan="2">8.2</td><td>EXCISE MOVEMENT e-AD</td><td>R</td><td></td><td colspan="3"></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Export Declaration Acceptance or Goods Released for Export</td><td>R</td><td></td><td colspan="3">Possible values:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
 0 corresponds to the acceptance of the export declaration and 1 corresponds to the release of goods for export. </td><td>n1</td></tr>
<tr><td colspan="2">8.3</td><td>TRADER Consignee</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="9"></td><td rowspan="9">a</td><td rowspan="9">Trader Identification</td><td rowspan="9">C</td><td rowspan="9"><table><tbody><tr><td>—</td><td>‘R’ if &lt;Destination Type Code&gt; is:<table><tbody><tr><td>—</td><td>"Destination – Tax warehouse"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Temporary registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination - Direct delivery"</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="9">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ for Destination Type Code ‘6’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (See box 1a in Table 1 of Annex I to Delegated Regulation (EU) No 2022/1636) </td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(2) of Council Directive (EU) 2020/262.</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">8.4</td><td>CUSTOMS OFFICE Export Place</td><td>O</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">8.5</td><td>EXPORT DECLARATION ACCEPTANCE/RELEASE</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Reference Number of Sender Customs Office</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>b</td><td>Sender Customs Officer Identification</td><td>O</td><td></td><td colspan="3"></td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>Date of Acceptance</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Export Declaration Acceptance</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply for Goods Released for Export</td></tr>
</tbody>
</table>
 (See box 8.2c.) </td><td colspan="3"></td><td>date</td></tr>
<tr><td></td><td>d</td><td>Date of Release</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Goods Released for Export</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply for Export Declaration Acceptance</td></tr>
</tbody>
</table>
 (See box 8.2c.) </td><td colspan="3"></td><td>date</td></tr>
<tr><td></td><td>e</td><td>Document Reference Number</td><td>R</td><td></td><td colspan="3">A valid MRN confirmed against Customs data, according to the Customs case. MRN = Movement Reference Number </td><td>an..21</td></tr>
<tr><td colspan="2">9</td><td>All Notifications of invalidation by Customs</td><td>O</td><td></td><td colspan="3">The set of all Customs invalidation of export declaration messages relating to the movement</td><td>99x</td></tr>
<tr><td colspan="2">9.1</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td>999X</td></tr>
<tr><td></td><td>a</td><td>Administrative Reference Code</td><td>R</td><td></td><td colspan="3">Provide the ARC of the e-AD. See Code list 2 of Annex II of Delegated Regulation (EU) No 2022/1636.</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of this field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">9.1.1</td><td>EXPORT OPERATION</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>MRN</td><td>R</td><td></td><td colspan="3"></td><td>an18</td></tr>
<tr><td></td><td>b</td><td>Invalidation date</td><td>R</td><td></td><td colspan="3"></td><td>an10</td></tr>
<tr><td colspan="2">9.1.2</td><td>CUSTOMS OFFICE OF EXPORT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Reference Number</td><td>R</td><td></td><td colspan="3">Provide the code of the office of the competent authorities in the Member State of export responsible for excise control at the place of export. See Code list 4 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>an8</td></tr>
<tr><td colspan="2">9.1.3</td><td>MSA OF EXPORT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Country Code</td><td>R</td><td></td><td colspan="3">Provide the Member State in the territory of which the exportation of the excise goods is carried out, using the Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td colspan="2">9.1.4</td><td>GOODS SHIPMENT</td><td>O</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td colspan="2">9.1.4.1</td><td>PREVIOUS DOCUMENT</td><td>O</td><td></td><td colspan="3"></td><td>999X</td></tr>
<tr><td></td><td>a</td><td>Sequence number</td><td>R</td><td></td><td colspan="3"></td><td>n..5</td></tr>
<tr><td></td><td>b</td><td>Type</td><td>R</td><td></td><td colspan="3"></td><td>an4</td></tr>
<tr><td></td><td>c</td><td>Reference number</td><td>R</td><td></td><td colspan="3"></td><td>an..70</td></tr>
<tr><td colspan="2">10</td><td>All Notifications of rejection by Customs</td><td>O</td><td></td><td colspan="3">The set of all Customs rejection of e-AD messages relating to the movement</td><td>99x</td></tr>
<tr><td colspan="2">10.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date and Time of Issuance</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td colspan="2">10.2</td><td>The concerned draft e-AD</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘1’or ‘2’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Codes ‘4’ and ‘5’</td></tr>
</tbody>
</table>
 (see Rejection Reason Code in box 10.4) </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Local Reference Number</td><td>R</td><td></td><td colspan="3"></td><td>an..22</td></tr>
<tr><td colspan="2">10.3</td><td>All concerned validated e-ADs</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘4’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘1’ and ‘2’</td></tr>
</tbody>
</table>
 (see Rejection Reason Code in box 10.4) </td><td colspan="3"></td><td>99X</td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3"></td><td>n..2</td></tr>
<tr><td colspan="2">10.4</td><td>REJECTION</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Rejection Date and Time</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td></td><td>b</td><td>Rejection Reason Code</td><td>R</td><td></td><td colspan="3">The possible values are:<table><tbody><tr><td>—</td><td>1 = Import data not found</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = The contents of the e-AD does not match with import data</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>3 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>4 = Negative Cross-check result</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>5 = Unsatisfactory Control Result at Office of Export</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">10.5</td><td>EXPORT DECLARATION INFORMATION</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘‘R’ for Rejection Reason Code ‘4’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘1’ and ‘2’</td></tr>
</tbody>
</table>
 (see Rejection Reason Code in box 10.4b) </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Local Reference Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘4’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘5’.</td></tr>
</tbody>
</table>
 (See box 10.4b.) </td><td colspan="3"></td><td>an..22</td></tr>
<tr><td></td><td>b</td><td>Document Reference Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘4’.</td></tr>
</tbody>
</table>
 (See box 4b.) </td><td colspan="3">A valid MRN confirmed against Customs data, according to the Customs case. MRN = Movement Reference Number </td><td>an..21</td></tr>
<tr><td colspan="2">10.5.1</td><td>NEGATIVE CROSS-CHECK VALIDATION RESULT</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘4’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘1’, ‘2’ and ‘5’</td></tr>
</tbody>
</table>
 (See Rejection Reason Code in box 10.4b.) </td><td colspan="3"></td><td>99X</td></tr>
<tr><td colspan="2">10.5.1.1</td><td>UBR CROSS-CHECK RESULT</td><td>R</td><td></td><td colspan="3"></td><td>999X</td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Body Record Unique Reference</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..3</td></tr>
<tr><td></td><td>c</td><td>Diagnosis Code</td><td>R</td><td></td><td colspan="3">The possible values are:<table><tbody><tr><td>—</td><td>1 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Body Record Unique Reference does not exist in the e-AD or No corresponding GOODS ITEM in the export declaration</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>3 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>4 = Weight/mass do not match</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>5 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>6 = CN codes do not match</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>7 = Weight/mass do not match and CN codes do not match</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Validation Result</td><td>R</td><td></td><td colspan="3">Possible values:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
 0 means that the validation result is negative and 1 means that the validation result is positive. </td><td>n1</td></tr>
<tr><td></td><td>e</td><td>Rejection Reason</td><td>O</td><td></td><td colspan="3"></td><td>an..512</td></tr>
<tr><td colspan="2">10.5.1.1.1</td><td>COMBINED NOMENCLATURE CODE CROSS-CHECK RESULT</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if:<table><tbody><tr><td>—</td><td>the value in box 10.5.1.1.d is ‘1’ (Validation Result is Positive) and the value in box 10.5.1.1.c is ‘6’ (Diagnosis Code is ‘CN Codes do not match’) or;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>if the value in box 10.5.1.1.d is ‘0’ (Validation Result is Negative);</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Validation Result</td><td>R</td><td></td><td colspan="3">Possible values:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
 0 means that the validation result is negative and 1 means that the validation result is positive. </td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Rejection Reason</td><td>O</td><td></td><td colspan="3"></td><td>an..512</td></tr>
<tr><td colspan="2">10.5.1.1.2</td><td>NET MASS CROSS-CHECK RESULT</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the value in box 10.5.1.1.d is ‘1’ (Validation Result is Positive) and the value in box 10.5.1.1.c is ‘4’ (Diagnosis Code is ‘Weight/mass do not match’);</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise.</td></tr>
</tbody>
</table>
</td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Validation Result</td><td>R</td><td></td><td colspan="3">Possible values:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
 0 means that the validation result is negative and 1 means that the validation result is positive. </td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Rejection Reason</td><td>O</td><td></td><td colspan="3"></td><td>an..512</td></tr>
<tr><td colspan="2">10.5.2</td><td>All export non-release notifications</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ for Rejection Reason Code ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn’t apply for Rejection Reason Code ‘1’, ‘2’ and ‘4’</td></tr>
</tbody>
</table>
 (See box 10.4b.) </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Document Reference Number</td><td>R</td><td></td><td colspan="3"></td><td>an..21</td></tr>
<tr><td colspan="2">10.6</td><td>TRADER Consignee</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="9"></td><td rowspan="9">a</td><td rowspan="9">Trader Identification</td><td rowspan="9">C</td><td rowspan="9"><table><tbody><tr><td>—</td><td>‘R’ if &lt;Destination Type Code&gt; is:<table><tbody><tr><td>—</td><td>"Destination – Tax warehouse"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Temporary registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination - Direct delivery"</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="9">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(2) of Directive (EU) 2020/262.</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">10.7</td><td>CUSTOMS OFFICE Export Place</td><td>O</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">11</td><td>The Possible Interruption of Movement</td><td>O</td><td></td><td colspan="3">The content of a possible Interruption of movement message relating to the movement, the structure of which is set out in Table 13</td><td>1x</td></tr>
<tr><td colspan="2">12</td><td>The Possible Cancellation of e-AD</td><td>O</td><td></td><td colspan="3">The content of a possible Cancellation message relating to the movement, the structure of which is set out in Table 2 of Annex I to Delegated Regulation (EU) 2022/1636</td><td>1x</td></tr>
<tr><td colspan="2">13</td><td>All Changes of Destination</td><td>O</td><td></td><td colspan="3">The set of all Change of destination messages relating to the movement, the structure of which is set out in Table 3 of Annex I to Delegated Regulation (EU) 2022/1636</td><td>99x</td></tr>
<tr><td colspan="2">14</td><td>All Alerts or Rejections of an e-AD/e-SAD</td><td>O</td><td></td><td colspan="3">The set of all Alert or Rejection of an e-AD/e-SAD messages relating to the movement, the structure of which is set out in Table 14</td><td>99x</td></tr>
<tr><td colspan="2">14.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date and Time of Validation of Alert or Rejection</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ after successful validation</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td colspan="2">14.2</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">14.3</td><td>TRADER Consignee</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="12"></td><td rowspan="12">a</td><td rowspan="12">Trader Identification</td><td rowspan="12">C</td><td rowspan="12"><table><tbody><tr><td>—</td><td>‘R’ if &lt;Destination Type Code&gt; is:<table><tbody><tr><td>—</td><td>"Destination – Tax warehouse"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Temporary registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Direct delivery"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Destination – Certified consignee”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Destination – Temporary certified consignee”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Return to the place of dispatch of the consignor, for a Duty Paid B2B movement"</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="12">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td><table><tbody><tr><td>9 -</td><td>Destination – Certified consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (6)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>10 -</td><td>Destination – Temporary certified consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (7)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>11 -</td><td>Destination-Return to the place of dispatch of the consignor, for a Duty Paid B2B movement</td></tr>
</tbody>
</table>
</td><td>Excise Number (8) or Temporary Authorisation Reference (9)</td><td>Any identification (*)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(6)</td><td>The operator type of the consignee is "Certified consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(7)</td><td>The operator type of the consignee is "Temporary certified consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(8)</td><td>The operator type of the consignee is "Certified consignor". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(9)</td><td>An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt; with Operator Type Code "Temporary Certified Consignor".</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(2) of Directive (EU) 2020/262.</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">14.4</td><td>OFFICE of Destination</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 5 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">14.5</td><td>ALERT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date of Alert</td><td>R</td><td></td><td colspan="3"></td><td>date</td></tr>
<tr><td></td><td>b</td><td>Movement Rejected flag</td><td>R</td><td></td><td colspan="3">The format of Boolean is digital : '0' or '1' ('0' = No or False; '1' = Yes or True)</td><td>n1</td></tr>
<tr><td colspan="2">14.6</td><td>ALERT OR REJECTION OF MOVEMENT REASON Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Movement Rejected flag&gt; is True</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Movement Rejected flag&gt; is False</td></tr>
</tbody>
</table>
 (see Movement Rejected Flag in box 14.5b) </td><td colspan="3"></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Alert or Rejection of Movement Reason Code</td><td>R</td><td></td><td colspan="3">(see Code list 5 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Alert or Rejection of Movement Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Alert or Rejection of Movement Reason Code in box 14.6a) </td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">15</td><td>All Explanations on reason for shortage</td><td>O</td><td></td><td colspan="3"></td><td>99x</td></tr>
<tr><td colspan="2">15.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Submitter Type</td><td>R</td><td></td><td colspan="3">The possible values are :<table><tbody><tr><td>—</td><td>1 = Consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Consignee</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Validation of Explanation on Shortage</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ after successful validation</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td colspan="2">15.2</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">15.3</td><td>TRADER Consignor</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Submitter Type&gt; is "Consignor"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Submitter Type in box 15.1a) </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>R</td><td></td><td colspan="3">For TRADER Consignor An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;  The &lt;Operator Type Code&gt; of the referred &lt;TRADER&gt; must be: <table><tbody><tr><td>—</td><td>"Authorised warehouse keeper"; OR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Registered consignor"; OR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Certified consignor;</td></tr>
</tbody>
</table>
 OR  An existing identifier &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;. The &lt;Operator Type Code&gt; of the referred &lt;TRADER&gt; must be “Temporary certified consignor”.  For TRADER Place of dispatch  An existing identifier &lt;Tax Warehouse Reference&gt; (Excise Number in SEED).  (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>c</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>d</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">15.4</td><td>TRADER Consignee</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Submitter Type&gt; is not "Consignor"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Submitter Type in box 15.1a) </td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="13"></td><td rowspan="13">a</td><td rowspan="13">Trader Identification</td><td rowspan="13">C</td><td rowspan="13"><table><tbody><tr><td>—</td><td>‘R’ if &lt;Destination Type Code&gt; is:<table><tbody><tr><td>—</td><td>"Destination – Tax warehouse"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Temporary registered consignee"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Direct delivery"</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Destination – Certified consignee”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Destination – Temporary certified consignee”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Return to the place of dispatch of the consignor, for a Duty Paid B2B movement"</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="13">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist) </td></tr>
<tr><td><table><tbody><tr><td>8 -</td><td>Unknown destination</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>9 -</td><td>Destination – Certified consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (6)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>10 -</td><td>Destination – Temporary certified consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (7)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>11 -</td><td>Destination-Return to the place of dispatch of the consignor, for a Duty Paid B2B movement</td></tr>
</tbody>
</table>
</td><td>Excise Number (8) or Temporary Authorisation Reference (9)</td><td>Any identification (*)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(6)</td><td>The operator type of the consignee is "Certified consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(7)</td><td>The operator type of the consignee is "Temporary certified consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(8)</td><td>The operator type of the consignee is “Certified consignor”. An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(9)</td><td>An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt; with Operator Type Code “Temporary Certified Consignor”.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, “Any identification” means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td></td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(1) of Council Directive (EU) 2020/262</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">15.5</td><td>ANALYSIS</td><td>C</td><td>At least one of the &lt;ANALYSIS&gt; or &lt;ANALYSIS Body&gt; fields must be present</td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date of Analysis</td><td>R</td><td></td><td colspan="3"></td><td>date</td></tr>
<tr><td></td><td>b</td><td>Global Explanation</td><td>R</td><td></td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Global Explanation_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">15.6</td><td>ANALYSIS Body</td><td>C</td><td>At least one of the &lt;ANALYSIS&gt; or &lt;ANALYSIS Body&gt; fields must be present</td><td colspan="3"></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Body Record Unique Reference</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero. The &lt;Body Record Unique Reference&gt; must be unique within the message and must refer to a &lt;Body Record Unique Reference&gt; of the e-AD/e-SAD Body of the associated e-AD/e-SAD for which shortages or excesses have been declared. </td><td>n..3</td></tr>
<tr><td></td><td>b</td><td>Excise Product Code</td><td>R</td><td></td><td colspan="3">(see Code list 10 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an4</td></tr>
<tr><td></td><td>c</td><td>Explanation</td><td>O</td><td></td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>d</td><td>Explanation_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Actual Quantity</td><td>O</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td colspan="2">16</td><td>All reminder messages for Excise movement</td><td>O</td><td></td><td colspan="3"></td><td>99x</td></tr>
<tr><td colspan="2">16.1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td colspan="3">The possible values are:<table><tbody><tr><td>—</td><td>1 = Reminder message at expiry of time to change destination (or split)</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Reminder message at expiry of time to send the report of receipt/export</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>3 = Reminder message at expiry of time to give destination information (Article 22 of Directive (EU) 2020/262)</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Issuance of Reminder</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td></td><td>c</td><td>Limit date and Time</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td></td><td>d</td><td>Reminder Information</td><td>O</td><td></td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Reminder Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">16.2</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the Field must be greater than zero.</td><td>n..2</td></tr>
</tbody>
</table>

**Table 4**

**(referred to in Article 5)**

**Common Request**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Request for reference data</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Request for re-synchronisation of the register of economic operators</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Request for retrieval of a list of e-Ads/e-SADs</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = Request for SEED statistics</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = Request for retrieval of a list of e-Ads</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = Request for retrieval of a list of e-SADs</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Request Message Name</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td>The possible values are:<table><tbody><tr><td>‘C_COD_DAT’</td><td>=</td><td>Common list of codes</td></tr>
<tr><td>‘C_PAR_DAT’</td><td>=</td><td>Common system parameters</td></tr>
<tr><td>‘ALL’</td><td>=</td><td>For complete structure</td></tr>
</tbody>
</table>
</td><td>a..9</td></tr>
<tr><td></td><td>c</td><td>Requesting Office</td><td>R</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>d</td><td>Request Correlation Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’, ‘5’, ‘6’, or ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>An..44</td></tr>
<tr><td></td><td>e</td><td>Start Date</td><td>C</td><td rowspan="2">For 1 e and f:<table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td>Date</td></tr>
<tr><td></td><td>f</td><td>End Date</td><td>C</td><td></td><td>Date</td></tr>
<tr><td></td><td>g</td><td>Single Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td>Date</td></tr>
<tr><td colspan="2">2</td><td>E-AD/E-SAD LIST REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘6’, ‘8’ or ‘9’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>a2</td></tr>
<tr><td colspan="2">2.1</td><td>RA_PRIMARY CRITERION</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Primary Criterion Type Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = ARC</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Brand name of product</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Categories of excise products of the movement</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = City of consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = City of consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>10 = City of guarantor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>11 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>12 = City of place of delivery</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>13 = City of tax warehouse of dispatch</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>14 = City of transporter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>15 = CN code of product</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>16 = Date of invoice</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>17 = Excise number of consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>18 = Excise number of consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>19 = Excise number of guarantor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>20 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>21 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>22 = Excise number of the tax warehouse of destination</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>23 = Excise number of the tax warehouse of dispatch</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>24 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>25 = Excise product code</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>26 = Journey time</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>27 = Member State of destination</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>28 = Member State of dispatch</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>29 = Name of consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>30 = Name of consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>31 = Name of guarantor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>32 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>33 = Name of place of delivery</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>34 = Name of tax warehouse of dispatch</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>35 = Name of transporter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>36 = Number of invoice</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>37 = Postal code of consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>38 = Postal code of consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>39 = Postal code of guarantor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>40 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>41 = Postal code of place of delivery</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>42 = Postal code of tax warehouse of dispatch</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>43 = Postal code of transporter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>44 = Quantity of goods (in an e-AD/e-SAD body)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>45 = Local Reference Number, being a serial number, assigned by the consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>46 = Type of transport</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>47 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>48 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>49 = VAT number of the consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>50 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>51 = VAT number of the transporter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>52 = Change of destination (sequence number ≥ 2)</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td colspan="2">2.1.1</td><td>RA_PRIMARY VALUE</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Value</td><td>R</td><td></td><td>If &lt;Primary Criterion Type Code&gt; is ‘46’ (Type of transport), then an existing &lt;Transport Mode Code&gt; in the list of &lt;TRANSPORT MODES&gt; shall be used.</td><td>An..255</td></tr>
<tr><td colspan="2">3</td><td>STA_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Statistic Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Active/Inactive and Deleted economic operators</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Pending expirations</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Economic operators by type and tax warehouses</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Excise activity</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Changes to excise authorisations</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">3.1</td><td>LIST OF MEMBER STATES Code</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>a2</td></tr>
<tr><td colspan="2">4</td><td>STA_PERIOD</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Year</td><td>R</td><td></td><td>The value of the field must be greater than zero.</td><td>N4</td></tr>
<tr><td></td><td>b</td><td>Semester</td><td>C</td><td rowspan="3">For 4 b, c, and d: The three following data fields are optional and exclusive: <table><tbody><tr><td>—</td><td>&lt;Semester&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Quarter&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Month&gt;</td></tr>
</tbody>
</table>
 i.e. If one of these data fields is given then the two other data fields do not apply </td><td>The possible values are:<table><tbody><tr><td></td><td>1 = First semester</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Second semester</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>c</td><td>Quarter</td><td>C</td><td>The possible values are:<table><tbody><tr><td></td><td>1 = First quarter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Second quarter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Third quarter</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Fourth quarter</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Month</td><td>C</td><td>The possible values are:<table><tbody><tr><td></td><td>1 = January</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = February</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = March</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = April</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = May</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = June</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = July</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = August</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = September</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>10 = October</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>11 = November</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>12 = December</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td colspan="2">5</td><td>REFERENCE SYNCHRONISATION</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise.</td></tr>
</tbody>
</table>
 (See Request Type box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Period from date</td><td>R</td><td>–</td><td>This field must be prior or equal to field 5b. In case that an extraction is requested, the ‘Period from date’ and/or the ‘Period to date’ fields will be used to request occurrences valid in the specified period.  On the contrary, in case a retrieval is requested, the ‘Period from date’ and/or the ‘Period to date’ fields will be used to request occurrences modified and published in the specified period.  (See box 5c) </td><td>date</td></tr>
<tr><td></td><td>b</td><td>Period to date</td><td>R</td><td>–</td><td>In case that an extraction is requested, the ‘Period from date’ and/or the ‘Period to date’ fields will be used to request occurrences valid in the specified period. On the contrary, in case a retrieval is requested, the ‘Period from date’ and/or the ‘Period to date’ fields will be used to request occurrences modified and published in the specified period.  (See box 5c) </td><td>date</td></tr>
<tr><td></td><td>c</td><td>Extraction</td><td>O</td><td>–</td><td>The value of this field shall be:<table><tbody><tr><td>—</td><td>0: for retrieval (or missing in order to enable backward compatibility);</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>1: for extraction;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2: for non-invalidated records.</td></tr>
</tbody>
</table>
</td><td>N1</td></tr>
<tr><td></td><td>d</td><td>Member State Code</td><td>O</td><td>–</td><td>(see Code list 3 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>a2</td></tr>
<tr><td colspan="2">6</td><td>REF_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Common Risk Assessment Criteria flag</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">6.1</td><td>LIST OF CODES Code</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Requested List of Code</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Units of measure</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Events types</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Evidence types</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Language codes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = National Administrations</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = Country codes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = Packaging codes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>10 = Reasons for unsatisfactory receipt or control report</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>11 = Reasons for interruption</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>12 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>13 = Transport modes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>14 = Transport units</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>15 = Wine-growing zones</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>16 = Wine operation codes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>17 = Excise product categories</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>18 = Excise products</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>19 = CN codes</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>20 = Correspondences CN code – Excise product</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>21 = Cancellation reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>22 = Alert or rejection of e-AD reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>23 = Delay explanations</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>24 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>25 = Event submitting persons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>26 = Refusal reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>27 = Reasons for delayed result</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>28 = Request actions</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>29 = Request reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>30 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>31 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>32 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>33 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>34 = Administrative cooperation action not possible reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>35 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>36 = Type of document</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>37 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>38 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>39 = Manual Closure Request Reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>40 = Manual Closure Rejection Reasons</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>41 = National Administration – Degree Plato</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
</tbody>
</table>

**Table 5**

**(as referred to in Article 5(2))**

**List of e-AD/e-SAD as result of a general query**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td colspan="3">F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Requesting Office</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>b</td><td>Request Correlation Identifier</td><td>R</td><td></td><td colspan="3">The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>An..44</td></tr>
<tr><td colspan="2">2</td><td>E-AD/E-SAD LIST ITEM</td><td>O</td><td></td><td colspan="3"></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Dispatch Date</td><td>R</td><td></td><td colspan="3"></td><td>date</td></tr>
<tr><td colspan="2">2.1</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Validation of e-AD/e-SAD</td><td>R</td><td></td><td colspan="3"></td><td>dateTime</td></tr>
<tr><td></td><td>c</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">2.2</td><td>TRADER Consignor</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>R</td><td></td><td colspan="3">Provide a valid SEED registration number of the authorised warehousekeeper, registered consignor, certified consignor or temporary certified consignor. (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td colspan="2">2.3</td><td>TRADER Place of Dispatch</td><td>C</td><td>IF &lt;E-AD/E-SAD.Origin Type Code&gt; is ‘Origin – Tax warehouse’ or ‘Origin – Duty Paid’ THEN  &lt;TRADER Place of Dispatch&gt; is ‘R’  &lt;OFFICE of Dispatch – Import&gt; does not apply  ELSE  &lt;TRADER Place of Dispatch&gt; does not apply  &lt;OFFICE of Dispatch – Import&gt; is ‘R’ </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Tax Warehouse Reference</td><td>C</td><td>Doesn’t apply for Origin Type Code in box 9d ‘3’ (See for Origin Type Code box 9d in Table 1 of Delegated Regulation (EU) No 2022/1636) </td><td colspan="3">For TRADER Place of dispatch An existing identifier &lt;Tax Warehouse Reference&gt; (Excise Number in SEED).  (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>C</td><td>‘R’ if Origin Type Code in box 9d is ‘3’ (See for Origin Type Code box 9d in Table 1 of Delegated Regulation (EU) No 2022/1636) </td><td colspan="3"></td><td>an..182</td></tr>
<tr><td colspan="2">2.4</td><td>OFFICE of Dispatch – Import</td><td>C</td><td>IF &lt;E-AD.Origin Type Code&gt; is ‘Origin – Tax warehouse’ or ‘Origin – Duty Paid’ THEN  &lt;TRADER Place of Dispatch&gt; is ‘R’  &lt;OFFICE of Dispatch – Import&gt; does not apply  ELSE  &lt;TRADER Place of Dispatch&gt; does not apply  &lt;OFFICE of Dispatch – Import&gt; is ‘R’ </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">2.5</td><td>TRADER Consignee</td><td>C</td><td>‘R’, except –for Destination Type Code 8</td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="13"></td><td rowspan="13">a</td><td rowspan="13">Trader Identification</td><td rowspan="13">C</td><td rowspan="13">IF &lt;Destination Type Code&gt; is in:<table><tbody><tr><td>—</td><td>‘Destination – Tax warehouse’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Registered consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Temporary registered consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Direct delivery’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Certified consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Temporary certified consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Destination – Return to the place of dispatch of the consignor, for a Duty Paid B2B movement”</td></tr>
</tbody>
</table>
 THEN &lt;TRADER Consignee.Trader Identification&gt; is ‘R’  ELSE  IF &lt;Destination Type Code&gt; is: <table><tbody><tr><td>—</td><td>‘Destination – Export’</td></tr>
</tbody>
</table>
 THEN &lt;TRADER Consignee.Trader Identification&gt; is ‘O’  ELSE &lt;TRADER Consignee.Trader Identification&gt; does not apply </td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="13">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 –</td><td>Destination – Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 –</td><td>Destination – Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 –</td><td>Destination – Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 –</td><td>Destination – Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 –</td><td>Destination – Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 –</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td><table><tbody><tr><td>8 –</td><td>Unknown destination</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>9 –</td><td>Destination – Certified consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (6)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>10 –</td><td>Destination – Temporary certified consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (7)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>11 –</td><td>Destination-Return to the place of dispatch of the consignor, for a Duty Paid B2B movement</td></tr>
</tbody>
</table>
</td><td>Excise Number (8) or Temporary Authorisation Reference (9)</td><td>Any identification (*)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is “Authorised warehouse keeper”. An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is “Registered consignee”. An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either “Authorised warehouse keeper” or “Registered consignee”. An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is “Temporary registered consignee”. An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(6)</td><td>The operator type of the consignee is “Certified consignee”. An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(7)</td><td>The operator type of the consignee is “Temporary certified consignee”. An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(8)</td><td>The operator type of the consignee is "Certified consignor". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(9)</td><td>An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt; with Operator Type Code "Temporary Certified Consignor".</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination – Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(1) of Council Directive (EU) 2020/262.</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td colspan="2">2.6</td><td>TRADER Place of Delivery</td><td>C</td><td>The optionality of field &lt;TRADER Place of Delivery&gt; is described below, according to the &lt;Destination Type Code&gt;:<table><tbody><tr><td>—</td><td>‘R’ for Destination Type Code 1, 4, ‘9’ and ‘10’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ for Destination Type Code 2, 3 and 5</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>does not apply otherwise.</td></tr>
</tbody>
</table>
</td><td colspan="3">–</td><td>–</td></tr>
<tr><td rowspan="13"></td><td rowspan="13">a</td><td rowspan="13">Trader Identification</td><td rowspan="13">C</td><td rowspan="13">IF &lt;Destination Type Code&gt; is ‘Destination - Tax warehouse’ or ‘Destination – Certified consignee’ or ‘Destination - Temporary certified consignee’ THEN &lt;TRADER Place of Delivery. Trader Identification&gt; is ‘R’  ELSE  IF &lt;Destination Type Code&gt; is ‘Destination - Direct delivery’  THEN &lt;TRADER Place of Delivery. Trader Identification&gt; does not apply  ELSE &lt;TRADER Place of Delivery. Trader Identification&gt; is ‘O’ </td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="13">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td><table><tbody><tr><td>8 -</td><td>Unknown destination</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>9 -</td><td>Destination – Certified consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (6)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>10 -</td><td>Destination – Temporary certified consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (7)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>11 -</td><td>Destination-Return to the place of dispatch of the consignor, for a Duty Paid B2B movement</td></tr>
</tbody>
</table>
</td><td>Excise Number (8) or Temporary Authorisation Reference (9)</td><td>Any identification (*)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(6)</td><td>The operator type of the consignee is "Certified consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(7)</td><td>The operator type of the consignee is "Temporary certified consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(8)</td><td>The operator type of the consignee is "Certified consignor". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(9)</td><td>An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt; with Operator Type Code "Temporary Certified Consignor".</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>C</td><td>IF &lt;Destination Type Code&gt; is ‘Destination - Direct delivery’ THEN &lt;Trader Name&gt; is ‘O’  ELSE &lt;Trader Name&gt; is ‘R’ </td><td colspan="3"></td><td>an..182</td></tr>
<tr><td colspan="2">2.7</td><td>OFFICE Place of Delivery - Customs</td><td>C</td><td>The optionality of the field &lt;OFFICE Place of delivery – Customs&gt; is described below, according to &lt;Destination Type Code&gt;:<table><tbody><tr><td>—</td><td>‘R’ for Destination Type Code 6</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">2.8</td><td>EXCISE PRODUCTS CATEGORY Code</td><td>R</td><td></td><td colspan="3"></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Category Code</td><td>R</td><td></td><td colspan="3">(see Code list 3 in Annex II to Regulation (EU) No 612/2013)</td><td>a1</td></tr>
<tr><td colspan="2">2.9</td><td>TRADER Transport Arranger</td><td>C</td><td>IF &lt;E-AD/E-SAD Header.Transport Arrangement&gt;(IE801) (or &lt;E-AD/E-SAD Header.Transport Arrangement&gt;(IE815)) is ‘Consignor’ or ‘consignee’ THEN &lt;TRADER Transport Arranger&gt; does not apply  ELSE &lt;TRADER Transport Arranger&gt; is ‘R’ </td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>VAT Number</td><td>O</td><td></td><td colspan="3"></td><td>an..14</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td colspan="2">2.10</td><td>TRADER First Transporter</td><td>O</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>VAT Number</td><td>O</td><td></td><td colspan="3"></td><td>an..14</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
</tbody>
</table>

**Table 6**

**(referred to in Article 5)**

**Refusal of Common Request**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>Common Request Message</td><td>R</td><td></td><td>The context of the Common Request message relating to the movement, the structure of which is set out in Table 4</td><td></td></tr>
<tr><td colspan="2">2</td><td>Rejection</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Rejection Date and Time</td><td>R</td><td></td><td></td><td>dateTime</td></tr>
<tr><td></td><td>b</td><td>Rejection Reason Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>0 = Other</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = No e-AD(s) /e-SAD(s) retrieved matching selection criteria</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>3 = Reference data not available</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>4 = Excise Office List not available</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>5 = SEED data not available</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>7 = Unknown requested data</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>8 = Increment number out of range</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>26 = Duplicate detected</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>112 = Incorrect (code) value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>115 = Not supported in this position</td></tr>
</tbody>
</table>
</td><td>n..3</td></tr>
</tbody>
</table>

**Table 7**

**(as referred to in Article 6(1))**

**Administrative Cooperation Common Request**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Administrative cooperation</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = reserved</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Deadline for Results</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td colspan="2">2</td><td>FOLLOW UP</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Follow-Up Correlation ID</td><td>R</td><td></td><td>(see Code list 1 in Annex II)</td><td>an28</td></tr>
<tr><td></td><td>b</td><td>Date of Issuance</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>c</td><td>Sender Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Sender Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>e</td><td>Sender Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Addressee Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>g</td><td>Addressee Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>h</td><td>Addressee Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>i</td><td>National Case Reference Identifier</td><td>O</td><td></td><td></td><td>an..99</td></tr>
<tr><td colspan="2">3</td><td>ACO_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘1’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Administrative Cooperation Request Information</td><td>R</td><td></td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Administrative Cooperation Request Information_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Flag</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">3.1</td><td>REQUEST REASON Code</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Administrative Cooperation Request Reason Code</td><td>R</td><td></td><td>(see Code list 8 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>ACO_Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Administrative Cooperation Request Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..999</td></tr>
<tr><td></td><td>c</td><td>ACO_Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">3.1.1</td><td>RISK ASSESSMENT REFERENCE</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Other Risk Profile</td><td>O</td><td></td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Other Risk Profile_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">3.2</td><td>ARC List</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>O</td><td></td><td>The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">3.3</td><td>TRADER Person</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>C</td><td rowspan="3">For 3.3 a, b, and c: at least one of the following attributes must be present:<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;VAT Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>An existing identifier (Excise Number) &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt; or &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;. (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>VAT Number</td><td>C</td><td></td><td>an..14</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>C</td><td></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Member State Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Trader Name&gt; is given and &lt;Trader Excise Number&gt; is not given and &lt;VAT Number&gt; is not given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Trader Excise Number in box 3.3a, VAT Number in box 3.3b, Trader Name in box 3.3c) </td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Street Name</td><td>O</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>f</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>g</td><td>Postcode</td><td>O</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>h</td><td>City</td><td>O</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>i</td><td>NAD_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>j</td><td>Phone Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>k</td><td>Fax Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>l</td><td>Email Address</td><td>O</td><td></td><td></td><td>an..70</td></tr>
<tr><td colspan="2">3.4</td><td>SUPPORTING DOCUMENTS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Short Description of Supporting Document</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Supporting Document Type&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn't apply otherwise</td></tr>
</tbody>
</table>
 (see Reference of Supporting Document in box 3.4c and Image of Document in box 3.4e) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Short Description of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Reference of Supporting Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Short Description of Supporting Document in box 3.4a and Image of Document in box 3.4e) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Reference of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II, to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Image of Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Short Description of Supporting Document in box 3.4a and Reference of Supporting Document in box 3.4c) </td><td></td><td></td></tr>
<tr><td></td><td>f</td><td>Supporting Document Type</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 See Reference of Supporting Document in box 3.4c and Image of Document in box 3.4e </td><td>(see code list 15 in Annex II)</td><td>an..4</td></tr>
<tr><td colspan="2">3.5</td><td>ACTIONS Requested</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Administrative Cooperation Action Code</td><td>R</td><td></td><td>(see Code list 9 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>ACO Action Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Administrative Cooperation Action Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Administrative Cooperation Action Code in box 3.5a) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>c</td><td>ACO Action Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">4</td><td>CONTACT</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>b</td><td>Submitting Excise Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>Tel. Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>d</td><td>Fax Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Email Address</td><td>O</td><td></td><td></td><td>an..70</td></tr>
</tbody>
</table>

**Table 8**

**(referred to in Article 7)**

**Answer message**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>1 = Administrative Cooperation answer message</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = reserved</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">2</td><td>FOLLOW UP</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Follow Up Correlation ID</td><td>R</td><td></td><td>(see Code list 1 in Annex II)</td><td>an28</td></tr>
<tr><td></td><td>b</td><td>Date of Issuance</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>c</td><td>Sender Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Sender Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>e</td><td>Sender Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Addressee Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636</td><td>a2</td></tr>
<tr><td></td><td>g</td><td>Addressee Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>h</td><td>Addressee Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>i</td><td>National Case Reference Identifier</td><td>C</td><td>- 'O' If &lt;Follow Up Correlation ID&gt; does not match with &lt;Follow Up Correlation ID&gt; in a request message<table><tbody><tr><td>—</td><td>"R" If &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND</td></tr>
</tbody>
</table>
 &lt;National Case Reference Identifier&gt; is present in the request message </td><td>IF &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND &lt;National Case Reference Identifier&gt; is present in the request message THEN  &lt;National Case Reference Identifier&gt; must be equal to the value of &lt;National Case Reference Identifier&gt; in the request message. </td><td>an..99</td></tr>
<tr><td colspan="2">3</td><td>ANSWER</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Deadline for Results</td><td>C</td><td rowspan="2">For 3 a and b:<table><tbody><tr><td>—</td><td>‘R’ if &lt; Refusal Reason Code&gt; is provided</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Refusal Reason Code in box 3c) </td><td></td><td>dateTime</td></tr>
<tr><td></td><td>b</td><td>Delayed Result Reason Code</td><td>C</td><td>(see Code list 3 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Refusal Reason Code</td><td>O</td><td></td><td>(see Code list 4 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>d</td><td>Refusal Reason Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt; Refusal Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Refusal Reason Code in box 3c) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>e</td><td>Refusal Reason Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
</tbody>
</table>

**Table 9**

**(referred to in Article 7)**

**Reminder Message for Administrative Cooperation**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>—</td><td>1 = Administrative cooperation results reminder message</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>2 = Reserved</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">2</td><td>FOLLOW UP</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Follow Up Correlation ID</td><td>R</td><td></td><td>(see Code list 1 in Annex II)</td><td>an28</td></tr>
<tr><td></td><td>b</td><td>Date of Issuance</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>c</td><td>Sender Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Sender Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>e</td><td>Sender Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Addressee Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636</td><td>a2</td></tr>
<tr><td></td><td>g</td><td>Addressee Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>h</td><td>Addressee Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>i</td><td>National Case Reference Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>'O' If &lt;Follow Up Correlation ID&gt; does not match with &lt;Follow Up Correlation ID&gt; in a request message</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"R" If &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND &lt;National Case Reference Identifier&gt; is present in the request message </td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Otherwise it does not apply.</td></tr>
</tbody>
</table>
</td><td>IF &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND &lt;National Case Reference Identifier&gt; is present in the request message THEN  &lt;National Case Reference Identifier&gt; must be equal to the value of &lt;National Case Reference Identifier&gt; in the request message. </td><td>an..99</td></tr>
</tbody>
</table>

**Table 10**

**(as referred to in Article 6(3), Article 9(1) and Articles 10 and 16)**

**Administrative Cooperation Results**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>FOLLOW UP</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Follow Up Correlation ID</td><td>R</td><td></td><td>(see Code list 1 in Annex II)</td><td>an28</td></tr>
<tr><td></td><td>b</td><td>Date of Issuance</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>c</td><td>Sender Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Sender Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>e</td><td>Sender Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Addressee Member State Code</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>g</td><td>Addressee Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>h</td><td>Addressee Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>i</td><td>National Case Reference Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ If &lt;Follow Up Correlation ID&gt; does not match with &lt;Follow Up Correlation ID&gt; in a request message</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘R’ If &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND &lt;National Case Reference Identifier&gt; is present in the request message </td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Otherwise it does not apply.</td></tr>
</tbody>
</table>
</td><td>IF &lt;Follow Up Correlation ID&gt; matches with &lt;Follow Up Correlation ID&gt; in a request message AND &lt;National Case Reference Identifier&gt; is present in the request message THEN  &lt;National Case Reference Identifier&gt; must be equal to the value of &lt;National Case Reference Identifier&gt; in the request message. </td><td>an..99</td></tr>
<tr><td colspan="2">2</td><td>CONTACT</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>b</td><td>Submitting Excise Officer</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>Tel. Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>d</td><td>Fax Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Email Address</td><td>O</td><td></td><td></td><td>an..70</td></tr>
<tr><td colspan="2">3</td><td>ACO_ACTION RESULT</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>O</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;ARC&gt; is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see ARC in box 3a) </td><td>The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Administrative Cooperation Action Code</td><td>R</td><td></td><td>(see Code list 9 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>d</td><td>ACO Action Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Administrative Cooperation Action Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Administrative Cooperation Action Code in box 3c) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>e</td><td>ACO Action Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>ACO Action Not Possible Reason Code</td><td>O</td><td></td><td>(see Code list 11 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>g</td><td>ACO Action Not Possible Reason Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;ACO Action Not Possible Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see ACO Action Not Possible Reason Code in box 3f) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>h</td><td>ACO Action Not Possible Reason Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>i</td><td>Finding at Destination</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = Other finding</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = (reserved)</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Consignment in order</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Consignment has not reached destination</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Consignment arrived late</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Shortage detected</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Excise products not in order</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = Consignment not entered in stock records</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = Trader could not be contacted</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = Missing trader</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>10 = Excess detected</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>11 = Wrong EPC</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>12 = Wrong destination type code</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>13 = Differences confirmed</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>14 = Manual closing recommended</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>15 = Interruption recommended</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>16 = Irregularities Found</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td></td><td>j</td><td>Other Finding Type</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Finding at Destination&gt; is ‘Other finding’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Finding at Destination in box 3i) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>k</td><td>Other Finding Type_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636 , Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>l</td><td>Complementary Explanations</td><td>O</td><td></td><td></td><td>an..999</td></tr>
<tr><td></td><td>m</td><td>Complementary Explanations_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>n</td><td>Control Report Reference</td><td>O</td><td></td><td>(see Code list 2 in Annex II) A ‘Control Report’ message exists in the system (including the case that it is encapsulated in a received ‘History of a movement’ message) having the same &lt;Control Report Reference&gt; with that of the submitted message. In addition if the &lt;ARC&gt; is provided in the submitted message then it coincides with the &lt;ARC&gt; of the referenced ‘Control Report’ message.  (see ARC in box 3a) </td><td>an16</td></tr>
<tr><td colspan="2">4</td><td>FEEDBACK REQUEST</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Feedback Requested or Provided</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = No feedback requested</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Feedback requested</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Feedback provided</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Follow Up Actions</td><td>C</td><td>At least one among these two fields if box 4a is given:<table><tbody><tr><td>—</td><td>&lt;Follow Up Actions&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Relevance of Information&gt;</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..999</td></tr>
<tr><td></td><td>c</td><td>Follow Up Actions_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Relevance of Information Provided</td><td>C</td><td>At least one among these two fields if box 4a is given:<table><tbody><tr><td>—</td><td>&lt; Follow Up Actions&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Relevance of Information&gt;</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..999</td></tr>
<tr><td></td><td>e</td><td>Relevance of Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5</td><td>SUPPORTING DOCUMENTS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Short Description of Supporting Document</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Supporting Document Type&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Doesn't apply otherwise</td></tr>
</tbody>
</table>
 (See Supporting Document Type in box 5f) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Short Description of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Reference of Supporting Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Short Description of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Short Description of Supporting Document in box.5a and Image of Document in box 5e) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Reference of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Image of Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Short Description of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Short Description of Supporting Document in box 5a and Reference of Supporting Document in box 5c) </td><td></td><td></td></tr>
<tr><td></td><td>f</td><td>Supporting Document Type</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Short Description of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Short Description of Supporting Document in box 5a, Reference of Supporting Document in box 5c and Image of Document in box5e) </td><td>(see code list 15 in Annex II)</td><td>an..4</td></tr>
</tbody>
</table>

**Table 11**

**(as referred to in Article 9(2) and Article 11)**

**Control Report**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Validated document</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Validation of Control Report</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ after successful validation</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>dateTime</td></tr>
<tr><td colspan="2">2</td><td>CONTROL REPORT HEADER</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Control Report Reference</td><td>R</td><td></td><td>(see Code list 2 in Annex II)</td><td>an16</td></tr>
<tr><td colspan="2">2.1</td><td>CONTROL OFFICE</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Control Office Reference Number</td><td>O</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td></td><td>b</td><td>Member State Code</td><td>C</td><td rowspan="6">For 2.1 b, c, d, e, f, and g:<table><tbody><tr><td>—</td><td>‘R’ except for &lt;Street Number&gt;, which is ‘O’, if &lt;Control Office Reference Number&gt; is not given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Control Office Reference Number in box 2.1a) </td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Control Office Name</td><td>C</td><td></td><td>an..35</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>C</td><td></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>C</td><td></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>C</td><td></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>C</td><td></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>Phone Number</td><td>C</td><td rowspan="3">For 2.1 h, i and j: If &lt;Control Office Reference Number&gt; is not given, at least one of the following three attributes must be present: <table><tbody><tr><td>—</td><td>&lt;Phone Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Fax Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Email Address&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>otherwise, none of the three attributes are applicable</td></tr>
</tbody>
</table>
 (see Control Office Reference Number in box 2.1a) </td><td></td><td>an..35</td></tr>
<tr><td></td><td>i</td><td>Fax Number</td><td>C</td><td></td><td>an..35</td></tr>
<tr><td></td><td>j</td><td>Email Address</td><td>C</td><td></td><td>an..70</td></tr>
<tr><td></td><td>k</td><td>NAD_LNG</td><td>C</td><td>‘R’ if the corresponding free text field(s) is (are) used</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">3</td><td>EXCISE MOVEMENT</td><td>C</td><td>One of the &lt;EXCISE MOVEMENT&gt; or &lt;OTHER ACCOMPANYING DOCUMENT&gt; fields must be present</td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td>The value of the Field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">4</td><td>OTHER ACCOMPANYING DOCUMENT</td><td>C</td><td>One of the &lt;EXCISE MOVEMENT&gt; or &lt;OTHER ACCOMPANYING DOCUMENT&gt; fields must be present</td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Other Accompanying Document Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = Other</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = (reserved)</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Short Description of Other Accompanying Document</td><td>C</td><td>‘R’ if &lt;Other Accompanying Document Type&gt; is ‘Other’ It doesn't apply otherwise </td><td></td><td>an…350</td></tr>
<tr><td></td><td>c</td><td>Short Description of Other Accompanying Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>n2</td></tr>
<tr><td></td><td>d</td><td>Other Accompanying Document Number</td><td>R</td><td></td><td></td><td>an…350</td></tr>
<tr><td></td><td>e</td><td>Other Accompanying Document Date</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>f</td><td>Image of Other Accompanying Document</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>g</td><td>Member State of Dispatch</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>h</td><td>Member State of Destination</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td colspan="2">4.1</td><td>TRADER Person Involved in Movement</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>C</td><td>At least one of the following attributes must be present:<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>An existing identifier (Excise Number) &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt; or &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;. (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Identification</td><td>C</td><td>At least one of the following attributes must be present:<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>A VAT number or any other National number.</td><td>an16</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>C</td><td>At least one of the following attributes must be present:<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Trader Person Type</td><td>O</td><td></td><td>The possible values are the following:<table><tbody><tr><td></td><td>1 = Consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Tax representative</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Vendor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Liable person</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Customer private individual</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td></td><td>e</td><td>Member State Code</td><td>C</td><td>‘R’ if &lt;Trader Name&gt; is given AND &lt;Trader Excise Number&gt; and &lt;Trader Identification&gt; is not given. It doesn't apply otherwise </td><td>(see Code list 3 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>Street Name</td><td>O</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>g</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>h</td><td>Postcode</td><td>O</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>i</td><td>City</td><td>O</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>j</td><td>NAD_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) No 2022/1636 , Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>k</td><td>Phone Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>m</td><td>Email Address</td><td>O</td><td></td><td></td><td>an..70</td></tr>
<tr><td colspan="2">4.2</td><td>GOODS ITEM</td><td>O</td><td></td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Description of the Goods</td><td>O</td><td></td><td></td><td>an..55</td></tr>
<tr><td></td><td>b</td><td>CN Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box4 and 4f) </td><td>The value of the Field must be greater than zero.</td><td>n8</td></tr>
<tr><td></td><td>c</td><td>Commercial Description of the Goods</td><td>O</td><td></td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Additional code</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Quantity</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box4 and 4f) </td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>f</td><td>Unit of Measure Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box4 and 4f) </td><td>(See Annex II to Delegated Regulation (EU) 2022/1636, Code list 11)</td><td>n..2</td></tr>
<tr><td></td><td>g</td><td>Gross Mass</td><td>O</td><td></td><td>The Gross Mass must be equal to or higher than Net Mass. The value of the Field must be greater than zero. </td><td>n..16,6</td></tr>
<tr><td></td><td>h</td><td>Net Mass</td><td>O</td><td></td><td>The Gross Mass must be equal to or higher than Net Mass. The value of the Field must be greater than zero. </td><td>n..16,6</td></tr>
<tr><td colspan="2">4.3</td><td>MEANS OF TRANSPORT</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box4 and 4f) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Trader Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>b</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>c</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>d</td><td>Transporter Country</td><td>R</td><td></td><td>Provide a ‘Country Code’ listed in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636 .</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>Transport Mode Code</td><td>R</td><td></td><td>Provide the mode of transport using the codes in Code list 6 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>n..2</td></tr>
<tr><td></td><td>h</td><td>ACO_Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;MEANS OF TRANSPORT. Transport Mode Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box 4.3g) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>i</td><td>ACO_Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>j</td><td>Registration</td><td>R</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>k</td><td>Country of Registration</td><td>R</td><td></td><td>Provide a ‘Country Code’ listed in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td colspan="2">5</td><td>CONTROL REPORT</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Date of Control</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>b</td><td>Place of Control</td><td>R</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Place of Control_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Control Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Physical control</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Documentary control</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>e</td><td>Reason for Control</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = Other reason</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Control started at random</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Event signalled</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Request for assistance received</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Request from another office</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Alert received</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>f</td><td>Complementary Origin Reference</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Origin Reference_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>h</td><td>Control Officer Identity</td><td>R</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>i</td><td>Control Officer Identity_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>j</td><td>Global Control Conclusion</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Satisfactory</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Minor discrepancies found</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Interruption recommended</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Intention to make claim under Article 9 or Article 46 of Council Directive (EU) 2020/262</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Allowable loss detected, in relation to Article 6 or Article 45 of Council Directive (EU) 2020/262</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>k</td><td>Control at Arrival Required</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>l</td><td>Flag</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = No or False</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>m</td><td>Comments</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>n</td><td>Comments_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5.1</td><td>PERFORMED CONTROL ACTION</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Performed Control Action</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = Other control action</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>1 = Verified counted packs</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Unloaded</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Opened packs</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Annotated paper copy of documents</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Counting</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Sampling</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>7 = Administrative control</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>8 = Goods weighted/measured</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>9 = Random check</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>10 = Control of records</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>11 = Compare documents presented with e-AD/e-SAD</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Other Control Action</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Performed Control Action&gt; is ‘0’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Performed Control Action in box 5.1a) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Other Control Action_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5.2</td><td>SUPPORTING EVIDENCE</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Reason for Control&gt; is ‘2’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Reason for Control in box 5e) </td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Issuing Authority</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>b</td><td>Issuing Authority_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Evidence Type Code</td><td>R</td><td></td><td>(see Code list 6 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>d</td><td>Evidence Type Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Evidence Type Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Evidence Type Code in box 5.2c) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Evidence Type Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>Reference of Evidence</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Reference of Evidence_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text(s) field is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>h</td><td>Image of Evidence</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td colspan="2">5.3</td><td>UNSATISFACTORY REASON</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Unsatisfactory Reason Code</td><td>R</td><td></td><td>(see Code list 12 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Unsatisfactory Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Unsatisfactory Reason Code in box 5.3a) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5.4</td><td>TRANSPORT DETAILS</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Transport Unit Code</td><td>R</td><td></td><td>(see Code list 7 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Identity of Transport Units</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Transport Unit Code&gt; is not ‘Fixed transport installations’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Transport Unit Code in box 5.4a) </td><td></td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>Identity of Commercial Seal</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>d</td><td>Seal Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Seal Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5.5</td><td>CONTROL REPORT Body</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Body Record Unique Reference</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;EXCISE MOVEMENT &gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>This value refers to the &lt;Body Record Unique Reference&gt; of the e-AD/e-SAD Body of the associated e-AD/e-SAD and must be unique within the message. The value of the Field must be greater than zero. </td><td>n..3</td></tr>
<tr><td></td><td>b</td><td>Description of the Goods</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..55</td></tr>
<tr><td></td><td>c</td><td>CN Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>The value of the Field must be greater than zero.</td><td>n8</td></tr>
<tr><td></td><td>d</td><td>Additional code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Indicator of Shortage or Excess</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>S = Shortage</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>E = Excess</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>f</td><td>Observed Shortage or Excess</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Indicator of Shortage or Excess&gt; is given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Indicator of Shortage or Excess in box 5.5e) </td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>g</td><td>Comments</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>h</td><td>Comments_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5.5.1</td><td>UNSATISFACTORY REASON</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Unsatisfactory Reason Code</td><td>R</td><td></td><td>(see Code list 12 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Unsatisfactory Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Indicator of Unsatisfactory Reason Code in box 5.5.1a) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
</tbody>
</table>

**Table 12**

**(as referred to in Article 14)**

**Event Report**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Initial submission</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Validated document</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Validation of Event Report</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ after successful validation,</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>dateTime</td></tr>
<tr><td colspan="2">2</td><td>EVENT REPORT HEADER</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Event Report Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Message Type&gt; is ‘3’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Message Type in box 1a) </td><td>(see Code list 2 in Annex II)</td><td>an16</td></tr>
<tr><td></td><td>b</td><td>MS of Submission Event Report Reference</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Message Type&gt; is ‘1’ or ‘3’ and the MS of submission is different from the MS of event</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Message Type&gt; is ‘1’ or ‘3’ and the MS of submission is the MS of event</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Message Type in box 1a) </td><td>The format of &lt;MS of Submission Event Report Reference&gt; is:<table><tbody><tr><td>—</td><td>2 alphabetic characters: Identifier of the National Administration of Submission of the event report</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>followed by a nationally assigned, unique code</td></tr>
</tbody>
</table>
</td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>d</td><td>Sequence Number</td><td>R</td><td></td><td>The value of the field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">3</td><td>OTHER ACCOMPANYING DOCUMENT</td><td>C</td><td>One of the &lt;EXCISE MOVEMENT &gt; or &lt;OTHER ACCOMPANYING DOCUMENT&gt; fields must be present </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Other Accompanying Document Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>0 = Other</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = (reserved)</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Short Description of Other Accompanying Document</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Other Accompanying Document Type&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>It doesn't apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Short Description of Other Accompanying Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Other Accompanying Document Number</td><td>R</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Other Accompanying Document Date</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>f</td><td>Image of Other Accompanying Document</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>g</td><td>Member State of Dispatch</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>h</td><td>Member State of Destination</td><td>R</td><td></td><td>A National Administration identified by a Country Code in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td colspan="2">3.1</td><td>TRADER Person Involved in Movement</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>At least one of the following attributes must be present:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>An existing identifier (Excise Number) &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt; or &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;. (see Code list 1 in Annex II to Regulation (EU) No 612/2013) </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Identification</td><td>C</td><td><table><tbody><tr><td>—</td><td>At least one of the following attributes must be present:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>A VAT number or any other National number.</td><td>an16</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>C</td><td><table><tbody><tr><td>—</td><td>At least one of the following attributes must be present:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Excise Number&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Identification&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Trader Name&gt;</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Trader Person Type</td><td>O</td><td></td><td>The possible values are the following:<table><tbody><tr><td></td><td>1 = Consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Tax representative</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Vendor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>5 = Liable person</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>6 = Customer private individual</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td></td><td>e</td><td>Member State Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Trader Name&gt; is given AND &lt;Trader Excise Number&gt; and &lt;Trader Identification&gt; is not given.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>It doesn't apply otherwise</td></tr>
</tbody>
</table>
</td><td>(see Code list 3 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>Street Name</td><td>O</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>g</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>h</td><td>Postcode</td><td>O</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>i</td><td>City</td><td>O</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>j</td><td>NAD_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>k</td><td>Phone Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>l</td><td>Fax Number</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>m</td><td>Email Address</td><td>O</td><td></td><td></td><td>an..70</td></tr>
<tr><td colspan="2">3.2</td><td>GOODS ITEM</td><td>O</td><td></td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Description of the Goods</td><td>O</td><td></td><td></td><td>an..55</td></tr>
<tr><td></td><td>b</td><td>CN Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT. Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box 3 and 3f) </td><td>The value of the Field must be greater than zero.</td><td>n8</td></tr>
<tr><td></td><td>c</td><td>Commercial Description of the Goods</td><td>O</td><td></td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Additional code</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Quantity</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box3 and 3f) </td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>f</td><td>Unit of Measure Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box3 and 3f) </td><td>(See Annex II to Delegated Regulation (EU) 2022/1636, Code list 11)</td><td>n..2</td></tr>
<tr><td></td><td>g</td><td>Gross Mass</td><td>O</td><td></td><td>The Gross Mass must be equal to or higher than Net Mass. The value of the Field must be greater than zero. </td><td>n..16,6</td></tr>
<tr><td></td><td>h</td><td>Net Mass</td><td>O</td><td></td><td>The Gross Mass must be equal to or higher than Net Mass. The value of the Field must be greater than zero. </td><td>n..16,6</td></tr>
<tr><td colspan="2">3.3</td><td>MEANS OF TRANSPORT</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;OTHER ACCOMPANYING DOCUMENT.Image of Other Accompanying Document&gt; is not present in the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box3 and 3f) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Trader Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>b</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>c</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>d</td><td>Transporter Country</td><td>R</td><td></td><td>Provide a ‘Country Code’ listed in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>Transport Mode Code</td><td>R</td><td></td><td>Provide the mode of transport using the codes in Code list 6 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>n..2</td></tr>
<tr><td></td><td>h</td><td>ACO_Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;MEANS OF TRANSPORT.Transport Mode Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see box 3.3g) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>i</td><td>ACO_Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is (are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>j</td><td>Registration</td><td>R</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>k</td><td>Country of Registration</td><td>R</td><td></td><td>Provide a ‘Country Code’ listed in Code list 3 of Annex II to Delegated Regulation (EU) 2022/1636.</td><td>a2</td></tr>
<tr><td colspan="2">4</td><td>EVENT REPORT</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Date of Event</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>b</td><td>Place of Event</td><td>R</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Place of Event_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Excise Officer Identification</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>e</td><td>Submitting Person</td><td>R</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Submitting Person Code</td><td>R</td><td></td><td>(see Code list 10 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>g</td><td>Submitting Person Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Submitting Person Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Submitting Person Code in box 4f) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>h</td><td>Submitting Person Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>i</td><td>Changed Transport Arrangement</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Consignor</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Consignee</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Owner of goods</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Other</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>j</td><td>Comments</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>k</td><td>Comments_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">5</td><td>EVIDENCE OF EVENT</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Issuing Authority</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>b</td><td>Issuing Authority_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Evidence Type Code</td><td>R</td><td></td><td>(see Code list 6 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>d</td><td>Evidence Type Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ &lt;Evidence Type Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Evidence Type Code in box 5c) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Evidence Type Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>2</td></tr>
<tr><td></td><td>f</td><td>Reference of Evidence</td><td>R</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Reference of Evidence_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>h</td><td>Image of Evidence</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td colspan="2">6</td><td>TRADER New Transport Arranger</td><td>C</td><td><table><tbody><tr><td>—</td><td>Does not apply if &lt;Changed Transport Arrangement&gt; is ‘1’, ‘2’, or is not used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘R’ otherwise</td></tr>
</tbody>
</table>
 (see Changed Transport Arrangement in box 4i) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>VAT Number</td><td>O</td><td></td><td></td><td>an..14</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>c</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>d</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>NAD_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">7</td><td>TRADER New Transporter</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>VAT Number</td><td>O</td><td></td><td></td><td>an..14</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>c</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>d</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>NAD_LNG</td><td>R</td><td></td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">8</td><td>TRANSPORT DETAILS</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Transport Unit Code</td><td>R</td><td></td><td>(see Code list 7 in Annex II to Delegated Regulation (EU) 2022/1636 )</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Identity of Transport Units</td><td>C</td><td><table><tbody><tr><td>—</td><td>Does not apply if &lt;Transport Unit Code&gt; is ‘Fixed transport installations’.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘R’ otherwise</td></tr>
</tbody>
</table>
 (see Transport Unit Code in box 8a) </td><td></td><td>an..35</td></tr>
<tr><td></td><td>c</td><td>Identity of Commercial Seal</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>d</td><td>Seal Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>e</td><td>Seal Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">9</td><td>EVENT REPORT Body</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;TRADER New Transport Arranger&gt; is used, or &lt;TRADER New Transporter&gt; is used, or &lt;TRANSPORT DETAILS&gt; is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘R’ otherwise</td></tr>
</tbody>
</table>
 (see TRADER New Transport Arranger in 6, TRADER New Transport in 7, and TRANSPORT DETAILS in 8) </td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Event Type Code</td><td>R</td><td></td><td>(see Code list 14 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Associated Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Event Type Code&gt; is ‘0’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Event Type Code in box 9a) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Associated Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>d</td><td>Body Record Unique Reference</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;EXCISE MOVEMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>This value refers to the &lt;Body Record Unique Reference&gt; of the e-AD/e-SAD Body of the associated e-AD/e-SAD and must be unique within the message. The value of the Field must be greater than zero. </td><td>n..3</td></tr>
<tr><td></td><td>e</td><td>Description of the Goods</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..55</td></tr>
<tr><td></td><td>f</td><td>CN Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>The value of the Field must be greater than zero.</td><td>n8</td></tr>
<tr><td></td><td>g</td><td>Additional code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if the &lt;OTHER ACCOMPANYING DOCUMENT&gt; field is present</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>–</td><td>an..35</td></tr>
<tr><td></td><td>h</td><td>Indicator of Shortage or Excess</td><td>C</td><td rowspan="2">For 9h and 9i:<table><tbody><tr><td>—</td><td>‘R’ if &lt;Body Record Unique Reference&gt; or &lt;Description of the Goods&gt; or &lt;CN Code&gt; or &lt;Additional Code&gt; is given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Body Record Unique Reference in box 9d, Description of the Goods in box 9e, CN Code in box 9f and Additional Code in box 9g) </td><td>The possible values are:<table><tbody><tr><td>S</td><td>=</td><td>Shortage</td></tr>
<tr><td>E</td><td>=</td><td>Excess</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>i</td><td>Observed Shortage or Excess</td><td>C</td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
</tbody>
</table>

**Table 13**

**(referred to in Article 12)**

**Interruption of Movement**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>(see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Date and Time of Issuance</td><td>R</td><td></td><td></td><td>dateTime</td></tr>
<tr><td></td><td>c</td><td>Reason for Interruption Code</td><td>R</td><td></td><td>(see Code list 13 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>d</td><td>Excise Office Reference Number</td><td>R</td><td></td><td>(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636])</td><td>an8</td></tr>
<tr><td></td><td>e</td><td>Excise Officer Identification</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Reason for Interruption Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>'O' otherwise</td></tr>
</tbody>
</table>
 (see Reason for Interruption Code in box 1c) </td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field</td><td>a2</td></tr>
<tr><td colspan="2">2</td><td>CONTROL REPORT Reference</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Control Report Reference</td><td>R</td><td></td><td>(see Code list 2 in Annex II) A ‘Control Report’ message exists in the system (including the case that it is encapsulated in a received ‘History of a movement’ message) having the same &lt;Control Report Reference&gt; and &lt;ARC&gt; with that of the submitted message.  (see ARC in box 1a) </td><td>an16</td></tr>
<tr><td colspan="2">3</td><td>EVENT REPORT Reference</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Event Report Number</td><td>R</td><td></td><td>(see Code list 2 in Annex II) An ‘Event Report’ message exists in the system (including the case that it is encapsulated in a received ‘History of a movement’ message) having the same &lt;Event Report Number&gt; and &lt;ARC&gt; with that of the submitted message  (see ARC in box 1a) </td><td>an16</td></tr>
</tbody>
</table>

**Table 14**

**(as referred to in Article 13)**

**Alert or Rejection of an e-AD/e-SAD**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td colspan="3">F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date and Time of Validation of Alert or Rejection</td><td>C</td><td><table><tbody><tr><td>—</td><td>R if corresponding field is validated</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">–</td><td>dateTime</td></tr>
<tr><td colspan="2">2</td><td>EXCISE MOVEMENT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td colspan="3">Provide the ARC of the e-AD/e-SAD. (see Code list 2 in Annex to Delegated Regulation (EU) 2022/1636) </td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td colspan="3">The value of the field must be greater than zero.</td><td>n..2</td></tr>
<tr><td colspan="2">3</td><td>TRADER Consignee</td><td>D</td><td>‘R’, except for Destination Type Code 8 (See Destination Type Code in box 1a of Table 1 in Delegated Regulation (EU) No 2022/1636) </td><td colspan="3"></td><td></td></tr>
<tr><td rowspan="12"></td><td rowspan="12">a</td><td rowspan="12">Trader Identification</td><td rowspan="12">C</td><td rowspan="12"><table><tbody><tr><td>—</td><td>‘R’ if &lt;Destination Type Code&gt; is:<table><tbody><tr><td>—</td><td>‘Destination - Tax warehouse’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination - Registered consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination - Temporary registered consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination - Direct delivery’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Certified consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘Destination – Temporary certified consignee’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>"Destination – Return to the place of dispatch of the consignor, for a Duty Paid B2B movement"</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination - Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">The possible values of &lt;Trader Identification&gt; are described in the following table:</td><td rowspan="12">an..16</td></tr>
<tr><td>Destination Type Code</td><td>TRADER CONSIGNEE. Trader Identification</td><td>TRADER Place of Delivery.Trader Identification</td></tr>
<tr><td><table><tbody><tr><td>1 -</td><td>Destination - Tax warehouse</td></tr>
</tbody>
</table>
</td><td>Excise number (1)</td><td>Tax Warehouse Reference (Excise Number) (5)</td></tr>
<tr><td><table><tbody><tr><td>2 -</td><td>Destination - Registered consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (2)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>3 -</td><td>Destination - Temporary registered consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (4)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>4 -</td><td>Destination - Direct delivery</td></tr>
</tbody>
</table>
</td><td>Excise number (3)</td><td>(Does not apply)</td></tr>
<tr><td><table><tbody><tr><td>5 -</td><td>Destination - Exempted consignee</td></tr>
</tbody>
</table>
</td><td>(Does not apply)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>6 -</td><td>Destination – Export</td></tr>
</tbody>
</table>
</td><td>VAT number (optional)</td><td>(The field &lt;TRADER Place of Delivery&gt; does not exist)</td></tr>
<tr><td><table><tbody><tr><td>9 -</td><td>Destination – Certified consignee</td></tr>
</tbody>
</table>
</td><td>Excise number (6)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>10 -</td><td>Destination – Temporary certified consignee</td></tr>
</tbody>
</table>
</td><td>Temporary authorisation reference (7)</td><td>Any identification (*)</td></tr>
<tr><td><table><tbody><tr><td>11 -</td><td>Destination-Return to the place of dispatch of the consignor, for a Duty Paid B2B movement</td></tr>
</tbody>
</table>
</td><td>Excise Number (8) or Temporary Authorisation Reference (9)</td><td>Any identification (*)</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>(1)</td><td>The operator type of the consignee is "Authorised warehouse keeper". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(2)</td><td>The operator type of the consignee is "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(3)</td><td>The operator type of the consignee is either "Authorised warehouse keeper" or "Registered consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(4)</td><td>The operator type of the consignee is "Temporary registered consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(5)</td><td>An existing identifier &lt;Tax Warehouse Reference&gt; in the set of &lt;TAX WAREHOUSE&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(6)</td><td>The operator type of the consignee is "Certified consignee". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(7)</td><td>The operator type of the consignee is "Temporary certified consignee". An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(8)</td><td>The operator type of the consignee is "Certified consignor". An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(9)</td><td>An existing &lt;Temporary Authorisation Reference&gt; in the set of &lt;TEMPORARY AUTHORISATION&gt; with Operator Type Code "Temporary Certified Consignor".</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(*)</td><td>For the place of delivery, "Any identification" means: a VAT number or any other identifier; it is optional.</td></tr>
</tbody>
</table>
 (see Code list 1 and Code list 2 in Annex II to Regulation (EU) No 612/2013, if applicable) </td></tr>
<tr><td></td><td>b</td><td>EORI Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘O’ if &lt;Destination Type Code&gt; is ‘Destination - Export’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the EORI number of the person responsible for lodging the export declaration as set out in Article 21(2) of Directive (EU) 2020/262.</td><td>an..17</td></tr>
<tr><td></td><td>c</td><td>Trader Name</td><td>R</td><td></td><td colspan="3"></td><td>an..182</td></tr>
<tr><td></td><td>d</td><td>Street Name</td><td>R</td><td></td><td colspan="3"></td><td>an..65</td></tr>
<tr><td></td><td>e</td><td>Street Number</td><td>O</td><td></td><td colspan="3"></td><td>an..11</td></tr>
<tr><td></td><td>f</td><td>Postcode</td><td>R</td><td></td><td colspan="3"></td><td>an..10</td></tr>
<tr><td></td><td>g</td><td>City</td><td>R</td><td></td><td colspan="3"></td><td>an..50</td></tr>
<tr><td></td><td>h</td><td>NAD_LNG</td><td>R</td><td></td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">4</td><td>OFFICE OF DESTINATION</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Office Reference Number</td><td>R</td><td></td><td colspan="3">(see Code list 4 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an8</td></tr>
<tr><td colspan="2">5</td><td>ALERT</td><td>R</td><td></td><td colspan="3"></td><td></td></tr>
<tr><td></td><td>a</td><td>Date of Alert</td><td>R</td><td></td><td colspan="3"></td><td>date</td></tr>
<tr><td></td><td>b</td><td>e-AD /e-SAD Rejected flag</td><td>R</td><td></td><td colspan="3">The format of Boolean is digital: ‘0’ or ‘1’ (‘0’ = No or False; ‘1’ = Yes or True).</td><td>n1</td></tr>
<tr><td colspan="2">6</td><td>ALERT OR REJECTION OF E-AD/E-SAD REASON Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;e-AD/e-SAD Rejected flag&gt; is True</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ if otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">–</td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Alert or Rejection of Movement Reason Code</td><td>R</td><td></td><td colspan="3">(see Code list 5 in Annex II)</td><td>n..2</td></tr>
<tr><td></td><td>b</td><td>Complementary Information</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Alert or Rejection of Movement Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Alert or Rejection of Movement Reason Code in box 6a) </td><td colspan="3"></td><td>an..350</td></tr>
<tr><td></td><td>c</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td colspan="3">Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
</tbody>
</table>

**Table 15**

**(as referred to in Article 6a)**

**Manual Closure Request**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTE</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>Provide the ARC of the e-AD or e-SAD. (see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636) </td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td>Provide the sequence number of the e-AD/e-SAD.</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Manual Closure Request Reason Code</td><td>R</td><td></td><td>(see code list 16 in Annex II)</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Manual Closure Reason Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Manual Closure Request Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
</td><td></td><td>an..999</td></tr>
<tr><td></td><td>e</td><td>Manual Closure Reason Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">2</td><td>SUPPORTING DOCUMENTS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Short Description of Supporting Document</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Supporting Document Type&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Short Description of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Reference of Supporting Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Image of Document in box 2e and Supporting Document Type in box 2f) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Reference of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Image of Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Reference of Supporting Document in box 2c and Supporting Document Type in box 2f) </td><td></td><td></td></tr>
<tr><td></td><td>f</td><td>Supporting Document Type</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Reference of Supporting Document in box 2c and Image of Document in box 2e) </td><td>(see code list 15 in Annex II)</td><td>an..4</td></tr>
<tr><td colspan="2">3</td><td>MANUAL CLOSURE Body</td><td>O</td><td></td><td></td><td>999X</td></tr>
<tr><td></td><td>a</td><td>Body Record Unique Reference</td><td>R</td><td></td><td>This value refers to the &lt;Body Record Unique Reference&gt; of the Body of the associated e-AD / e-SAD and must be unique within the message. The value of this field must be greater than zero. </td><td>n..3</td></tr>
<tr><td></td><td>b</td><td>Indicator of Shortage or Excess</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>S</td><td>=</td><td>Shortage</td></tr>
<tr><td>E</td><td>=</td><td>Excess</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>c</td><td>Observed Shortage or Excess</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Indicator of Shortage or Excess&gt; is given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>(see Indicator of Shortage or Excess in box 3b)</td></tr>
</tbody>
</table>
</td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>d</td><td>Excise Product Code</td><td>O</td><td></td><td>(see Code list 10 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an4</td></tr>
<tr><td></td><td>e</td><td>Refused Quantity</td><td>O</td><td></td><td>The value of this field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
</tbody>
</table>

**Table 16**

**(as referred to in Article 14a)**

**Manual Closure Response**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTE</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>ARC</td><td>R</td><td></td><td>Provide the ARC of the e-AD /e-SAD. (see Code list 2 in Annex II to Delegated Regulation (EU) 2022/1636) </td><td>an21</td></tr>
<tr><td></td><td>b</td><td>Sequence Number</td><td>R</td><td></td><td>Provide the sequence number of the e-AD / e-SAD</td><td>n..2</td></tr>
<tr><td></td><td>c</td><td>Date of Arrival of Excise Products</td><td>O</td><td></td><td>The date at which the movement ends in accordance with Article 19(2) of Council Directive (EU) 2020/262.</td><td>date</td></tr>
<tr><td></td><td>d</td><td>Global Conclusion of Receipt</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td></td><td>1 = Receipt accepted and satisfactory,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>2 = Receipt accepted although unsatisfactory,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>3 = Receipt refused,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>4 = Receipt partially refused,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>21 = Exit accepted and satisfactory,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>22 = Exit accepted with minor discrepancies detected,</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>23 = Exit refused.</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td></td><td>e</td><td>Complementary Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>f</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>g</td><td>Manual Closure Request Reason Code</td><td>R</td><td></td><td>(see code list 16 in Annex II)</td><td>n1</td></tr>
<tr><td></td><td>h</td><td>Manual Closure Reason Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Manual Closure Request Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
</td><td></td><td>an..999</td></tr>
<tr><td></td><td>i</td><td>Manual Closure Reason Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>j</td><td>Manual Closure Request Accepted</td><td>R</td><td>–</td><td>The format of Boolean is digital: ‘0’ or ‘1’ (‘0’ = No or False; ‘1’ = Yes or True).</td><td>n1</td></tr>
<tr><td></td><td>k</td><td>Manual Closure Rejection Reason Code</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Manual Closure Request Accepted&gt; is ‘0’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>(see code list 17 in Annex II)</td><td>n1</td></tr>
<tr><td></td><td>l</td><td>Manual Closure Rejection Complement</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Manual Closure Rejection Reason Code&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
</td><td></td><td>an..999</td></tr>
<tr><td></td><td>m</td><td>Manual Closure Rejection Complement_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td colspan="2">2</td><td>SUPPORTING DOCUMENTS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Short Description of Supporting Document</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Supporting Document Type&gt; is ‘Other’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td></td><td>an..999</td></tr>
<tr><td></td><td>b</td><td>Short Description of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>c</td><td>Reference of Supporting Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Image of Document in box 2e and Supporting Document Type in box 2f) </td><td></td><td>an..999</td></tr>
<tr><td></td><td>d</td><td>Reference of Supporting Document_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field(s) is(are) used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2</td></tr>
<tr><td></td><td>e</td><td>Image of Document</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Reference of Supporting Document in box 2c and Supporting Document Type in box 2f) </td><td></td><td></td></tr>
<tr><td></td><td>f</td><td>Supporting Document Type</td><td>C</td><td>At least one, among these three fields, must be present:<table><tbody><tr><td>—</td><td>&lt;Supporting Document Type&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Reference of Supporting Document&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Image of Document&gt;</td></tr>
</tbody>
</table>
 (see Reference of Supporting Document in box 2c and Image of Document in box 2e) </td><td>(see code list 15 in Annex II)</td><td>an..4</td></tr>
<tr><td colspan="2">3</td><td>MANUAL CLOSURE Body</td><td>O</td><td></td><td></td><td>999X</td></tr>
<tr><td></td><td>a</td><td>Body Record Unique Reference</td><td>R</td><td></td><td>This value refers to the &lt;Body Record Unique Reference&gt; of the Body of the associated e-AD /e-SAD and must be unique within the message. The value of this field must be greater than zero. </td><td>n..3</td></tr>
<tr><td></td><td>b</td><td>Indicator of Shortage or Excess</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>S</td><td>=</td><td>Shortage</td></tr>
<tr><td>E</td><td>=</td><td>Excess</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>c</td><td>Observed Shortage or Excess</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Indicator of Shortage or Excess&gt; is given</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
<table><tbody><tr><td></td><td>(see Indicator of Shortage or Excess in box 3b)</td></tr>
</tbody>
</table>
</td><td>The value of the Field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>d</td><td>Excise Product Code</td><td>O</td><td></td><td>(see Code list 10 in Annex II to Delegated Regulation (EU) 2022/1636)</td><td>an4</td></tr>
<tr><td></td><td>e</td><td>Refused Quantity</td><td>O</td><td></td><td>The value of this field must be greater than zero.</td><td>n..15,3</td></tr>
<tr><td></td><td>f</td><td>Complementary Information</td><td>O</td><td></td><td></td><td>an..350</td></tr>
<tr><td></td><td>g</td><td>Complementary Information_LNG</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if the corresponding text field is used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
</td><td>Provide the language code presented in Annex II to Delegated Regulation (EU) 2022/1636, Code list 1 to define the language used in this field.</td><td>a2’</td></tr>
</tbody>
</table>

(2) in Annex II, code list 15 is replaced by the following:

**‘ Code list 15: Type of Document**

| Code | Description |
| --- | --- |
| 0 | Other |
| 1 | e-AD |
| 2 | e-SAD |
| 3 | Invoice |
| 4 | Delivery note |
| 5 | CMR |
| 6 | Bill of lading |
| 7 | Way Bill |
| 8 | Contract |
| 9 | Trader’s Application |
| 10 | Official record |
| 11 | Request |
| 12 | Answer |
| 13 | Fallback documents, Fallback Printout |
| 14 | Photo |
| 15 | Export Declaration |
| 16 | Anticipated Export Record |
| 17 | Exit Results |
| 18 | Custom Declaration |
| 19 | Certificate of independent small producer of alcoholic beverages |
| <TARIC CODE> | Any TARIC code used in Data Element 1203000000 (sub-element 002000)of the export declaration’ |

ELI: http://data.europa.eu/eli/reg_impl/2024/289/oj

ISSN 1977-0677 (electronic edition)
