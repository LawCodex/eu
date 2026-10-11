---
title: "Commission Implementing Regulation (EU) 2020/1227 of 12 November 2019 laying down implementing technical standards with regard to templates for the provision of information in accordance with the STS notification requirements (Text with EEA relevance)"
identifier: "32020R1227"
eli: "http://data.europa.eu/eli/reg_impl/2020/1227/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2019-11-12
entry_into_force: 2020-10-06
last_amended: 2022-11-02
consolidated_version: "02020R1227-20221102"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02020R1227-20221102"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2020/1227 of 12 November 2019 laying down implementing technical standards with regard to templates for the provision of information in accordance with the STS notification requirements (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2020/1227**

**of 12 November 2019**

**laying down implementing technical standards with regard to templates for the provision of information in accordance with the STS notification requirements**

**(Text with EEA relevance)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING REGULATION (EU) 2022/1929 of 31 March 2022 </td><td> L 266</td><td>1</td><td>13.10.2022</td></tr>
</table>

**COMMISSION IMPLEMENTING REGULATION (EU) 2020/1227**

**of 12 November 2019**

**laying down implementing technical standards with regard to templates for the provision of information in accordance with the STS notification requirements**

**(Text with EEA relevance)**

## Article 1 — Templates for STS notification

1\. The information referred to in Article 1(1)(a) and Article 1(2)(a) of Commission Delegated Regulation (EU) 2020/1226 ( 1 ) shall be provided by means of the template set out in Annex I to this Regulation.

2\. The information referred to in Article 1(1)(b) and Article 1(2)(b) of Delegated Regulation (EU) 2020/1226 shall be provided by means of the template set out in Annex II to this Regulation.

3\. The information referred to in Article 1(1)(c) and Article 1(2)(c) of Delegated Regulation (EU) 2020/1226 shall be provided by means of the template set out in Annex III to this Regulation.

3a. The information referred to in Article 1(1), point (d), and Article 1(2), point (d), of Delegated Regulation (EU) 2020/1226 shall be provided by means of the template set out in Annex IV to this Regulation.

4\. Where the information to be provided pursuant to this Article is not available or required due to the application of the transitional provisions laid down in Articles 43 and 43a of Regulation (EU) 2017/2402, the notification shall state ‘Not applicable due to the application of transitional provisions’ in the relevant field or fields of the Annexes to this Regulation.

5\. The information referred to in this Article shall be submitted in an electronic and machine-readable form.

6\. The additional information referred to in Article 2 of Delegated Regulation (EU) 2020/1226 shall be included in the field ‘Box to complete’ of Annexes I to IV to this Regulation.

## Article 2 — Entry into force

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

## ANNEX I

**Field formats to be applied to the STS notification form**

| SYMBOL | DATA TYPE | DEFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Up to n alphanumeric characters | Free text field. Should be entered in ASCII format (no accented characters). |
| {COUNTRYCODE_2} | 2 alphanumeric characters | 2 letter country code, as defined by ISO 3166-1 alpha-2 country code. Should be entered in ASCII format (no accented characters). |
| {CURRENCYCODE_3} | 3 alphanumeric characters | 3 letter currency code, as defined by ISO 4217 currency codes. Should be entered in ASCII format (no accented characters). |
| {DATEFORMAT} | ISO 8601 date format | Dates shall be formatted by the following format: YYYY-MM-DD |
| {Y/N} | 1 alphanumeric character | ‘true’- Y ’false’ – N |
| {ISIN} | 12 alphanumeric characters | ISIN code, as defined in ISO 6166 |
| {LEI} | 20 alphanumeric characters | Legal entity identifier, as defined in ISO 17442 |

**STS notification form for non-ABCP securitisations**

