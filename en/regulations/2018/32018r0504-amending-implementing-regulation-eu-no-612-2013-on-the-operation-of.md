---
title: "Commission Implementing Regulation (EU) 2018/504 of 7 March 2018 amending Implementing Regulation (EU) No 612/2013 on the operation of the register of economic operators and tax warehouses, related statistics and reporting pursuant to Council Regulation (EU) No 389/2012 on administrative cooperation in the field of excise duties"
identifier: "32018R0504"
eli: "http://data.europa.eu/eli/reg_impl/2018/504/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2018-03-07
entry_into_force: 2018-11-07
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0504"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2018/504 of 7 March 2018 amending Implementing Regulation (EU) No 612/2013 on the operation of the register of economic operators and tax warehouses, related statistics and reporting pursuant to Council Regulation (EU) No 389/2012 on administrative cooperation in the field of excise duties

**COMMISSION IMPLEMENTING REGULATION (EU) 2018/504**

**of 7 March 2018**

**amending Implementing Regulation (EU) No 612/2013 on the operation of the register of economic operators and tax warehouses, related statistics and reporting pursuant to Council Regulation (EU) No 389/2012 on administrative cooperation in the field of excise duties**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Council Regulation (EU) No 389/2012 of 2 May 2012 on administrative cooperation in the field of excise duties and repealing Regulation (EC) No 2073/2004 (1), and in particular Article 22 thereof,

Whereas:

(1) Annex I to Commission Implementing Regulation (EU) No 612/2013 (2) lays down the structure and content of messages relating to the registration of economic operators and tax warehouses in the national registers and the Central Register. In order to improve the quality of data used in those messages Tables 1, 2 and 4 of Annex I to Implementing Regulation (EU) No 612/2013 should be amended.

(2) In accordance with Article 22 of Council Directive 2008/118/EC (3) in the case of movement of energy products under a duty suspension arrangement by sea or inland waterways, the competent authorities of the Member State of dispatch may authorise the consignor to omit the details of the consignee at the time of dispatch in the draft electronic administrative document referred to in Article 21(2) of that Directive. In accordance with Regulation (EU) No 612/2013 only an authorised warehouse keeper is allowed to omit the details of the consignee. Therefore it is also necessary to enable a registered consignor to leave empty the destination fields in the draft electronic administrative document when moving energy products under duty suspension arrangement by sea or inland waterways in order to align with Article 22 of Directive 2008/118/EC.

(3) The explanation in column F of Table 1 of Annex I to Implementing Regulation (EU) No 612/2013 should provide a clearer identification of the ‘Requesting Office’ data element in order to align with the definition in Annex II to Regulation (EC) No 684/2009.

(4) Implementing Regulation (EU) No 612/2013 should therefore be amended accordingly.

(5) In order to align the application date of this Regulation with the application date for a new version of the computerised system established by Decision No 1152/2003/EC of the European Parliament and of the Council (4) and to allow the Member States adequate time to prepare for the changes resulting from this Regulation, it should apply from 15 February 2018.

(6) The measures provided for in this Regulation are in accordance with the opinion of the Committee on Excise Duty,

HAS ADOPTED THIS REGULATION:

## Article 1

Annex I of Implementing Regulation (EU) No 612/2013 is amended as set out in the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

It shall apply from 15 February 2018.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 7 March 2018.

For the Commission

The President

Jean-Claude JUNCKER

(1) OJ L 121, 8.5.2012, p. 1.

(2) Commission Implementing Regulation (EU) No 612/2013 of 25 June 2013 on the operation of the register of economic operators and tax warehouses, related statistics and reporting pursuant to Council Regulation (EU) No 389/2012 on administrative cooperation in the field of excise duties (OJ L 173, 26.6.2013, p. 9).

(3) Council Directive 2008/118/EC of 16 December 2008 concerning the general arrangements for excise duty and repealing Directive 92/12/EEC (OJ L 9, 14.1.2009, p. 12).

(4) Decision No 1152/2003/EC of the European Parliament and of the Council of 16 June 2003 on computerising the movement and surveillance of excisable products (OJ L 162, 1.7.2003, p. 5).

## ANNEX

Annex I to Implementing Regulation (EU) No 612/2013 is amended as follows:

(1) Tables 1 and 2 are replaced by the following:

**‘Table 1**

**Common request**

