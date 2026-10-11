---
title: "Commission Implementing Regulation (EU) 2016/378 of 11 March 2016 laying down implementing technical standards with regard to the timing, format and template of the submission of notifications to competent authorities according to Regulation (EU) No 596/2014 of the European Parliament and of the Council (Text with EEA relevance)"
identifier: "32016R0378"
eli: "http://data.europa.eu/eli/reg_impl/2016/378/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2016-03-11
entry_into_force: 2016-11-02
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0378"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2016/378 of 11 March 2016 laying down implementing technical standards with regard to the timing, format and template of the submission of notifications to competent authorities according to Regulation (EU) No 596/2014 of the European Parliament and of the Council (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2016/378**

**of 11 March 2016**

**laying down implementing technical standards with regard to the timing, format and template of the submission of notifications to competent authorities according to Regulation (EU) No 596/2014 of the European Parliament and of the Council**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) No 596/2014 of the European Parliament and of the Council of 16 April 2014 on market abuse (market abuse regulation) and repealing Directive 2003/6/EC of the European Parliament and of the Council and Commission Directives 2003/124/EC, 2003/125/EC and 2004/72/EC (1), and in particular, the third subparagraph of Article 4(5) thereof,

Whereas:

(1) In order to ensure the coherence of reporting obligations and to reduce the administrative burden for entities subject to such obligations, it is necessary to align the reporting obligations under this Regulation and under Commission Delegated Regulation to be adopted in accordance with the third subparagraph of Article 27(3) of Regulation (EU) No 600/2014 of the European Parliament and of the Council (2).

(2) In order to enable the competent authorities and the European Securities and Markets Authority (ESMA) to ensure data quality and effective market monitoring, for the benefit of market integrity, the competent authorities and ESMA should be able to promptly receive complete notifications in respect of each trading day.

(3) For the purposes of effective and efficient use of data by competent authorities, there should be consistency in the templates and formats used when submitting notifications of financial instruments. Adherence to the relevant international standards with regard to the details included in those notifications promotes those purposes.

(4) This Regulation is based on the draft implementing technical standards submitted by ESMA to the Commission.

(5) ESMA has conducted open public consultations on the draft implementing technical standard on which this Regulation is based, analysed the potential related costs and benefits and requested the opinion of the Securities and Markets Stakeholder Group established by Article 37 of Regulation (EU) No 1095/2010 of the European Parliament and of the Council (3).

(6) In order to ensure the smooth functioning of the financial markets, it is necessary that this Regulation enters into force as a matter of urgency and that the provisions laid down in this Regulation apply from the same date as those laid down in Regulation (EU) No 596/2014,

HAS ADOPTED THIS REGULATION:

## Article 1

1\. By no later than 21.00 CET on each day that it is open for trading, a trading venue shall, using automated processes, provide to its competent authority pursuant to Article 4(1) of Regulation (EU) No 596/2014 the notifications of all financial instruments which, before 18.00 CET on that day, were for the first time subject to a request for admission to trading or admitted to trading or traded on that trading venue, including where orders or quotes were placed through its system, or ceased to be traded or to be admitted to trading on the trading venue.

2\. Notifications of financial instruments which, after 18.00 CET, were for the first time subject to a request for admission to trading or admitted to trading or traded on the trading venue, including where orders or quotes were placed through its system, or ceased to be traded or to be admitted to trading on the trading venue, shall be made, using automated processes, by the trading venue to the competent authority by no later than 21.00 CET of the next day on which it is open for trading.

3\. Competent authorities shall transmit notifications referred to in paragraphs 1 and 2 pursuant to Article 4(2) of Regulation (EU) No 596/2014 to ESMA each day by no later than 23.59 CET using automated processes and secure electronic communication channels between them and ESMA.

## Article 2

All details to be included in notifications pursuant to Article 4(1) and (2) of Regulation (EU) No 596/2014 shall be submitted in accordance with the standards and formats specified in the Annex to this Regulation, in an electronic and machine-readable form and in a common XML template in accordance with the ISO 20022 methodology.

## Article 3

This Regulation shall enter into force on the day following that of its publication in the Official Journal of the European Union.

It shall apply from 3 July 2016.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 11 March 2016.

