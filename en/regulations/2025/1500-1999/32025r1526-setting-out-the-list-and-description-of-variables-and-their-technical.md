---
title: "Commission Implementing Regulation (EU) 2025/1526 of 29 July 2025 setting out the list and description of variables and their technical specifications, statistical classifications and precision targets for the topic structure of earnings pursuant to Regulation (EU) 2025/941 of the European Parliament and of the Council"
identifier: "32025R1526"
eli: "http://data.europa.eu/eli/reg_impl/2025/1526/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2025-07-29
entry_into_force: 2026-01-01
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1526"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2025/1526 of 29 July 2025 setting out the list and description of variables and their technical specifications, statistical classifications and precision targets for the topic structure of earnings pursuant to Regulation (EU) 2025/941 of the European Parliament and of the Council

**COMMISSION IMPLEMENTING REGULATION (EU) 2025/1526**

**of 29 July 2025**

**setting out the list and description of variables and their technical specifications, statistical classifications and precision targets for the topic ‘structure of earnings’ pursuant to Regulation (EU) 2025/941 of the European Parliament and of the Council**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2025/941 of the European Parliament and of the Council of 7 May 2025 on European Union labour market statistics on businesses, repealing Council Regulation (EC) No 530/1999 and Regulations (EC) No 450/2003 and (EC) No 453/2008 of the European Parliament and of the Council (1) and in particular Article 4(7) thereof,

Whereas:

(1) In order to ensure the accurate implementation of the data collection of the topic ‘structure of earnings’, the Commission is to specify the content and technical items of the data set, the statistical concepts, the precision targets and the formats for transmission of information.

(2) Statistics on territorial units, economic sectors, occupations and education levels should be comparable internationally, and therefore the Member States and the Union institutions should use statistical classifications, that are compatible with the NUTS (2), NACE (3) ISCO (4) and ISCED (5) classifications.

(3) The measures provided for in this Regulation are in accordance with the opinion of the European Statistical System Committee,

HAS ADOPTED THIS REGULATION:

## Article 1 — List and description of variables and their technical specifications

1\. The list and description of variables, and their technical specifications, to be transmitted to the Commission (Eurostat) for the topic ‘structure of earnings’ as well as the statistical classifications to be used shall be as set out in Annex I.

2\. A limited set of variables shall be collected on local units belonging to enterprises with 1 to 9 employees, as set out in Annex I.

## Article 2 — Precision targets

The precision targets for statistical surveys shall be as set out in Annex II.

## Article 3 — Formats for transmitting information

1\. Member States shall transmit to the Commission (Eurostat) data sets in electronic form with fully checked and edited microdata that comply with validation rules in accordance with the specification of variables for their coding set out in Annex I. Revised data shall be transmitted in complete data sets covering all variables, regardless of the number of revised observations and variables.

2\. Member States shall make available to the Commission (Eurostat) the data required under this Regulation using the statistical data exchange standards specified by the Commission (Eurostat) and the single entry point for data.

## Article 4 — Entry into force

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 29 July 2025.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L, 2025/941, 20.5.2025, ELI: http://data.europa.eu/eli/reg/2025/941/oj.

