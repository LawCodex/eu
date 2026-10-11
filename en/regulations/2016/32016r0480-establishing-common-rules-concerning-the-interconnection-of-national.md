---
title: "Commission Implementing Regulation (EU) 2016/480 of 1 April 2016 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010 (Text with EEA relevance)"
identifier: "32016R0480"
eli: "http://data.europa.eu/eli/reg_impl/2016/480/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2016-04-01
entry_into_force: 2016-07-20
last_amended: 2023-10-25
consolidated_version: "02016R0480-20231025"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0480-20231025"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2016/480 of 1 April 2016 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010 (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2016/480**

**of 1 April 2016**

**establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010**

**(Text with EEA relevance)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING REGULATION (EU) 2017/1440 of 8 August 2017 </td><td> L 206</td><td>3</td><td>9.8.2017</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING REGULATION (EU) 2023/2381 of 29 September 2023 </td><td> L </td><td>1</td><td>5.10.2023</td></tr>
</table>

**COMMISSION IMPLEMENTING REGULATION (EU) 2016/480**

**of 1 April 2016**

**establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010**

**(Text with EEA relevance)**

## Article 1 — Subject matter

This Regulation lays down the requirements regarding the connection of the national electronic registers on road transport undertakings to the ERRU messaging system, as set out in Article 16(5) of Regulation (EC) No 1071/2009.

## Article 2 — Definitions

For the purpose of this Regulation and in addition to the definitions laid down in Article 2 of Regulation (EC) No 1071/2009, the following definitions shall apply:

(a) ‘ERRU (European Registers of Road Transport Undertakings)’ means a system of interconnection of national electronic registers, set up in accordance Article 16(5) of Regulation (EC) No 1071/2009;

(b) ‘Asynchronous interface’ means a process whereby a message in response to a request is returned on a new HTTP connection;

(c) ‘Broadcast search’ means a request message from a Member State addressed to all other Member States;

(d) ‘Central hub’ means the information system enabling the routing of ERRU messages between Member States;

(e) ‘CPC’ means certificate of professional competence, as referred to in Article 8(8) of Regulation (EC) No 1071/2009;

(f) ‘Member State of infringement’ means the Member State in which a transport undertaking has committed an infringement;

(g) ‘Member State of establishment’ means the Member State in which an undertaking is established;

(h) ‘National system’ means the information system set up in each Member State for the purpose of emitting, processing and responding to ERRU messages;

(i) ‘Synchronous interface’ means a process whereby a message in response to a request is returned on the same HTTP connection as the one used for the request;

(j) ‘Requesting Member State’ means the Member State emitting a request or a notification, which is then routed to the responding Member States;

(k) ‘Responding Member State’ means the Member State to whom the ERRU request or notification is directed;

(l) ‘Clean check’ means a check where no infringements are detected.

## Article 3 — Obligation to connect to ERRU

Member States shall carry out the interconnection of the national electronic registers referred to in Article 16 of Regulation (EC) No 1071/2009 to ERRU in accordance with the procedures and technical requirements laid down in this Regulation.

The connection to ERRU of a Member State shall be considered to be established after the completion of the connection, integration and performance tests in accordance with the instructions and under the supervision of the Commission. The maximum duration of the tests shall be six months. The Commission shall take measures in case of failure of the above-mentioned tests. If those measures prove insufficient, the Commission may withdraw the testing support until the Member State proves that sufficient progress has been made at national level regarding connection to ERRU.

## Article 4 — Technical specifications

ERRU shall fulfil the technical specifications laid down in Annexes I to VII to this Regulation.

## Article 5 — Use of ERRU

1\. When exchanging information through ERRU, the competent authorities shall follow the procedures set out in Annex VIII to this Regulation.

2\. Member States shall grant control bodies in charge of roadside checks access to the Check Transport Undertaking Data functionality.

3\. In cases where several national control bodies are involved in roadside checks, the Member State shall decide which ones of those bodies shall be granted the access referred to in paragraph 2.

## Article 6 — Repeal

Regulation (EU) No 1213/2010 is hereby repealed as from the date of application of this Regulation. References to the repealed Regulation shall be construed as references to this Regulation.

