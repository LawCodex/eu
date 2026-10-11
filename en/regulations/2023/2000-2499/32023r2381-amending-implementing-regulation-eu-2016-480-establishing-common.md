---
title: "Commission Implementing Regulation (EU) 2023/2381 of 29 September 2023 amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings"
identifier: "32023R2381"
eli: "http://data.europa.eu/eli/reg_impl/2023/2381/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2023-09-29
entry_into_force: 2025-01-01
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2381"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2023/2381 of 29 September 2023 amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings

**COMMISSION IMPLEMENTING REGULATION (EU) 2023/2381**

**of 29 September 2023**

**amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EC) No 1071/2009 of the European Parliament and of the Council of 21 October 2009 establishing common rules concerning the conditions to be complied with to pursue the occupation of road transport operator and repealing Council Directive 96/26/EC (1), and in particular Article 16(6) thereof,

After consulting the Road Transport Committee referred to in Article 42(1) of Regulation (EU) No 165/2014 of the European Parliament and of the Council (2),

Whereas:

(1) Article 16(1) of Regulation (EC) No 1071/2009 requires the Member States to keep a national electronic register of road transport undertakings that have been authorised by a competent authority to engage in the occupation of road transport operator.

(2) Article 16(5) and (6) of Regulation (EC) No 1071/2009 requires the national electronic registers to be interconnected, mandating the Commission to adopt common rules concerning such interconnection.

(3) Commission Implementing Regulation (EU) 2016/480 (3) sets up an electronic system for the interconnection of the national electronic registers, called the European Registers of Road Transport Undertakings (‘ERRU’). By interconnecting all the national electronic registers, the information contained in each national electronic register is made available to the competent national authorities of all Member States.

(4) Regulation (EC) No 1071/2009 has been amended by Regulation (EU) 2020/1055 (4), now requiring national registers to include additional information on road transport undertakings. Such additional information must also be made available to the competent national authorities of the Member States during roadside checks. Consequently, ERRU should be updated to provide the functionalities that allow the additional information to be exchanged, as well as made available to the relevant authorities.

(5) Implementing Regulation (EU) 2016/480 should therefore be amended accordingly.

HAS ADOPTED THIS REGULATION:

## Article 1

Implementing Regulation (EU) 2016/480 is amended as follows:

(1) In Article 2, the following point is added:

‘(l) “Clean check” means a check where no infringements are detected’;

(2) In Article 5, paragraph 2 is replaced by the following:

‘2. Member States shall grant control bodies in charge of roadside checks access to the Check Transport Undertaking Data functionality.’

;

(3) Annexes II, III, VI and VIII are amended in accordance with the Annex to this Regulation.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 29 September 2023.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 300, 14.11.2009, p. 51.

(2) Regulation (EU) No 165/2014 of the European Parliament and of the Council of 4 February 2014 on tachographs in road transport, repealing Council Regulation (EEC) No 3821/85 on recording equipment in road transport and amending Regulation (EC) No 561/2006 of the European Parliament and of the Council on the harmonisation of certain social legislation relating to road transport (OJ L 60, 28.2.2014, p. 1).

(3) Commission Implementing Regulation (EU) 2016/480 of 1 April 2016 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010 (OJ L 87, 2.4.2016, p. 4).

(4) Regulation (EU) 2020/1055 of the European Parliament and of the Council of 15 July 2020 amending Regulations (EC) No 1071/2009, (EC) No 1072/2009 and (EU) No 1024/2012 with a view to adapting them to developments in the road transport sector (OJ L 249, 31.7.2020, p. 17).

## ANNEX

Annexes II, III, VI and VIII to Implementing Regulation (EU) 2016/480 are amended as follows:

(1) in Annex II, point 1 is replaced by the following:

‘1. The following functionalities shall be provided through ERRU:

1.1. Check Good Repute (CGR): allows the requesting Member State to send a query to one or all responding Member States, to determine the fitness of a transport manager and so the authorisation to operate a transport undertaking.