For the Commission

The President

Jean-Claude JUNCKER

(1) OJ L 173, 12.6.2014, p. 1.

(2) Regulation (EU) No 600/2014 of the European Parliament and of the Council of 15 May 2014 on markets in financial instruments and amending Regulation (EU) No 648/2012 (OJ L 173, 12.6.2014, p. 84).

(3) Regulation (EU) No 1095/2010 of the European Parliament and of the Council of 24 November 2010 establishing a European Supervisory Authority (European Securities and Markets Authority), amending Decision No 716/2009/EC and repealing Commission Decision 2009/77/EC (OJ L 331, 15.12.2010, p. 84).

## ANNEX

**Standards and formats of the submission of notifications to competent authorities according to Regulation (EU) No 596/2014**

**Table 1**

**Legend for Table 3**

<table>
<tbody><tr><td>SYMBOL</td><td>DATA TYPE</td><td>DEFINITION</td></tr>
<tr><td>{ALPHANUM-n}</td><td>Up to n alphanumerical characters</td><td>Free text field.</td></tr>
<tr><td>{CFI_CODE}</td><td>6 characters</td><td>ISO 10962 CFI code.</td></tr>
<tr><td>{COUNTRYCODE_2}</td><td>2 alphanumerical characters</td><td>2-letter country code, as defined by ISO 3166-1 alpha-2 country code.</td></tr>
<tr><td>{CURRENCYCODE_3}</td><td>3 alphanumerical characters</td><td>3-letter currency code, as defined by ISO 4217 currency codes</td></tr>
<tr><td>{DATE_TIME_FORMAT}</td><td>ISO 8601 date and time format</td><td><table><tbody><tr><td>—</td><td>Date and time in the following format:</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>YYYY-MM-DDThh:mm:ss.ddddddZ.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘YYYY’ is the year;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘MM’ is the month;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘DD’ is the day;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘T’ — means that the letter ‘T’ shall be used</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘hh’ is the hour;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘mm’ is the minute;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>‘ss.dddddd’ is the second and its fraction of a second;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>Z is UTC time.</td></tr>
</tbody>
</table>
 Dates and times shall be reported in UTC. </td></tr>
<tr><td>{DATEFORMAT}</td><td>ISO 8601 date format</td><td>Dates shall be formatted by the following format: YYYY-MM-DD. </td></tr>
<tr><td>{DECIMAL-n/m}</td><td>Decimal number of up to n digits in total of which up to m digits can be fraction digits</td><td>Numerical field for both positive and negative values.<table><tbody><tr><td>—</td><td>decimal separator is ‘.’ (full stop);</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>negative numbers are prefixed with ‘-’ (minus);</td></tr>
</tbody>
</table>
 Values are rounded and not truncated. </td></tr>
<tr><td>{INDEX}</td><td>4 alphabetic characters</td><td>‘EONA’ — EONIA ‘EONS’ — EONIA SWAP  ‘EURI’ — EURIBOR  ‘EUUS’ — EURODOLLAR  ‘EUCH’ — EuroSwiss  ‘GCFR’ — GCF REPO  ‘ISDA’ — ISDAFIX  ‘LIBI’ — LIBID  ‘LIBO’ — LIBOR  ‘MAAA’ — Muni AAA  ‘PFAN’ — Pfandbriefe  ‘TIBO’ — TIBOR  ‘STBO’ — STIBOR  ‘BBSW’ — BBSW  ‘JIBA’ — JIBAR  ‘BUBO’ — BUBOR  ‘CDOR’ — CDOR  ‘CIBO’ — CIBOR  ‘MOSP’ — MOSPRIM  ‘NIBO’ — NIBOR  ‘PRBO’ — PRIBOR  ‘TLBO’ — TELBOR  ‘WIBO’ — WIBOR  ‘TREA’ — Treasury  ‘SWAP’ — SWAP  ‘FUSW’ — Future SWAP </td></tr>
<tr><td>{INTEGER-n}</td><td>Integer number of up to n digits in total</td><td>Numerical field for both positive and negative integer values.</td></tr>
<tr><td>{ISIN}</td><td>12 alphanumerical characters</td><td>ISIN code, as defined in ISO 6166.</td></tr>
<tr><td>{LEI}</td><td>20 alphanumerical characters</td><td>Legal entity identifier as defined in ISO 17442.</td></tr>
<tr><td>{MIC}</td><td>4 alphanumerical characters</td><td>Market identifier as defined in ISO 10383.</td></tr>
<tr><td>{FISN}</td><td>35 alphanumeric characters</td><td>FISN code as defined in ISO 18774.</td></tr>
</tbody>
</table>