## Article 7 — Entry into force

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

It shall apply from 30 January 2019.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

## ANNEX I

**GENERAL ASPECTS OF ERRU**

**1\. ARCHITECTURE**

ERRU shall be composed of the following parts:

1.1. A central hub, which shall be able to receive a request from the requesting Member State, validate it and process it by forwarding it to the responding Member States. The central hub will wait for each responding Member State to answer, consolidate all the answers and forward the consolidated response to the requesting Member State.

1.2. A national system per Member State, which shall be fitted with an interface capable of both sending requests to the central hub and receiving the corresponding replies. National systems may use propriety or commercial software to transmit and receive messages from the central hub.

1.3. All messages exchanged shall be routed through the central hub.

**2\. MANAGEMENT**

2.1. The central hub shall be managed by the Commission, which shall be responsible for the technical operation and maintenance of the central hub.

2.2. The central hub shall not store data for a period exceeding 6 months, other than the logging, statistical and routing data set out in Annex VII.

2.3. The central hub shall not provide access to personal data, except for authorised Commission personnel, when necessary for the purpose of monitoring the technical operation, maintenance and troubleshooting.

2.4. Member States shall be responsible for:

2.4.1. The setup and management of their national systems, including the interface with the central hub.

2.4.2. The installation and maintenance of their national system, both hardware and software, whether proprietary or commercial.

2.4.3. The correct interoperability of their national system with the central hub, including the management of error messages received from the central hub.

2.4.4. Taking all the measures to ensure the confidentiality, integrity and availability of the information.

2.4.5. The operation of the national systems in accordance with the service levels set out in Annex VI.

2.5. MOVEHUB web portal

The Commission shall provide a web based application with secured access, referred to as ‘MOVEHUB web portal’, providing at least the following services:

(a) Member State availability statistics

(b) Notification of maintenance on the central hub and Member State national systems.

(c) Aggregated reports

(d) Contact management

(e) XSD schemas

2.6. Contact management

The contact management functionality will provide each Member State with the ability to manage the contact details regarding policy, business, operational and technical categories of that Member State, being each Member State's competent authority responsible for the maintenance of its own contacts. It will be possible to view, but not edit, the contact details of the other Member States.

## ANNEX II

**ERRU FUNCTIONALITIES**

1\. The following functionalities shall be provided through ERRU:

1.1. Check Good Repute (CGR): allows the requesting Member State to send a query to one or all responding Member States, to determine the fitness of a transport manager and so the authorisation to operate a transport undertaking.

1.2. Notification of Check Result (NCR): allows the Member State where the check was carried out to notify the result of a check to the Member State of establishment. When a serious infringement has been found during the check, the Member State where the infringement was detected notifies the Member State of establishment through NCR that the transport undertaking has committed a serious infringement, and may request penalties to be applied to the transport undertaking in the Member State of establishment. When no infringement has been detected during the check, NCR allows the Member State where the check has been carried out to notify the Member State of establishment the positive result of the check.

1.3. Check Transport Undertaking Data (CTUD): allows the requesting Member State to send a query to the responding Member State about the following data that are specific to a transport undertaking:

— information about the Community Licence and the certified true copies,

— risk rating and risk rating band,

— number of vehicles at the disposal of the transport undertaking,

— registration number and registration country of the vehicles at the disposal of the transport undertaking,

— number of employees.

1.4. Notification of Unfitness (NU): allows a Member State to inform all other Member States that a transport manager has been declared unfit and that as a result, its certificate of professional competence is no longer valid in any Member State.

2\. Other message types deemed suitable for the efficient functioning of ERRU shall be included, for instance error notifications.

## ANNEX III

**ERRU MESSAGE PROVISIONS**

**1\. GENERAL TECHNICAL REQUIREMENTS**

1.1. The central hub will provide both synchronous and asynchronous interfaces for the exchange of messages. Member States may choose the most suitable technology to interface with their own applications.

1.2. All messages exchanged between the central hub and the national systems must be UTF-8 encoded.

1.3. Member States will ensure that their national systems can receive and process messages containing Greek or Cyrillic characters.

**2\. XML MESSAGES STRUCTURE AND SCHEMA DEFINITION (XSD)**