<table>
<tbody><tr><td>FIELD CODE</td><td>FIELD NAME</td><td>BOX TO COMPLETE</td><td>FIELD FORMAT</td></tr>
<tr><td>STSS0</td><td>First contact point</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS1</td><td>Instrument identification code</td><td>  </td><td>{ISIN}</td></tr>
<tr><td>STSS2</td><td>LEI of the originator or sponsor or original lender</td><td>  </td><td>{LEI}</td></tr>
<tr><td>STSS3</td><td>Notification identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS4</td><td>Unique identifier</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS5</td><td>Prospectus Identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSS6</td><td>Securitisation repository</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS7</td><td>Securitisation Name</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSS8</td><td>Country of establishment</td><td>  </td><td>{COUNTRYCODE_2}</td></tr>
<tr><td>STSS9</td><td>Securitisation classification</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSS10</td><td>Underlying Exposures Type</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSS11</td><td>Issue date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSS12</td><td>Notification Date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSS13</td><td>Authorised third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSS14</td><td>Authorised third party (name and country of establishment)</td><td>  </td><td>{ALPHANUM-1000} {COUNTRYCODE_2} </td></tr>
<tr><td>STSS15</td><td>Competent authority which has authorised the third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSS16</td><td>STS status</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS17</td><td>Originator (or original lender) is a credit institution</td><td>  </td><td>{Y/N}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS18</td><td>Confirmation of credit-granting criteria</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS19</td><td>Declaration that credit-granting criteria are subject to supervision</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS20</td><td>Underlying exposures acquired by true sale</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS21</td><td>Subject to severe clawback</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS22</td><td>Exemption for clawback provisions in national insolvency laws</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSS23</td><td>Transfer where the seller is not the original lender</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS24</td><td>Transfer performed by means of an assignment and perfected at a later stage</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS25</td><td>Representations and warranties</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS26</td><td>Criteria for active Portfolio Management</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS27</td><td>Homogeneity of assets</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS28</td><td>Underlying Exposure Obligations/no re-securitisation</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS29</td><td>Soundness of the underwriting standard</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS30</td><td>Originator/Lender Expertise</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS31</td><td>Defaulted Assets</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS32</td><td>At least one payment at the time of transfer</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS33</td><td>Repayment of the holders/sale of assets.</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS34</td><td>Compliance with the risk retention requirements</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSS35</td><td>Mitigation of Interest rates (IR) and currency risks (FX) Risks</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS36</td><td>Derivatives Purchased/Sold by SSPE</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS37</td><td>Derivatives using common standards</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS38</td><td>Referenced interest payments based on generally used interest rates</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS39</td><td>No trapping of cash following enforcement or acceleration notice</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS40</td><td>No amount of cash shall be trapped</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS41</td><td>Principal receipts shall be passed to investors</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS42</td><td>Repayment shall not be reversed with regard to their seniority</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS43</td><td>No provisions shall require automatic liquidation of the underlying exposures at market value</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS44</td><td>Securitisations featuring non-sequential priority of payments</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS45</td><td>Revolving securitisation with early amortisation events for termination of revolving period based on prescribed triggers</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS46</td><td>Deterioration in the credit quality of the underlying exposures</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS47</td><td>Occurrence of an insolvency-related event of the originator or servicer</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS48</td><td>Value of the underlying exposures held by the SSPE falls below a pre-determined threshold</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS49</td><td>Failure to generate sufficient new underlying exposures meeting pre-determined credit quality (trigger for termination of the revolving period)</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS50</td><td>Information regarding contractual obligations of the servicer, trustee and other ancillary service providers</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS51</td><td>Servicing Continuity Provisions</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS52</td><td>Derivative Counterparties Continuity Provisions</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS53</td><td>Liquidity providers and account bank continuity provisions</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS54</td><td>Required expertise from the servicer & policies & adequate procedures & risk management controls in place</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSS55</td><td>Clear & consistent definitions (problem loans)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS56</td><td>Priorities of payment and triggers events</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS57</td><td>Timely resolution of conflicts between classes of investors and responsibilities of trustees</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS58</td><td>Historical Default and Loss Performance Data</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS59</td><td>Sample of the underlying exposures subject to external verifications</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS60</td><td>Availability of a liability cash flow model to potential investors</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSS61</td><td>Environmental performance/residential loans or car loans or leases</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSS62</td><td>Originator and sponsor responsible for compliance with Article 7 of Regulation (EU) 2017/2402</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
</tbody>
</table>

## ANNEX II

**Field formats to be applied to the STS notification form**

| SYMBOL | DATA TYPE | DEFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Up to n alphanumeric characters | Free text field. Should be entered in ASCII format (no accented characters). |
| {COUNTRYCODE_2} | 2 alphanumeric characters | 2 letter country code, as defined by ISO 3166-1 alpha-2 country code. Should be entered in ASCII format (no accented characters). |
| {CURRENCYCODE_3} | 3 alphanumeric characters | 3 letter currency code, as defined by ISO 4217 currency codes. Should be entered in ASCII format (no accented characters). |
| {DATEFORMAT} | ISO 8601 date format | Dates shall be formatted by the following format: YYYY-MM-DD |
| {Y/N} | 1 alphanumeric character | ‘true’- Y ’false’ – N |
| {ISIN} | 12 alphanumeric characters | ISIN code, as defined in ISO 6166 |
| {LEI} | 20 alphanumeric characters | Legal entity identifier, as defined in ISO 17442 |

