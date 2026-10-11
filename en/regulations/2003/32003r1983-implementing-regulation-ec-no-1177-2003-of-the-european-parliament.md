---
title: "Commission Regulation (EC) No 1983/2003 of 7 November 2003 implementing Regulation (EC) No 1177/2003 of the European Parliament and of the Council concerning Community statistics on income and living conditions (EU-SILC) as regards the list of target primary variables (Text with EEA relevance.)"
identifier: "32003R1983"
eli: "http://data.europa.eu/eli/reg/2003/1983/oj"
type: regulation
jurisdiction: eu
language: en
date: 2003-11-07
entry_into_force: 2004-01-01
last_amended: 2015-12-25
consolidated_version: "02003R1983-20151225"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02003R1983-20151225"
retrieved: 2026-10-11
---

# Commission Regulation (EC) No 1983/2003 of 7 November 2003 implementing Regulation (EC) No 1177/2003 of the European Parliament and of the Council concerning Community statistics on income and living conditions (EU-SILC) as regards the list of target primary variables (Text with EEA relevance.)

**COMMISSION REGULATION (EC) No 1983/2003**

**of 7 November 2003**

**implementing Regulation (EC) No 1177/2003 of the European Parliament and of the Council concerning Community statistics on income and living conditions (EU-SILC) as regards the list of target primary variables**

**(Text with EEA relevance)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION REGULATION (EC) No 973/2007 of 20 August 2007 </td><td> L 216</td><td>10</td><td>21.8.2007</td></tr>
<tr><td></td><td> COMMISSION REGULATION (EU) No 317/2013 of 8 April 2013 </td><td> L 99</td><td>1</td><td>9.4.2013</td></tr>
<tr><td></td><td> COMMISSION REGULATION (EU) 2015/2256 of 4 December 2015 </td><td> L 321</td><td>12</td><td>5.12.2015</td></tr>
</table>

**COMMISSION REGULATION (EC) No 1983/2003**

**of 7 November 2003**

**implementing Regulation (EC) No 1177/2003 of the European Parliament and of the Council concerning Community statistics on income and living conditions (EU-SILC) as regards the list of target primary variables**

**(Text with EEA relevance)**

## Article 1

The list of target primary variables, the variables codes and the technical format of data transmission for the main operation of the Community statistics on income and living conditions (EU-SILC), shall be as laid down in the Annex.

## Article 2

This Regulation shall enter into force on the 20th day following its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

## ANNEX

