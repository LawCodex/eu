---
title: "Commission Implementing Regulation (EU) 2019/2221 of 12 December 2019 amending Implementing Regulation (EU) No 612/2013 as regards the data registered in messages relating to the registration of economic operators and tax warehouses in the national registers and the Central Register"
identifier: "32019R2221"
eli: "http://data.europa.eu/eli/reg_impl/2019/2221/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2019-12-12
entry_into_force: 2020-01-16
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019R2221"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2019/2221 of 12 December 2019 amending Implementing Regulation (EU) No 612/2013 as regards the data registered in messages relating to the registration of economic operators and tax warehouses in the national registers and the Central Register

**COMMISSION IMPLEMENTING REGULATION (EU) 2019/2221**

**of 12 December 2019**

**amending Implementing Regulation (EU) No 612/2013 as regards the data registered in messages relating to the registration of economic operators and tax warehouses in the national registers and the Central Register**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Council Regulation (EU) No 389/2012 of 2 May 2012 on administrative cooperation in the field of excise duties and repealing Regulation (EC) No 2073/2004 (1), and in particular Article 22 thereof,

Whereas:

(1) Annex I to Commission Implementing Regulation (EU) No 612/2013 (2) lays down the structure and content of messages relating to the registration of economic operators and tax warehouses in the national registers and the Central Register.

(2) In order to achieve consistency between the structure of common request messages defined in Implementing Regulation (EU) No 612/2013 and in Commission Implementing Regulation (EU) 2016/323 (3), the possible values for the ‘Request Type’ data item should be modified in Table 1 of Annex I to Implementing Regulation (EU) No 612/2013 taking into account changes in the data requirements of a new version of the computerised system established by Decision No 1152/2003/EC of the European Parliament and of the Council (4).

(3) The explanation in column F in Table 1 of Annex I to Implementing Regulation (EU) No 612/2013 should be updated to provide a clear identification of the ‘Value’ data element when the ‘Primary Criterion’ type code is set to the value ‘46 = Type of Transport’.

(4) There is a need for further technical corrections of Table 1 of Annex I to Implementing Regulation (EU) No 612/2013 in order to bring clarity and precision to the applicable provisions.

(5) Implementing Regulation (EU) No 612/2013 should therefore be amended accordingly.

(6) In order to align the application date of this Regulation with the application date for a new version of the computerised system established by Decision No 1152/2003/EC, this Regulation should apply from 13 February 2020.

(7) The measures provided for in this Regulation are in accordance with the opinion of the Committee on Excise Duty,

HAS ADOPTED THIS REGULATION:

## Article 1

Annex I to Implementing Regulation (EU) No 612/2013 is amended in accordance with the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

It shall apply from 13 February 2020.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 12 December 2019.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 121, 8.5.2012, p. 1.

(2) Commission Implementing Regulation (EU) No 612/2013 of 25 June 2013 on the operation of the register of economic operators and tax warehouses, related statistics and reporting pursuant to Council Regulation (EU) No 389/2012 on administrative cooperation in the field of excise duties (OJ L 173, 26.6.2013, p. 9).

(3) Commission Implementing Regulation (EU) 2016/323 of 24 February 2016 laying down detailed rules on cooperation and exchange of information between Member States regarding goods under excise duty suspension pursuant to Council Regulation (EU) No 389/2012 (OJ L 66, 11.3.2016, p. 1).

(4) Decision No 1152/2003/EC of the European Parliament and of the Council of 16 June 2003 on computerising the movement and surveillance of excisable products (OJ L 162, 1.7.2003, p. 5).

## ANNEX

In Annex I to Regulation (EU) No 612/2013, Table 1 is replaced by the following:

(referred to in Article 4(5), Article 7(2) and Article 8(2))