1.2. Notification of Check Result (NCR): allows the Member State where the check was carried out to notify the result of a check to the Member State of establishment. When a serious infringement has been found during the check, the Member State where the infringement was detected notifies the Member State of establishment through NCR that the transport undertaking has committed a serious infringement, and may request penalties to be applied to the transport undertaking in the Member State of establishment. When no infringement has been detected during the check, NCR allows the Member State where the check has been carried out to notify the Member State of establishment the positive result of the check.

1.3. Check Transport Undertaking Data (CTUD): allows the requesting Member State to send a query to the responding Member State about the following data that are specific to a transport undertaking:

— information about the Community Licence and the certified true copies,

— risk rating and risk rating band,

— number of vehicles at the disposal of the transport undertaking,

— registration number and registration country of the vehicles at the disposal of the transport undertaking,

— number of employees.

1.4. Notification of Unfitness (NU): allows a Member State to inform all other Member States that a transport manager has been declared unfit and that as a result, its certificate of professional competence is no longer valid in any Member State.’;

(2) In Annex III, the Appendix is replaced by the following:

**‘Appendix**

**Minimum requirements for the content of the XML messages**

<table>
<tbody><tr><td colspan="2">Common Header</td><td>Mandatory</td></tr>
<tr><td>Version</td><td>The official version of the XML specifications will be specified through the namespace defined in the message XSD and in the version attribute of the Header element of any XML message. The version number (“n.m”) will be defined as fixed value in every release of the XML Schema Definition file (xsd).</td><td>Yes</td></tr>
<tr><td>Test Identifier</td><td>Optional id for testing. The originator of the test will populate the id and all participants in the workflow will forward/return the same id. In production it should be ignored and will not be used if it is supplied.</td><td>No</td></tr>
<tr><td>Technical Identifier</td><td>A UUID uniquely identifying each individual message. The sender generates a UUID and populates this attribute. This data is not used in any business capacity.</td><td>Yes</td></tr>
<tr><td>Workflow Identifier</td><td>The workflowId is a UUID and should be generated by the requesting Member State. This id is then used in all messages to correlate the workflow.</td><td>Yes</td></tr>
<tr><td>Sent At</td><td>The date and time (UTC) that the message was sent.</td><td>Yes</td></tr>
<tr><td>Timeout</td><td>This is an optional date and time (in UTC format) attribute. This value will be set only by the central hub for forwarded requests and is calculated based on the date/time the initial request has been received by the central hub. This will inform the responding Member State of the time when the request will be timed out. This value is not required in initial requests sent to the central hub and all response messages.</td><td>No</td></tr>
<tr><td>From</td><td>The ISO 3166-1 Alpha 2 code of the Member State sending the message or “EU”.</td><td>Yes</td></tr>
<tr><td>To</td><td>The ISO 3166-1 Alpha 2 code of the Member State to which the message is being sent or “EU”.</td><td>Yes</td></tr>
</tbody>
</table>

**Check Good Repute**