(2) Regulation (EC) No 1059/2003 of the European Parliament and of the Council of 26 May 2003 on the establishment of a common classification of territorial units for statistics (NUTS) (OJ L 154, 21.6.2003, p. 1, ELI: http://data.europa.eu/eli/reg/2003/1059/oj).

(3) Regulation (EC) No 1893/2006 of the European Parliament and of the Council of 20 December 2006 establishing the statistical classification of economic activities NACE Revision 2 and amending Council Regulation (EEC) No 3037/90 as well as certain EC Regulations on specific statistical domains (OJ L 393, 30.12.2006, p. 1, ELI: http://data.europa.eu/eli/reg/2006/1893/oj).

(4) Commission Recommendation of 29 October 2009 on the use of the International Standard Classification of Occupations (ISCO-08) (OJ L 292, 10.11.2009, p. 31, ELI: http://data.europa.eu/eli/reco/2009/824/oj).

(5) International Standard Classification of Education 2011; http://uis.unesco.org/sites/default/files/documents/international-standard-classification-of-education-isced-2011-en.pdf.

## ANNEX I

**I.A LIST AND DESCRIPTION OF VARIABLES**

The individual data concerning each local unit and each employee shall be provided in the form of two data sets with microdata records:

Data set A: Records for the local units

Data set B: Records for the employees

The employee records shall be linked to the local unit records by a key which does not disclose the identity of the business. This could be a sequential number or an existing non-identifying key, provided the same key is used for both the local unit and the employee records (KEY_L). Additionally, for easy identification of an employee, a non-identifying key for each employee (KEY_E) shall be provided which does not identify the person.

Complete information shall be supplied for all variables on all microdata records unless marked ‘ optional ’ or ‘ optional for local units that belong to enterprises with 1 to 9 employees ’.

When information is available for an optional variable, data should preferably be provided for all local units or employees.

All items for the records in data set A and B shall be completed in full. There shall be entries for all individual items, including optional variables, and none shall be left blank. The relevant codes for ‘not provided’ shall be used, see modality codes below.

Zero value ‘ 0 ’ shall be used only for those variables where a zero value may sometimes genuinely occur (e.g. when an employee has no overtime in the reference month).

Where variables relate to monetary values (e.g. hourly, monthly, annual earnings and bonuses, taxes, social security contributions, payments in kind), these shall be expressed in units of the national currency of the country concerned.

**Data set A: Records for the local units**

<table>
<tbody><tr><td>Detailed topic</td><td>Variable identifier</td><td>Variable name</td><td>Modality code or value</td><td>Modality label</td></tr>
<tr><td>Technical items of the survey</td><td>TABLE</td><td>Data set identification</td><td>A</td><td>Information on the local unit</td></tr>
<tr><td>Technical items of the survey</td><td>YEAR</td><td>Reference year</td><td>4 digits, numeric</td><td>Reference year</td></tr>
<tr><td>Technical items of the survey</td><td>KEY_L</td><td>Key attached to a given local unit</td><td>6 characters, alpha-numeric</td><td>Key attached to a given local unit (either numbers or letters or a combination of both)</td></tr>
<tr><td>Technical items of the survey</td><td>A51</td><td>Grossing-up factor for the local unit</td><td>Numeric</td><td>Weight of the local unit: grossing-up factor for the local unit (with 2 digits of decimals separated by a dot)</td></tr>
<tr><td rowspan="2">Technical items of the survey</td><td rowspan="2">KEY_B</td><td rowspan="2">Key attached to a given enterprise (optional)</td><td>6 characters, alpha-numeric</td><td>Key attached to a given enterprise (either numbers or letters or a combination of both)</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
<tr><td>Employer’s characteristics</td><td>A11</td><td>Geographical location of the local unit (NUTS-1)</td><td>3 characters, alpha-numeric</td><td>NUTS 1 region</td></tr>
<tr><td rowspan="6">Employer’s characteristics</td><td rowspan="6">A12</td><td rowspan="6">Size of the enterprise to which the local unit belongs</td><td>E1_9</td><td>1 to 9</td></tr>
<tr><td>E10_49</td><td>10 to 49</td></tr>
<tr><td>E50_249</td><td>50 to 249</td></tr>
<tr><td>E250_499</td><td>250 to 499</td></tr>
<tr><td>E500_999</td><td>500 to 999</td></tr>
<tr><td>E1000</td><td>1 000 or more employees</td></tr>
<tr><td>Employer’s characteristics</td><td>A13</td><td>Principal economic activity of the local unit</td><td>3 characters, alpha-numeric</td><td>Economic activity Coded at 2-digit level/divisions of NACE preceded by a character </td></tr>
<tr><td rowspan="2">Employer’s characteristics</td><td rowspan="2">A14</td><td rowspan="2">Form of economic and financial control of the enterprise to which the local unit belongs</td><td>A</td><td>Public control</td></tr>
<tr><td>B</td><td>Private control</td></tr>
<tr><td rowspan="7">Employer’s characteristics</td><td rowspan="7">A15</td><td rowspan="7">Collective pay agreement</td><td>A</td><td>National level or inter-confederal agreement</td></tr>
<tr><td>B</td><td>Industry agreement</td></tr>
<tr><td>C</td><td>Agreement for individual industries in individual regions</td></tr>
<tr><td>D</td><td>Enterprise or single employer agreement</td></tr>
<tr><td>E</td><td>Agreement applying only to the employees in one local unit</td></tr>
<tr><td>F</td><td>Any other type of agreement</td></tr>
<tr><td>N</td><td>No collective pay agreement</td></tr>
<tr><td rowspan="2">Employer’s characteristics</td><td rowspan="2">A16</td><td rowspan="2">Total number of employees in the local unit in the reference month (optional)</td><td>1-9999999</td><td>Number of employees</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="3">Employer’s characteristics</td><td rowspan="3">A17</td><td rowspan="3">Affiliation of the local unit to a group of enterprises (optional)</td><td>Y</td><td>Yes</td></tr>
<tr><td>N</td><td>No</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
<tr><td rowspan="5">Employer’s characteristics</td><td rowspan="5">A18</td><td rowspan="5">Institutional sector of the enterprise (optional for local units that belong to enterprises with 1 to 9 employees)</td><td>S11</td><td>Non-financial corporations</td></tr>
<tr><td>S12</td><td>Financial corporations</td></tr>
<tr><td>S13</td><td>General government</td></tr>
<tr><td>S15</td><td>Non-profit institutions serving households</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
</tbody>
</table>

**Data set B: Records for the employees**

<table>
<tbody><tr><td>Detailed topic</td><td>Variable identifier</td><td>Variable name</td><td>Modality code or value</td><td>Modality label</td></tr>
<tr><td>Technical items of the survey</td><td>TABLE</td><td>Data set identification</td><td>B</td><td>Information on the individual employee</td></tr>
<tr><td>Technical items of the survey</td><td>YEAR</td><td>Reference year</td><td>4 digits, numeric</td><td>Reference year</td></tr>
<tr><td>Technical items of the survey</td><td>KEY_E</td><td>Key attached to a given employee</td><td>6 characters, alpha-numeric</td><td>Key attached to a given employee (either numbers or letters or a combination of both)</td></tr>
<tr><td>Technical items of the survey</td><td>B52</td><td>Grossing-up factor for the employee</td><td>Numeric</td><td>Weight of the employee: grossing-up factor for the employee (with 2 digits of decimals separated by a dot)</td></tr>
<tr><td>Technical items of the survey</td><td>KEY_L</td><td>Key attached to the local unit the employee belongs to</td><td>6 characters, alpha-numeric</td><td>Key attached to the local unit the employee belongs to (either numbers or letters or a combination of both)</td></tr>
<tr><td rowspan="2">Employee’s characteristics</td><td rowspan="2">B21</td><td rowspan="2">Sex</td><td>F</td><td>Female</td></tr>
<tr><td>M</td><td>Male</td></tr>
<tr><td>Employee’s characteristics</td><td>B22</td><td>Year of birth</td><td>4 digits, numeric</td><td>Year of birth</td></tr>
<tr><td>Employee’s characteristics</td><td>B23</td><td>Occupation in the reference month</td><td>3 characters (2 characters for local units that belong to enterprises with 1 to 9 employees), alpha-numeric </td><td>Occupation Coded at 3-digit level/minor groups of ISCO preceded by two characters  (Coded at 2-digit level/sub-major groups of ISCO for local units that belong to enterprises with 1 to 9 employees) </td></tr>
<tr><td rowspan="3">Employee’s characteristics</td><td rowspan="3">B24</td><td rowspan="3">Managerial / supervisory position (optional)</td><td>Y</td><td>Yes (the employee has some form of management function)</td></tr>
<tr><td>N</td><td>No</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
<tr><td rowspan="4">Employee’s characteristics</td><td rowspan="4">B25</td><td rowspan="4">Educational attainment level</td><td>G1</td><td>Low education (No formal education or below ISCED 1, ISCED 1 Primary education, ISCED 2 Lower secondary education) </td></tr>
<tr><td>G2</td><td>Medium education (ISCED 3 Upper secondary education, ISCED 4 Post-secondary non-tertiary education) </td></tr>
<tr><td>G3</td><td>Tertiary education – up to 4 years (ISCED 5 Short-cycle tertiary education, ISCED 6 Bachelor’s or equivalent level) </td></tr>
<tr><td>G4</td><td>Tertiary education – more than 4 years (ISCED 7 Master’s or equivalent level, ISCED 8 Doctoral or equivalent level) </td></tr>
<tr><td rowspan="2">Employee’s characteristics</td><td rowspan="2">B26</td><td rowspan="2">Length of service in the enterprise (optional for local units that belong to enterprises with 1 to 9 employees) </td><td>0-60</td><td>Length of service in the enterprise (in years)</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Employee’s characteristics</td><td rowspan="2">B27</td><td rowspan="2">Contractual working time (full-time or part-time)</td><td>FT</td><td>Full-time employee</td></tr>
<tr><td>PT</td><td>Part-time employee</td></tr>
<tr><td>Employee’s characteristics</td><td>B271</td><td>Share of a full-timer’s normal hours</td><td>0.01-100.00</td><td>% share of a full-timer’s normal hours (with 2 digits of decimals separated by a dot)</td></tr>
<tr><td rowspan="3">Employee’s characteristics</td><td rowspan="3">B28</td><td rowspan="3">Type of employment contract</td><td>A</td><td>Indefinite duration/permanent</td></tr>
<tr><td>B</td><td>Fixed duration (excluding apprentices, including paid trainees and interns)</td></tr>
<tr><td>C</td><td>Apprentice</td></tr>
<tr><td rowspan="5">Employee’s characteristics</td><td rowspan="5">B29</td><td rowspan="5">Citizenship and residence (optional)</td><td>A</td><td>Resident with national citizenship</td></tr>
<tr><td>B</td><td>Resident with foreign citizenship</td></tr>
<tr><td>C</td><td>Non-resident (commuter from another country) with national citizenship</td></tr>
<tr><td>D</td><td>Non-resident (commuter from another country) with foreign citizenship</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
<tr><td>Working periods</td><td>B31</td><td>Number of weeks in the reference year to which the gross annual earnings relate</td><td>0.01-53.00</td><td>Number of weeks in the reference year to which the gross annual earnings relate (with 2 digits of decimals separated by a dot)</td></tr>
<tr><td>Working periods</td><td>B32</td><td>Number of hours paid during the reference month</td><td>1-744</td><td>Number of hours paid during the reference month</td></tr>
<tr><td rowspan="2">Working periods</td><td rowspan="2">B321</td><td rowspan="2">Number of overtime hours paid in the reference month (optional for local units that belong to enterprises with 1 to 9 employees)</td><td>0-744</td><td>Number of overtime hours paid in the reference month</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="6">Working periods</td><td rowspan="6">B322</td><td rowspan="6">Pay schedule (optional)</td><td>H</td><td>Hourly</td></tr>
<tr><td>D</td><td>Daily</td></tr>
<tr><td>W</td><td>Weekly</td></tr>
<tr><td>M</td><td>Monthly</td></tr>
<tr><td>O</td><td>Other</td></tr>
<tr><td>OPT</td><td>Not provided</td></tr>
<tr><td rowspan="2">Working periods</td><td rowspan="2">B33</td><td rowspan="2">Annual days of holiday leave (optional)</td><td>0-366</td><td>Annual days of holiday leave (in full days)</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Working periods</td><td rowspan="2">B34</td><td rowspan="2">Other annual days of paid absence (optional)</td><td>0-366</td><td>Other annual days of paid absence</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td>Earnings</td><td>B41</td><td>Gross annual earnings in the reference year</td><td>1-99999999</td><td>Gross annual earnings in the reference year</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B411</td><td rowspan="2">Annual bonuses and allowances not paid at each pay period (optional for local units that belong to enterprises with 1 to 9 employees)</td><td>0-99999999</td><td>Annual bonuses and allowances not paid at each pay period</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B412</td><td rowspan="2">Annual payments in kind (optional)</td><td>0-99999999</td><td>Annual payments in kind</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td>Earnings</td><td>B42</td><td>Gross earnings in the reference month</td><td>1-99999999</td><td>Gross earnings in the reference month</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B421</td><td rowspan="2">Earnings related to overtime (optional for local units that belong to enterprises with 1 to 9 employees)</td><td>0-99999999</td><td>Earnings related to overtime</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B422</td><td rowspan="2">Special payments for shift work (optional for local units that belong to enterprises with 1 to 9 employees)</td><td>0-99999999</td><td>Special payments for shift work</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B423</td><td rowspan="2">Compulsory social security contributions and taxes paid by the employer on behalf of the employee (optional)</td><td>0-99999999</td><td>Compulsory social security contributions and taxes paid by the employer on behalf of the employee</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B4231</td><td rowspan="2">Compulsory social security contributions paid by the employer on behalf of the employee (optional)</td><td>0-99999999</td><td>Compulsory social security contributions paid by the employer on behalf of the employee</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td rowspan="2">Earnings</td><td rowspan="2">B4232</td><td rowspan="2">Taxes paid by the employer on behalf of the employee (optional)</td><td>0-99999999</td><td>Taxes</td></tr>
<tr><td>-1</td><td>Not provided</td></tr>
<tr><td>Earnings</td><td>B43</td><td>Average gross hourly earnings in the reference month</td><td>0.01-999999.99</td><td>Average gross hourly earnings in the reference month (with 2 digits of decimals separated by a dot)</td></tr>
</tbody>
</table>

**I.B TECHNICAL SPECIFICATIONS**

**1\. Information on the local unit to which the sampled employees are attached**

**1.1. Form of economic and financial control of the enterprise to which the local unit belongs (A14)**

This variable distinguishes between the categories ‘public control’ and ‘private control’. The first category refers to any undertaking over which the public authorities may exercise, directly or indirectly, a dominant influence by virtue of their ownership of it, their financial participation therein, or the rules which govern it. A dominant influence (or control) on the part of the public authorities should be presumed when these authorities directly or indirectly:

— hold the major part of the undertaking’s subscribed capital (> 50 %), or

— control the majority of the votes attached to shares issued by the undertaking or can appoint more than half of the members of the undertaking’s administrative, managerial or supervisory body.

The second category is defined analogously. Balanced public and private ownership (50/50 ‘shared control’) is very rare in practice. Such cases should therefore not be coded separately and should, if they occur, be treated as being under ‘private control’.

**1.2. Collective pay agreement (A15)**

This variable provides information on the kinds of collective pay agreements, among those listed below that cover more than 50 % of the employees in the local unit:

— an agreement at national level, or an inter-confederal agreement, covering employees of more than one industry, and usually signed by one or more trade-union confederations and by one or more national employers’ organisations,

— an industry agreement setting the terms and conditions of employment for all or most workers and employees in an individual industry or economic sector,

— an agreement for individual industries in individual regions,

— an enterprise or single employer agreement covering only those employees with the same employer, regardless of size. The agreement may cover only certain local units or groups of employees within the enterprise,

— an agreement applying only to the employees in one local unit,

— any other type of agreement not covered above,

— no collective pay agreement covers 50 % or more of the employees in the local unit.

Instead of directly asking for the type of collective agreement, the unit may be asked what collective provisions are applied and the type of collective agreement determined on the basis of the answers. Even if several categories may apply simultaneously, only one of the above categories is to be chosen, namely the one covering more than 50 % of the employees in the local unit.

**1.3. Total number of employees in the local unit in the reference month (A16) (optional)**

This variable represents a head count of the total number of employees in the reference month (e.g. on 1 or 31 October) and covers all employees, including apprentices, paid trainees and interns (for the concept ‘employees’, see 2.1.).

**1.4. Affiliation of the local unit to a group of enterprises (A17) (optional)**

This variable indicates whether a local unit belongs to a group of enterprises. The group of enterprises is a statistical unit defined in Council Regulation (EEC) No 696/93 (1). The group of enterprises should be considered at world level. In most cases the local unit belongs to an enterprise which is not controlled by any national or foreign group. If local units belong to an enterprise group, this is generally well known. A practical guideline that can be given to respondents is whether the accounts of the enterprise concerned are fully consolidated in the accounts of its group of enterprises.

**1.5. Institutional sector of the enterprise (A18) (optional for local units that belong to enterprises with 1 to 9 employees)**

This variable records the institutional sector of the enterprise, as defined in ESA 2010, §2.31, from which only the following sectors apply:

— S.11 Non-financial corporations

— S.12 Financial corporations

— S.13 General government

— S.15 Non-profit institutions serving households

**1.6. Grossing-up factor for the local unit (A51)**

The grossing-up factor for the local unit is the number of local units in the population represented by a local unit record in the sample. It is used to extrapolate the variables on local units from the sample to the whole population.

Grossing-up factors are specific to each local unit, depending on elements such as the sampling rate, sampling design, non-response, a posteriori calibration, etc. The total of all grossing-up factors, over the whole sample of local units, is equal to the number of local units in the population.

**2\. Information on the individual characteristics of each employee in the sample relating to the reference month**

**2.1. Employees**

Employees are all persons irrespective of nationality, residency or time worked in a Member State, who have a direct employment relationship with an employer, established by a formal contract or an informal agreement, and who receive remuneration, irrespective of the type of work performed, the number of hours worked (full-time or part-time) or the duration of the contract or agreement (fixed or indefinite, including seasonal); the remuneration of employees can take the form of wages and salaries, and includes bonuses, pay for piecework and shift work, allowances, fees, commission and remuneration in kind.

This concept of employees covers manual and non-manual workers and management personnel in the private and public sectors.

The following list gives illustrative examples of categories of employees that are included:

— civil servants (2) (including from armed forces (3)),

— sales representatives, provided they are on the payroll and receive another form of remuneration in addition to any commission,

— paid working proprietors,

— apprentices,

— paid trainees and interns (articled clerks, student nurses, research or teaching assistants, hospital interns, etc.) who have a formal commitment whereby they contribute to the unit’s production process in return for remuneration,

— interim or temporary workers (e.g. secretarial staff) recruited, employed and remunerated by employment agencies to work elsewhere, often for temporary periods,

— seasonal and occasional workers, if they have a formal or informal agreement with the enterprise or local unit and pre-defined working hours,

— employees for whom labour costs were incurred, for the work done during the reference year, but who were temporarily not at work because of illness or injury, holiday or vacation, strike or lock-out, educational or training leave, maternity or parental (4) leave, reduced economic activity, suspension of work due to bad weather, mechanical breakdowns, lack of materials, fuels or power, or other temporary absence with or without leave,

— those working abroad if they continue to receive remuneration from the employer,

— outworkers (5), including home workers and teleworkers, if there is an explicit agreement that such workers are remunerated, at least partially, on the basis of the work done: that is, the amount of labour (in hours actually worked) which is contributed as an input into some process of production [ESA 2010, §11.13(g)].

The following categories should be excluded:

— sales representatives and other persons who are wholly remunerated by way of fees or commission, are not on the payroll, or who are self-employed,

— owners, directors or managers whose remuneration wholly takes the form of a share in profits,

— family workers who are not employees (as defined above) of the enterprise or local unit,

— own-account workers,

— outworkers exclusively paid on piecework rates [ESA 2010, §4.07(e)] bound by a commercial contract (as opposed to a formal, informal or implicit employment contract),

— unpaid voluntary workers (e.g. those who typically work for non-profit institutions such as charities).

Employees to be included in the topic ‘structure of earnings’ are those who actually received remuneration for working during the reference month. Employees who did not receive such remuneration should be excluded.

**2.2. Sex (B21)**

Sex is the combination of biological and physiological characteristics that define a person to be either male or female. In cases where the biological sex of a person is not known, the information may be replaced by either the information from administrative data or the self-declared sex (survey data).

**2.3. Year of birth (B22)**

This variable records the year of birth of the surveyed employee.

**2.4. Occupation in the reference month (B23)**

This variable records the occupation as coded according to the International Standard Classification of Occupations (ISCO). This information is collected at the 3-digit level except for local units that belong to enterprises with 1 to 9 employees (2-digit level with the 3-digit level being optional). The essential information for determining the occupation is usually the employee’s job title and a description of the main tasks undertaken in the course of his/her duties.

Paid trainees or students with an employment contract and apprentices are classified in the occupation for which they carry out their apprenticeship, traineeship or internship.

**2.5. Managerial / supervisory position (B24) (optional)**

This variable indicates whether an employee has some form of managerial or supervisory function. The word ‘managerial’ is not identical to ‘supervisory’ because some managers do not supervise other employees. A supervisory position can occur in any of the ISCO groups, including manual workers.

Managerial functions are related to determining, formulating, implementing, directing or advising policies and activities of enterprises or institutions. They often include supervisory responsibilities.

A person is considered to have a supervisory position when he or she supervises the work of at least one person (other than apprentices, paid trainees or interns). Typically, such a person might have a job title/description of ‘foreman’ or ‘supervisor’ together with the name of the occupation.

**2.6. Educational attainment level (B25)**

The educational attainment level of an individual is the highest ISCED (International Standard Classification of Education) level successfully completed. The successful completion of an education programme is validated by a qualification officially recognised by the relevant national education authorities or recognised as equivalent to another qualification of formal education. In countries where education programmes, in particular those belonging to ISCED levels 1 and 2, do not lead to a qualification, the criterion of full attendance of the programme and normally gaining access to a higher level of education may be used instead. When determining the highest level, both general and vocational education should be taken into consideration.

**2.7. Length of service in the enterprise (B26) (optional for local units that belong to enterprises with 1 to 9 employees)**

The total length of service in the reference month should be based on the number of completed years of service. Any point of time during the reference month will suffice as a qualifying date (e.g. 1 or 31 October). The total length of service relates to the period since the employee joined the enterprise, which may have been in another local unit. Where enterprises have been merged or there have been changes of ownership, the length of service is to be recorded as counted by the enterprise.

Only fully completed years of service should be counted. For instance, a total service of 5 years and 10 months should be reported as 5 years.

Short periods away from work of less than 12 months (e.g. on maternity or sick leave) should be included as part of the total service (on the opposite, career breaks exceeding one year should be subtracted).

**2.8. Contractual working time (full-time or part-time) (B27)**

Full-time employees are those whose regular working hours are the same as the collectively agreed or customary hours worked in the local unit under consideration, even if their contract is for less than one year.

Part-time employees are those whose regular working hours are less than the collectively agreed or customary hours worked in the local unit, whether daily, weekly or monthly (half-day, three quarter time, four fifths time, etc.).

Apprentices, paid trainees and interns can be either full-time or part-time employees.

**2.9. Share of a full-timer’s normal hours (B271)**

For a full-time employee, this share is always 100 %. For a part-time employee, the hours contractually worked should be expressed as a percentage of the number of normal hours worked by a full-time employee in the local unit (in a job equivalent to that of the part-time employee).

**2.10. Type of employment contract (B28)**

The following information on the type of employment contract is requested:

— indefinite duration/permanent,

— fixed duration (excluding apprentices, including paid trainees and interns),

— apprentice.

An indefinite duration/permanent contract of employment is a contract between the employee and the employer, for which the actual duration of the contract has not been agreed in advance and that guarantees a minimum number of hours worked.

An employment contract is of fixed duration if it was the intention of the employer and employee that the duration of the contract was to be determined by certain conditions such as a definite time schedule for the completion of the work, the completion of a certain task, or the return to work of another employee who was currently being replaced. Apprentices are excluded, paid trainees and interns are included.

Apprentices, paid trainees and interns are employees who perform any activity to produce goods or provide services for others, in order to acquire workplace experience or skills in a trade or profession and receive payment in return for work performed. Acquiring workplace experience or skills may occur through traditional, formal or informal arrangements whether or not a specific qualification or certification is issued. They are usually remunerated at a reduced rate compared to fully qualified workers. They exclude workers who are: (a) undergoing periods of probation associated with the start of a job; (b) undertaking general on-the-job training or life-long learning while in employment.

In addition, apprentices should meet the following conditions:

(a) Be engaged in a formal education programme shorter than 6 years.

(b) Have an apprenticeship contract that lasts more than 6 months, alternates practical training at the workplace with theoretical education in an educational institution and leads to a formal qualification.

**2.11. Citizenship and residence (B29) (optional)**

The country of the person’s main citizenship, defined as the particular legal bond between an individual and his or her State, acquired by birth or naturalisation, whether by declaration, choice, marriage or other means according to national legislation. A person with two or more citizenships should be allocated to only one country of citizenship, to be determined in the following order of priority: (1) reporting country, (2) if the person does not have the citizenship of the reporting country: other Member State, (3) if the person does not have the citizenship of a Member State: other country outside the Union.

One of the following should be selected:

— resident with national citizenship,

— resident with foreign citizenship,

— non-resident (commuter from another country) with national citizenship,

— non-resident (commuter from another country) with foreign citizenship.

**3\. Information on working periods for each employee in the sample**

**3.1. Number of weeks in the reference year to which the gross annual earnings relate (B31)**

This variable refers to the employee’s working time paid during the year and should correspond to the actual gross annual earnings (variable B41). It is used to gross up the actual gross annual earnings and the annual bonuses and allowances where the employee has worked for less than a full year, i.e. less than 52,14 weeks.

Part-time employees should be treated like full-time employees, irrespective of the hours worked. ‘52.14’ should be recorded if a part-timer has been paid for a full year and, e.g. ‘26.07’ if he/she has been paid for 6 months.

**3.2. Number of hours paid during the reference month (B32)**

The total number of hours paid by the employer during the reference month should not be the number of hours in a standard working month.

Hours actually paid include all normal and overtime hours worked and remunerated by the employer during the month. Hours not worked but nevertheless paid should be counted as ‘paid hours’ (e.g. for annual leave, public holidays, paid sick leave, paid vocational training, paid special leave, other hours paid, including time off for medical examinations, births, weddings, funerals, moving house). For employees paid on a daily rate, hours paid should be calculated as the average number of hours paid per day worked multiplied by the number of working days in the reference month.

For employees paid on a weekly rate, hours paid should be calculated as the average number of hours paid per week worked multiplied by 31/7 = 4,43, the number of weeks in the reference month. A similar calculation can be done for employees paid on a bi-weekly rate (with 2,21 as the multiplicative factor).

In the case of employees paid on a monthly rate, hours paid should be based on the contractual hours paid for a standard month, complemented with the overtime hours paid during the reference month.

Variable B32 should be consistent with the gross earnings for the reference month (variable B42). This implies that hours paid by the employer at a reduced rate for periods of absence are not counted, neither in variable B32 nor B42. Moreover, if the employee’s paid hours are affected by unpaid absence, they should be adjusted to obtain paid hours for a full month using the same correction factor as for variable B42.

**3.3. Number of overtime hours paid in the reference month (B321) (optional for local units that belong to enterprises with 1 to 9 employees)**

Overtime hours include those worked in addition to those of the normal or conventional working month and that are paid at a higher rate than normal working hours. If, for example, four hours are paid at a rate of 1,5 times the normal rate, 4 hours should be recorded and not 6. Time off in lieu of unpaid work periods and travel time are not regarded as overtime.

Variable B321 should be consistent with overtime earnings in the reference month (variable B421). Hence, only those overtime hours corresponding to overtime pay registered in B321 should be included.

Moreover, if the employee’s paid hours are affected by unpaid absence, they should be adjusted to obtain paid hours for a full month using the same correction factor as for variable B421.

**3.4. Annual days of holiday leave (B33) (optional)**

This refers to the total number of paid annual holidays, excluding sick leave and public holidays, expressed in days. It relates to the annual total of all normal paid leave days, including those granted to the employee on the grounds of age, performance of special duties, seniority, etc.

It is recognised that many employers are unable to state the number of holidays actually taken by the employee during the year. For this reason, variable B33 refers to annual holiday entitlement, which acts as a proxy for annual holidays actually taken.

The following are not regarded as holidays:

— sick leave,

— training leave,

— paid special leave granted for personal reasons,

— additional time off granted under working time reduction agreements.

For purposes of comparison, each week of holiday corresponds to five days. Saturdays and Sundays should not be included. For example, if a full-time employee is normally entitled to five weeks’ annual holiday, this corresponds to 25 days.

In contrast, five weeks’ holiday entitlement for a part-timer who works 60 % of the normal full-timer’s hours (variable B271) represents an entitlement to only 15 ‘full’ days of leave.

**3.5. Other annual days of paid absence (B34) (optional)**

This variable is again expressed in days. It includes, for example:

— the total number of paid sick leave days actually taken during the year,

— paid special leave granted for personal reasons,

— public holidays.

It excludes paid days which are treated as being equivalent to days actually worked, such as paid annual days spent by the employee on vocational training.

**4\. Information on earnings for each employee in the sample**

The employees to be included in all the following variables on annual, monthly and hourly earnings are those who actually received remuneration for work during the reference month. Employees who did not receive remuneration in the reference month should be excluded.

Further, if the employee’s gross earnings in the reference month (variable B42) are affected by unpaid absence (due to sickness, maternity or study leave, etc.) and cannot be suitably adjusted in order to provide a satisfactory estimate of the employee’s earnings for a full month, then that employee should also be excluded.

The grossing-up factors for the employees (variable B52) should strictly relate to those sampled employees for whom soundly based estimates of gross monthly earnings can be provided. The other employees should be excluded from the sample and the grossing-up factors should be corrected accordingly.

Finally, it should be noted that none of the variables defined below should be calendar adjusted.

**4.1. Gross annual earnings in the reference year (B41)**

Gross annual earnings cover remuneration in cash and in kind payable by the employer to the employee in return for the work done during the reference year before any tax deductions and social security contributions payable by wage earners and retained by the employer.

They exclude the amounts paid by the employer and reimbursed in full by e.g. social security.

The main difference between annual and monthly earnings is that annual earnings are not only the sum of the direct remuneration, bonuses and allowances paid to an employee in each pay period. Annual earnings hence usually exceed the figure produced by multiplying the ‘standard monthly package’ by 12.

The ‘standard monthly package’ includes those bonuses and allowances which are paid in every pay period, even if the amount for these ‘regular’ bonuses and allowances varies, but excludes bonuses and allowances not accruing in every pay period. Furthermore, monthly earnings leave payments in kind out of consideration. However, annual earnings also cover all ‘non-standard payments’, i.e. payments not occurring in each pay period (variable B411), and payments in kind (variable B412).

Data for variable B41 should be provided for all employees for whom gross monthly earnings (variable B42) can be supplied, i.e. variable B41 should not be provided for employees for whom an estimate of an employee’s gross monthly earnings is not feasible. These employees should be excluded from the sample and the weights adjusted accordingly.

It does not matter if the employee’s earnings do not always relate to a full year. Some employees will have periods of unpaid absence, or will have joined or left the enterprise during the year. The actual gross earnings in the reference year are required. When variable B31 (number of weeks to which the gross annual earnings relate) is less than 52,14 weeks, variable B31 should be used to gross up variable B41 and its components.

**4.2. Annual bonuses and allowances not paid at each pay period (B411) (optional for local units that belong to enterprises with 1 to 9 employees)**

This variable covers all items (direct remuneration, bonuses and allowances) which do not occur in each pay period, such as:

— 13th or 14th month pay, Christmas and New Year bonuses [ESA 2010, §4.03(d)],

— holiday bonuses,

— quarterly or annual company bonuses,

— productivity bonuses depending on pre-set targets, employee recognition awards, recruitment incentives,

— leaving or retirement bonuses, where those payments are not linked to a collective agreement nor required by law [ESA 2010, §4.03(i)],

— back-dated arrears.

**4.3. Annual payments in kind (B412) (optional)**

This variable refers to an estimate of the value of all goods and services made available to employees through the employer during the reference year, free of charge or at a reduced price. Included are company products, staff housing, company cars, stock options and share purchase schemes. If information is available from personal income taxation on wages and salaries in kind, this may be used as a proxy.

When variable B31 is less than 52,14 weeks, variable B412 should not be adjusted.

**4.4. Gross earnings in the reference month (B42)**

This variable covers remuneration in cash paid during the reference month before any tax deductions and social security contributions payable by wage earners and retained by the employer. Variable B42 should be consistent with the number of hours paid during the reference month (variable B32).

The following elements are included:

— all payments relating to this period (even if paid outside the representative month), including any overtime pay, shift premium, bonus, commission, etc.,

— payments for overtime, allowances for teamwork, night work, weekend work, commissions, etc.,

— bonuses and allowances paid regularly in each pay period, even if the amount varies monthly,

— payments for periods of absence and work stoppage paid for entirely by the employer,

— family allowances and other gratuities in cash fixed by collective agreements or voluntarily agreed,

— payments to employees’ savings scheme.

The following are excluded:

— payments paid in this period but relating to other periods, such as arrears, advances or pay for holiday or sickness absences outside this period,

— periodic bonuses and gratuities not paid regularly at each pay date,

— payments for periods of absence paid by the employer at a reduced rate,

— statutory family allowances,

— allowances for work clothes or tools,

— reimbursements or payments for travel, subsistence, etc., and expenses incurred in carrying out the employer’s business,

— payments in kind.

Where the employee’s gross monthly earnings are affected by unpaid absence (due to sickness, maternity or study leave, etc., or simply because the employee joined or left the enterprise during the reference month), they should be suitably adjusted in order to provide an estimate of the employee’s earnings for a full month. If, for instance, it is known that an employee had 20 % of the reference month as unpaid absence, the gross monthly earnings actually paid (at full rate) for the period of presence should be multiplied by the correction factor 1,25 [100/(100-20)].

Where it is not feasible to adjust the employee’s gross monthly earnings so that the estimated figure corresponds to a full month’s earnings, then the employee should be excluded from the sample.

**4.5. Earnings related to overtime (B421) (optional for local units that belong to enterprises with 1 to 9 employees)**

The amount of overtime earnings paid for overtime hours. The full rate should be counted, not just the premium element added to the normal hourly rate. Variable B421 should be consistent with variable B321 (number of overtime hours paid in the reference month).

**4.6. Special payments for shift work (B422) (optional for local units that belong to enterprises with 1 to 9 employees)**

This relates to the special premium payments for shift work, night work or weekend work where these are not treated as overtime. The amount to include is the premium element or supplementary payment, not the total payment for such shift work.

**4.7. Compulsory social security contributions and taxes paid by the employer on behalf of the employee (B423) (optional)**

This variable refers to the total amount of compulsory social contributions and taxes paid by the employer on behalf of the employee to government authorities during the reference month. This information is requested in order to obtain net monthly earnings for each employee.

If the employee’s monthly earnings are affected by unpaid absence, then variable B423 (together with its sub-components B4231 and B4232) should be adjusted to obtain the estimated deductions for a full month.

**4.8. Compulsory social security contributions paid by the employer on behalf of the employee (B4231) (optional)**

This refers to the amount of the employee’s social security contributions laid down by law or by collective agreements and withheld by the employer.

**4.9. Taxes paid by the employer on behalf of the employee (B4232) (optional)**

This refers to the amount of all taxes on the employee’s earnings withheld by the employer for the reference month and paid by the employer to the tax authorities on behalf of the employee.

**4.10. Average gross hourly earnings in the reference month (B43)**

The figure required is the average gross earnings per hour paid to the employee in the reference month. This figure should be consistent with the average gross hourly earnings derived from gross earnings for the reference month (variable B42) divided by the number of hours paid during the same period (variable B32).

**4.11. Grossing-up factor for employees (B52)**

The grossing-up factor for employees is the number of employees in the population represented by a given employee record. It is used to extrapolate the variables on employees from the sample to the whole population. Grossing-up factors are specific to each employee, depending on elements such as the sampling rate, sampling design, non-response, a posteriori calibration, etc. The total of all grossing-up factors, over the whole sample of employees, is equal to the number of employees in the population.

(1) Council Regulation (EEC) No 696/93 of 15 March 1993 on the statistical units for the observation and analysis of the production system in the Community (OJ L 76, 30.3.1993, p. 1, ELI: http://data.europa.eu/eli/reg/1993/696/oj).

(2) This category includes ‘civil servants and other government employees whose terms and conditions of employment are laid down by public law’ [ESA 2010, §11.13(b)].

(3) ‘Members of the armed forces are those personnel who are currently serving in the armed forces, including auxiliary services, whether on a voluntary or compulsory basis, and who are not free to accept civilian employment and are subject to military discipline. Included are regular members of the army, navy, air force and other military services, as well as conscripts enrolled for military training or other service for a specified period’ (International Standard Classification of Occupations – ISCO-08).

(4) Employees on parental leave should be included provided there was at least one hour paid by the employer to the employee during the reference month. In the case of employees who are replaced during their parental leave, one should record:

(a) Only one employee in the number of employees, this avoiding the double counting of the job-holder and his/her substitute;

(b) Earnings for both the job-holder and his/her substitute, during the reference period;

(c) Hours paid for both the job-holder and his/her substitute for the reference month.

(5) An outworker is a person who agrees to work for a particular enterprise or to supply a certain quantity of goods or services to a particular enterprise by prior arrangement or contract with that enterprise, but whose place of work is not within it.

## ANNEX II — PRECISION TARGETS

(1)

Member States shall aim at keeping the coefficient of variation below 1 %, for the mean hourly earnings measured for all (part-time and full-time) employees, working in a resident local unit of 1 or more employees belonging to the total of all NACE sections in the scope of the topic ‘structure of earnings’ as defined in Article 6(3) of Regulation (EU) 2025/941.

(2)

Member States shall aim at keeping the coefficient of variation below 10 %, for the mean hourly earnings measured for all (part-time and full-time) employees, working in a resident local unit of 1 or more employees, for each NACE section within the scope of the topic ‘structure of earnings’ as defined in Article 6(3) of Regulation (EU) 2025/941, except those representing less than 1 % of the total monthly earnings recorded in the reference year.

ELI: http://data.europa.eu/eli/reg_impl/2025/1526/oj

ISSN 1977-0677 (electronic edition)