<table>
<tbody><tr><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr>
<tr><td colspan="2">1</td><td>ATTRIBUTES</td><td>R</td><td></td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Request Type</td><td>R</td><td></td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>(reserved)</td></tr>
<tr><td>2</td><td>=</td><td>Request for reference data</td></tr>
<tr><td>3</td><td>=</td><td>(reserved)</td></tr>
<tr><td>4</td><td>=</td><td>(reserved)</td></tr>
<tr><td>5</td><td>=</td><td>Request for re-synchronisation of the register of economic operators</td></tr>
<tr><td>6</td><td>=</td><td>Request for retrieval of a list of e-ADs</td></tr>
<tr><td>7</td><td>=</td><td>Request for SEED statistics</td></tr>
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
<tr><td></td><td>c</td><td>Requesting Office</td><td>R</td><td></td><td>(see Code list 5 in Annex II to Regulation (EC) No 684/2009)</td><td>an8</td></tr>
<tr><td></td><td>d</td><td>Request Correlation Identifier</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’, ‘5’, ‘6’ or ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td>The value of &lt;Request Correlation Identifier&gt; is unique per Member State.</td><td>an..44</td></tr>
<tr><td></td><td>e</td><td>Start Date</td><td>C</td><td rowspan="2">For 1 e and f:<table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td>date</td></tr>
<tr><td></td><td>f</td><td>End Date</td><td>C</td><td></td><td>date</td></tr>
<tr><td></td><td>g</td><td>Single Date</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’ or ‘5’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td>date</td></tr>
<tr><td colspan="2">2</td><td>E-AD LIST REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘6’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td></td></tr>
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
<tr><td></td><td>a</td><td>Value</td><td>R</td><td></td><td>If &lt;Primary Criterion Type Code&gt; is ‘46’ (Type of transport), then an existing &lt;Transport Mode Code&gt; in the list of &lt;TRANSPORT MODES&gt; shall be used.</td><td>an..255</td></tr>
<tr><td colspan="2">3</td><td>STA_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td></td></tr>
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
<tr><td colspan="2">4</td><td>STA_PERIOD</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘7’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td></td></tr>
<tr><td></td><td>a</td><td>Year</td><td>R</td><td></td><td></td><td>n4</td></tr>
<tr><td></td><td>b</td><td>Semester</td><td>C</td><td rowspan="3">For 4 b, c, and d: The three following data fields are optional and exclusive: <table><tbody><tr><td>—</td><td>&lt;Semester&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Quarter&gt;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>&lt;Month&gt; i.e. If one of these data fields is given then the two other data fields do not apply </td></tr>
</tbody>
</table>
</td><td>The possible values are:<table><tbody><tr><td>1</td><td>=</td><td>First semester</td></tr>
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
<tr><td colspan="2">5</td><td>REF_REQUEST</td><td>C</td><td><table><tbody><tr><td>—</td><td>‘R’ if &lt;Request Type&gt; is ‘2’</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Does not apply otherwise (see Request Type in box 1a) </td></tr>
</tbody>
</table>
</td><td></td><td></td></tr>
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
<tr><td>7</td><td>=</td><td>Member States</td></tr>
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
<tr><td>28</td><td>=</td><td>Request actions</td></tr>
<tr><td>29</td><td>=</td><td>Request reasons</td></tr>
<tr><td>30</td><td>=</td><td>(reserved)</td></tr>
<tr><td>31</td><td>=</td><td>(reserved)</td></tr>
<tr><td>32</td><td>=</td><td>(reserved)</td></tr>
<tr><td>33</td><td>=</td><td>(reserved)</td></tr>
<tr><td>34</td><td>=</td><td>Administrative cooperation action not possible reasons</td></tr>
<tr><td>35</td><td>=</td><td>(reserved)</td></tr>
<tr><td>36</td><td>=</td><td>Type of document</td></tr>
<tr><td>37</td><td>=</td><td>(reserved)</td></tr>
<tr><td>38</td><td>=</td><td>(reserved)</td></tr>
<tr><td>39</td><td>=</td><td>Manual Closure Request Reasons</td></tr>
<tr><td>40</td><td>=</td><td>Manual Closure Rejection Reasons’</td></tr>
</tbody>
</table>
</td><td>n..2</td></tr>
</tbody>
</table>