<table>
<tbody><tr><td colspan="2">Check Good Repute Request</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number identifying each individual request.</td><td>Yes</td></tr>
<tr><td>Requesting Competent Authority</td><td>The competent authority that has issued the search request.</td><td>Yes</td></tr>
<tr><td colspan="2">Transport Manager Details</td><td>Yes, if no CPC details</td></tr>
<tr><td>Family Name</td><td>Transport manager’s family name(s) as indicated on the CPC.</td><td>Yes</td></tr>
<tr><td>First Name</td><td>Transport manager’s complete given name as indicated on the certificate of professional competence.</td><td>Yes</td></tr>
<tr><td>Date of Birth</td><td>Transport manager’s birth date in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>Place of Birth</td><td>Transport manager’s place of birth.</td><td>No</td></tr>
<tr><td>Address</td><td>The address, city, postcode and country of the transport manager.</td><td>No</td></tr>
<tr><td colspan="2">CPC Details</td><td>Yes, if no transport manager details</td></tr>
<tr><td>CPC Number</td><td>Number of certificate of professional competence</td><td>Yes</td></tr>
<tr><td>CPC Issue Date</td><td>Date of issuance of the CPC, in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>CPC Issue Country</td><td>Issuing country of the CPC in ISO 3166-1 alpha 2 format.</td><td>Yes</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td colspan="2">Check Good Repute Response</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number matching the business case identifier of the request.</td><td>Yes</td></tr>
<tr><td>Requesting Competent Authority</td><td>The competent authority that has issued the search request.</td><td>Yes</td></tr>
<tr><td>Responding Competent Authority</td><td>The competent authority that has responded to the search request.</td><td>Yes</td></tr>
<tr><td>Status Code</td><td>The status code of the search (e.g. found, not found, error, etc.).</td><td>Yes</td></tr>
<tr><td>Status Message</td><td>An explanatory status description (if necessary).</td><td>No</td></tr>
<tr><td colspan="2">Found Transport Manager Details</td><td>Yes if Status Code is Found</td></tr>
<tr><td>Family Name</td><td>Transport manager’s family name(s) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>First Name</td><td>Transport manager’s complete given name as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Date of Birth</td><td>Transport manager’s birth date in ISO 8601 format (YYYY-MM-DD) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Place of Birth</td><td>Transport manager’s place of birth as recorded in the register.</td><td>No</td></tr>
<tr><td>CPC Number</td><td>Number of certificate of professional competence as recorded in the register.</td><td>Yes</td></tr>
<tr><td>CPC Issue Date</td><td>Date of issuance of the CPC, in ISO 8601 format (YYYY-MM-DD) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>CPC Issue Country</td><td>Issuing country of the CPC in ISO 3166-1 alpha 2 format as recorded in the register.</td><td>Yes</td></tr>
<tr><td>CPC Validity</td><td>Declaration of either “Valid” or “Invalid”</td><td>Yes</td></tr>
<tr><td>Total Managed Undertakings</td><td>The number of transport undertakings with which the transport manager is associated.</td><td>Yes</td></tr>
<tr><td>Total Managed Vehicles</td><td>The total number of vehicles with which the transport manager is associated.</td><td>Yes</td></tr>
<tr><td>Fitness</td><td>Declaration of either “Fit” or “Unfit”.</td><td>Yes</td></tr>
<tr><td>Start Date of Unfitness</td><td>Start date of unfitness of the transport manager in ISO 8601 format (YYYY-MM-DD).</td><td>Yes if “Fitness” is “Unfit”.</td></tr>
<tr><td>End Date of Unfitness</td><td>End date of unfitness of the transport manager in ISO 8601 format (YYYY-MM-DD).</td><td>Yes if “Fitness” is “Unfit”.</td></tr>
<tr><td>Search Method</td><td>The method used to find the transport manager: NYSIIS, CPC, Custom.</td><td>Yes</td></tr>
<tr><td colspan="2">Transport Undertaking (for each found Transport Manager)</td><td>Yes if Managed Undertakings &gt; 0</td></tr>
<tr><td>Transport Undertaking Name</td><td>The name of the transport undertaking (name and legal form) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Address</td><td>The address of the transport undertaking (address, postal code, city, country) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Community Licence Number</td><td>The serial number of the Community licence of the transport undertaking (free text alphanumeric field with length 1 to 20).</td><td>Yes</td></tr>
<tr><td>Community Licence Status</td><td>The status of the community licence of the transport undertaking as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Managed Vehicles</td><td>The number of vehicles managed as recorded in the register.</td><td>Yes</td></tr>
</tbody>
</table>

**Notification of Check Result**