2.1. The general structure of XML messages shall follow the format defined by the XSD schemas installed in the central hub.

2.2. The central hub and the national systems shall transmit and receive messages that conform to the message XSD schema.

2.3. National systems will be capable of sending, receiving and processing all messages corresponding to any of the functionalities set out in Annex II.

2.4. The XML messages shall include at least the minimum requirements laid down in the Appendix to this Annex.

## Appendix — Minimum requirements for the content of the XML messages

<table>
<tbody><tr><td colspan="2">Common Header</td><td>Mandatory</td></tr>
<tr><td>Version</td><td>The official version of the XML specifications will be specified through the namespace defined in the message XSD and in the version attribute of the Header element of any XML message. The version number (‘n.m’) will be defined as fixed value in every release of the XML Schema Definition file (xsd).</td><td>Yes</td></tr>
<tr><td>Test Identifier</td><td>Optional id for testing. The originator of the test will populate the id and all participants in the workflow will forward/return the same id. In production it should be ignored and will not be used if it is supplied.</td><td>No</td></tr>
<tr><td>Technical Identifier</td><td>A UUID uniquely identifying each individual message. The sender generates a UUID and populates this attribute. This data is not used in any business capacity.</td><td>Yes</td></tr>
<tr><td>Workflow Identifier</td><td>The workflowId is a UUID and should be generated by the requesting Member State. This id is then used in all messages to correlate the workflow.</td><td>Yes</td></tr>
<tr><td>Sent At</td><td>The date and time (UTC) that the message was sent.</td><td>Yes</td></tr>
<tr><td>Timeout</td><td>This is an optional date and time (in UTC format) attribute. This value will be set only by the central hub for forwarded requests and is calculated based on the date/time the initial request has been received by the central hub. This will inform the responding Member State of the time when the request will be timed out. This value is not required in initial requests sent to the central hub and all response messages.</td><td>No</td></tr>
<tr><td>From</td><td>The ISO 3166-1 Alpha 2 code of the Member State sending the message or ‘EU’.</td><td>Yes</td></tr>
<tr><td>To</td><td>The ISO 3166-1 Alpha 2 code of the Member State to which the message is being sent or ‘EU’.</td><td>Yes</td></tr>
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
<tr><td>CPC Validity</td><td>Declaration of either ‘Valid’ or ‘Invalid’</td><td>Yes</td></tr>
<tr><td>Total Managed Undertakings</td><td>The number of transport undertakings with which the transport manager is associated.</td><td>Yes</td></tr>
<tr><td>Total Managed Vehicles</td><td>The total number of vehicles with which the transport manager is associated.</td><td>Yes</td></tr>
<tr><td>Fitness</td><td>Declaration of either ‘Fit’ or ‘Unfit’.</td><td>Yes</td></tr>
<tr><td>Start Date of Unfitness</td><td>Start date of unfitness of the transport manager in ISO 8601 format (YYYY-MM-DD).</td><td>Yes if ‘Fitness’ is ‘Unfit’.</td></tr>
<tr><td>End Date of Unfitness</td><td>End date of unfitness of the transport manager in ISO 8601 format (YYYY-MM-DD).</td><td>Yes if ‘Fitness’ is ‘Unfit’.</td></tr>
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
<tr><td colspan="2">General information about the check</td><td>  </td></tr>
<tr><td>Date of check</td><td>Date of check in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Clean check</td><td>Yes/No</td><td>Yes</td></tr>
<tr><td colspan="2">Minor infringements</td><td>Yes, if minor infringement(s) detected during the check</td></tr>
<tr><td>Date of minor infringement</td><td>Date of the infringement in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Number of minor infringements</td><td>The number of minor infringements detected.</td><td>Yes</td></tr>
<tr><td colspan="2">Serious infringement</td><td>Yes, if serious infringement detected during the check</td></tr>
<tr><td>Date of Infringement</td><td>Date of the infringement in ISO 8601 format (YYYY-MM-DD)</td><td>Yes</td></tr>
<tr><td>Category</td><td>The category of the infringement: — MSI: Most serious infringement  — VSI: Very serious infringement  — SI: Serious infringement </td><td>Yes</td></tr>
<tr><td>Infringement Type</td><td>In accordance with the classification provided in Annex IV to Regulation (EC) No 1071/2009 and Annex I to Commission Regulation No (EU) 2016/403 (1)</td><td>Yes</td></tr>
<tr><td>Appeal Possible</td><td>If an appeal against the infringement is still possible at the time of notification. Yes/No </td><td>Yes</td></tr>
<tr><td colspan="2">Penalty Imposed (for each serious infringement)</td><td>Yes, if relevant</td></tr>
<tr><td>Penalty Imposed Identifier</td><td>The serial number of the individual penalty imposed.</td><td>Yes</td></tr>
<tr><td>Final Decision Date</td><td>The final decision date of the penalty imposed in ISO 8601 format (YYYY-MM-DD).</td><td>Yes</td></tr>
<tr><td>Penalty Type Imposed</td><td>Declaration of either: — 101: ‘Warning’  — 201: ‘Temporary ban on cabotage operations’  — 202: ‘Fine’  — 203: ‘Prohibition’  — 204: ‘Immobilisation’  — 102: ‘Other’ </td><td>Yes</td></tr>
<tr><td>Start Date</td><td>The start date of the penalty imposed in ISO 8601 format (YYYY-MM-DD)</td><td>No</td></tr>
<tr><td>End Date</td><td>The end date of the penalty imposed in ISO 8601 format (YYYY-MM-DD)</td><td>No</td></tr>
<tr><td>Executed</td><td>Yes/No</td><td>Yes</td></tr>
<tr><td colspan="2">Penalty Requested (for each Serious Infringement)</td><td>No</td></tr>
<tr><td>Penalty Requested Identifier</td><td>The serial number of the individual penalty requested.</td><td>Yes</td></tr>
<tr><td>Penalty Type Requested</td><td>Declaration of either: — 101: ‘Warning’  — 301: ‘Temporary withdrawal of some or all of the certified true copies of the Community licence’  — 302: ‘Permanent withdrawal of some or all of the certified true copies of the Community licence’  — 303: ‘Temporary withdrawal of the Community licence’  — 304: ‘Permanent withdrawal of the Community licence’  — 305: ‘Suspension of the issue of driver attestations’  — 306: ‘Withdrawal of driver attestations’  — 307: ‘Issue of driver attestations subject to additional conditions in order to prevent misuse’ </td><td>Yes</td></tr>
<tr><td>Duration</td><td>The duration of the requested penalty (calendar days).</td><td>No</td></tr>
<tr><td colspan="3">(1)  Commission Regulation (EU) 2016/403 of 18 March 2016 supplementing Regulation (EC) No 1071/2009 of the European Parliament and of the Council with regard to the classification of serious infringements of the Union rules, which may lead to the loss of good repute by the road transport operator, and amending Annex III to Directive 2006/22/EC of the European Parliament and of the Council (OJ L 74, 19.3.2016, p. 8). </td></tr>
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
<tr><td>Penalty Type Imposed</td><td>Declaration of either: — 101: ‘Warning’  — 301: ‘Temporary withdrawal of some or all of the certified true copies of the Community licence’  — 302: ‘Permanent withdrawal of some or all of the certified true copies of the Community licence’  — 303: ‘Temporary withdrawal of the Community licence’  — 304: ‘Permanent withdrawal of the Community licence’  — 305: ‘Suspension of the issue of driver attestations’  — 306: ‘Withdrawal of driver attestations’  — 307: ‘Issue of driver attestations subject to additional conditions in order to prevent misuse’  — 102: ‘Other’ </td><td>Yes</td></tr>
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
<tr><td>Originating Competent Authority</td><td>For a NCRN_Ack: in the legislation this field is represented as ‘Destination Competent Authority Identifier’. For a NCRR_Ack: in the legislation this field is represented as ‘Acknowledging Competent Authority Identifier’. </td><td>Yes</td></tr>
<tr><td>Licensing Competent Authority</td><td>For a NCRN_Ack: in the legislation this field is represented as ‘Acknowledging Competent Authority Identifier’. For a NCRR_Ack: in the legislation this field is represented as ‘Destination Competent Authority Identifier’. </td><td>Yes</td></tr>
<tr><td>Acknowledgement Type</td><td>Defining Acknowledgement Type Possible Values:  — ‘NCRN_Ack’  — ‘NCRR_Ack’ </td><td>Yes</td></tr>
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
<tr><td>Licence Type</td><td>The type of the community licence as recorded in the register. A declaration of: — ‘Community licence for passenger transport’  — ‘National licence for passenger transport’  — ‘Community licence for goods transport’  — ‘Community licence for goods transport, exclusively ≤ 3,5 t’  — ‘National licence for goods transport’ </td><td>Yes</td></tr>
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
<tr><td colspan="2">Vehicle Details</td><td>Yes, if value of ‘Request All Vehicles’ in CTUD Request is ‘Yes’.</td></tr>
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

