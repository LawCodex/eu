---
title: "Commission Implementing Regulation (EU) 2017/1440 of 8 August 2017 amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings (Text with EEA relevance. )"
identifier: "32017R1440"
eli: "http://data.europa.eu/eli/reg_impl/2017/1440/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2017-08-08
entry_into_force: 2018-01-04
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R1440"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2017/1440 of 8 August 2017 amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings (Text with EEA relevance. )

**COMMISSION IMPLEMENTING REGULATION (EU) 2017/1440**

**of 8 August 2017**

**amending Implementing Regulation (EU) 2016/480 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EC) No 1071/2009 of the European Parliament and of the Council of 21 October 2009 establishing common rules concerning the conditions to be complied with to pursue the occupation of road transport operator and repealing Council Directive 96/26/EC (1), and in particular Article 16(5) thereof,

Whereas:

(1) Article 16(1) of Regulation (EC) No 1071/2009 requires the Member States to keep a national electronic register of road transport undertakings that have been authorised by a competent authority to engage in the occupation of road transport operator.

(2) Article 16(5) and (6) of Regulation (EC) No 1071/2009 provide for all the national electronic registers to be interconnected by 31 December 2012, and mandate the Commission to adopt common rules concerning such interconnection.

(3) The Commission adopted Regulation (EU) No 1213/2010 (2), in order to make possible the interconnection of the national electronic registers requested by Regulation (EC) No 1071/2009, through an electronic message exchange system called ERRU (European Registers of Road Transport Undertakings).

(4) Regulation (EU) No 1213/2010 has been repealed by Commission Implementing Regulation (EU) 2016/480 (3) in order to set up an enhanced version of ERRU by 30 January 2019.

(5) ERRU consists of two parallel architectures regarding the exchange of messages between Member States. The first one is based on a central hub managed by the Commission. This central hub centralises the data traffic by collecting the messages sent by Member States and forwarding them subsequently to the Member States to which the messages are addressed. Alternatively, Member States may choose to use a compatible commercial network to exchange messages directly amongst themselves (peer-to-peer configuration), without those messages going through the central hub.

(6) Given that messages exchanged directly between Member States are not routed through the central hub, eventual system faults related to those messages go unnoticed to the Commission; the Commission is therefore unable to fulfil its role as general manager of ERRU by taking the corresponding corrective action, which consequently jeopardizes the good performance of the whole system.

(7) The peer-to-peer configuration does not allow the Commission to have timely access to information on the volume and characteristics of the messages exchanged; it is not possible therefore for the Commission to have an overall view on the usage of ERRU, information that is useful for future improvements of the system.

(8) The problems encountered with the peer-to-peer configuration make it necessary to ensure that all messages exchanged in the framework of ERRU are routed through the central hub, and thus remove this possibility from the scope of Implementing Regulation (EU) 2016/480.

(9) Furthermore, some minor additions and changes in Implementing Regulation (EU) 2016/480 have to be made in order to address the following aspects in a more precise and clearer manner: the procedure for connection to ERRU, the tests to be performed and the consequences of failure, the content of some XML messages, the definition of the escalation procedure to be followed by Member States in case of system errors, and the time that personal data can be retained in the logs of the central hub. Consequently, Implementing Regulation (EU) 2016/480 should be amended accordingly.

(10) The measures provided for in this Regulation are adopted in accordance with the advisory procedure set out in Article 4 of Regulation (EU) No 182/2011 of the European Parliament and of the Council (4),

HAS ADOPTED THIS REGULATION:

## Article 1

In Article 3 of Implementing Regulation (EU) 2016/480, the following paragraph is added:

‘The connection to ERRU of a Member State shall be considered to be established after the completion of the connection, integration and performance tests in accordance with the instructions and under the supervision of the Commission. The maximum duration of the tests shall be six months. The Commission shall take measures in case of failure of the above-mentioned tests. If those measures prove insufficient, the Commission may withdraw the testing support until the Member State proves that sufficient progress has been made at national level regarding connection to ERRU’;

## Article 2

Annexes I, III, VI, VII and VIII to Implementing Regulation (EU) 2016/480 are amended in accordance with the Annex to this Regulation.

## Article 3

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 8 August 2017.

For the Commission

The President

Jean-Claude JUNCKER

(1) OJ L 300, 14.11.2009, p. 51.

(2) Commission Regulation (EU) No 1213/2010 of 16 December 2010 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings (OJ L 335, 18.12.2010, p. 21).

(3) Commission Implementing Regulation (EU) 2016/480 of 1 April 2016 establishing common rules concerning the interconnection of national electronic registers on road transport undertakings and repealing Regulation (EU) No 1213/2010 (OJ L 87, 2.4.2016, p. 4).

(4) Regulation (EU) No 182/2011 of the European Parliament and of the Council of 16 February 2011 laying down the rules and general principles concerning mechanisms for control by Member States of the Commission's exercise of implementing powers (OJ L 55, 28.2.2011, p. 13).

## ANNEX

Annexes I, III, VI, VII and VIII to Implementing Regulation (EU) 2016/480 are amended as follows:

(1) Annex I is amended as follows:

(a) point 1.3 is replaced by the following:

‘1.3. All messages exchanged shall be routed through the central hub.’;

(b) point 2.2 is replaced by the following:

‘2.2. The central hub shall not store data for a period exceeding 6 months, other than the logging, statistical and routing data set out in Annex VII.’;