<table>
<tbody><tr><td colspan="2">Notification of Check Result</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number identifying each individual notification.</td><td>Yes</td></tr>
<tr><td>Notifying Competent Authority</td><td>The competent authority that issues the notification.</td><td>Yes</td></tr>
<tr><td colspan="2">Transport Undertaking</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Name</td><td>The name of the transport undertaking being object of the check.</td><td>Yes</td></tr>
<tr><td>Community Licence Number</td><td>The serial number of the community licence or of the certified true copy of the transport undertaking (free text alphanumeric field with length 1 to 20).</td><td>Yes</td></tr>
<tr><td>Vehicle Registration Number</td><td>The vehicle registration number of the vehicle checked</td><td>Yes</td></tr>
<tr><td>Vehicle Registration Country</td><td>The country in which the vehicle checked is registered</td><td>Yes</td></tr>
<tr><td colspan="2">General information about the check</td><td></td></tr>
<tr><td>Date of check</td><td>Date of check in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Clean check</td><td>Yes/No</td><td>Yes</td></tr>
<tr><td colspan="2">Minor infringements</td><td>Yes, if minor infringement(s) detected during the check</td></tr>
<tr><td>Date of minor infringement</td><td>Date of the infringement in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Number of minor infringements</td><td>The number of minor infringements detected.</td><td>Yes</td></tr>
<tr><td colspan="2">Serious infringement</td><td>Yes, if serious infringement detected during the check</td></tr>
<tr><td>Date of Infringement</td><td>Date of the infringement in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Category</td><td>The category of the infringement:<table><tbody><tr><td>—</td><td>MSI: Most serious infringement</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>VSI: Very serious infringement</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>SI: Serious infringement</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
<tr><td>Infringement Type</td><td>In accordance with the classification provided in Annex IV to Regulation (EC) No 1071/2009 and Annex I to Commission Regulation No (EU) 2016/403 (1)</td><td>Yes</td></tr>
<tr><td>Appeal Possible</td><td>If an appeal against the infringement is still possible at the time of notification. Yes/No </td><td>Yes</td></tr>
<tr><td colspan="2">Penalty Imposed (for each serious infringement)</td><td>Yes, if relevant</td></tr>
<tr><td>Penalty Imposed Identifier</td><td>The serial number of the individual penalty imposed.</td><td>Yes</td></tr>
<tr><td>Final Decision Date</td><td>The final decision date of the penalty imposed in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>Penalty Type Imposed</td><td>Declaration of either:<table><tbody><tr><td>—</td><td>101: “Warning”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>201: “Temporary ban on cabotage operations”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>202: “Fine”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>203: “Prohibition”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>204: “Immobilisation”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>102: “Other”</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
<tr><td>Start Date</td><td>The start date of the penalty imposed in ISO 8601 format (YYYY-MM-DD)</td><td>No</td></tr>
<tr><td>End Date</td><td>The end date of the penalty imposed in ISO 8601 format (YYYY-MM-DD)</td><td>No</td></tr>
<tr><td>Executed</td><td>Yes/No</td><td>Yes</td></tr>
<tr><td colspan="2">Penalty Requested (for each Serious Infringement)</td><td>No</td></tr>
<tr><td>Penalty Requested Identifier</td><td>The serial number of the individual penalty requested.</td><td>Yes</td></tr>
<tr><td>Penalty Type Requested</td><td>Declaration of either:<table><tbody><tr><td>—</td><td>101: “Warning”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>301: “Temporary withdrawal of some or all of the certified true copies of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>302: “Permanent withdrawal of some or all of the certified true copies of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>303: “Temporary withdrawal of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>304: “Permanent withdrawal of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>305: “Suspension of the issue of driver attestations”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>306: “Withdrawal of driver attestations”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>307: “Issue of driver attestations subject to additional conditions in order to prevent misuse”</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
<tr><td>Duration</td><td>The duration of the requested penalty (calendar days).</td><td>No</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td colspan="2">Notification of Check Result Response</td><td>Mandatory, if infringement(s) detected during the check</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number matching the business case identifier of the notification.</td><td>Yes</td></tr>
<tr><td>Originating Competent Authority</td><td>The competent authority that issued the original infringement notification.</td><td>Yes</td></tr>
<tr><td>Licensing Competent Authority</td><td>The competent authority responding to the infringement notification.</td><td>Yes</td></tr>
<tr><td>Status Code</td><td>The status code of the infringement response (e.g. found, not found, error, etc.).</td><td>Yes</td></tr>
<tr><td>Status Message</td><td>An explanatory status description (if necessary).</td><td>No</td></tr>
<tr><td colspan="2">Transport Undertaking</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Name</td><td>The name of the transport undertaking as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Address</td><td>The address of the transport undertaking (address, postal code, city, country) as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Community Licence Number</td><td>The serial number of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20).</td><td>Yes</td></tr>
<tr><td>Community Licence Status</td><td>The status of the community licence of the transport undertaking as recorded in the register.</td><td>Yes</td></tr>
<tr><td colspan="2">Penalty Imposed</td><td>No</td></tr>
<tr><td>Penalty Imposed Identifier</td><td>The serial number of the individual penalty imposed (given in the Penalty Requested Identifier of the Notification of Check Result).</td><td>Yes</td></tr>
<tr><td>Competent Authority Imposing Penalty</td><td>The name of the competent authority imposing the penalty.</td><td>Yes</td></tr>
<tr><td>Is Imposed</td><td>Yes/No</td><td>Yes</td></tr>
<tr><td>Penalty Type Imposed</td><td>Declaration of either:<table><tbody><tr><td>—</td><td>101: “Warning”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>301: “Temporary withdrawal of some or all of the certified true copies of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>302: “Permanent withdrawal of some or all of the certified true copies of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>303: “Temporary withdrawal of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>304: “Permanent withdrawal of the Community licence”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>305: “Suspension of the issue of driver attestations”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>306: “Withdrawal of driver attestations”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>307: “Issue of driver attestations subject to additional conditions in order to prevent misuse”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>102: “Other”</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
<tr><td>Start Date</td><td>The start date of the penalty imposed in ISO 8601 format (YYYY-MM-DD).</td><td>No</td></tr>
<tr><td>End Date</td><td>The end date of the penalty imposed in ISO 8601 format (YYYY-MM-DD).</td><td>No</td></tr>
<tr><td>Reason</td><td>Reason if penalty is not imposed.</td><td>No</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td colspan="2">Notification of Check Result Acknowledgement</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number matching the business case identifier of the notification or the response.</td><td>Yes</td></tr>
<tr><td>Status Code</td><td>Status code of the acknowledgement.</td><td>Yes</td></tr>
<tr><td>Status Message</td><td>Status Message String</td><td>No</td></tr>
<tr><td>Originating Competent Authority</td><td>For a NCRN_Ack: in the legislation this field is represented as “Destination Competent Authority Identifier”. For a NCRR_Ack: in the legislation this field is represented as “Acknowledging Competent Authority Identifier”. </td><td>Yes</td></tr>
<tr><td>Licensing Competent Authority</td><td>For a NCRN_Ack: in the legislation this field is represented as “Acknowledging Competent Authority Identifier”. For a NCRR_Ack: in the legislation this field is represented as “Destination Competent Authority Identifier”. </td><td>Yes</td></tr>
<tr><td>Acknowledgement Type</td><td>Defining Acknowledgement Type Possible Values: <table><tbody><tr><td>—</td><td>“NCRN_Ack”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“NCRR_Ack”</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
</tbody>
</table>