**(referred to in Article 4(5), Article 7(2) and Article 8(2))**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>2</td><td>=</td><td>Request for extraction of reference data</td></tr>
<tr><td>3</td><td>=</td><td>Request for retrieval of reference data</td></tr>
<tr><td>4</td><td>=</td><td>Request for extraction of economic operators</td></tr>
<tr><td>5</td><td>=</td><td>Request for retrieval of economic operators</td></tr>
<tr><td>6</td><td>=</td><td>Request for EOL</td></tr>
<tr><td>7</td><td>=</td><td>Request for retrieval of a list of e-ADs</td></tr>
<tr><td>8</td><td>=</td><td>Request for SEED statistics</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Request Message Name</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘3’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td>The possible values are:<table><tbody><tr><td>“C_COD_DAT”</td><td>=</td><td>Common list of codes</td></tr>
<tr><td>“C_PAR_DAT”</td><td>=</td><td>Common system parameters</td></tr>
<tr><td>“ALL”</td><td>=</td><td>For complete structure</td></tr>
</tbody>
</table>
</td><td>a..9</td></tr>
<tr><td></td><td>c</td><td>Requesting Office</td><td>R</td><td></td><td>(see Code list 5 in Annex II to Regulation (EC) No 684/2009)</td><td>an8</td></tr>
<tr><td></td><td>d</td><td>Request Correlation Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’, ‘3’, ‘4’, ‘5’, ‘7’, or ‘8’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State</td><td>an..44</td></tr>
<tr><td></td><td>e</td><td>Start Date</td><td>C</td><td rowspan="2">For 1 e and f:<table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘3’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td>date</td></tr>
<tr><td></td><td>f</td><td>End Date</td><td>C</td><td></td><td>date</td></tr>
<tr><td></td><td>g</td><td>Single Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘4’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td>date</td></tr>
<tr><td colspan="2">2</td><td>E-AD LIST REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">2.1</td><td>RA_PRIMARY CRITERION</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Primary Criterion Type Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>ARC</td></tr>
<tr><td>2</td><td>=</td><td>Brand name of product</td></tr>
<tr><td>3</td><td>=</td><td>Categories of excise products of the movement</td></tr>
<tr><td>4</td><td>=</td><td>(reserved)</td></tr>
<tr><td>5</td><td>=</td><td>(reserved)</td></tr>
<tr><td>6</td><td>=</td><td>(reserved)</td></tr>
<tr><td>7</td><td>=</td><td>(reserved)</td></tr>
<tr><td>8</td><td>=</td><td>City of consignee</td></tr>
<tr><td>9</td><td>=</td><td>City of consignor</td></tr>
<tr><td>10</td><td>=</td><td>City of guarantor</td></tr>
<tr><td>11</td><td>=</td><td>(reserved)</td></tr>
<tr><td>12</td><td>=</td><td>City of place of delivery</td></tr>
<tr><td>13</td><td>=</td><td>City of tax warehouse of dispatch</td></tr>
<tr><td>14</td><td>=</td><td>City of transporter</td></tr>
<tr><td>15</td><td>=</td><td>CN code of product</td></tr>
<tr><td>16</td><td>=</td><td>Date of invoice</td></tr>
<tr><td>17</td><td>=</td><td>Excise number of consignee</td></tr>
<tr><td>18</td><td>=</td><td>Excise number of consignor</td></tr>
<tr><td>19</td><td>=</td><td>Excise number of guarantor</td></tr>
<tr><td>20</td><td>=</td><td>(reserved)</td></tr>
<tr><td>21</td><td>=</td><td>(reserved)</td></tr>
<tr><td>22</td><td>=</td><td>Excise number of the tax warehouse of destination</td></tr>
<tr><td>23</td><td>=</td><td>Excise number of the tax warehouse of dispatch</td></tr>
<tr><td>24</td><td>=</td><td>(reserved)</td></tr>
<tr><td>25</td><td>=</td><td>Excise product code</td></tr>
<tr><td>26</td><td>=</td><td>Journey time</td></tr>
<tr><td>27</td><td>=</td><td>Member State of destination</td></tr>
<tr><td>28</td><td>=</td><td>Member State of dispatch</td></tr>
<tr><td>29</td><td>=</td><td>Name of consignee</td></tr>
<tr><td>30</td><td>=</td><td>Name of consignor</td></tr>
<tr><td>31</td><td>=</td><td>Name of guarantor</td></tr>
<tr><td>32</td><td>=</td><td>(reserved)</td></tr>
<tr><td>33</td><td>=</td><td>Name of place of delivery</td></tr>
<tr><td>34</td><td>=</td><td>Name of tax warehouse of dispatch</td></tr>
<tr><td>35</td><td>=</td><td>Name of transporter</td></tr>
<tr><td>36</td><td>=</td><td>Number of invoice</td></tr>
<tr><td>37</td><td>=</td><td>Postal code of consignee</td></tr>
<tr><td>38</td><td>=</td><td>Postal code of consignor</td></tr>
<tr><td>39</td><td>=</td><td>Postal code of guarantor</td></tr>
<tr><td>40</td><td>=</td><td>(reserved)</td></tr>
<tr><td>41</td><td>=</td><td>Postal code of place of delivery</td></tr>
<tr><td>42</td><td>=</td><td>Postal code of tax warehouse of dispatch</td></tr>
<tr><td>43</td><td>=</td><td>Postal code of transporter</td></tr>
<tr><td>44</td><td>=</td><td>Quantity of goods (in an e-AD body)</td></tr>
<tr><td>45</td><td>=</td><td>Local Reference Number, being a serial number, assigned by the consignor</td></tr>
<tr><td>46</td><td>=</td><td>Type of transport</td></tr>
<tr><td>47</td><td>=</td><td>(reserved)</td></tr>
<tr><td>48</td><td>=</td><td>(reserved)</td></tr>
<tr><td>49</td><td>=</td><td>VAT number of the consignee</td></tr>
<tr><td>50</td><td>=</td><td>(reserved)</td></tr>
<tr><td>51</td><td>=</td><td>VAT number of the transporter</td></tr>
<tr><td>52</td><td>=</td><td>Change of destination (sequence number ≥ 2)</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td colspan="2">2.1.1</td><td>RA_PRIMARY VALUE</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Value</td><td>R</td><td></td><td></td><td>an..255</td></tr>
<tr><td colspan="2">3</td><td>STA_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘8’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Statistic Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Active and inactive economic operators</td></tr>
<tr><td>2</td><td>=</td><td>Pending expirations</td></tr>
<tr><td>3</td><td>=</td><td>Economic operators by type and tax warehouses</td></tr>
<tr><td>4</td><td>=</td><td>Excise activity</td></tr>
<tr><td>5</td><td>=</td><td>Changes to excise authorisations</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">3.1</td><td>LIST OF MEMBER STATES Code</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">4</td><td>STA_PERIOD</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘8’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Year</td><td>R</td><td></td><td></td><td>n4</td></tr>
<tr><td></td><td>b</td><td>Semester</td><td>C</td><td rowspan="3">For 4 b, c, and d: The three following data fields are optional and exclusive: <table><tbody><tr><td>—</td><td>&lt;Semester&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Quarter&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Month&gt;</td></tr>
</tbody>
</table>
 i.e. If one of these data fields is given then the two other data fields do not apply </td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>First semester</td></tr>