**STS notification form for ABCP securitisations**

<table>
<tbody><tr><td>FIELD CODE</td><td>FIELD NAME</td><td>BOX TO COMPLETE</td><td>FIELD FORMAT</td></tr>
<tr><td>STSAT0</td><td>First contact point</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT1</td><td>Instrument identification code</td><td>  </td><td>{ISIN}</td></tr>
<tr><td>STSAT2</td><td>LEI of the originator or sponsor or original lender</td><td>  </td><td>{LEI}</td></tr>
<tr><td>STSAT3</td><td>Notification identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT4</td><td>Unique identifier</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT5</td><td>Prospectus Identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAT6</td><td>Securitisation repository</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT7</td><td>Securitisation Name</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAT8</td><td>Place of establishment</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT9</td><td>Securitisation Type</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSAT10</td><td>Underlying Exposures Type</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSAT11</td><td>Issue date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSAT12</td><td>Notification Date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSAT13</td><td>Authorised third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAT14</td><td>Authorised third party (name and country of establishment)</td><td>  </td><td>{ALPHANUM-1000} {COUNTRYCODE_2} </td></tr>
<tr><td>STSAT15</td><td>Competent authority which has authorised the third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAT16</td><td>STS status</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT17</td><td>Originator (or original lender) is a credit institution</td><td>  </td><td>{Y/N}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT18</td><td>Confirmation of credit-granting criteria</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT19</td><td>Declaration that credit-granting criteria are subject to supervision</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT20</td><td>Underlying exposures acquired by true sale</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT21</td><td>Subject to severe clawback</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT22</td><td>Exemption for clawback provisions in national insolvency laws</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAT23</td><td>Transfer where the seller is not the original lender</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT24</td><td>Transfer performed by means of an assignment and perfected at a later stage</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT25</td><td>Representations and warranties</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT26</td><td>Criteria for active Portfolio Management</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT27</td><td>No re-securitisation</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT28</td><td>Transferred underlying exposures without defaulted exposures</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT29</td><td>At least one payment made at the time of transfer</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT30</td><td>Repayment of the holders/sale of assets.</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT31</td><td>Mitigation of Interest rates (IR) and currency risks (FX) Risks</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT32</td><td>Derivatives Purchased/Sold by SSPE</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT33</td><td>Derivatives in Underlying Exposures</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT34</td><td>Derivatives using common standards</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT35</td><td>Clear and consistent definitions relating to the treatment of problem loans</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT36</td><td>Priority of Payments and triggers events</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT37</td><td>Historical Default and Loss Performance Data</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT38</td><td>Homogeneity of assets</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT39</td><td>Underlying Exposure Obligations</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT40</td><td>Underlying Exposure Obligations</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT41</td><td>Referenced interest payments based on generally used interest rates</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT42</td><td>No trapping of cash flow following enforcement or acceleration notice</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAT43</td><td>No trapping of cash/enforcement or acceleration</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT44</td><td>Principal receipts shall be passed to investors</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT45</td><td>No provisions shall require automatic liquidation of the underlying exposures at market value</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT46</td><td>Soundness of the underwriting standards</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT47</td><td>Seller Expertise</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT48</td><td>Revolving ABCP transaction/credit quality trigger.</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAT49</td><td>Securitisation Participant Duties</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT50</td><td>Servicing Continuity Provisions</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT51</td><td>Derivative counterparty and account bank continuity provisions</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAT52</td><td>Sponsor Robustness</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
</tbody>
</table>

## ANNEX III

**Field formats to be applied to the STS notification form**

| SYMBOL | DATA TYPE | DEFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Up to n alphanumeric characters | Free text field. Should be entered in ASCII format (no accented characters). |
| {COUNTRYCODE_2} | 2 alphanumeric characters | 2 letter country code, as defined by ISO 3166-1 alpha-2 country code. Should be entered in ASCII format (no accented characters). |
| {CURRENCYCODE_3} | 3 alphanumeric characters | 3 letter currency code, as defined by ISO 4217 currency codes. Should be entered in ASCII format (no accented characters). |
| {DATEFORMAT} | ISO 8601 date format | Dates shall be formatted by the following format: YYYY-MM-DD |
| {Y/N} | 1 alphanumeric character | ‘true’- Y ’false’ – N |
| {ISIN} | 12 alphanumeric characters | ISIN code, as defined in ISO 6166 |
| {LEI} | 20 alphanumeric characters | Legal entity identifier, as defined in ISO 17442 |

**STS notification form for ABCP Programme**