**Check Transport Undertaking Data**

<table>
<tbody><tr><td colspan="2">Check Transport Undertaking Data Request</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number identifying each individual request.</td><td>Yes</td></tr>
<tr><td>Originating Competent Authority</td><td>The competent authority issuing the search request.</td><td>Yes</td></tr>
<tr><td colspan="2">Transport Undertaking Identification</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Name</td><td>The name of the transport undertaking.</td><td rowspan="3">At least two of the search fields are required.</td></tr>
<tr><td>Community Licence Number</td><td>The serial number of the community licence or of the certified true copy (free text alphanumeric field with length 1 to 20).</td></tr>
<tr><td>Vehicle Registration Number</td><td>The registration number of one of the vehicles of the transport undertaking.</td></tr>
<tr><td>Vehicle Registration Country</td><td>The country of registration of the vehicle.</td><td>Yes, if vehicle registration number provided.</td></tr>
<tr><td>Request All Vehicles</td><td>To request the registration numbers of all vehicles managed by the undertaking. Yes/No </td><td>Yes</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td colspan="2">Check Transport Undertaking Data Response</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number identifying each individual request</td><td>Yes</td></tr>
<tr><td>Originating Competent Authority</td><td>The competent authority issuing the search request.</td><td>Yes</td></tr>
<tr><td>Responding Competent Authority</td><td>The competent authority providing the response.</td><td>Yes</td></tr>
<tr><td>Status Code</td><td>The status code of the response (e.g. found, not found, error, etc.).</td><td>Yes</td></tr>
<tr><td>Status Message</td><td>An explanatory status description (if necessary).</td><td>No</td></tr>
<tr><td colspan="2">General Information about the Transport Undertaking</td><td>Yes, if status code is found</td></tr>
<tr><td>Transport Undertaking Name</td><td>The name of the transport undertaking (name and legal form).</td><td>Yes</td></tr>
<tr><td>Transport Undertaking Address</td><td>The address of the transport undertaking (address, postal code, city, country) as recorded in the register</td><td>Yes</td></tr>
<tr><td>Number of Managed Vehicles</td><td>The number of vehicles managed as recorded in the register.</td><td>Yes</td></tr>
<tr><td>Number of People Employed</td><td>The number of people employed in the undertaking on last 31 December.</td><td>Yes</td></tr>
<tr><td>Risk Rating</td><td>The risk rating of the undertaking.</td><td>Yes</td></tr>
<tr><td>Risk Rating Band</td><td>The risk rating band of the undertaking (green, amber, red, grey).</td><td>Yes</td></tr>
<tr><td colspan="2">Community Licence Details</td><td>Yes, if status code is found</td></tr>
<tr><td>Licencing Competent Authority</td><td>The competent authority that issued the community licence to the transport undertaking</td><td>Yes</td></tr>
<tr><td>Community Licence Number</td><td>The serial number of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20)</td><td>Yes</td></tr>
<tr><td>Licence Status</td><td>The status of the community licence of the transport undertaking as recorded in the register</td><td>Yes</td></tr>
<tr><td>Licence Type</td><td>The type of the community licence as recorded in the register. A declaration of:<table><tbody><tr><td>—</td><td>“Community licence for passenger transport”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“National licence for passenger transport”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Community licence for goods transport”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“Community licence for goods transport, exclusively ≤ 3,5 t”</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>“National licence for goods transport”</td></tr>
</tbody>
</table>
</td><td>Yes</td></tr>
<tr><td>Start Date</td><td>The start date of the community licence</td><td>Yes</td></tr>
<tr><td>Expiry Date</td><td>The expiry date of the community licence</td><td>Yes</td></tr>
<tr><td>Withdrawal Date</td><td>The withdrawal date of the community licence</td><td>Yes, if found</td></tr>
<tr><td>Suspension Date</td><td>The suspension date of the community licence</td><td>Yes, if found</td></tr>
<tr><td>Suspension Expiry Date</td><td>The date on which the community licence suspension expires</td><td>Yes, if found</td></tr>
<tr><td colspan="2">Certified True Copy Details</td><td>Yes</td></tr>
<tr><td>Certified True Copy Number</td><td>The serial number of each certified true copy of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20)</td><td>Yes</td></tr>
<tr><td>Start Date</td><td>The start date of each certified true copy of the community licence.</td><td>Yes</td></tr>
<tr><td>Expiry Date</td><td>The expiry date of each certified true copy of the community licence.</td><td>Yes</td></tr>
<tr><td>Withdrawal Date</td><td>The withdrawal date of each certified true copy of the community licence.</td><td>Yes, if found</td></tr>
<tr><td>Suspension Date</td><td>The suspension date of the certified true copy of the community licence.</td><td>Yes, if found</td></tr>
<tr><td>Suspension Expiry Date</td><td>The date on which each certified true copy of the community licence suspension expires.</td><td>Yes, if found</td></tr>
<tr><td colspan="2">Vehicle Details</td><td>Yes, if value of “Request All Vehicles” in CTUD Request is “Yes”.</td></tr>
<tr><td>Vehicle Registration Number</td><td>The registration number of each of the vehicles of the transport undertaking</td><td>Yes</td></tr>
<tr><td>Vehicle registration country</td><td>The registration country of each of the vehicles of the transport undertaking.</td><td>Yes</td></tr>
</tbody>
</table>