<tr><td>2</td><td>=</td><td>Second semester</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>c</td><td>Quarter</td><td>C</td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>First quarter</td></tr>
<tr><td>2</td><td>=</td><td>Second quarter</td></tr>
<tr><td>3</td><td>=</td><td>Third quarter</td></tr>
<tr><td>4</td><td>=</td><td>Fourth quarter</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Month</td><td>C</td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>January</td></tr>
<tr><td>2</td><td>=</td><td>February</td></tr>
<tr><td>3</td><td>=</td><td>March</td></tr>
<tr><td>4</td><td>=</td><td>April</td></tr>
<tr><td>5</td><td>=</td><td>May</td></tr>
<tr><td>6</td><td>=</td><td>June</td></tr>
<tr><td>7</td><td>=</td><td>July</td></tr>
<tr><td>8</td><td>=</td><td>August</td></tr>
<tr><td>9</td><td>=</td><td>September</td></tr>
<tr><td>10</td><td>=</td><td>October</td></tr>
<tr><td>11</td><td>=</td><td>November</td></tr>
<tr><td>12</td><td>=</td><td>December</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td colspan="2">5</td><td>REF_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘3’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Request Type in box 1a) </td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Common Risk Assessment Criteria flag</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>0</td><td>=</td><td>No or False</td></tr>
<tr><td>1</td><td>=</td><td>Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">5.1</td><td>LIST OF CODES Code</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Requested List of Code</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Units of measure</td></tr>
<tr><td>2</td><td>=</td><td>Events types</td></tr>
<tr><td>3</td><td>=</td><td>Evidence types</td></tr>
<tr><td>4</td><td>=</td><td>(reserved)</td></tr>
<tr><td>5</td><td>=</td><td>(reserved)</td></tr>
<tr><td>6</td><td>=</td><td>Language codes</td></tr>
<tr><td>7</td><td>=</td><td>Member states</td></tr>
<tr><td>8</td><td>=</td><td>Country codes</td></tr>
<tr><td>9</td><td>=</td><td>Packaging codes</td></tr>
<tr><td>10</td><td>=</td><td>Reasons for unsatisfactory receipt or control report</td></tr>
<tr><td>11</td><td>=</td><td>Reasons for interruption</td></tr>
<tr><td>12</td><td>=</td><td>(reserved)</td></tr>
<tr><td>13</td><td>=</td><td>Transport modes</td></tr>
<tr><td>14</td><td>=</td><td>Transport units</td></tr>
<tr><td>15</td><td>=</td><td>Wine-growing zones</td></tr>
<tr><td>16</td><td>=</td><td>Wine operation codes</td></tr>
<tr><td>17</td><td>=</td><td>Excise product categories</td></tr>
<tr><td>18</td><td>=</td><td>Excise products</td></tr>
<tr><td>19</td><td>=</td><td>CN codes</td></tr>
<tr><td>20</td><td>=</td><td>Correspondences CN code Excise product</td></tr>
<tr><td>21</td><td>=</td><td>Cancellation reasons</td></tr>
<tr><td>22</td><td>=</td><td>Alert or rejection of e-AD reasons</td></tr>
<tr><td>23</td><td>=</td><td>Delay explanations</td></tr>
<tr><td>24</td><td>=</td><td>(reserved)</td></tr>
<tr><td>25</td><td>=</td><td>Event submitting persons</td></tr>
<tr><td>26</td><td>=</td><td>Refusal reasons</td></tr>
<tr><td>27</td><td>=</td><td>Reasons for delayed result</td></tr>
<tr><td>28</td><td>=</td><td>Administrative cooperation actions</td></tr>
<tr><td>29</td><td>=</td><td>Administrative cooperation request reasons</td></tr>
<tr><td>30</td><td>=</td><td>(reserved)</td></tr>
<tr><td>31</td><td>=</td><td>(reserved)</td></tr>
<tr><td>32</td><td>=</td><td>(reserved)</td></tr>
<tr><td>33</td><td>=</td><td>(reserved)</td></tr>
<tr><td>34</td><td>=</td><td>Administrative cooperation action not possible reasons</td></tr>
<tr><td>35</td><td>=</td><td>Common request rejection reasons</td></tr>
<tr><td>36</td><td>=</td><td>(reserved)</td></tr>
<tr><td>37</td><td>=</td><td>Movement verification request reasons</td></tr>
<tr><td>38</td><td>=</td><td>Movement verification actions</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
</tbody>
</table>