<table>
<tbody><tr><td>FIELD CODE</td><td>FIELD NAME</td><td>BOX TO COMPLETE</td><td>FIELD FORMAT</td></tr>
<tr><td>STSAP0</td><td>First contact point</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP1</td><td>Instrument identification code</td><td>  </td><td>{ISIN}</td></tr>
<tr><td>STSAP2</td><td>LEI of the sponsor</td><td>  </td><td>{LEI}</td></tr>
<tr><td>STSAP3</td><td>Notification identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAP4</td><td>Unique identifier</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td colspan="4"></td></tr>
<tr><td>STSAP5</td><td>Prospectus Identifier</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAP6</td><td>Securitisation repository</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP7</td><td>ABCP programme name</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAP8</td><td>Country of establishment</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP9</td><td>Instrument classification</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSAP10</td><td>Issue date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSAP11</td><td>Notification date</td><td>  </td><td>{DATEFORMAT}</td></tr>
<tr><td>STSAP12</td><td>Authorised third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAP13</td><td>Authorised third party (name and country of establishment)</td><td>  </td><td>{ALPHANUM-1000} {COUNTRYCODE_2} </td></tr>
<tr><td>STSAP14</td><td>Competent authority which has authorised the third party</td><td>  </td><td>{ALPHANUM-100}</td></tr>
<tr><td>STSAP15</td><td>STS status</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP16</td><td>Sponsor to be supervised credit institution</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP17</td><td>Sponsor Support as liquidity provider</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP18</td><td>Demonstration to credit institution’s competent authority</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP19</td><td>Compliance with sponsor’s due diligence requirements</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP20</td><td>Compliance with the risk retention requirements (transaction level/programme level)</td><td>  </td><td>{LIST}</td></tr>
<tr><td>STSAP21</td><td>Compliance at ABCP programme level with Article 7 of Regulation (EU) 2017/2402</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP22</td><td>Drawn down of liquidity where liquidity facility are not renewed</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAP23</td><td>Compliance of ABCP transactions within an ABCP programme with Article 24(1) to (8) and (12) to (20) of Regulation (EU) 2017/2402</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP24</td><td>Maximum of 5 % of the aggregate amount of the underlying exposures being temporally non-compliant</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAP25</td><td>Remaining weighted of the average life (WAL) not more than two years</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP26</td><td>Fully supported ABCP Programme (Sponsor Support)</td><td>  </td><td>{ALPHANUM-10000}</td></tr>
<tr><td>STSAP27</td><td>No re-securitisation and no credit enhancement establishing a second layer of tranching at the ABCP programme level</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP28</td><td>No call options</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP29</td><td>Interest rate and currency risks at ABCP programme appropriately mitigated and documented</td><td>  </td><td>{ALPHANUM}</td></tr>
<tr><td>STSAP30</td><td>Requirements for ABCP programme documentation (responsibilities of the trustee to investors)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP31</td><td>Requirements for the ABCP programme documentation (contractual obligations of the sponsor)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP32</td><td>Requirements for the ABCP programme documentation (process & responsibilities in case of defaulted servicer)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP33</td><td>Requirements for the ABCP programme documentation (provisions for replacement of derivatives counterparties and the account bank)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP34</td><td>Requirements for the ABCP programme documentation (procedures to ensure collateralisation of the funding commitment)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP35</td><td>Requirements for the ABCP programme documentation (liquidity facility & maturing securities to be repaid where the sponsor does not renew the funding commitment of the liquidity facility before its expiry)</td><td>  </td><td>{ALPHANUM-1000}</td></tr>
<tr><td>STSAP36</td><td>Servicer Expertise</td><td>  </td><td>{ALPHANUM}</td></tr>
</tbody>
</table>

## ANNEX IV

**Field formats to be applied to the STS notification form**

| SYMBOL | DATA TYPE | DEFINITION |
| --- | --- | --- |
| {ALPHANUM-n} | Up to n alphanumeric characters | Free text field. Should be entered in ASCII format (no accented characters). |
| {COUNTRYCODE_2} | 2 alphanumeric characters | 2 letter country code, as defined by ISO 3166-1 alpha-2 country code. Should be entered in ASCII format (no accented characters). |
| {CURRENCYCODE_3} | 3 alphanumeric characters | 3 letter currency code, as defined by ISO 4217 currency codes. Should be entered in ASCII format (no accented characters). |
| {DATEFORMAT} | ISO 8601 date format | Dates shall be formatted by the following format: YYYY-MM-DD |
| {Y/N} | 1 alphanumeric character | ‘true’- Y ‘false’ – N |
| {ISIN} | 12 alphanumeric characters | ISIN code, as defined in ISO 6166 |
| {LEI} | 20 alphanumeric characters | Legal entity identifier, as defined in ISO 17442 |