**Table 2**

**Classification of commodity and emission allowances derivatives for Table 3 (fields 35-37)**

<table>
<tbody><tr><td>Base product</td><td>Sub product</td><td>Further sub product</td></tr>
<tr><td rowspan="9">‘AGRI’ — Agricultural</td><td>‘GROS’ — Grains and Oil Seeds</td><td>‘FWHT’ — Feed Wheat ‘SOYB’ — Soybeans  ‘CORN’ — Maize  ‘RPSD’ — Rapeseed  ‘RICE’ — Rice  ‘OTHR’ — Other </td></tr>
<tr><td>‘SOFT’ — Softs</td><td>‘CCOA’ — Cocoa ‘ROBU’ — Robusta Coffee  ‘WHSG’ — White Sugar  ‘BRWN’ — Raw Sugar  ‘OTHR’ — Other </td></tr>
<tr><td>‘POTA’ — Potato</td><td></td></tr>
<tr><td>‘OOLI’ — Olive oil</td><td>‘LAMP’ — Lampante'</td></tr>
<tr><td>‘DIRY’ — Dairy</td><td></td></tr>
<tr><td>‘FRST’ — Forestry</td><td></td></tr>
<tr><td>‘SEAF’ — Seafood</td><td></td></tr>
<tr><td>‘LSTK’ — Livestock</td><td></td></tr>
<tr><td>‘GRIN’ — Grain</td><td>‘MWHT’ — Milling Wheat</td></tr>
<tr><td rowspan="4">‘NRGY’ — Energy</td><td>‘ELEC’ -Electricity</td><td>‘BSLD’ — Base load ‘FITR’ — Financial Transmission Rights  ‘PKLD’ — Peak load  ‘OFFP’ — Off-peak  ‘OTHR’ — Other </td></tr>
<tr><td>‘NGAS’ — Natural Gas</td><td>‘GASP’ — GASPOOL ‘LNGG’ — LNG  ‘NBPG’ — NBP  ‘NCGG’ — NCG  ‘TTFG’ — TTF </td></tr>
<tr><td>‘OILP’ — Oil</td><td>‘BAKK’ — Bakken ‘BDSL’ — Biodiesel  ‘BRNT’ — Brent  ‘BRNX’ — Brent NX  ‘CNDA’ — Canadian  ‘COND’ — Condensate  ‘DSEL’ — Diesel  ‘DUBA’ — Dubai  ‘ESPO’ — ESPO  ‘ETHA’ — Ethanol  ‘FUEL’ — Fuel  ‘FOIL’ — Fuel Oil  ‘GOIL’ — Gasoil  ‘GSLN’ — Gasoline  ‘HEAT’ — Heating Oil  ‘JTFL’ — Jet Fuel  ‘KERO’ — Kerosene  ‘LLSO’ — Light Louisiana Sweet (LLS)  ‘MARS’ — Mars  ‘NAPH’ — Naptha  ‘NGLO’ — NGL  ‘TAPI’ — Tapis  ‘URAL’ — Urals  ‘WTIO’ — WTI </td></tr>
<tr><td>‘COAL’ — Coal ‘INRG’ — Inter Energy  ‘RNNG’ — Renewable energy  ‘LGHT’ — Light ends  ‘DIST’ — Distillates </td><td></td></tr>
<tr><td rowspan="2">‘ENVR’ — Environmental</td><td>‘EMIS’ — Emissions</td><td>‘CERE’ — CER ‘ERUE’ — ERU  ‘EUAE’ — EUA  ‘EUAA’ — EUAA  ‘OTHR’ — Other </td></tr>
<tr><td>‘WTHR’ — Weather ‘CRBR’ — Carbon-related' </td><td></td></tr>
<tr><td rowspan="3">‘FRGT’ — ‘Freight’</td><td>‘WETF’ — Wet</td><td>‘TNKR’ -Tankers</td></tr>
<tr><td>‘DRYF’ — Dry</td><td>‘DBCR’ -Dry bulk carriers</td></tr>
<tr><td>‘CSHP’ — Container ships</td><td></td></tr>
<tr><td>‘FRTL’ — ‘Fertilizer’</td><td>‘AMMO’ — Ammonia ‘DAPH’ — DAP (Diammonium Phosphate)  ‘PTSH’ — Potash  ‘SLPH’ — Sulphur  ‘UREA’ — Urea  ‘UAAN’ — UAN (urea and ammonium nitrate) </td><td></td></tr>
<tr><td>‘INDP’ — Industrial products'</td><td>‘CSTR’ — Construction ‘MFTG’ — Manufacturing </td><td></td></tr>
<tr><td rowspan="2">‘METL’ — Metals'</td><td>‘NPRM’ — Non-Precious</td><td>‘ALUM’ — Aluminium ‘ALUA’ — Aluminium Alloy  ‘CBLT’ — Cobalt  ‘COPR’ — Copper  ‘IRON’ — Iron ore  ‘LEAD’ — Lead  ‘MOLY’ — Molybdenum  ‘NASC’ — NASAAC  ‘NICK’ — Nickel  ‘STEL’ — Steel  ‘TINN’ — Tin  ‘ZINC’ — Zinc  ‘OTHR’ — Other </td></tr>
<tr><td>‘PRME’ — Precious</td><td>‘GOLD’ — Gold ‘SLVR’ — Silver  ‘PTNM’ — Platinum  ‘PLDM’ — Palladium  ‘OTHR’ — Other </td></tr>
<tr><td>‘MCEX’ — Multi Commodity Exotic'</td><td></td><td></td></tr>
<tr><td>‘PAPR’ — Paper</td><td>‘CBRD’ — Containerboard ‘NSPT’ — Newsprint  ‘PULP’ — Pulp  ‘RCVP’ — Recovered paper </td><td></td></tr>
<tr><td>‘POLY’ — Polypropylene</td><td>‘PLST’ — Plastic</td><td></td></tr>
<tr><td>‘INFL’ — Inflation</td><td></td><td></td></tr>
<tr><td>‘OEST’ — Official economic statistics'</td><td></td><td></td></tr>
<tr><td>‘OTHC’ — Other C10 ‘as defined in Table 10.1 Section 10 of Annex III to Commission Delegated Regulation supplementing Regulation (EU) No 600/2014 of the European Parliament and of the Council with regard to regulatory technical standards on transparency requirements for trading venues and investment firms in respect of bonds, structured finance products, emission allowances and derivatives.</td><td>'DLVR’ — Deliverable ‘NDLV’ — Non-deliverable </td><td></td></tr>
<tr><td>‘OTHR’ — Other</td><td></td><td></td></tr>
</tbody>
</table>