## ANNEX IV

**TRANSLITERATION AND NYSIIS SERVICES**

1\. The NYSIIS algorithm implemented in the central hub shall be used to encode the names of all the transport managers in the national register.

2\. Member States should always use the NYSIIS key as the primary search mechanism when searching the register for a transport manager via the CGR functionality.

3\. Additionally, Member States may employ a custom algorithm to return additional results.

4\. The search results will indicate via which search mechanism a record was found, either NYSIIS, or CPC or custom.

## ANNEX V

**SECURITY REQUIREMENTS**

1\. HTTPS must always be used for the exchange of messages between the central hub and the national systems.

2\. National systems will use the PKI certificates provided by the Commission for the purposes of securing the transmission of messages between the national system and the hub.

3\. National systems shall implement, as a minimum, certificates using the SHA-2 (SHA-256) signature hash algorithm and a 2 048 bit public key length.

## ANNEX VI

**SERVICE LEVELS**

1\. National systems shall fulfil the following minimum level of service:

1.1. They shall be available 24 hours a day, 7 days a week.

1.2. Their availability shall be monitored by a heartbeat message issued from the central hub.

1.3. Their availability rate shall be 98 %, according to the following table (the figures have been rounded to the nearest convenient unit):

<table>
<tbody><tr><td rowspan="2">An availability of</td><td colspan="3">means an unavailability of</td></tr>
<tr><td>Daily</td><td>Monthly</td><td>Yearly</td></tr>
<tr><td>98 %</td><td>0,5 hours</td><td>15 hours</td><td>7,5 days</td></tr>
</tbody>
</table>