**STS notification form for on-balance-sheet securitisations**

| FIELD CODE | FIELD NAME | BOX TO COMPLETE | FIELD FORMAT |
| --- | --- | --- | --- |
| STSSY 1 | First contact point |  | {LEI} |
| STSSY 2 | Notification date |  | {DATEFORMAT} |
| STSSY 3 | Instrument identification code |  | {ISIN} |
| STSSY 4 | Legal Entity Identifier (LEI) |  | {LEI} |
| STSSY 5 | Protection seller |  | {ALPHANUM-100} |
| STSSY 6 | Notification identifier |  | {ALPHANUM-100} |
| STSSY 7 | Unique identifier |  | {ALPHANUM-1000} |
| STSSY 8 | Securitisation Repository |  | {ALPHANUM-100} |
| STSSY 9 | Country of establishment |  | {COUNTRYCODE_2} |
| STSSY 10 | Synthetic securitisation classification |  | {LIST} |
| STSSY 11 | Synthetic securitisation with unfunded credit protection |  | {LIST} |
| STSSY 12 | Credit Protection Agreement used |  | {LIST} |
| STSSY 13 | Underlying exposures classification |  | {LIST} |
| STSSY 14 | Issue date |  | {DATEFORMAT} |
| STSSY 15 | Authorised Third party verifier – statement |  | {ALPHANUM-100} |
| STSSY 16 | Authorised Third party verifier – country of establishment |  | {COUNTRYCODE_2} |
| STSSY 17 | Authorised Third party verifier – competent authority |  | {ALPHANUM-100} |
| STSSY 18 | STS status |  | {ALPHANUM-1000} |
| STSSY 19 | The originator is a supervised entity in the Union |  | {ALPHANUM-1000} |
| STSSY 20 | Originator applying the purchased third party’s exposures policies |  | {ALPHANUM-10000} |
| STSSY 21 | Underlying exposures’ origination |  | {ALPHANUM-10000} |
| STSSY 22 | Assets held on originator’s balance sheet at transaction closing |  | {ALPHANUM-1000} |
| STSSY 23 | Group category |  | {ALPHANUM-1000} |
| STSSY 24 | No further hedging of originator’s exposure |  | {ALPHANUM-1000} |
| STSSY 25 | Credit protection agreement meeting Article 249 of Regulation (EU) No 575/2013 |  | {ALPHANUM-1000} |
| STSSY 26 | Credit protection agreement meeting other credit mitigation rules |  | {ALPHANUM-10000} |
| STSSY27 | Representations and warranties – Legal title to the underlying exposures |  | {ALPHANUM-10000} |
| STSSY28 | Representations and warranties – Originator keeps the credit risk of the underlying assets |  | {ALPHANUM-10000} |
| STSSY29 | Representations and warranties – Exposure compliance with eligibility criteria |  | {ALPHANUM-10000} |
| STSSY30 | Representations and warranties – Legal and enforceable obligation to the obligor |  | {ALPHANUM-10000} |
| STSSY31 | Representations and warranties – Underwriting criteria |  | {ALPHANUM-10000} |
| STSSY32 | Representations and warranties – No obligors in material breach or default |  | {ALPHANUM-10000} |
| STSSY33 | Representations and warranties – No false information in transaction documentation |  | {ALPHANUM-10000} |
| STSSY34 | Representations and warranties – Enforceability or collectability of the underlying exposures |  | {ALPHANUM-10000} |
| STSSY35 | Eligibility criteria which do not allow for active portfolio management of the underlying exposures on a discretionary basis |  | {ALPHANUM-10000} |
| STSSY36 | Exemption to the prohibition of active portfolio management |  | {ALPHANUM-10000} |
| STSSY37 | Exposure added after the closing date of the transaction meeting eligibility criteria |  | {ALPHANUM-10000} |
| STSSY 38 | Fully repaid exposure |  | {ALPHANUM-10000} |
| STSSY 39 | Underlying exposures disposed of |  | {ALPHANUM-10000} |
| STSSY 40 | Not credit driven amendment |  | {ALPHANUM-10000} |
| STSSY 41 | Eligibility criteria not met |  | {ALPHANUM-10000} |
| STSSY 42 | Homogeneity of assets |  | {ALPHANUM} |
| STSSY 43 | Only one asset type |  | {ALPHANUM} |
| STSSY 44 | Obligations that are contractually binding and enforceable |  | {ALPHANUM-10000} |
| STSSY 45 | Defined periodic payment |  | {ALPHANUM} |
| STSSY 46 | Proceeds from the sale of assets |  | {ALPHANUM} |
| STSSY 47 | No transferable securities |  | {ALPHANUM} |
| STSSY 48 | No re-securitisation |  | {ALPHANUM-1000} |
| STSSY 49 | Underwriting standards disclosed to potential investors |  | {ALPHANUM-1000} |
| STSSY 50 | Full recourse to an obligor |  | {ALPHANUM-1000} |
| STSSY 51 | Underwriting standards – No third parties |  | {ALPHANUM-1000} |
| STSSY 52 | Underwriting standards – Residential loans |  | {ALPHANUM-1000} |
| STSSY 53 | Underwriting standards – Borrower assessment |  | {ALPHANUM-1000} |
| STSSY 54 | Originator or original lender expertise |  | {ALPHANUM-1000} |
| STSSY 55 | No exposures at default |  | {ALPHANUM-10000} |
| STSSY 56 | No adverse credit history |  | {ALPHANUM-10000} |
| STSSY 57 | Risk of non-payment is not higher than for non-securitisation exposures |  | {ALPHANUM-1000} |
| STSSY 58 | At least one payment made at the time of inclusion of the underlying assets |  | {ALPHANUM-1000} |
| STSSY 59 | Compliance with risk retention requirements |  | {ALPHANUM} |
| STSSY 60 | Mitigation of interest rates and currency risks |  | {ALPHANUM-1000} |
| STSSY 61 | Credit protection collateral and credit protection payment denominated in same currency |  | {ALPHANUM-1000} |
| STSSY 62 | SSPE’s liabilities equal or less than the SSPE’s income |  | {ALPHANUM-10000} |
| STSSY 63 | No derivatives used except for hedging interest or currency risks |  | {ALPHANUM-1000} |
| STSSY 64 | Using derivatives based on common standards |  | {ALPHANUM-10000} |
| STSSY 65 | Referenced interest payments based on generally used interest rates without complex formulae or derivatives |  | {ALPHANUM-10000} |
| STSSY 66 | Enforcement event without prejudice for investor’s enforcement action |  | {ALPHANUM-10000} |
| STSSY 67 | Enforcement of the credit protection agreement – No amount of cash shall be trapped in the SSPE |  | {ALPHANUM-10000} |
| STSSY 68 | Losses allocated in order of seniority |  | {ALPHANUM-10000} |
| STSSY 69 | Sequential amortisation |  | {ALPHANUM-10000} |
| STSSY 70 | Non-sequential priority of payments |  | {ALPHANUM-10000} |
| STSSY 71 | Performance-related triggers |  | {ALPHANUM} |
| STSSY 72 | Performance-related triggers |  | {ALPHANUM} |
| STSSY 73 | Performance-related triggers |  | {ALPHANUM} |
| STSSY 74 | Amount of collateral equal to the amount of tranches being amortised |  | {ALPHANUM-10000} |
| STSSY 75 | Credit event occurred and amount of credit protection available at any payment date. |  | {ALPHANUM-10000} |
| STSSY 76 | Early amortisation provisions or triggers – Credit quality |  | {ALPHANUM-10000} |
| STSSY 77 | Early amortisation provisions or triggers – Losses |  | {ALPHANUM-10000} |
| STSSY 78 | Early amortisation provisions or triggers – New exposures |  | {ALPHANUM-10000} |
| STSSY 79 | Contractual obligations, duties and responsibilities – Servicer |  | {ALPHANUM-10000} |
| STSSY 80 | Contractual obligations, duties and responsibilities – Trustee |  | {ALPHANUM-10000} |
| STSSY 81 | Contractual obligations, duties and responsibilities – Third-party verification agent |  | {ALPHANUM-10000} |
| STSSY 82 | Contractual obligations, duties and responsibilities – Default or insolvency |  | {ALPHANUM-10000} |
| STSSY 83 | Contractual obligations, duties and responsibilities – Servicing procedures |  | {ALPHANUM-10000} |
| STSSY 84 | Servicing standards |  | {ALPHANUM-10000} |
| STSSY 85 | Required expertise from the servicer |  | {ALPHANUM-1000} |
| STSSY 86 | Well documented and adequate policies, procedures and risk management controls in place |  | {ALPHANUM-1000} |
| STSSY 87 | Servicing procedures at least as stringent as the ones applied to similar not securitised exposures |  | {ALPHANUM-1000} |
| STSSY 88 | Reference register in place |  | {ALPHANUM} |
| STSSY 89 | Reference register – Content |  | {ALPHANUM-10000} |
| STSSY 90 | Timely resolution of conflicts between different classes of investors |  | {ALPHANUM-1000} |
| STSSY 91 | SSPE – Voting rights clearly defined |  | {ALPHANUM-1000} |
| STSSY 92 | Historical Default and Loss Performance Data |  | {ALPHANUM-1000} |
| STSSY 93 | Sample of the underlying exposures subject to external verification |  | {ALPHANUM-1000} |
| STSSY 94 | Availability of a liability cash flow model to potential investors |  | {ALPHANUM-1000} |
| STSSY 95 | Publication on environmental performance of underlying exposures consisting of residential loans or auto loans or leases |  | {ALPHANUM-10000} |
| STSSY 96 | Derogation from the requirement to publish environmental performance of underlying exposures consisting of residential loans or car loans or leases |  | {ALPHANUM-10000} |
| STSSY97 | Originator responsible for compliance with Article 7 of Regulation (EU) 2017/2402 |  | {ALPHANUM-1000} |
| STSSY 98 | Information on Article 7(1), point (a), of Regulation (EU) 2017/2402 available to potential investors |  | {ALPHANUM-1000} |
| STSSY 99 | Information on Article 7(1), points (b), (c) and (d) of Regulation (EU) 2017/2402 available to potential investors at least in draft or initial form |  | {ALPHANUM-1000} |
| STSSY 100 | Credit events and use of guarantees |  | {ALPHANUM-10000} |
| STSSY 101 | Credit events and use of credit derivatives |  | {ALPHANUM-10000} |
| STSSY 102 | Credit protection agreement documented |  | {ALPHANUM-10000} |
| STSSY 103 | Forbearance measures do not preclude the triggering of eligible credit events |  | {ALPHANUM-10000} |
| STSSY 104 | Credit protection payment based on the actual realised loss and standard recovery policies and procedures |  | {ALPHANUM-10000} |
| STSSY 105 | Credit protection payment payable within a specified period of time |  | {ALPHANUM-10000} |
| STSSY 106 | Interim credit protection payment at the latest six months after a credit event |  | {ALPHANUM-10000} |
| STSSY 107 | Interim credit protection payment higher than the applicable expected loss amount |  | {ALPHANUM-10000} |
| STSSY 108 | Terms of the interim credit protection payment |  | {ALPHANUM-10000} |
| STSSY 109 | Method for calculation of interim and final credit protection payments |  | {ALPHANUM-10000} |
| STSSY 110 | Credit protection payment proportional to the share of the outstanding nominal amount |  | {ALPHANUM-10000} |
| STSSY 111 | Enforceability of the credit protection payment |  | {ALPHANUM-10000} |
| STSSY 112 | Amount payable under the credit protection agreement by investors is set out in the credit protection agreement. |  | {ALPHANUM-10000} |
| STSSY 113 | Calculation of the amounts in all circumstances |  | {ALPHANUM-10000} |
| STSSY 114 | Investors payments circumstances set out under the credit protection agreement. |  | {ALPHANUM-10000} |
| STSSY 115 | Third-party verification agent’s assessment of circumstances triggering investors payments |  | {ALPHANUM-10000} |
| STSSY 116 | Credit protection payment calculated at individual underlying exposure level. |  | {ALPHANUM-10000} |
| STSSY 117 | Specification of maximum extension period for the debt workout process |  | {ALPHANUM-10000} |
| STSSY 118 | Extension period less than two years |  | {ALPHANUM-10000} |
| STSSY 119 | Final credit protection payment based on the originator’s final loss estimate |  | {ALPHANUM-10000} |
| STSSY 120 | Termination of the credit protection agreement |  | {ALPHANUM-10000} |
| STSSY 121 | Credit protection premiums contingent on the outstanding nominal amount |  | {ALPHANUM-10000} |
| STSSY 122 | Credit protection agreement not stipulating mechanisms that may avoid or reduce the actual allocation of losses to the investors |  | {ALPHANUM-10000} |
| STSSY 123 | Derogation for upfront premium payments |  | {ALPHANUM-10000} |
| STSSY 124 | Description of the credit protection premium in the transaction documentation |  | {ALPHANUM-10000} |
| STSSY 125 | Enforceability of the investor rights |  | {ALPHANUM-10000} |
| STSSY 126 | Appointment of a third-party verification agent before the closing date of the transaction |  | {ALPHANUM-1000} |
| STSSY 127 | Third party verification agent check – Credit event notice specified in the terms of the credit protection agreement |  | {ALPHANUM-1000} |
| STSSY 128 | Third party verification agent check – Underlying exposure included in the reference portfolio |  | {ALPHANUM-1000} |
| STSSY 129 | Third party verification agent check – Eligible criteria met at the time of inclusion in the reference portfolio |  | {ALPHANUM-1000} |
| STSSY 130 | Third party verification agent check – Compliance with the replenishment conditions |  | {{ALPHANUM-1000} |
| STSSY 131 | Third party verification agent check – Losses consistent with originator’s profit and loss statement |  | {ALPHANUM-1000} |
| STSSY 132 | Third party verification agent check – Losses correctly allocated to investors |  | {ALPHANUM-1000} |
| STSSY 133 | Third-party verification agent independent from originators, investors and (where applicable) the SSPE |  | {ALPHANUM-10000} |
| STSSY 134 | Appointment of the third-party verification agent by the closing date |  | {ALPHANUM-10000} |
| STSSY 135 | Third-party verification agent’s check made on a sample basis |  | {ALPHANUM-10000} |
| STSSY 136 | Possibility for investors to require the third-party verification agent to check any underlying exposure |  | {ALPHANUM-10000} |
| STSSY 137 | Possibility for the third-party verification agent to have access to all relevant information |  | {ALPHANUM-10000} |
| STSS 138 | Termination events |  | {ALPHANUM-10000} |
| STSS 139 | Transaction documentation – Call rights |  | {ALPHANUM-10000} |
| STSS 140 | Transaction documentation – Time call not structured to avoid allocating losses to credit enhancements positions |  | {ALPHANUM-10000} |
| STSS 141 | Time call |  | {ALPHANUM-10000} |
| STSS 142 | Funded credit protection – Collateral return to investors in order of the seniority of the tranches |  | {ALPHANUM-10000} |
| STSS 143 | Termination of transaction by investors upon failure to pay the credit protection premium |  | {ALPHANUM-10000} |
| STSSY 144 | Amount of synthetic excess spread to investors specified in transaction documentation and expressed as a fixed percentage of the total outstanding portfolio balance |  | {ALPHANUM-10000} |
| STSSY 145 | Unused synthetic excess spread to be returned to originator |  | {ALPHANUM-10000} |
| STSSY 146 | Originators using Internal-Ratings-Based approach – Total committed amount per year not higher than the one-year regulatory expected loss amounts |  | {ALPHANUM-10000} |
| STSSY 147 | Originators not using Internal-Ratings-Based approach – calculation of the one-year expected loss of the underlying portfolio be clearly determined in the transaction documentation |  | {ALPHANUM-10000} |
| STSSY 148 | Synthetic excess spread conditions laid down in transaction documentation |  | {ALPHANUM-10000} |
| STSS 149 | Credit protection used |  | {ALPHANUM-10000} |
| STSSY 150 | Enforceability of the originator’s right to use the collateral to meet the protection payment obligations of the investors through appropriate collateral arrangements |  | {ALPHANUM} |
| STSSY 151 | Investors’ right to receive any unused collateral when securitisation is unwound or as tranches amortise |  | {ALPHANUM-10000} |
| STSSY 152 | Collateral invested in securities – Eligibility criteria and custody arrangement specified in transaction documentation |  | {ALPHANUM} |
| STSSY 153 | Investors exposed to originator’s credit risk |  | {ALPHANUM-10000} |
| STSSY 154 | Legal opinion confirming the enforceability of the credit protection in all jurisdictions |  | {ALPHANUM-1000} |
| STSSY 155 | High quality collateral – 0 % risk-weighted debt securities |  | {ALPHANUM-10000} |
| STSSY 156 | High quality collateral – cash with a third-party credit institution with a credit quality step 3 or above |  | {ALPHANUM-10000} |
| STSSY 157 | Derogation – collateral in the form of cash on deposit with the originator |  | {ALPHANUM} |
| STSSY 158 | Collateral in the form of cash on deposit with the originator – permission by competent authority |  | {ALPHANUM} |
| STSSY 159 | Transfer of collateral where third-party credit institution or originator no longer satisfies the minimum credit quality step |  | {ALPHANUM} |
| STSSY 160 | Compliance with collateral requirements in the case of investments in credit linked notes issued by the originator |  | {ALPHANUM-1000} |

( 1 ) Commission Delegated Regulation (EU) 2020/1226 of 12 November 2019 supplementing Regulation (EU) 2017/2402 of the European Parliament and of the Council and laying down regulatory technical standards specifying the information to be provided in accordance with the STS notification requirements (See page 285 of this Official Journal).