**Table 2**

**Operations on the register of economic operators**

**(referred to in Article 3(3), Article 4(2) and (3) and Article 6(3))**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Message Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Update of economic operators (Notification of changes to CD/RD)</td></tr>
<tr><td>2</td><td>=</td><td>Dissemination of updates of economic operators</td></tr>
<tr><td>3</td><td>=</td><td>Retrieval of economic operators</td></tr>
<tr><td>4</td><td>=</td><td>Extraction of economic operators</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Request Correlation Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Message Type&gt; is ‘3’ or ‘4’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Message Type in box 1a) </td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State</td><td>an..44</td></tr>
<tr><td colspan="2">2</td><td>TRADER AUTHORISATION</td><td>O</td><td></td><td></td><td>999999x</td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>R</td><td></td><td>(See Code list 1 in Annex II) The &lt;Trader Excise Number&gt; must be unique in the list of &lt;TRADER AUTHORISATION&gt;. </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>VAT Number</td><td>O</td><td></td><td></td><td>an..14</td></tr>
<tr><td></td><td>c</td><td>Authorisation Start Date</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>d</td><td>Authorisation End Date</td><td>O</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>e</td><td>Operator Type Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Authorised warehouse keeper</td></tr>
<tr><td>2</td><td>=</td><td>Registered consignee</td></tr>
<tr><td>3</td><td>=</td><td>Registered consignor</td></tr>
</tbody>
</table>
 The value of the &lt;Operator Type Code&gt; data item cannot be changed after the creation of the TRADER AUTHORISATION </td><td>n1</td></tr>