**Notification of Unfitness**

<table>
<tbody><tr><td colspan="2">Notification of Unfitness</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number identifying each individual notification.</td><td>Yes</td></tr>
<tr><td>Notifying Competent Authority</td><td>The competent authority that issues the notification.</td><td>Yes</td></tr>
<tr><td colspan="2">Transport Manager Details</td><td>Yes, if no CPC details</td></tr>
<tr><td>Family Name</td><td>Transport manager’s family name(s) as indicated on the CPC.</td><td>Yes</td></tr>
<tr><td>First Name</td><td>Transport manager’s complete given name as indicated on the certificate of professional competence.</td><td>Yes</td></tr>
<tr><td>Date of Birth</td><td>Transport manager’s birth date in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>Place of Birth</td><td>Transport manager’s place of birth.</td><td>No</td></tr>
<tr><td colspan="2">CPC Details</td><td>Yes, if no transport manager details</td></tr>
<tr><td>CPC Number</td><td>Number of certificate of professional competence</td><td>Yes</td></tr>
<tr><td>CPC Issue Date</td><td>Date of issuance of the CPC, in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>CPC Issue Country</td><td>Issuing country of the CPC in ISO 3166-1 alpha 2 format.</td><td>Yes</td></tr>
<tr><td colspan="2">Declaration of Unfitness</td><td>Yes</td></tr>
<tr><td>Start Date of Unfitness</td><td>Start date of unfitness, in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td colspan="2">Notification of Unfitness Acknowledgement</td><td>Mandatory</td></tr>
<tr><td>Business Case Identifier</td><td>A serial or reference number matching the business case identifier of the notification.</td><td>Yes</td></tr>
<tr><td>Originating Competent Authority</td><td>The competent authority issuing the notification.</td><td>Yes</td></tr>
<tr><td>Responding Competent Authority</td><td>The competent authority providing the acknowledgement.</td><td>Yes</td></tr>
<tr><td>Status Code</td><td>Status code of the acknowledgement.</td><td>Yes</td></tr>
<tr><td>Status Message</td><td>Status Message String</td><td>No</td></tr>
</tbody>
</table>