**Table 3**

**Standards and formats to be used in the notifications to be submitted in accordance with Article 4(1) and (2) of Regulation (EU) No 596/2014**

<table>
<tbody><tr><td>N.</td><td>FIELD</td><td>STANDARDS AND FORMATS TO BE USED FOR REPORTING</td></tr>
<tr><td colspan="3">General Fields</td></tr>
<tr></tr>
<tr><td>1</td><td>Instrument identification code</td><td>{ISIN}</td></tr>
<tr><td>2</td><td>Instrument full name</td><td>{ALPHANUM-350}</td></tr>
<tr><td>3</td><td>Instrument classification</td><td>{CFI_CODE}</td></tr>
<tr><td>4</td><td>Commodities derivative indicator</td><td>‘true’ — Yes ‘false’ — No </td></tr>
<tr><td colspan="3">Issuer related fields</td></tr>
<tr></tr>
<tr><td>5</td><td>Issuer or operator of the trading venue identifier</td><td>{LEI}</td></tr>
<tr><td colspan="3">Venue related fields</td></tr>
<tr></tr>
<tr><td>6</td><td>Trading venue</td><td>{MIC}</td></tr>
<tr><td>7</td><td>Financial instrument short name</td><td>{FISN}</td></tr>
<tr><td>8</td><td>Request for admission to trading by issuer</td><td>‘true’ — Yes ‘false’ — No </td></tr>
<tr><td>9</td><td>Date of approval of the admission to trading</td><td>{DATE_TIME_FORMAT}</td></tr>
<tr><td>10</td><td>Date of request for admission to trading</td><td>{DATE_TIME_FORMAT}</td></tr>
<tr><td>11</td><td>Date of admission to trading or date of first trade</td><td>{DATE_TIME_FORMAT}</td></tr>
<tr><td>12</td><td>Termination date</td><td>{DATE_TIME_FORMAT}</td></tr>
<tr><td colspan="3">Notional related fields</td></tr>
<tr></tr>
<tr><td>13</td><td>Notional currency 1</td><td>{CURRENCYCODE_3}</td></tr>
<tr><td colspan="3">Bonds or other forms of securitised debt related fields</td></tr>
<tr></tr>
<tr><td>14</td><td>Total issued nominal amount</td><td>{DECIMAL-18/5}</td></tr>
<tr><td>15</td><td>Maturity date</td><td>{DATEFORMAT}</td></tr>
<tr><td>16</td><td>Currency of nominal value</td><td>{CURRENCYCODE_3}</td></tr>
<tr><td>17</td><td>Nominal value per unit/minimum traded value</td><td>{DECIMAL-18/5}</td></tr>
<tr><td>18</td><td>Fixed rate</td><td>{DECIMAL-11/10} Expressed as a percentage (e.g. 7.0 means 7 % and 0.3 means 0,3 %) </td></tr>
<tr><td>19</td><td>Identifier of the index/benchmark of a floating rate bond</td><td>{ISIN}</td></tr>
<tr><td>20</td><td>Name of the index/benchmark of a floating rate bond</td><td>{INDEX} Or  {ALPHANUM-25} — if the index name is not included in the {INDEX} list </td></tr>
<tr><td>21</td><td>Term of the index/benchmark of a floating rate bond.</td><td>{INTEGER-3}+‘DAYS’ — days {INTEGER-3}+‘WEEK’ — weeks  {INTEGER-3}+‘MNTH’ — months  {INTEGER-3}+‘YEAR’ — years </td></tr>
<tr><td>22</td><td>Base Point Spread of the index/benchmark of a floating rate bond</td><td>{INTEGER-5}</td></tr>
<tr><td>23</td><td>Seniority of the bond</td><td>‘SNDB’ — Senior Debt ‘MZZD’ — Mezzanine  ‘SBOD’ — Subordinated Debt  ‘JUND’ — Junior Debt </td></tr>
<tr><td colspan="3">Derivatives and Securitised Derivatives related fields</td></tr>
<tr></tr>
<tr><td>24</td><td>Expiry date</td><td>{DATEFORMAT}</td></tr>
<tr><td>25</td><td>Price multiplier</td><td>{DECIMAL-18/17}</td></tr>
<tr><td>26</td><td>Underlying instrument code</td><td>{ISIN}</td></tr>
<tr><td>27</td><td>Underlying issuer</td><td>{LEI}</td></tr>
<tr><td>28</td><td>Underlying index name</td><td>{INDEX} Or  {ALPHANUM-25} — if the index name is not included in the {INDEX} list </td></tr>
<tr><td>29</td><td>Term of the underlying index</td><td>{INTEGER-3}+‘DAYS’ — days {INTEGER-3}+‘WEEK’ — weeks  {INTEGER-3}+‘MNTH’ — months  {INTEGER-3}+‘YEAR’ — years </td></tr>
<tr><td>30</td><td>Option type</td><td>‘PUTO’ — Put ‘CALL’ — Call  ‘OTHR’ — where it cannot be determined whether it is a call or a put </td></tr>
<tr><td>31</td><td>Strike price</td><td>{DECIMAL-18/13} in case the price is expressed as monetary value {DECIMAL-11/10} in case the price is expressed as percentage or yield  {DECIMAL-18/17} in case the price is expressed as basis points  ‘PNDG’ in case the price is not available </td></tr>
<tr><td>32</td><td>Strike price currency</td><td>{CURRENCYCODE_3}</td></tr>
<tr><td>33</td><td>Option exercise style</td><td>‘EURO’ — European ‘AMER’ — American  ‘ASIA’ — Asian  ‘BERM’ — Bermudan  ‘OTHR’ — Any other type </td></tr>
<tr><td>34</td><td>Delivery type</td><td>‘PHYS’ — Physically Settled ‘CASH’ — Cash settled  ‘OPTN’ — Optional for counterparty or when determined by a third party </td></tr>
<tr><td colspan="3">Commodity and emission allowances derivatives</td></tr>
<tr></tr>
<tr><td>35</td><td>Base product</td><td>Only values in the ‘Base product’ column of the classification of commodities and emission allowances derivatives table are allowed.</td></tr>
<tr><td>36</td><td>Sub product</td><td>Only values in the ‘Sub product’ column of the classification of commodities and emission allowances derivatives table are allowed.</td></tr>
<tr><td>37</td><td>Further sub product</td><td>Only values in the ‘Further sub product’ of the classification of commodities and emission allowances derivatives table are allowed.</td></tr>
<tr><td>38</td><td>Transaction type</td><td>‘FUTR’ — Futures ‘OPTN’ — Options  ‘TAPO’ — TAPOS  ‘SWAP’ — SWAPS  ‘MINI’ — Minis  ‘OTCT’ — OTC  ‘ORIT’ — Outright  ‘CRCK’ — Crack  ‘DIFF’ — Differential  ‘OTHR’ — Other </td></tr>
<tr><td>39</td><td>Final price type</td><td>‘ARGM’ — Argus/McCloskey ‘BLTC’ — Baltic  ‘EXOF’ — Exchange  ‘GBCL’ — GlobalCOAL  ‘IHSM’ — IHS McCloskey  ‘PLAT’ — Platts  ‘OTHR’ — Other </td></tr>
<tr><td colspan="3">Interest rate derivatives</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>—</td><td>The fields in this section should only be populated for instruments that have non-financial instrument of type interest rates as underlying.</td></tr>
</tbody>
</table>
</td></tr>
<tr><td>40</td><td>Reference rate</td><td>{INDEX} Or  {ALPHANUM-25}- if the reference rate is not included in the {INDEX} list </td></tr>
<tr><td>41</td><td>IR Term of contract</td><td>{INTEGER-3}+‘DAYS’ — days {INTEGER-3}+‘WEEK’ — weeks  {INTEGER-3}+‘MNTH’ — months  {INTEGER-3}+‘YEAR’ — years </td></tr>
<tr><td>42</td><td>Notional currency 2</td><td>{CURRENCYCODE_3}</td></tr>
<tr><td>43</td><td>Fixed rate of leg 1</td><td>{DECIMAL -11/10} Expressed as a percentage (e.g. 7.0 means 7 % and 0.3 means 0,3 %) </td></tr>
<tr><td>44</td><td>Fixed rate of leg 2</td><td>{DECIMAL -11/10} Expressed as a percentage (e.g. 7.0 means 7 % and 0.3 means 0,3 %) </td></tr>
<tr><td>45</td><td>Floating rate of leg 2</td><td>{INDEX} Or  {ALPHANUM-25} — if the reference rate is not included in the {INDEX} list </td></tr>
<tr><td>46</td><td>IR Term of contract of leg 2</td><td>{INTEGER-3}+‘DAYS’ — days {INTEGER-3}+‘WEEK’ — weeks  {INTEGER-3}+‘MNTH’ — months  {INTEGER-3}+‘YEAR’ — years </td></tr>
<tr><td colspan="3">Foreign exchange derivatives</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>—</td><td>The fields in this section should only be populated for instruments that have non-financial instrument of type foreign exchange as underlying.</td></tr>
</tbody>
</table>
</td></tr>
<tr><td>47</td><td>Notional currency 2</td><td>{CURRENCYCODE_3}</td></tr>
<tr><td>48</td><td>FX Type</td><td>‘FXCR’ — FX Cross Rates ‘FXEM’ — FX Emerging Markets  ‘FXMJ’ — FX Majors </td></tr>
</tbody>
</table>