<tr><td></td><td>f</td><td>Excise Office Reference Number</td><td>R</td><td></td><td>(see Code list 5 in Annex II to Regulation (EC) No 684/2009)</td><td>an8</td></tr>
<tr><td colspan="2">2.1</td><td>ACTION</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Operation</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>C</td><td>=</td><td>Create</td></tr>
<tr><td>U</td><td>=</td><td>Update</td></tr>
<tr><td>I</td><td>=</td><td>Invalidate</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>b</td><td>Activation Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Operation&gt; is ‘C’ or ‘U’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Operation in box 2.1a) </td><td>If &lt;Activation Date&gt; is not entered the Activation Date of the Invalidate operation is considered to be the date that the Invalidate operation is incorporated into the central register.</td><td>date</td></tr>
<tr><td></td><td>c</td><td>Responsible Data Manager</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td colspan="2">2.2</td><td>NAME AND ADDRESS</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>b</td><td>NAD_LNG</td><td>R</td><td></td><td>(see Code list 1 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">2.2.1</td><td>ADDRESS</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>b</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>c</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>d</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>e</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">2.3</td><td>OPERATOR ROLE Code</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Operator Role Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Allowed to practise direct delivery</td></tr>
<tr><td>2</td><td>=</td><td>Allowed to leave empty the destination fields according to Article 22 of Directive 2008/118/EC.</td></tr>
</tbody>
</table>
 The couplings &lt;Operator Type / Operator Role Code&gt; are as follows: <table><tbody><tr><td>OP/OR TYPE / OP/OR ROLE</td><td>AUTH. WH KEEPER</td><td>REG. CON/EE</td><td>REG. CON/OR</td></tr>
<tr><td>Allowed to practise direct delivery</td><td>X</td><td>X</td><td></td></tr>
<tr><td>Allowed to leave empty the destination fields according to Article 22 of Directive 2008/118/EC</td><td>X</td><td></td><td>X</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">2.4</td><td>EXCISE PRODUCTS CATEGORY Code</td><td>C</td><td>At least one of the &lt;EXCISE PRODUCTS CATEGORY code&gt; or &lt;EXCISE PRODUCT code&gt; data groups must be present</td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Excise Products Category Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II) The &lt;Excise Products Category Code&gt; must be unique in the list of &lt;EXCISE PRODUCTS CATEGORY Code&gt; inside the same &lt;TRADER AUTHORISATION&gt; or &lt;TAX WAREHOUSE&gt; </td><td>a1</td></tr>
<tr><td colspan="2">2.5</td><td>EXCISE PRODUCT Code</td><td>C</td><td>At least one of the &lt;EXCISE PRODUCTS CATEGORY code&gt; or &lt;EXCISE PRODUCT code&gt; data groups must be present</td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Code</td><td>R</td><td></td><td>(see Code list 11 in Annex II to Regulation (EC) No 684/2009) The &lt;Excise Products Category Code&gt; of the &lt;Excise Product Code&gt; must not exist inside the same &lt;TRADER AUTHORISATION&gt; or &lt;TAX WAREHOUSE&gt;  The &lt;Excise Product Code&gt; must be unique in the list of &lt;EXCISE PRODUCT Code&gt; inside the same &lt;TRADER AUTHORISATION&gt;, &lt;TAX WAREHOUSE&gt;, or &lt;TEMPORARY AUTHORISATION&gt; </td><td>an..4</td></tr>
<tr><td colspan="2">2.6</td><td>(USING) TAX WAREHOUSE</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Operator Type Code&gt; is ‘Authorised warehouse keeper’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise</td></tr>
</tbody>
</table>
 (see Operator Type Code in box 2e) </td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Tax Warehouse Reference</td><td>R</td><td></td><td>(see Code list 1in Annex II) The “Tax Warehouse Reference” shall be one of the &lt;TAX WAREHOUSE. Tax Warehouse Reference&gt; such that there exists at least one Active version having its Validity Interval intersecting the Validity Interval of the &lt;TRADER AUTHORISATION&gt;, after the Activation Date of the latter, by at least one day  The &lt;Tax Warehouse Reference&gt; must be unique in the list of &lt;TAX WAREHOUSE&gt;. </td><td>an13</td></tr>
<tr><td colspan="2">3</td><td>TAX WAREHOUSE</td><td>O</td><td></td><td></td><td>999999x</td></tr>
<tr><td></td><td>a</td><td>Tax Warehouse Reference</td><td>R</td><td></td><td>(see Code list 1 in Annex II) The &lt;Tax Warehouse Reference&gt; must be unique in the list of &lt;TAX WAREHOUSE&gt;.  The “Tax Warehouse Reference” shall be the same as one of the &lt;(USING) TAX WAREHOUSE. Tax Warehouse Reference&gt; within one or more &lt;TRADER AUTHORISATION&gt; data groups of “Authorised Warehouse Keeper” type satisfying also Rule204 </td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Validity Begin Date</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>c</td><td>Validity End Date</td><td>O</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>d</td><td>Excise Office Reference Number</td><td>R</td><td></td><td>(see Code list 5 in Annex II to Regulation (EC) No 684/2009)</td><td>an8</td></tr>
<tr><td colspan="2">3.1</td><td>ACTION</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Operation</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>C</td><td>=</td><td>Create</td></tr>
<tr><td>U</td><td>=</td><td>Update</td></tr>
<tr><td>I</td><td>=</td><td>Invalidate</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>b</td><td>Activation Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Operation&gt; is ‘C’ or ‘U’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Operation in box 3.1a) </td><td>If &lt;Activation Date&gt; is not entered the Activation Date of the Invalidate operation is considered to be the date that the Invalidate operation is incorporated into the central register.</td><td>date</td></tr>
<tr><td></td><td>c</td><td>Responsible Data Manager</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td colspan="2">3.2</td><td>NAME AND ADDRESS</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>b</td><td>NAD_LNG</td><td>R</td><td></td><td>(see Code list 1 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">3.2.1</td><td>ADDRESS</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>b</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>c</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>d</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>e</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">3.4</td><td>EXCISE PRODUCTS CATEGORY Code</td><td>C</td><td>At least one of the &lt;EXCISE PRODUCTS CATEGORY code&gt; or &lt;EXCISE PRODUCT code&gt; data groups must be present</td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Excise Products Category Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II) The &lt;Excise Products Category Code&gt; must be unique in the list of &lt;EXCISE PRODUCTS CATEGORY Code&gt; inside the same &lt;TRADER AUTHORISATION&gt; or &lt;TAX WAREHOUSE&gt; </td><td>an1</td></tr>
<tr><td colspan="2">3.5</td><td>EXCISE PRODUCT Code</td><td>C</td><td>At least one of the &lt;EXCISE PRODUCTS CATEGORY code&gt; or &lt;EXCISE PRODUCT code&gt; data groups must be present</td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Code</td><td>R</td><td></td><td>(see Code list 11 in Annex II to Regulation (EC) No 684/2009) The &lt;Excise Products Category Code&gt; of the &lt;Excise Product Code&gt; must not exist inside the same &lt;TRADER AUTHORISATION&gt; or &lt;TAX WAREHOUSE&gt;  The &lt;Excise Product Code&gt; must be unique in the list of &lt;EXCISE PRODUCT Code&gt; inside the same &lt;TRADER AUTHORISATION&gt;, &lt;TAX WAREHOUSE&gt;, or &lt;TEMPORARY AUTHORISATION&gt; </td><td>an..4</td></tr>
<tr><td colspan="2">4</td><td>TEMPORARY AUTHORISATION</td><td>O</td><td></td><td></td><td>999999x</td></tr>
<tr><td></td><td>a</td><td>Temporary Authorisation Reference</td><td>R</td><td></td><td>(see Code list 2 in Annex II)</td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Office Reference Number of Issuance</td><td>R</td><td></td><td>(see Code list 5 in Annex II to Regulation (EC) No 684/2009)</td><td>an8</td></tr>
<tr><td></td><td>c</td><td>Date of Expiry</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>d</td><td>Re-usable Temporary Authorisation flag</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>0</td><td>=</td><td>No or False</td></tr>
<tr><td>1</td><td>=</td><td>Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>e</td><td>VAT Number</td><td>O</td><td></td><td></td><td>an..14</td></tr>
<tr><td></td><td>f</td><td>Authorisation Start Date</td><td>R</td><td></td><td></td><td>date</td></tr>
<tr><td></td><td>g</td><td>Small Wine Producer flag</td><td>O</td><td></td><td>The possible values are:<table><tbody><tr><td>0</td><td>=</td><td>No or False</td></tr>
<tr><td>1</td><td>=</td><td>Yes or True</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td colspan="2">4.1</td><td>ACTION</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Operation</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>C</td><td>=</td><td>Create</td></tr>
<tr><td>U</td><td>=</td><td>Update</td></tr>
<tr><td>I</td><td>=</td><td>Invalidate</td></tr>
</tbody>
</table>
</td><td>a1</td></tr>
<tr><td></td><td>b</td><td>Activation Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Operation&gt; is ‘C’ or ‘U’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
 (see Operation in box 4.1a) </td><td>If &lt;Activation Date&gt; is not entered the Activation Date of the Invalidate operation is considered to be the date that the Invalidate operation is incorporated into the central register.</td><td>date</td></tr>