<table>
<tbody><tr><td>Component</td><td>Variable name</td><td>Code</td><td>Target variable</td></tr>
<tr><td colspan="4">Household register</td></tr>
transformed by post treatment<tr><td>Basic data</td></tr>
<tr><td colspan="4">BASIC HOUSEHOLD DATA, INCLUDING DEGREE OF URBANISATION</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB010</td><td>  </td><td>Year of the survey</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB020</td><td>  </td><td>Country</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB030</td><td>  </td><td>Household ID</td></tr>
<tr><td>ID number</td><td>Household identification number (HID)</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB040</td><td>  </td><td>Region</td></tr>
<tr><td>NUTS 2 code(1)</td><td>NUTS</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB040_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB050</td><td>  </td><td>Primary strata as used in the selection of the sample(2)</td></tr>
<tr><td>0001 — 9999</td><td>Primary strata</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB050_F</td><td>-2</td><td>na</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB060</td><td>  </td><td>PSU-1 (first stage) as used in the selection of the sample(2)</td></tr>
<tr><td>0001 — 9999</td><td>PSU</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB060_F</td><td>-2</td><td>na</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB062</td><td>  </td><td>PSU-2 (second stage) as used in the selection of the sample(2)</td></tr>
<tr><td>0001 — 9999</td><td>PSU</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB062_F</td><td>-2</td><td>na</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB070</td><td>  </td><td>Order of the selection of PSU as used in the selection of the sample(2)</td></tr>
<tr><td>0001 — 9999</td><td>Order of the selection of PSU</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB070_F</td><td>-2</td><td>na</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB075</td><td>  </td><td>Rotational group</td></tr>
<tr><td>1 — 8</td><td>To which sub-sample belongs</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB075_F</td><td>-2</td><td>na (no rotational design is used)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB080</td><td>  </td><td>Household design weight</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">DB080_F</td><td>-2 (L)</td><td>only longitudinal: na (household not first time in survey or split off household)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">DB090</td><td>  </td><td>Household cross-sectional weight</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td>  </td><td>DB090_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">DB100</td><td>  </td><td>Degree of urbanisation</td></tr>
<tr><td>1</td><td>Densely populated area</td></tr>
<tr><td>2</td><td>Intermediate area</td></tr>
<tr><td>3</td><td>Thinly populated area</td></tr>
<tr><td>  </td><td>DB100_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="16">L</td><td rowspan="16">DB110</td><td>  </td><td>Household status</td></tr>
<tr><td>  </td><td>Household from previous wave</td></tr>
<tr><td>1</td><td>At the same address as last interview</td></tr>
<tr><td>2</td><td>Entire household moved to a private household within the country</td></tr>
<tr><td>  </td><td>Household no longer in-scope</td></tr>
<tr><td>3</td><td>Entire household moved to a collective household or institution within the country</td></tr>
<tr><td>4</td><td>Household moved outside the country</td></tr>
<tr><td>5</td><td>Entire household died</td></tr>
<tr><td>6</td><td>Household does not contain sample person</td></tr>
<tr><td>  </td><td>Address non-contacted</td></tr>
<tr><td>7</td><td>Address not contacted (unable to access or lost, i.e. no record of what happened to the household)</td></tr>
<tr><td>  </td><td>New household for this wave</td></tr>
<tr><td>8</td><td>Split-off household</td></tr>
<tr><td>9</td><td>New address added to the sample this wave or first wave</td></tr>
<tr><td>  </td><td>Fusion</td></tr>
<tr><td>10</td><td>Fusion</td></tr>
<tr><td>  </td><td>DB110_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="6">X,L</td><td rowspan="6">DB120</td><td>  </td><td>Record of contact at address</td></tr>
<tr><td>11</td><td>Address contacted</td></tr>
<tr><td>  </td><td>Address non-contacted</td></tr>
<tr><td>21</td><td>Address cannot be located</td></tr>
<tr><td>22</td><td>Address unable to access</td></tr>
<tr><td>23</td><td>Address does not exist or is non-residential address or is unoccupied or not principal residence</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">DB120_F</td><td>-2 (L)</td><td>Only longitudinal: na (DB110 not = 2, 8 or 9)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="7">X,L</td><td rowspan="7">DB130</td><td>  </td><td>Household questionnaire result</td></tr>
<tr><td>11</td><td>Household questionnaire completed</td></tr>
<tr><td>  </td><td>Interview not completed</td></tr>
<tr><td>21</td><td>Refusal to cooperate</td></tr>
<tr><td>22</td><td>Entire household temporarily away for duration of fieldwork</td></tr>
<tr><td>23</td><td>Household unable to respond (illness, incapacity, etc.)</td></tr>
<tr><td>24</td><td>Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">DB130_F</td><td>-2</td><td>na (DB120 not = 11 and DB110 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">DB135</td><td>  </td><td>Household interview acceptance</td></tr>
<tr><td>1</td><td>Interview accepted for database</td></tr>
<tr><td>2</td><td>Rejected (because no personal interview completed)</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">DB135_F</td><td>-2</td><td>na (DB130 not = 11)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Personal register</td></tr>
transformed by post treatment<tr><td>Basic data</td></tr>
<tr><td colspan="4">BASIC PERSONAL DATA</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB010</td><td>  </td><td>Year of the survey</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB020</td><td>  </td><td>Country</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB030</td><td>  </td><td>Personal ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID)</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB040</td><td>  </td><td>Current household ID</td></tr>
<tr><td>ID number</td><td>Household identification number (HID)</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RB050</td><td>  </td><td>Personal cross-sectional weight</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td>  </td><td>RB050_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB060</td><td>  </td><td>Personal base weight</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td>  </td><td>RB060_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">L</td><td rowspan="3">RB100</td><td>  </td><td>Sample person or co-resident</td></tr>
<tr><td>1</td><td>Sample person</td></tr>
<tr><td>2</td><td>Co-resident</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB100_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">DEMOGRAPHIC DATA</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB070</td><td>  </td><td>Month of birth</td></tr>
<tr><td>1 — 12</td><td>Month of birth</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB070_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB080</td><td>  </td><td>Year of birth</td></tr>
<tr><td>1890 — year of survey</td><td>Year of birth</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB080_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">RB090</td><td>  </td><td>Sex</td></tr>
<tr><td>1</td><td>Male</td></tr>
<tr><td>2</td><td>Female</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB090_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="10">L</td><td rowspan="10">RB110</td><td>  </td><td>Membership status</td></tr>
<tr><td>  </td><td>For current household members</td></tr>
<tr><td>1</td><td>Was in this household in previous waves or current household member</td></tr>
<tr><td>2</td><td>Moved into this household from another sample household since previous wave</td></tr>
<tr><td>3</td><td>Moved into this household from outside sample since previous wave</td></tr>
<tr><td>4</td><td>Newly born into this household since last wave</td></tr>
<tr><td>  </td><td>Not current household members</td></tr>
<tr><td>5</td><td>Moved out since previous wave or last interview if not contacted in previous wave</td></tr>
<tr><td>6</td><td>Died</td></tr>
<tr><td>7</td><td>Lived in the household at least three months during the income reference period but was not recorded in the register of this household</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB110_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="5">L</td><td rowspan="5">RB120</td><td>  </td><td>To where did the person move</td></tr>
<tr><td>1</td><td>To a private household within the country</td></tr>
<tr><td>2</td><td>To a collective household or institution within the country</td></tr>
<tr><td>3</td><td>Abroad</td></tr>
<tr><td>4</td><td>Lost</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB120_F</td><td>-2</td><td>na (RB110 not = 5)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB140</td><td>  </td><td>Month when the person moved out or died</td></tr>
<tr><td>1 — 12</td><td>Month</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB140_F</td><td>-2</td><td>na (RB110 not = 5 or 6)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB150</td><td>  </td><td>Year when the person moved out or died</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB150_F</td><td>-2</td><td>na (RB110 not = 5 or 6)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB160</td><td>  </td><td>Number of months in household during the income reference period</td></tr>
<tr><td>0 — 12</td><td>Number of months</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB160_F</td><td>-2</td><td>na (RB110 not = 5 or 6 or 7)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="5">L</td><td rowspan="5">RB170</td><td>  </td><td>Main activity status during the income reference period</td></tr>
<tr><td>1</td><td>At work</td></tr>
<tr><td>2</td><td>Unemployed</td></tr>
<tr><td>3</td><td>In retirement or early retirement</td></tr>
<tr><td>4</td><td>Other inactive person</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB170_F</td><td>-2</td><td>na (RB110 not = 5 or 6 or 7)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB180</td><td>  </td><td>Month when the person moved in</td></tr>
<tr><td>1 — 12</td><td>Month</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB180_F</td><td>-2</td><td>na (RB110 not = 3)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">RB190</td><td>  </td><td>Year when the person moved in</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB190_F</td><td>-2</td><td>na (RB110 not = 3)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">RB200</td><td>  </td><td>Residential status</td></tr>
<tr><td>1</td><td>Currently living in the household</td></tr>
<tr><td>2</td><td>Temporarily absent</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB200_F</td><td>-2 (L)</td><td>Only longitudinal: na (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="5">X,L</td><td rowspan="5">RB210</td><td>  </td><td>Basic activity status</td></tr>
<tr><td>1</td><td>Working</td></tr>
<tr><td>2</td><td>Unemployed</td></tr>
<tr><td>3</td><td>In retirement or early retirement</td></tr>
<tr><td>4</td><td>Other inactive person</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB210_F</td><td>-2 (L)</td><td>Only longitudinal: na (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB220</td><td>  </td><td>Father ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of father</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB220_F</td><td>-2</td><td>na (father is not a household member) or only longitudinal: (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB230</td><td>  </td><td>Mother ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of mother</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB230_F</td><td>-2</td><td>na (mother is not a household member) or only longitudinal: (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB240</td><td>  </td><td>Spouse/partner ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of spouse/partner</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB240_F</td><td>-2</td><td>na (person has no spouse/partner or spouse/partner is not a household member) or only longitudinal: (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">BASIC PERSONAL DATA</td></tr>
<tr><td rowspan="8">X,L</td><td rowspan="8">RB245</td><td>  </td><td>Respondent status</td></tr>
<tr><td>  </td><td>All household members aged 16 and over are interviewed</td></tr>
<tr><td>1</td><td>Current households members aged 16 and over</td></tr>
<tr><td>  </td><td>Only selected household member aged 16 and over</td></tr>
<tr><td>2</td><td>Selected respondent</td></tr>
<tr><td>3</td><td>Non-selected respondent</td></tr>
<tr><td>  </td><td>Household members aged less than 16 at the end of the income reference period</td></tr>
<tr><td>4</td><td>Not eligible person</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB245_F</td><td>-2 (L)</td><td>Only longitudinal: na (RB110 not = 1 or 2 or 3 or 4)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="14">X,L</td><td rowspan="14">RB250</td><td>  </td><td>Data status</td></tr>
<tr><td>  </td><td>Information or interview completed</td></tr>
<tr><td>11</td><td>Information completed only from interview</td></tr>
<tr><td>12</td><td>Information completed only from registers</td></tr>
<tr><td>13</td><td>Information completed from both interview and registers</td></tr>
<tr><td>  </td><td>Interview not completed, though contact made</td></tr>
<tr><td>21</td><td>Individual unable to respond (illness, incapacity, etc.) and no proxy possible</td></tr>
<tr><td>22</td><td>Failed to return self-administered questionnaire</td></tr>
<tr><td>23</td><td>Refusal to cooperate</td></tr>
<tr><td>  </td><td>Individual not contacted because</td></tr>
<tr><td>31</td><td>Person temporarily away and no proxy possible</td></tr>
<tr><td>32</td><td>No contact for other reasons</td></tr>
<tr><td>  </td><td>Information not completed</td></tr>
<tr><td>33</td><td>Information not completed, reason unknown</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">RB250_F</td><td>-2</td><td>na (RB245 not = 1 or 2 or 3)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="6">X,L</td><td rowspan="6">RB260</td><td>  </td><td>Type of interview</td></tr>
<tr><td>1</td><td>Questionnaire completed (face-to-face interview-PAPI)</td></tr>
<tr><td>2</td><td>Questionnaire completed (face-to-face interview-CAPI)</td></tr>
<tr><td>3</td><td>Questionnaire completed (CATI)</td></tr>
<tr><td>4</td><td>Self-administered by respondent</td></tr>
<tr><td>5</td><td>Proxy interview</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB260_F</td><td>-2</td><td>na (RB250 not = 11 or 13)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">RB270</td><td>  </td><td>Personal ID of person who filled in the individual questionnaire</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of person who filled in the individual questionnaire</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RB270_F</td><td>-2</td><td>na (RB260 not = 5)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Personal register</td></tr>
transformed by post treatment<tr><td>Labour information</td></tr>
<tr><td colspan="4">CHILD CARE</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL010</td><td>  </td><td>Education at pre-school</td></tr>
<tr><td>0 — 99 (3)</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL010_F</td><td>-2</td><td>na (person is not admitted to pre-school because of his/her age, is at compulsory school or is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL020</td><td>  </td><td>Education at compulsory school</td></tr>
<tr><td>0 — 99 (3)</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL020_F</td><td>-2</td><td>na (person is not admitted to compulsory school because of his/her age or is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL030</td><td>  </td><td>Childcare at centre-based services outside school hours (before/after)</td></tr>
<tr><td>0 — 99</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL030_F</td><td>-2</td><td>na (person is neither at pre-school nor at school or is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL040</td><td>  </td><td>Childcare at day-care centre</td></tr>
<tr><td>0 — 99</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL040_F</td><td>-2</td><td>na (person is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL050</td><td>  </td><td>Childcare by a professional child-minder at child's home or at child-minder's home</td></tr>
<tr><td>0 — 99</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL050_F</td><td>-2</td><td>na (person is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">RL060</td><td>  </td><td>Childcare by grandparents, household members other than parents, other relatives, friends or neighbours</td></tr>
<tr><td>0 — 99</td><td>Number of hours during a usual week</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">RL060_F</td><td>-2</td><td>na (person is more than 12 years old or is a former household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Household data</td></tr>
transformed by post treatment<tr><td>Basic data</td></tr>
<tr><td colspan="4">BASIC HOUSEHOLD DATA</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB010</td><td>  </td><td>Year of the survey</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB020</td><td>  </td><td>Country</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB030</td><td>  </td><td>Household ID</td></tr>
<tr><td>ID number</td><td>Household identification number (HID)</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB040</td><td>  </td><td>Day of household interview</td></tr>
<tr><td>01 — 31</td><td>Day</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HB040_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB050</td><td>  </td><td>Month of household interview</td></tr>
<tr><td>1 — 12</td><td>Month</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HB050_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB060</td><td>  </td><td>Year of household interview</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td>  </td><td>HB060_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB070</td><td>  </td><td>Personal ID of person responding to the household questionnaire</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of person responding to the household questionnaire</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HB070_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB080</td><td>  </td><td>Personal ID of person 1 responsible for the accommodation</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of person 1 responsible for the accommodation</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HB080_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB090</td><td>  </td><td>Personal ID of person 2 responsible for the accommodation</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of person 2 responsible for the accommodation</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HB090_F</td><td>-2</td><td>na (no second responsible person)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HB100</td><td>  </td><td>Number of minutes to complete the household questionnaire</td></tr>
<tr><td>1 — 90</td><td>Number of minutes to complete the household questionnaire</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HB100_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Household data</td></tr>
transformed by post treatment<tr><td>Income</td></tr>
<tr><td colspan="4">TOTAL HOUSEHOLD INCOME (4)</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HY010</td><td>  </td><td>Total household gross income(without inflation factor)</td></tr>
<tr><td>-999999.99 — 999999.99</td><td>Total amount</td></tr>
<tr><td rowspan="11">  </td><td rowspan="11">HY010_F</td><td>-5 (5)</td><td>Not filled: no conversion to gross is done</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags(7)(8)</td><td>  </td></tr>
<tr><td>First digit</td><td>Net/Gross (at data collection)</td></tr>
<tr><td>0</td><td>No income (no second digits)</td></tr>
<tr><td>1</td><td>Net</td></tr>
<tr><td>2</td><td>Gross</td></tr>
<tr><td>3</td><td>Net and gross (part of components collected net, part gross)</td></tr>
<tr><td>4</td><td>Unknown</td></tr>
<tr><td>Following digits(9)</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HY020</td><td>  </td><td>Total disposable household income(without inflation factor)</td></tr>
<tr><td>-999999.99 — 999999.99</td><td>Total amount</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HY020_F</td><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY010_F</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HY022</td><td>  </td><td>Total disposable household income, before social transfersother thanold-age and survivors' benefits(without inflation factor)</td></tr>
<tr><td>-999999.99 — 999999.99</td><td>Total amount</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HY022_F</td><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY010_F</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HY023</td><td>  </td><td>Total disposable household income, before social transfersINCLUDINGold-age and survivors' benefits(without inflation factor)</td></tr>
<tr><td>-999999.99 — 999999.99</td><td>Total amount</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HY023_F</td><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY010_F</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HY025</td><td>  </td><td>Within-household non-response inflation factor (10)</td></tr>
<tr><td>1.00000 — 5.00000</td><td>Factor</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HY025_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Value is filled</td></tr>
<tr><td colspan="4">NET SERIES OF INCOME COMPONENTS AT HOUSEHOLD LEVEL (4)</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY030N</td><td>  </td><td>Imputed rent(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">HY030N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY040N</td><td>  </td><td>Net income from rental of a property or land</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="17">  </td><td rowspan="17">HY040N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags(12)</td><td>  </td></tr>
<tr><td>First digit</td><td>Net/Gross (at data collection)</td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>4</td><td>Gross (13)</td></tr>
<tr><td>5</td><td>Unknown</td></tr>
<tr><td>Second digit</td><td>Net (recorded)</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>5</td><td>Unknown (only possible with first digit = 5)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY050N</td><td>  </td><td>Family/children-related allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY050N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY060N</td><td>  </td><td>Social exclusion not elsewhere classified</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY060N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY070N</td><td>  </td><td>Housing allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY070N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY080N</td><td>  </td><td>Regular inter-household cash transfer received</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY080N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY090N</td><td>  </td><td>Net interest, dividends, profit from capital investments in unincorporated business</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY090N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY100N</td><td>  </td><td>Interest paid on mortgage(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY100N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY110N</td><td>  </td><td>Net income received by people aged under 16</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY110N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY120N</td><td>  </td><td>Regular taxes on wealth</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="9">  </td><td rowspan="9">HY120N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY130N</td><td>  </td><td>Regular inter-household cash transfer paid</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY130N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040N_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY140N</td><td>  </td><td>Tax on income and social insurance contributions</td></tr>
<tr><td>-999999.99 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY140N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HY145N</td><td>  </td><td>Repayments/receipts for tax adjustments</td></tr>
<tr><td>-999999.99 — -1</td><td>Receipts</td></tr>
<tr><td>1 — 999999.99</td><td>Repayments</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY145N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td colspan="4">GROSS SERIES OF INCOME COMPONENTS AT HOUSEHOLD LEVEL (4)(14)(15)</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY030G</td><td>  </td><td>Imputed rent(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">HY030G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY040G</td><td>  </td><td>Gross income from rental of a property or land</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="12">  </td><td rowspan="12">HY040G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags(12)</td><td>  </td></tr>
<tr><td>First digit</td><td>Net/Gross (at data collection)</td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>4</td><td>Gross (3)</td></tr>
<tr><td>5</td><td>Unknown</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY050G</td><td>  </td><td>Family/children-related allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY050G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY060G</td><td>  </td><td>Social exclusion not elsewhere classified</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY060G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY070G</td><td>  </td><td>Housing allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY070G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY080G</td><td>  </td><td>Regular inter-household cash transfer received</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY080G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY090G</td><td>  </td><td>Gross interest, dividends, profit from capital investments in unincorporated business</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY090G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY100G</td><td>  </td><td>Interest paid on mortgage(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY100G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY110G</td><td>  </td><td>Gross income received by people aged under 16</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY110G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY120G</td><td>  </td><td>Regular taxes on wealth</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY120G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY130G</td><td>  </td><td>Regular inter-household cash transfer paid</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HY130G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See HY040G_F</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HY140G</td><td>  </td><td>Tax on income and social insurance contributions</td></tr>
<tr><td>- 999999.99 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">HY140G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td colspan="4">Household data</td></tr>
transformed by post treatment<tr><td>Social Exclusion</td></tr>
<tr><td colspan="4">HOUSING AND NON-HOUSING RELATED ARREARS</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS010</td><td>  </td><td>Whether the household has been in arrears on mortgage or rent payments in last 12 months</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HS010_F</td><td>-2</td><td>na (outright owner or rent-free during the last 12 months)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS020</td><td>  </td><td>Whether the household has been in arrears on utility bills (electricity, water, gas) in last 12 months</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HS020_F</td><td>-2</td><td>na (no utility bills)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS030</td><td>  </td><td>Whether the household has been in arrears on hire purchase instalments or other loan payments (non housing-related debts) in last 12 months</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HS030_F</td><td>-2</td><td>na (no hire purchase instalments and no other loan payments)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">NON-MONETARY HOUSEHOLD DEPRIVATION INDICATORS, INCLUDING PROBLEMS IN MAKING ENDS MEET, EXTENT OF DEBT AND ENFORCED LACK OF BASIC NECESSITIES</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS040</td><td>  </td><td>Capacity to afford paying for one week annual holiday away from home</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS040_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS050</td><td>  </td><td>Capacity to afford a meal with meat, chicken, fish (or vegetarian equivalent) every second day</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS050_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HS060</td><td>  </td><td>Capacity to face unexpected financial expenses</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">HS060_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4"> —————</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HS090</td><td>  </td><td>Do you have a computer?</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — other reason</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">HS090_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4"> —————</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HS110</td><td>  </td><td>Do you have a car?</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — other reason</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS110_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="7">X,L</td><td rowspan="7">HS120</td><td>  </td><td>Ability to make ends meet</td></tr>
<tr><td>1</td><td>With great difficulty</td></tr>
<tr><td>2</td><td>With difficulty</td></tr>
<tr><td>3</td><td>With some difficulty</td></tr>
<tr><td>4</td><td>Fairly easily</td></tr>
<tr><td>5</td><td>Easily</td></tr>
<tr><td>6</td><td>Very easily</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS120_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HS130</td><td>  </td><td>Lowest monthly income to make ends meet(16)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS130_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HS140</td><td>  </td><td>Total housing cost is a financial burden to the household</td></tr>
<tr><td>1</td><td>A heavy burden</td></tr>
<tr><td>2</td><td>Somewhat of a burden</td></tr>
<tr><td>3</td><td>Not a burden at all</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS140_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HS150</td><td>  </td><td>Repayment of debts from hire purchases or loans other than mortgage or loan connected with the house is a financial burden to the household</td></tr>
<tr><td>1</td><td>Repayment is a heavy burden</td></tr>
<tr><td>2</td><td>Repayment is somewhat of a burden</td></tr>
<tr><td>3</td><td>Repayment is not a burden at all</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">HS150_F</td><td>-2</td><td>na (no repayment of debts)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">HD080</td><td>  </td><td>Replace worn-out furniture</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — household cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HD080_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td colspan="4">PHYSICAL AND SOCIAL ENVIRONMENT</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">HS160</td><td>  </td><td>Problems with the dwelling: too dark, not enough light</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS160_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">HS170</td><td>  </td><td>Noise from neighbours or noise from the street (traffic, business, factories, etc.)</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS170_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">HS180</td><td>  </td><td>Pollution, grime or other environmental problems in area caused by traffic or industry</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS180_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">HS190</td><td>  </td><td>Crime, violence or vandalism in the area</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HS190_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Household data</td></tr>
transformed by post treatment<tr><td>Housing</td></tr>
<tr><td colspan="4">DWELLING TYPE, TENURE STATUS AND HOUSING CONDITIONS</td></tr>
<tr><td rowspan="6">X,L</td><td rowspan="6">HH010</td><td>  </td><td>Dwelling type</td></tr>
<tr><td>1</td><td>Detached house</td></tr>
<tr><td>2</td><td>Semi-detached or terraced house</td></tr>
<tr><td>3</td><td>Apartment or flat in a building with fewer than 10 dwellings</td></tr>
<tr><td>4</td><td>Apartment or flat in a building with 10 dwellings or more</td></tr>
<tr><td>5</td><td>Some other kind of accommodation</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH010_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="5">X,L</td><td rowspan="5">HH020</td><td>  </td><td>Tenure status</td></tr>
<tr><td>1</td><td>Owner</td></tr>
<tr><td>2</td><td>Tenant or subtenant paying rent at prevailing or market rate</td></tr>
<tr><td>3</td><td>Accommodation is rented at a reduced rate (lower price than the market price)</td></tr>
<tr><td>4</td><td>Accommodation is provided rent-free</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH020_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HH030</td><td>  </td><td>Number of rooms available to household</td></tr>
<tr><td>1 — 9</td><td>Number of rooms</td></tr>
<tr><td>10</td><td>10 or more rooms</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH030_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HH031 (17)</td><td>  </td><td>Year of contract or purchase or installation</td></tr>
<tr><td>Year (4 digits)</td><td>Year of contract or purchase or installation</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HH031_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>-2</td><td>Na (Member State using objective national methods to calculate imputed rent)</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HH040</td><td>  </td><td>Leaking roof, damp walls/floors/foundation, or rot in window frames or floor</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH040_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L</td><td rowspan="3">HH050</td><td>  </td><td>Ability to keep home adequately warm</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH050_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">HOUSING COSTS (4)</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HH060</td><td>  </td><td>Current rent related to occupied dwelling, if any</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HH060_F</td><td>-2</td><td>na (HH020 not = 2 or 3)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">HH061 (18)</td><td>  </td><td>Subjective rent related to non-tenant paying rent at market price</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HH061_F</td><td>-2</td><td>na (HH020 not = 1 or 3 or 4) or Member State does not use subjective method to calculate imputed rent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">HH070</td><td>  </td><td>Total housing cost (including electricity, water, gas and heating)</td></tr>
<tr><td>0 — 999999.99</td><td>Amount</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">HH070_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">AMENITIES IN THE DWELLING</td></tr>
<tr><td rowspan="3">X,L (17)</td><td rowspan="3">HH080</td><td>  </td><td>Bath or shower in dwelling</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HH080_F</td><td>-2 (L)</td><td>na (Member State using objective national methods to calculate imputed rent)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X,L (17)</td><td rowspan="3">HH090</td><td>  </td><td>Indoor flushing toilet for sole use of household</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">HH090_F</td><td>-2 (L)</td><td>na (Member State using objective national methods to calculate imputed rent)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Basic data</td></tr>
<tr><td colspan="4">BASIC PERSONAL DATA (16 +)</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">PB010</td><td>  </td><td>Year of the survey</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">PB020</td><td>  </td><td>Country</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">X,L</td><td rowspan="2">PB030</td><td>  </td><td>Personal ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID)</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PB080</td><td>  </td><td>Personal base weight for selected respondent</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB080_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PB050</td><td>  </td><td>Personal base weight (all households members aged 16 and over)</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td>  </td><td>PB050_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB070</td><td>  </td><td>Personal design weight for selected respondent</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB070_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PB040</td><td>  </td><td>Personal cross-sectional weight (all households members aged 16 and over)</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td>  </td><td>PB040_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PB060</td><td>  </td><td>Personal cross-sectional weight for selected respondent</td></tr>
<tr><td>0+(format 2.5)</td><td>Weight</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB060_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB090</td><td>  </td><td>Day of the personal interview</td></tr>
<tr><td>1 — 31</td><td>Day</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB090_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB100</td><td>  </td><td>Month of the personal interview</td></tr>
<tr><td>1 — 12</td><td>Month</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB100_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB110</td><td>  </td><td>Year of the personal interview</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB110_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB120</td><td>  </td><td>Number of minutes to complete the personal questionnaire</td></tr>
<tr><td>1 — 90</td><td>Minutes</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PB120_F</td><td>-2</td><td>na (information only extracted from registers)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">DEMOGRAPHIC DATA (16+)</td></tr>
<tr><td>X, L</td><td>PB130</td><td>1 — 12</td><td>Month of birth</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB130_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB140</td><td>  </td><td>Year of birth</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB140_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PB150</td><td>  </td><td>Sex</td></tr>
<tr><td>1</td><td>Male</td></tr>
<tr><td>2</td><td>Female</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB150_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB160</td><td>  </td><td>Father ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of father</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PB160_F</td><td>-2</td><td>na (father is not a household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB170</td><td>  </td><td>Mother ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of mother</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PB170_F</td><td>-2</td><td>na (mother is not a household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PB180</td><td>  </td><td>Spouse/partner ID</td></tr>
<tr><td>ID number</td><td>Personal identification number (PID) of spouse/partner</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PB180_F</td><td>-2</td><td>na (person has no spouse/partner or spouse/partner is not a household member)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="6">X, L</td><td rowspan="6">PB190</td><td>  </td><td>Marital status</td></tr>
<tr><td>1</td><td>Never married</td></tr>
<tr><td>2</td><td>Married</td></tr>
<tr><td>3</td><td>Separated</td></tr>
<tr><td>4</td><td>Widowed</td></tr>
<tr><td>5</td><td>Divorced</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB190_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="4">X, L</td><td rowspan="4">PB200</td><td>  </td><td>Consensual Union</td></tr>
<tr><td>1</td><td>Yes, on a legal basis</td></tr>
<tr><td>2</td><td>Yes, without legal basis</td></tr>
<tr><td>3</td><td>No</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB200_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PB210</td><td>  </td><td>Country of birth</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB210_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PB220A</td><td>  </td><td>Citizenship 1</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PB220A_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PB220B</td><td>  </td><td>Citizenship 2</td></tr>
<tr><td>Country code</td><td>See Annex</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PB220B_F</td><td>-2</td><td>na (no second citizenship)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Social exclusion</td></tr>
<tr><td colspan="4">NON-MONETARY PERSONAL DEPRIVATION INDICATORS</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD020</td><td>  </td><td>Replace worn-out clothes by some new (not second-hand) ones</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD020_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD030</td><td>  </td><td>Two pairs of properly fitting shoes (including a pair of all-weather shoes)</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD030_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD050</td><td>  </td><td>Get-together with friends/family (relatives) for drink/meal at least once a month</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD050_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD060</td><td>  </td><td>Regularly participate in a leisure activity</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD060_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD070</td><td>  </td><td>Spend a small amount of money each week on yourself</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD070_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td rowspan="4">X,L</td><td rowspan="4">PD080</td><td>  </td><td>Internet connection for personal use at home</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No — cannot afford</td></tr>
<tr><td>3</td><td>No — Other reasons</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PD080_F</td><td>1</td><td>Variable is filled</td></tr>
<tr><td>– 1</td><td>Missing</td></tr>
<tr><td>– 3</td><td>Not selected respondent</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Education</td></tr>
<tr><td colspan="4">EDUCATION, INCLUDING HIGHEST ISCED LEVEL ATTAINED</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PE010</td><td>  </td><td>Current education activity</td></tr>
<tr><td>1</td><td>In education</td></tr>
<tr><td>2</td><td>Not in education</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PE010_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PE020</td><td>  </td><td>ISCED level currently attended</td></tr>
<tr><td>ISCED code(19)</td><td>ISCED</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PE020_F</td><td>-2</td><td>na (PE010 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PE030</td><td>  </td><td>Year when highest level of education was attained</td></tr>
<tr><td>Year</td><td>Four digits of year</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PE030_F</td><td>-2</td><td>na (the person has never been in education)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PE040</td><td>  </td><td>Highest ISCED level attained</td></tr>
<tr><td>ISCED code(19)</td><td>ISCED</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PE040_F</td><td>-2</td><td>na (the person has never been in education)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Labour information</td></tr>
<tr><td colspan="4">BASIC LABOUR INFORMATION ON CURRENT ACTIVITY STATUS AND CURRENT MAIN JOB, INCLUDING INFORMATION ON LAST MAIN JOB FOR UNEMPLOYED</td></tr>
<tr><td rowspan="10">X, L</td><td rowspan="10">PL030</td><td>  </td><td>Self-defined current activity status</td></tr>
<tr><td>1</td><td>Working full time</td></tr>
<tr><td>2</td><td>Working part time</td></tr>
<tr><td>3</td><td>Unemployed</td></tr>
<tr><td>4</td><td>Pupil, student, further training, unpaid work experience</td></tr>
<tr><td>5</td><td>In retirement or in early retirement or has given up business</td></tr>
<tr><td>6</td><td>Permanently disabled or/and unfit to work</td></tr>
<tr><td>7</td><td>In compulsory military or community service</td></tr>
<tr><td>8</td><td>Fulfilling domestic tasks and care responsibilities</td></tr>
<tr><td>9</td><td>Other inactive person</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL030_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PL035 (20)</td><td>  </td><td>Worked at least one hour during the previous week</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL035_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (person is not employee or Member State has other source to calculate the gender pay gap)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PL015</td><td>  </td><td>Have you ever worked?</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL015_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL030 = 1 or 2)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PL020</td><td>  </td><td>Actively looking for a job in previous four weeks</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL020_F</td><td>-2</td><td>na (PL030 = 1 or 2)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PL025</td><td>  </td><td>Are you available for work in the next two weeks</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL025_F</td><td>-2</td><td>na (PL020 = 2)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="5">X, L</td><td rowspan="5">PL040</td><td>  </td><td>Status in employment</td></tr>
<tr><td>1</td><td>Self-employed with employees</td></tr>
<tr><td>2</td><td>Self-employed without employees</td></tr>
<tr><td>3</td><td>Employee</td></tr>
<tr><td>4</td><td>Family worker</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL040_F</td><td>-2</td><td>na (PL030 not = 1 and not = 2 and PL015 and PL035 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PL050</td><td>  </td><td>Occupation (ISCO-88 (COM) (two digits))</td></tr>
<tr><td>ISCO code(21)</td><td>ISCO</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL050_F</td><td>-2</td><td>na (PL030 not =1 and not =2 and PL035 not =1 and PL015 not =1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X, L</td><td rowspan="2">PL060</td><td>  </td><td>Number of hours usually worked per week in main job</td></tr>
<tr><td>1 — 99</td><td>Number of hours</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL060_F</td><td>-6</td><td>Hours varying (even an average over four weeks is not possible)</td></tr>
<tr><td>-2</td><td>na (PL030 not = 1 and not =2 and PL035 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">BASIC INFORMATION ON ACTIVITY STATUS DURING INCOME REFERENCE PERIOD</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL070</td><td>  </td><td>Number of months spent at full-time work in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL070_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL072</td><td>  </td><td>Number of months spent at part-time work in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL072_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL080</td><td>  </td><td>Number of months spent in unemployment in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL080_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL085</td><td>  </td><td>Number of months spent in retirement in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL085_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL087</td><td>  </td><td>Number of months spent studying in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL087_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL090</td><td>  </td><td>Number of months spent in inactivity in income reference period</td></tr>
<tr><td>1 — 12</td><td>Months</td></tr>
<tr><td rowspan="2">  </td><td rowspan="2">PL090_F</td><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">TOTAL NUMBER OF HOURS WORKED ON CURRENT SECOND, THIRD, ETC. JOBS</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL100</td><td>  </td><td>Total number of hours usually worked in second, third etc. jobs</td></tr>
<tr><td>1 — 99</td><td>Number of hours</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL100_F</td><td>-2</td><td>na (person does not have a second job or PL030 not = 1 or 2)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">DETAILED LABOUR INFORMATION</td></tr>
<tr><td rowspan="2">X</td><td rowspan="2">PL110</td><td>  </td><td>NACE (2 digits)</td></tr>
<tr><td>NACE code(22)</td><td>NACE</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL110_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL030 not = 1 and not = 2 and PL035 not = 1 )</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="8">X</td><td rowspan="8">PL120</td><td>  </td><td>Reason for working less than 30 hours (in main and other jobs)</td></tr>
<tr><td>1</td><td>Undergoing education or training</td></tr>
<tr><td>2</td><td>Personal illness or disability</td></tr>
<tr><td>3</td><td>Want to work more hours but cannot find job(s) or work(s) for more hours</td></tr>
<tr><td>4</td><td>Do not want to work more hours</td></tr>
<tr><td>5</td><td>Number of hours in all job(s) are considered full-time job</td></tr>
<tr><td>6</td><td>Housework, looking after children or other persons</td></tr>
<tr><td>7</td><td>Other reasons</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL120_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL030 not = 1 and not = 2 or PL060+PL100 not &lt; 30)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="7">X</td><td rowspan="7">PL130 (23)</td><td>  </td><td>Number of persons working at the local unit</td></tr>
<tr><td>1 — 10</td><td>Exact number if between 1 and 10</td></tr>
<tr><td>11</td><td>if between 11 to 19 persons</td></tr>
<tr><td>12</td><td>if between 20 to 49 persons</td></tr>
<tr><td>13</td><td>if 50 persons or more</td></tr>
<tr><td>14</td><td>don't know but fewer than 11 persons</td></tr>
<tr><td>15</td><td>don't know but more than 10 persons</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL130_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL030 not = 1 and not = 2 and PL035 not = 1 )</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PL140</td><td>  </td><td>Type of contract</td></tr>
<tr><td>1</td><td>Permanent job/work contract of unlimited duration</td></tr>
<tr><td>2</td><td>Temporary job/work contract of limited duration</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL140_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL040 not = 3 )</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PL150</td><td>  </td><td>Managerial position</td></tr>
<tr><td>1</td><td>Supervisory</td></tr>
<tr><td>2</td><td>Non-supervisory</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL150_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL040 not = 3)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">L</td><td rowspan="3">PL160</td><td>  </td><td>Change of job since last year</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL160_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL030 not = 1 or not = 2)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="8">L</td><td rowspan="8">PL170</td><td>  </td><td>Reason for change</td></tr>
<tr><td>1</td><td>To take up or seek better job</td></tr>
<tr><td>2</td><td>End of temporary contract</td></tr>
<tr><td>3</td><td>Obliged to stop by employer (business closure, redundancy, early retirement, dismissal etc.)</td></tr>
<tr><td>4</td><td>Sale or closure of own/family business</td></tr>
<tr><td>5</td><td>Childcare and care for other dependent</td></tr>
<tr><td>6</td><td>Marriage, or partner's job required move to another area</td></tr>
<tr><td>7</td><td>Other reasons</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL170_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PL160 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="13">L</td><td rowspan="13">PL180</td><td>  </td><td>Most recent change in the individual's activity status</td></tr>
<tr><td>1</td><td>Employed-unemployed</td></tr>
<tr><td>2</td><td>Employed-retired</td></tr>
<tr><td>3</td><td>Employed-other inactive</td></tr>
<tr><td>4</td><td>Unemployed-employed</td></tr>
<tr><td>5</td><td>Unemployed-retired</td></tr>
<tr><td>6</td><td>Unemployed-other inactive</td></tr>
<tr><td>7</td><td>Retired-employed</td></tr>
<tr><td>8</td><td>Retired-unemployed</td></tr>
<tr><td>9</td><td>Retired-other inactive</td></tr>
<tr><td>10</td><td>Other inactive-employed</td></tr>
<tr><td>11</td><td>Other inactive-unemployed</td></tr>
<tr><td>12</td><td>Other inactive-retired</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL180_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (no change since last year)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">ACTIVITY HISTORY</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL190</td><td>  </td><td>When began first regular job</td></tr>
<tr><td>8 — 65</td><td>Age</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL190_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (person never worked)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL200</td><td>  </td><td>Number of years spent in paid work (as employee or self-employed)</td></tr>
<tr><td>0 — 65</td><td>Years</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PL200_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (person never worked)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">CALENDAR OF ACTIVITIES</td></tr>
<tr><td rowspan="10">L</td><td rowspan="10">PL210A</td><td>  </td><td>Main activity in January</td></tr>
<tr><td>1</td><td>Employee (full-time)</td></tr>
<tr><td>2</td><td>Employee (part-time)</td></tr>
<tr><td>3</td><td>Self-employed (full-time)</td></tr>
<tr><td>4</td><td>Self-employed (part-time)</td></tr>
<tr><td>5</td><td>Unemployed</td></tr>
<tr><td>6</td><td>Retired</td></tr>
<tr><td>7</td><td>Student</td></tr>
<tr><td>8</td><td>Other inactive</td></tr>
<tr><td>9</td><td>Compulsory military service</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PL210A_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210B</td><td>  </td><td>Main activity in February</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210B_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210C</td><td>  </td><td>Main activity in March</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210C_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210D</td><td>  </td><td>Main activity in April</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210D_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210E</td><td>  </td><td>Main activity in May</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210E_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210F</td><td>  </td><td>Main activity in June</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210F_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210G</td><td>  </td><td>Main activity in July</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210G_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210H</td><td>  </td><td>Main activity in August</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210H_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210I</td><td>  </td><td>Main activity in September</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210I_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210J</td><td>  </td><td>Main activity in October</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210J_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210K</td><td>  </td><td>Main activity in November</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210K_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td rowspan="2">L</td><td rowspan="2">PL210L</td><td>  </td><td>Main activity in December</td></tr>
<tr><td>  </td><td>See PL210A</td></tr>
<tr><td>  </td><td>PL210L_F</td><td>  </td><td>See PL210A_F</td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Health</td></tr>
<tr><td colspan="4">HEALTH, INCLUDING HEALTH STATUS AND CHRONIC ILLNESS OR CONDITION</td></tr>
<tr><td rowspan="6">X, L</td><td rowspan="6">PH010</td><td>  </td><td>General health</td></tr>
<tr><td>1</td><td>Very good</td></tr>
<tr><td>2</td><td>Good</td></tr>
<tr><td>3</td><td>Fair</td></tr>
<tr><td>4</td><td>Bad</td></tr>
<tr><td>5</td><td>Very bad</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PH010_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PH020</td><td>  </td><td>Suffer from any chronic (long-standing) illness or condition</td></tr>
<tr><td>1</td><td>Yes</td></tr>
<tr><td>2</td><td>No</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PH020_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="4">X, L</td><td rowspan="4">PH030</td><td>  </td><td>Limitation in activities people usually do, because of health problems and for at least the last six months</td></tr>
<tr><td>1</td><td>Yes, strongly limited</td></tr>
<tr><td>2</td><td>Yes, limited</td></tr>
<tr><td>3</td><td>No, not limited</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PH030_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">ACCESS TO HEALTH CARE</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PH040</td><td>  </td><td>Unmet need for medical examination or treatment during the last 12 months</td></tr>
<tr><td>1</td><td>Yes, there was at least one occasion when the person really needed examination or treatment but did not receive it</td></tr>
<tr><td>2</td><td>No, there was no occasion when the person really needed examination or treatment but did not receive it</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PH040_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="9">X</td><td rowspan="9">PH050</td><td>  </td><td>Main reason for unmet need for medical examination or treatment</td></tr>
<tr><td>1</td><td>Could not afford to (too expensive)</td></tr>
<tr><td>2</td><td>Waiting list</td></tr>
<tr><td>3</td><td>Could not take time because of work, care for children or for others</td></tr>
<tr><td>4</td><td>Too far to travel/no means of transportation</td></tr>
<tr><td>5</td><td>Fear of doctor/hospitals/examination/treatment</td></tr>
<tr><td>6</td><td>Wanted to wait and see if problem got better on its own</td></tr>
<tr><td>7</td><td>Didn't know any good doctor or specialist</td></tr>
<tr><td>8</td><td>Other reasons</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PH050_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PH040 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PH060</td><td>  </td><td>Unmet need for dental examination or treatment during the last 12 months</td></tr>
<tr><td>1</td><td>Yes, there was at least one occasion when the person really needed dental examination or treatment but did not receive it</td></tr>
<tr><td>2</td><td>No, there was no occasion when the person really needed dental examination or treatment but did not receive it</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PH060_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td rowspan="9">X</td><td rowspan="9">PH070</td><td>  </td><td>Reason for unmet need for dental examination or treatment</td></tr>
<tr><td>1</td><td>Could not afford to (too expensive)</td></tr>
<tr><td>2</td><td>Waiting list</td></tr>
<tr><td>3</td><td>Could not take time because of work, care for children or for others</td></tr>
<tr><td>4</td><td>Too far to travel/no means of transportation</td></tr>
<tr><td>5</td><td>Fear of doctor/hospitals/examination/treatment</td></tr>
<tr><td>6</td><td>Wanted to wait and see if problem got better on its own</td></tr>
<tr><td>7</td><td>Didn't know any good dentist</td></tr>
<tr><td>8</td><td>Other reasons</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PH070_F</td><td>-3</td><td>Not selected respondent</td></tr>
<tr><td>-2</td><td>na (PH060 not = 1)</td></tr>
<tr><td>-1</td><td>Missing</td></tr>
<tr><td>1</td><td>Variable is filled</td></tr>
<tr><td colspan="4">Personal data</td></tr>
transformed by post treatment<tr><td>Income</td></tr>
<tr><td colspan="4">NET SERIES OF PERSONAL INCOME AT COMPONENT LEVEL (4)</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY010N</td><td>  </td><td>Net cash or near cash employee income</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="17">  </td><td rowspan="17">PY010N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags(12)</td><td>  </td></tr>
<tr><td>First digit</td><td>Net/Gross (at data collection)</td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>4</td><td>Gross (13)</td></tr>
<tr><td>5</td><td>Unknown</td></tr>
<tr><td>Second digit</td><td>Net (recorded)</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>5</td><td>Unknown (only possible with first digit = 5)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY020N</td><td>  </td><td>Net non-cash employee income(24)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY020N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY035N (25)</td><td>  </td><td>Contributions to individual private pension plans</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">PY035N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (Variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="4">X, L</td><td rowspan="4">PY050N</td><td>  </td><td>Net cash profits or losses from self-employment (including royalties)</td></tr>
<tr><td>1 — 999999.99</td><td>Profits</td></tr>
<tr><td>-999999.99 — -1</td><td>Losses</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY050N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY070N</td><td>  </td><td>Value of goods produced for own consumption(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY070N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY080N (26)</td><td>  </td><td>Net pension from individual private plans (other than those covered under ESSPROS)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY080N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY090N</td><td>  </td><td>Net unemployment benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY090N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY100N</td><td>  </td><td>Net old-age benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY100N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY110N</td><td>  </td><td>Net survivor's benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY110N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY120N</td><td>  </td><td>Net sickness benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY120N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY130N</td><td>  </td><td>Net disability benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY130N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY140N</td><td>  </td><td>Education-related allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY140N_F</td><td>-5</td><td>Not filled: variable of gross series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td colspan="4">GROSS SERIES OF PERSONAL INCOME AT COMPONENT LEVEL (4)(14)(15)</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY010G</td><td>  </td><td>Gross cash or near cash employee income</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="12">  </td><td rowspan="12">PY010G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags(12)</td><td>  </td></tr>
<tr><td>First digit</td><td>Net/Gross (at data collection)</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td>1</td><td>Net of tax on income at source and social contributions</td></tr>
<tr><td>2</td><td>Net of tax on income at source</td></tr>
<tr><td>3</td><td>Net of social contributions</td></tr>
<tr><td>4</td><td>Gross (13)</td></tr>
<tr><td>5</td><td>Unknown</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY020G</td><td>  </td><td>Gross non-cash employee income(24)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY020G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY030G</td><td>  </td><td>Employers' social insurance contributions(27)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY030G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY035G (28)</td><td>  </td><td>Contributions to individual private pension plans</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="8">  </td><td rowspan="8">PY035G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Income flags</td><td>  </td></tr>
<tr><td>First digit</td><td>  </td></tr>
<tr><td>0</td><td>No income (no following digits)</td></tr>
<tr><td>1</td><td>Income (variable is filled)</td></tr>
<tr><td>Following digits</td><td>Imputation factor</td></tr>
<tr><td>000.00000 — 100.00000</td><td>Collected value/recorded value</td></tr>
<tr><td rowspan="4">X, L</td><td rowspan="4">PY050G</td><td>  </td><td>Gross cash profits or losses from self-employment (including royalties)</td></tr>
<tr><td>1 — 999999.99</td><td>Profits</td></tr>
<tr><td>-999999.99 — -1</td><td>Losses</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY050G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_G</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY070G</td><td>  </td><td>Value of goods produced for own consumption(11)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY070G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY080G (28)</td><td>  </td><td>Gross pension from individual private plans (other than those covered under ESSPROS)</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY080G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY090G</td><td>  </td><td>Gross unemployment benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY090G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY100G</td><td>  </td><td>Gross old-age benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY100G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY110G</td><td>  </td><td>Gross survivor's benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY110G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY120G</td><td>  </td><td>Gross sickness benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY120G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-4</td><td>Amount included in another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010N_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY130G</td><td>  </td><td>Gross disability benefits</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="4">  </td><td rowspan="4">PY130G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-4</td><td>Amount included on another income component</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td rowspan="3">X, L</td><td rowspan="3">PY140G</td><td>  </td><td>Education-related allowances</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td rowspan="3">  </td><td rowspan="3">PY140G_F</td><td>-5</td><td>Not filled: variable of net series is filled</td></tr>
<tr><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td colspan="4">GROSS MONTHLY EARNINGS FOR EMPLOYEES (4)(20)</td></tr>
<tr><td rowspan="3">X</td><td rowspan="3">PY200G</td><td>  </td><td>Gross monthly earnings for employees</td></tr>
<tr><td>1 — 999999.99</td><td>Amount</td></tr>
<tr><td>0</td><td>No income</td></tr>
<tr><td>  </td><td rowspan="3">PY200G_F</td><td>-2</td><td>na (PL035 not = 1)</td></tr>
<tr><td>  </td><td>-1 (6)</td><td>Missing</td></tr>
<tr><td>  </td><td>Flags apply</td><td>See PY010G_F</td></tr>
<tr><td colspan="4">(1)  NUTS 1999: Nomenclature of territorial units for statistics.  (2)  Must be filled only the first time the household is recorded (if applicable).  (3)  Number of hours &gt; 0 of childcare at pre-school and compulsory school are incompatible.  (4)  Amounts are in national currency. All amounts must have the same unit.  (5)  Allowed only as long as gross income components are not mandatory.  (6)  As missing values are imputed this code is only acceptable if no imputation is possible.  (7)  Income flags: The flag is composed of two elements:  1. the format (net/gross) of collection (can be different from the recorded format);  2. imputation factor = collected value divided by recorded value.  (8)  All the variables that compose the target variable have to be considered to determine the flag value.  (9)  The following digits will be linked with the first digit without any separator so that the result is a decimal number.  (10)  Factor by which it is necessary to multiply the total gross income, the total disposable income or the total disposable income before social transfers to compensate for missing individual questionnaires.  (11)  Mandatory only from 2007 onwards.  (12)  All the variables that compose the target variable have to be considered to determine the flag value.  (13)  Gross means that neither taxes nor social contributions have been deducted at source.  (14)  If the gross value is a conversion from net, the corresponding net variable should also be filled. If both — net and gross — values are collected, both should be recorded.  (15)  Code ‘-5’ in flag-variable allowed only as long as gross income components are not mandatory.  (16)  In national currency.  (17)  Compulsory only for Member States using Eurostat recommended regression method or subjective method to estimate imputed rent.  (18)  Only collected if calculation of imputed rent at national level uses subjective method.  (19) <br> ISCED 2011: International standard classification of education 2011.  (20)  Compulsory only for Member States which have no other source than EU-SILC to calculate the gender pay gap.  (21)  ISCO — 88 (COM): International standard classification of occupations (for European purposes), 1988 version.  (22)  NACE Rev. 2  : Statistical classification of economic activities in the European Community,  Rev. 2  .  (23)  Person himself/herself should be included in number, as the employer.  (24)  This variable with the exception of company car will only be collected from 2007 onwards.  (25)  PY035N belongs to ‘other items not considered as part of income’.  (26)  PY080N belongs to ‘other items not considered part of income’.  (27)  Will be recorded only if feasibility studies show it is possible.  (28)  PY035G and PY080G belong to ‘other items not included as part of income’. </td></tr>
</tbody>
</table>

**CLASSIFICATION OF COUNTRIES**

BE Belgique/Belgïe

DK Danmark

DE Deutschland

GR Ellada

ES España

FR France

IE Ireland

IT Italia

LU Luxembourg

NL Nederland

AT Österreich

PT Portugal

FI Suomi

SE Sverige

UK United Kingdom

BG Bulgaria

CY Cyprus

CZ Czech Republic

EE Estonia

HU Hungary

LV Latvia

LT Lithuania

MT Malta

PL Poland

RO Romania

SK Slovak Republic

SI Slovenia

TR Turkey

IS Iceland

NO Norway

CH Switzerland

OEU Other European countries

NAF North Africa

(Algeria, Egypt, Libyan Arab Jamahiriya, Morocco, Sudan, Tunisia, Western Sahara)

WAF West Africa

(Benin, Burkina Faso, Cape Verde, Côte d'Ivoire, Gambia, Ghana, Guinea, Guinea-Bissau, Liberia, Mali, Mauritania, Niger, Nigeria, Saint Helena, Senegal, Sierra Leone, Togo)

OAF Other Africa

USA United States of America

CAN Canada

CSA Central and South America

NME Near and Middle East

(Armenia, Azerbaijan, Bahrain, Georgia, Iraq, Israel, Jordan, Kuwait, Lebanon, Occupied Palestinian Territory, Oman, Qatar, Saudi Arabia, Syrian Arab Republic, United Arab Emirates, Yemen)

OAS Other Asia

OCE Australia and Oceania

OTH Other

**FILES TO TRANSMIT TO EUROSTAT**

The target variables will be sent to Eurostat in four different files:

1\. household register (D)

2\. personal register (R)

3\. household data (H)

4\. personal data (P)

The household register file (D) must contain every household (selected + substituted + split off (longitudinal only)), also those where the address could not be contacted or which could not be interviewed.

In the other files, records related to a household will only exist if the household has been contacted (DB120 = 11 (or DB110 = 1)) AND has a completed household interview in the household data file (H) (DB130 = 11) AND at least one member has complete data in the personal data file (P) (RB250 = 11, 12 or 13 => DB135 = 1). This member must be the selected respondent (RB245 = 2) if this mode of selection is used.

The personal register file (R) must contain a record for every person currently living in the household or temporarily absent. In the longitudinal component this file must contain also a record for every person who has moved out or died since the previous wave and for every person who lived in the household for at least three months during the income reference period and was not recorded otherwise in the register of this household.

The personal data file (P) must contain a record for every eligible person (RB245 = 1, 2 or 3) for whom the information could be completed from interview and/or registers (RB250 = 11, 12 or 13).

The technical format of transmission of the files to Eurostat will be the comma separated values format (CSV). The header row (first record) must contain the variable names.

( 1 ) OJ L 165, 3.7.2003, p. 1.