’;

(3) in Annex VI, point 1.5 is replaced by the following:

‘1.5. When sending Check Good Repute responses, Notification of Check Result acknowledgements, Check Transport Undertaking Data responses and Declaration of Unfitness acknowledgements in accordance with Annex VIII:

1.5.1. They shall respond to requests within 10 seconds.

1.5.2. The global request timeout (time within which the requestor may wait for a response) shall not exceed 20 seconds.

1.5.3. They shall be able to service a request rate of 6 messages per second.’;

(4) Annex VIII is replaced by the following:

**‘1. CHECKING THE GOOD REPUTE OF TRANSPORT MANAGERS**

When verifying through ERRU, in accordance with Article 11(4) of Regulation (EC) No 1071/2009, whether a transport manager has been declared in one of the Member States as unfit to manage the transport activities of an undertaking, Member States shall perform a broadcast CGR search by sending a Check Good Repute Request. The responding Member States shall reply to the request by sending a Check Good Repute Response.

**2\. NOTIFICATION OF CHECK RESULTS**

|  | 2.1. | For the notification of a serious infringement through ERRU, the Member State of infringement shall send a Notification of Check Result to the Member State of establishment with the information about the infringement. Infringements not categorised in Directive 2006/22/EC or in Regulation (EC) No 1071/2009 shall not be notified. |
| --- | --- | --- |