Member States are encouraged to respect the daily availability rate, however it is recognised that certain necessary activities, such as system maintenance, will require a down time of more than 30 minutes. However, the monthly and yearly availability rates remain mandatory.

1.4. They shall respond to a minimum of 98 % of the requests forwarded to them in 1 calendar month.

1.5. When sending Check Good Repute responses, Notification of Check Result acknowledgements, Check Transport Undertaking Data responses and Declaration of Unfitness acknowledgements in accordance with Annex VIII:

1.5.1. They shall respond to requests within 10 seconds.

1.5.2. The global request timeout (time within which the requestor may wait for a response) shall not exceed 20 seconds.

1.5.3. They shall be able to service a request rate of 6 messages per second.

1.6. National systems will not send requests to the ERRU hub at a rate exceeding 2 requests per second.

1.7. Every national system shall be able to cope with potential technical problems of the central hub or national systems in other Member States. These include, but are not limited to:

(a) Loss of connection to the central hub

(b) No response to a request

(c) Receipt of responses after message timeout

(d) Receipt of unsolicited messages

(e) Receipt of invalid messages

2\. The central hub shall:

2.1. Feature an availability rate of 98 %.

2.2. Provide to national systems notification of any errors, either via the response message or via a dedicated error message. The national systems, in turn, shall receive these dedicated error messages and have an escalation workflow in place to take any appropriate action to rectify the notified error. The escalation procedure should be detailed to the Commission upon request.

3\. Maintenance

Member States shall notify other Member States and the Commission of any routine maintenance activities via the web application, at least 1 week before the beginning of those activities if technically possible.

## ANNEX VII

**LOGGING AND STATISTICS**

1\. This annex provides details of logging and statistical data collected at the central hub, not at the Member States.