<tr><td></td><td>c</td><td>Responsible Data Manager</td><td>O</td><td></td><td></td><td>an..35</td></tr>
<tr><td colspan="2">4.2</td><td>TRADER Consignor</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Trader Excise Number</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Temporary Authorisation – Small Wine Producer flag&gt; is not present or is False</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘O’ otherwise</td></tr>
</tbody>
</table>
</td><td>For TRADER Consignor An existing identifier &lt;Trader Excise Number&gt; in the set of &lt;TRADER AUTHORISATION&gt;  The &lt;Operator Type Code&gt; of the referred &lt;TRADER&gt; must be: <table><tbody><tr><td>—</td><td>“Authorised warehouse keeper”; OR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Registered consignor”</td></tr>
</tbody>
</table>
</td><td>an13</td></tr>
<tr><td></td><td>b</td><td>Trader Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>c</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>d</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>e</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>f</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>g</td><td>NAD_LNG</td><td>R</td><td></td><td>(see Code list 1 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">4.3</td><td>TEMPORARY AUTHORISATION DETAILS</td><td>R</td><td></td><td></td><td>999x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Code</td><td>R</td><td></td><td>(see Code list 11 in Annex II to Regulation (EC) No 684/2009) The &lt;Excise Product Code&gt; must be unique in the list of &lt;EXCISE PRODUCT Code&gt; inside the same &lt;TRADER AUTHORISATION&gt;, &lt;TAX WAREHOUSE&gt;, or &lt;TEMPORARY AUTHORISATION&gt;  If &lt;Temporary Authorisation – Small Wine Producer&gt; is present and is True THEN the  &lt;Excise Product Code&gt; must be either: <table><tbody><tr><td>—</td><td>“W200”; OR</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“W300”</td></tr>
</tbody>
</table>
</td><td>an..4</td></tr>
<tr><td></td><td>b</td><td>Quantity</td><td>R</td><td></td><td></td><td>n..15,3</td></tr>
<tr><td colspan="2">4.4</td><td>NAME AND ADDRESS</td><td>R</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Name</td><td>R</td><td></td><td></td><td>an..182</td></tr>
<tr><td></td><td>b</td><td>NAD_LNG</td><td>R</td><td></td><td>(see Annex II, Code list 1 of Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td colspan="2">4.4.1</td><td>ADDRESS</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Street Name</td><td>R</td><td></td><td></td><td>an..65</td></tr>
<tr><td></td><td>b</td><td>Street Number</td><td>O</td><td></td><td></td><td>an..11</td></tr>
<tr><td></td><td>c</td><td>Postcode</td><td>R</td><td></td><td></td><td>an..10</td></tr>
<tr><td></td><td>d</td><td>City</td><td>R</td><td></td><td></td><td>an..50</td></tr>
<tr><td></td><td>e</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2’</td></tr>
</tbody>
</table>

(2) Table 4 is replaced by the following:

**‘Table 4**

**SEED statistics**

**(referred to in Article 7(2))**

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Correlation Identifier</td><td>R</td><td></td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>an..44</td></tr>
<tr><td colspan="2">2</td><td>STA_PERIOD</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Year</td><td>R</td><td></td><td></td><td>n4</td></tr>
<tr><td></td><td>b</td><td>Semester</td><td>C</td><td rowspan="3">For 2 b, c, and d: The three following data fields are optional and exclusive: <table><tbody><tr><td>—</td><td>&lt;Semester&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Quarter&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Month&gt;</td></tr>
</tbody>
</table>
 i.e. If one of these data fields is given then the two other data fields do not apply </td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>First semester</td></tr>
<tr><td>2</td><td>=</td><td>Second semester</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>c</td><td>Quarter</td><td>C</td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>First quarter</td></tr>
<tr><td>2</td><td>=</td><td>Second quarter</td></tr>
<tr><td>3</td><td>=</td><td>Third quarter</td></tr>
<tr><td>4</td><td>=</td><td>Fourth quarter</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>d</td><td>Month</td><td>C</td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>January</td></tr>
<tr><td>2</td><td>=</td><td>February</td></tr>
<tr><td>3</td><td>=</td><td>March</td></tr>
<tr><td>4</td><td>=</td><td>April</td></tr>
<tr><td>5</td><td>=</td><td>May</td></tr>
<tr><td>6</td><td>=</td><td>June</td></tr>
<tr><td>7</td><td>=</td><td>July</td></tr>
<tr><td>8</td><td>=</td><td>August</td></tr>
<tr><td>9</td><td>=</td><td>September</td></tr>
<tr><td>10</td><td>=</td><td>October</td></tr>
<tr><td>11</td><td>=</td><td>November</td></tr>
<tr><td>12</td><td>=</td><td>December</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
<tr><td colspan="2">3</td><td>STA_PER_MS</td><td>O</td><td></td><td></td><td>99x</td></tr>
<tr><td></td><td>a</td><td>Member State Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II to Regulation (EC) No 684/2009)</td><td>a2</td></tr>
<tr><td></td><td>b</td><td>Number of Active Economic Operators</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>c</td><td>Number of Inactive Economic Operators</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>d</td><td>Number of Pending Expirations</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>e</td><td>Number of Tax Warehouses</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>f</td><td>Number of Excise Authorisation Changes</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">3.1</td><td>OPERATOR_TYPE</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Operator Type Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Authorised warehouse keeper</td></tr>
<tr><td>2</td><td>=</td><td>Registered consignee</td></tr>
<tr><td>3</td><td>=</td><td>Registered consignor</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">3.2</td><td>EXCISE_PRODUCT_ CATEGORY_ACTIVITY</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Excise Products Category Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II)</td><td>a1</td></tr>
<tr><td></td><td>b</td><td>Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">3.3</td><td>EXCISE_PRODUCT_ ACTIVITY</td><td>O</td><td></td><td></td><td>9999x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Code</td><td>R</td><td></td><td>(see Code list 11 in Annex II to Regulation (EC) No 684/2009)</td><td>an..4</td></tr>
<tr><td></td><td>b</td><td>Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">4</td><td>STA_ALL_MS</td><td>O</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Total Number of Active Economic Operators</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>b</td><td>Total Number of Inactive Economic Operators</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>c</td><td>Total Number of Pending Expirations</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>d</td><td>Total Number of Tax Warehouses</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td></td><td>e</td><td>Total Number of Excise Authorisation Changes</td><td>O</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">4.1</td><td>OPERATOR_TYPE_ALL_MS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Operator Type Code</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>Authorised warehouse keeper</td></tr>
<tr><td>2</td><td>=</td><td>Registered consignee</td></tr>
<tr><td>3</td><td>=</td><td>Registered consignor</td></tr>
</tbody>
</table>
</td><td>n1</td></tr>
<tr><td></td><td>b</td><td>Total Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">4.2</td><td>EXCISE_PRODUCT_ CATEGORY_ACTIVITY_ ALL_MS</td><td>O</td><td></td><td></td><td>9x</td></tr>
<tr><td></td><td>a</td><td>Excise Products Category Code</td><td>R</td><td></td><td>(see Code list 3 in Annex II)</td><td>a1</td></tr>
<tr><td></td><td>b</td><td>Total Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15</td></tr>
<tr><td colspan="2">4.3</td><td>EXCISE_PRODUCT_ ACTIVITY_ALL_MS</td><td>O</td><td></td><td></td><td>9999x</td></tr>
<tr><td></td><td>a</td><td>Excise Product Code</td><td>R</td><td></td><td>(see Code list 11 in Annex II to Regulation (EC) No 684/2009)</td><td>an..4</td></tr>
<tr><td></td><td>b</td><td>Total Number of Economic Operators</td><td>R</td><td></td><td></td><td>n..15’</td></tr>
</tbody>
</table>