|  | 2.2. | When no infringement has been detected during the check, a Notification of Check Result shall be sent to the Member State of establishment consisting of the information about the clean check as set out in Annex III. |
| --- | --- | --- |

|  | 2.3. | A check shall not be considered as a clean check when minor infringements have been detected. Where only minor infringements have been detected during the check, a Notification of Check Result shall be sent to the Member State of establishment consisting of information about the date and number of minor infringements detected. |
| --- | --- | --- |

|  | 2.4. | The Notification of Check Result shall be sent as soon as possible, and at the latest within 6 weeks of the final decision on the infringements detected, if any, providing the information set out in Annex III. |
| --- | --- | --- |

|  | 2.5. | The Member State of establishment shall reply to the Notification of Check Result by sending a Notification of Check Result Response, as soon as possible and at the latest within 6 weeks of the final decision on the matter, informing of which, if any, of the penalties requested by the Member State of infringement have been imposed. If such penalties are not imposed, the Notification of Check Result Response shall include the reasons therefor. The Notification of Check Result Response shall not be necessary when the Notification of Check Result refers to a clean check. |
| --- | --- | --- |

|  | 2.6. | In all cases, a Notification of Check Result and a Notification of Check Result Response shall be acknowledged by means of a Notification of Check Result Acknowledgement. |
| --- | --- | --- |

**3\. CHECKING THE TRANSPORT UNDERTAKING DATA**

|  | 3.1. | When checking through ERRU any of the transport undertaking data referred to in point 1.3 of Annex II, a Member State shall send a Check Transport Undertaking Data Request to the Member State of establishment. |
| --- | --- | --- |

|  | 3.2. | The Member State of establishment shall reply by sending a Check Transport Undertaking Data Response. |
| --- | --- | --- |

|  | 3.3. | Queries sent through the CTUD functionality shall be carried out by entering either the name of the transport undertaking, its Community licence number or the number of any of the certified true copies, or the registration number of any of its vehicles, without being necessary to perform a query by typing more than two of the aforementioned entries. |
| --- | --- | --- |

|  | 3.4. | Responding Member States, when searching in their registers the result of a CTUD request on the basis of either the Community licence or the registration number of a vehicle, shall take measures to adapt the format of the data in the search request to the format of the data in the national register. In particular, Responding Member States, when searching in their registers the result of a CTUD request on the basis of either the Community licence or the registration number of a vehicle, shall ignore special characters such as hyphens or slashes. Blanks shall also be ignored. |
| --- | --- | --- |

|  | 3.5. | Responding Member States shall return to the requesting Member States all the information that is available through the XML messages defined in Annex III. If a part of the information requested has not been found, this shall not preclude responding Member States to provide the rest of the information requested that is available in the register, including the registration number of vehicles with no associated certified true copy. |
| --- | --- | --- |

**4\. NOTIFYING THE UNFITNESS OF A TRANSPORT MANAGER**

|  | 4.1. | When a transport manager has been declared to be unfit in one Member State, that Member State may send a Notification of Unfitness to all other Member States. |
| --- | --- | --- |

|  | 4.2. | In all cases, a Notification of Unfitness shall be acknowledged by means of a Notification of Unfitness Acknowledgement.’ |
| --- | --- | --- |

(1) Commission Regulation (EU) 2016/403 of 18 March 2016 supplementing Regulation (EC) No 1071/2009 of the European Parliament and of the Council with regard to the classification of serious infringements of the Union rules, which may lead to the loss of good repute by the road transport operator, and amending Annex III to Directive 2006/22/EC of the European Parliament and of the Council (OJ L 74, 19.3.2016, p. 8).

ELI: http://data.europa.eu/eli/reg_impl/2023/2381/oj

ISSN 1977-0677 (electronic edition)