2\. In order to ensure privacy, the data for statistical and routing purposes shall be anonymous. Data identifying a specific transport manager, transport undertaking, community licence or CPC will not be available for statistical purposes.

3\. Logging information shall keep track of all transactions for monitoring and debugging purposes, and allow the generation of statistics about these transactions.

4\. Personal data shall not be retained in the logs for more than 6 months after a transaction is complete. Statistical and routing information will be retained indefinitely.

5\. The statistical data used for reporting may include, among others:

(a) The requesting Member State.

(b) The responding Member State.

(c) The type of message.

(d) The status code of the response.

(e) The date and time of the messages.

(f) The response time.

## ANNEX VIII

**USE OF ERRU**

**1\. CHECKING THE GOOD REPUTE OF TRANSPORT MANAGERS**

When verifying through ERRU, in accordance with Article 11(4) of Regulation (EC) No 1071/2009, whether a transport manager has been declared in one of the Member States as unfit to manage the transport activities of an undertaking, Member States shall perform a broadcast CGR search by sending a Check Good Repute Request. The responding Member States shall reply to the request by sending a Check Good Repute Response.

**2\. NOTIFICATION OF CHECK RESULTS**

2.1. For the notification of a serious infringement through ERRU, the Member State of infringement shall send a Notification of Check Result to the Member State of establishment with the information about the infringement. Infringements not categorised in Directive 2006/22/EC or in Regulation (EC) No 1071/2009 shall not be notified.

2.2. When no infringement has been detected during the check, a Notification of Check Result shall be sent to the Member State of establishment consisting of the information about the clean check as set out in Annex III.

2.3. A check shall not be considered as a clean check when minor infringements have been detected. Where only minor infringements have been detected during the check, a Notification of Check Result shall be sent to the Member State of establishment consisting of information about the date and number of minor infringements detected.

2.4. The Notification of Check Result shall be sent as soon as possible, and at the latest within 6 weeks of the final decision on the infringements detected, if any, providing the information set out in Annex III.

2.5. The Member State of establishment shall reply to the Notification of Check Result by sending a Notification of Check Result Response, as soon as possible and at the latest within 6 weeks of the final decision on the matter, informing of which, if any, of the penalties requested by the Member State of infringement have been imposed. If such penalties are not imposed, the Notification of Check Result Response shall include the reasons therefor. The Notification of Check Result Response shall not be necessary when the Notification of Check Result refers to a clean check.

2.6. In all cases, a Notification of Check Result and a Notification of Check Result Response shall be acknowledged by means of a Notification of Check Result Acknowledgement.

**3\. CHECKING THE TRANSPORT UNDERTAKING DATA**

3.1. When checking through ERRU any of the transport undertaking data referred to in point 1.3 of Annex II, a Member State shall send a Check Transport Undertaking Data Request to the Member State of establishment.

3.2. The Member State of establishment shall reply by sending a Check Transport Undertaking Data Response.

3.3. Queries sent through the CTUD functionality shall be carried out by entering either the name of the transport undertaking, its Community licence number or the number of any of the certified true copies, or the registration number of any of its vehicles, without being necessary to perform a query by typing more than two of the aforementioned entries.

3.4. Responding Member States, when searching in their registers the result of a CTUD request on the basis of either the Community licence or the registration number of a vehicle, shall take measures to adapt the format of the data in the search request to the format of the data in the national register. In particular, Responding Member States, when searching in their registers the result of a CTUD request on the basis of either the Community licence or the registration number of a vehicle, shall ignore special characters such as hyphens or slashes. Blanks shall also be ignored.

3.5. Responding Member States shall return to the requesting Member States all the information that is available through the XML messages defined in Annex III. If a part of the information requested has not been found, this shall not preclude responding Member States to provide the rest of the information requested that is available in the register, including the registration number of vehicles with no associated certified true copy.

**4\. NOTIFYING THE UNFITNESS OF A TRANSPORT MANAGER**

4.1. When a transport manager has been declared to be unfit in one Member State, that Member State may send a Notification of Unfitness to all other Member States.

4.2. In all cases, a Notification of Unfitness shall be acknowledged by means of a Notification of Unfitness Acknowledgement.