(c) point 2.3 is replaced by the following:

‘2.3. The central hub shall not provide access to personal data, except for authorised Commission personnel, when necessary for the purpose of monitoring the technical operation, maintenance and troubleshooting.’;

(d) point 2.6 is replaced by the following:

**‘2.6. Contact management**

The contact management functionality will provide each Member State with the ability to manage the contact details regarding policy, business, operational and technical categories of that Member State, being each Member State's competent authority responsible for the maintenance of its own contacts. It will be possible to view, but not edit, the contact details of the other Member States.’;

(2) in Annex III, the Appendix is amended as follows:

(a) in the first table, the item ‘Timeout’ is replaced by the following:

| ‘Timeout | This is an optional date and time (in UTC format) attribute. This value will be set only by the central hub for forwarded requests and is calculated based on the date/time the initial request has been received by the central hub. This will inform the responding Member State of the time when the request will be timed out. This value is not required in initial requests sent to the central hub and all response messages. | No’ |
| --- | --- | --- |

(b) in the table with the heading ‘Check Good Repute Response’, the item ‘Community Licence Number’ is replaced by the following:

| ‘Community Licence Number | The serial number of the Community licence of the transport undertaking (free text alphanumeric field with length 1 to 20). | Yes’ |
| --- | --- | --- |

(c) in the table with the heading ‘Infringement Notification Request’, the item ‘Community Licence Number’ is replaced by the following:

| ‘Community Licence Number | The serial number of the certified true copy or of the Community licence of the transport undertaking (free text alphanumeric field with length 1 to 20). | Yes’ |
| --- | --- | --- |

(d) in the table with the heading ‘Infringement Notification Response’, the following items are inserted after the item ‘Transport Undertaking Name’:

| ‘Transport Undertaking Address | The address of the transport undertaking (address, postal code, city, country) as recorded in the register. | Yes |
| --- | --- | --- |
| Community Licence Number | The serial number of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20). | Yes |
| Community Licence Status | The status of the community licence of the transport undertaking as recorded in the register. | Yes |
| Managed Vehicles | The number of vehicles managed as recorded in the register. | Yes’ |

(e) in the table with the heading ‘Check Community Licence Request’ the item ‘Community Licence Number’ is replaced by the following:

| ‘Community Licence Number | The serial number of the certified true copy or of the community licence for which the details are requested (free text alphanumeric field with length 1 to 20). | Yes’ |
| --- | --- | --- |

(f) the table with the heading ‘Check Community Licence Response’ is amended as follows:

(i) the following items are inserted after the item ‘Originating Authority’:

| ‘Status Code | The status code of the response (e.g. found, not found, error, etc.). | Yes |
| --- | --- | --- |
| Status Message | An explanatory status description (if necessary). | No’ |

(ii) the item ‘Transport Undertaking’ is replaced by the following:

| ‘Transport Undertaking | Yes if status code is Found’ |
| --- | --- |

(iii) the item ‘Community Licence Details’ is replaced by the following:

| ‘Community Licence Details | Yes, if status code is Found’ |
| --- | --- |

(iv) the following item is inserted after the item ‘Community Licence Details’:

| ‘Licencing Authority | The authority that issued the community licence to the transport undertaking. | Yes’ |
| --- | --- | --- |

(v) the items ‘Licence Number’ and ‘Licence Status’ are replaced by the following:

| ‘Licence Number | The serial number of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20). | Yes |
| --- | --- | --- |
| Licence Status | The status of the community licence of the transport undertaking as recorded in the register. | Yes’ |

(vi) the items ‘Certified True Copy Details’ and ‘Licence Number’ are replaced by the following:

<table>
<tbody><tr><td colspan="2">‘Certified True Copy Details</td><td>No</td></tr>
<tr><td>Certified True Copy Number</td><td>The serial number of the certified true copy of the community licence of the transport undertaking as recorded in the register (free text alphanumeric field with length 1 to 20).</td><td>Yes’</td></tr>
</tbody>
</table>

(vii) the items ‘Licence Status’, ‘Licence Type’, ‘Start Date’ and ‘Suspension Date’ are deleted;

(viii) the item ‘Suspension Expiry Date’ is replaced by the following:

| ‘Withdrawal Expiry Date | The date on which the certified true copy of the community licence withdrawal expires. | No’ |
| --- | --- | --- |

(3) in Annex VI, the following sentence is added at the end of point 2.2:

‘The escalation procedure should be detailed to the Commission upon request’;

(4) Annex VII is amended as follows:

(a) point 2 is replaced by the following:

‘2. In order to ensure privacy, the data for statistical and routing purposes shall be anonymous. Data identifying a specific transport manager, transport undertaking, community licence or CPC will not be available for statistical purposes.’;

(b) points 4 and 5 are replaced by the following:

‘4. Personal data shall not be retained in the logs for more than 6 months after a transaction is complete. Statistical and routing information will be retained indefinitely.

5\. The statistical data used for reporting may include, among others:

(a) The requesting Member State.

(b) The responding Member State.

(c) The type of message.

(d) The status code of the response.

(e) The date and time of the messages.

(f) The response time.’;

(5) in Annex VIII, point 2.4 is replaced by the following:

‘2.4. In all cases, any Infringement Notification Request and Response shall be acknowledged with an Infringement Notification Acknowledgment’.
