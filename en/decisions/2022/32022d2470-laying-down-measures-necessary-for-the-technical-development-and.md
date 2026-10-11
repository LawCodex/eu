---
title: "Commission Implementing Decision (EU) 2022/2470 of 14 December 2022 laying down measures necessary for the technical development and implementation of the centralised system for the identification of Member States holding conviction information on third-country nationals and stateless persons (ECRIS-TCN)"
identifier: "32022D2470"
eli: "http://data.europa.eu/eli/dec_impl/2022/2470/oj"
type: decision
subtype: implementing
jurisdiction: eu
language: en
date: 2022-12-14
entry_into_force: 2022-09-07
last_amended: 2025-12-04
consolidated_version: "02022D2470-20251204"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02022D2470-20251204"
retrieved: 2026-10-11
---

# Commission Implementing Decision (EU) 2022/2470 of 14 December 2022 laying down measures necessary for the technical development and implementation of the centralised system for the identification of Member States holding conviction information on third-country nationals and stateless persons (ECRIS-TCN)

**COMMISSION IMPLEMENTING DECISION (EU) 2022/2470**

**of 14 December 2022**

**laying down measures necessary for the technical development and implementation of the centralised system for the identification of Member States holding conviction information on third-country nationals and stateless persons (ECRIS-TCN)**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING DECISION (EU) 2025/2281 of 13 November 2025 </td><td> L 2281</td><td>1</td><td>14.11.2025</td></tr>
</table>

**COMMISSION IMPLEMENTING DECISION (EU) 2022/2470**

**of 14 December 2022**

**laying down measures necessary for the technical development and implementation of the centralised system for the identification of Member States holding conviction information on third-country nationals and stateless persons (ECRIS-TCN)**

## Article 1 — Entering data into ECRIS-TCN

When entering data into ECRIS-TCN in accordance with Article 5 of Regulation (EU) 2019/816, the central authority of the convicting Member State shall use the data model set out in Section I of the Annex to this Decision.

The technical specifications for the data elements included in the data model shall be consistent with the data model for the ECRIS reference implementation referred to in Article 4(3) of that Regulation.

## Article 2 — Processing of data

1\. Where alphanumeric data together with either fingerprint data or the facial image of a person, or with both, are included in a data record created in ECRIS-TCN in accordance with Article 5 of Regulation (EU) 2019/816, the alphanumeric data shall be linked to their corresponding fingerprint data and facial image.

2\. The fingerprint images compression algorithm to be used shall follow the recommendations of National Institute of Standards and Technology (‘NIST’).

Fingerprint data with a resolution of 500 ppi shall be compressed using the WSQ algorithm (ISO/IEC 19794-5:2005).

Fingerprint data with a resolution of 1 000 ppi shall be compressed using the JPEG 2000 image compression standard (ISO/IEC 15444-1) and coding system.

The target compression ratio shall be 15:1.

3\. Replacement or update in ECRIS-TCN of the fingerprint data referred to in Article 4(7) shall be preceded by successful verification of the identity by the central authority of the convicting Member State. The technical specifications for that replacement or update shall be set in accordance with the principles contained in the design of the physical architecture of ECRIS-TCN referred to Article 11(3) of Regulation (EU) 2019/816.

4\. The facial images compression algorithm used shall follow the recommendations of the National Institute of Standards and Technology (‘NIST’).

Facial images shall be compressed only once with the following compression conditions:

(a) compressed with JPG (ISO/IEC 10918) or JPEG 2000 (ISO/IEC 15444) image compression standard and coding system;

(b) a 20:1 maximum allowed image compression ratio.

## Article 2a — Data quality verification mechanism

1\. When entering or modifying alphanumeric data, fingerprint data or facial images in ECRIS-TCN the central authority of the convicting Member State shall use a data quality verification mechanism or its equivalent in their national ECRIS implementation software referred to in Article 4(4) to (7) of Regulation (EU) 2019/816.

2\. The data quality verification mechanism referred to in paragraph 1 shall be integrated into the ECRIS reference implementation, developed as a software application and established in the ECRIS-TCN central system.

3\. eu-LISA shall be responsible for the development, maintenance and updating of the data quality verification mechanism, pursuant to Article 11(2) of Regulation (EU) 2019/816.

4\. Where Member States do not make use of the data quality verification mechanism referred to in paragraph 1 and use instead its equivalent in their national ECRIS implementation software, they shall ensure that it guarantees the same alphanumeric data, fingerprints data and facial images quality verification as that data quality verification mechanism.

## Article 3 — Alphanumeric data quality

3\. The data quality verification process shall apply to entering or modifying all alphanumeric data, and ensure that as a minimum the following conditions are met:

(a) all mandatory fields are filled in or hold the value ‘unknown’;

(b) when a first name contains the value ‘unknown’, the surname shall not hold the value ‘unknown’, and vice versa, unless a pseudonym, first name or surname of alias, or fingerprints for the same person are available;

(c) the data element ‘nationality or nationalities’ in the incoming message of the convicting Member State shall be verified against a predefined list of countries, but may contain one of the values ‘unknown’ or ‘stateless’.

4\. A new data record shall not be created where a record containing identical alphanumeric data has already been created in ECRIS-TCN by the same Member State, in particular where the same Member State Reference Code from the same Member State already exists.

When comparing the identicalness of the data records, only the alphanumeric data elements marked as relevant for such comparison in the data model set out in Section I of the Annex, shall be taken into account.

Empty alphanumeric data elements in any of the data records compared shall not be taken into account for the purpose of this comparison.

5\. Where a record contains any alphanumeric data which does not comply with the standards set out in paragraphs 3 and 4, that record shall be rejected by ECRIS-TCN in its entirety and shall not be stored nor processed.

## Article 4 — Fingerprint data quality

4\. For the purpose of the data quality verification process, Member States shall use at least version 2.0 of the Fingerprint Image Quality (NFIQ) metric, defined by NIST.

5\. The data quality verification process shall apply to all fingerprint data entered into or modified in ECRIS-TCN, and shall ensure that at least the following conditions are met:

(a) the fingerprint data consists of up to ten individual fingerprints: rolled, flat or both;

(b) all fingerprints are labelled;

(c) the fingerprint data is captured by live scans or inked on paper, provided that the fingerprints inked on paper have been scanned in the required resolution and with the same quality;

(d) the fingerprint data shall be provided in one file containing fingerprint digital images (the NIST file) and shall be submitted in accordance with the ANSI/NIST-ITL 1-2011 Update 2015 standard (or newer version);

(e) the NIST file shall allow for the inclusion of complementary information such as the conditions of fingerprint registration, the method used for acquiring individual fingerprint images and the quality value computed by the Member States during the data quality verification process;

(f) the fingerprint data has a nominal resolution of either 500 or 1000 ppi (with an acceptable deviation of +/– 10 ppi) with 256 grey levels;

(g) the fingerprint data meets the quality thresholds that shall be determined after carrying out the relevant tests referred to in Article 11(1) of Regulation (EU) 2019/816 during the implementation phase.

6\. When querying ECRIS-TCN with fingerprint data to identify the Member States holding criminal records information on a third-country national in accordance with Article 7 of Regulation (EU) 2019/816, the competent authorities shall use fingerprint data meeting the conditions referred to in paragraph 5, points (d) and (f) of this Article whenever possible.

7\. Fingerprint data, except fingerprint data referred to in paragraph 8, entered into or modified in ECRIS-TCN, which does not comply with the conditions set out in paragraph 5, shall be rejected by ECRIS-TCN in its entirety and shall not be stored nor processed.

8\. For the data records referred to in Article 5(5) of Regulation (EU) 2019/816, any fingerprint data which does not comply with the conditions set out in paragraph 5 of this Article shall be stored in ECRIS-TCN, but may be used only by the competent authorities to confirm the identity of a third-country national who has been identified as a result of an alphanumeric search. When entering such data records in ECRIS-TCN, the central authority of the convicting Member State shall ensure that these data records are clearly distinguishable from the other data records.

## Article 4a — Facial images quality

1\. The data quality verification process shall apply to all facial images entered into or modified in ECRIS-TCN, and shall ensure that at least the following conditions are met:

(a) only one facial image is provided in the NIST file and is submitted in accordance with the ANSI/NIST-ITL 1-2011 Update 2015 standard, or any newer version available;

(b) the facial images are either grayscale, colour or near infrared;

(c) the quality of the facial images is based on the image requirements of ISO/IEC 19794-5:2011 Frontal image type, or any newer version available;

(d) the NIST file allows the inclusion of complementary information, including the date when the image was taken;

(e) the facial images, in portrait mode, are at a minimum resolution of 600 pixels by 800 pixels and a maximum resolution of 1 200 pixels by 1 600 pixels;

(f) the face occupies a space within the image which ensures a minimum of 120 pixels between the centre of each eye.

2\. Facial images, entered into or modified in ECRIS-TCN, which do not comply with the conditions set out in paragraph 1, shall be rejected by ECRIS-TCN and shall neither be stored nor processed.

## Article 5 — Accessing and querying ECRIS-TCN

1\. When querying ECRIS-TCN to identify the Member States holding criminal records information on a third-country national in accordance with Article 7 of Regulation (EU) 2019/816, the competent authorities shall use the data model set out in Section II of the Annex to this Decision.

2\. When performing a query referred to in paragraph 1, the competent authorities shall fill in as many data elements identifying the third-country national concerned as available. Unless the query contains the fingerprint digital images (the NIST file), a minimum three such data elements shall be chosen among the ones marked for this purpose in the data model set out in Section II of the Annex.

3\. Following the tests referred to in Article 11(1) of Regulation (EU) 2019/816 carried out during the implementation phase, the following technical specifications shall be established:

(a) the list of data fields in respect of data that can be used for an inexact search;

(b) conditions when a search result is to be considered a match, taking into account the performance requirements of the ECRIS-TCN central system set out in Section III of the Annex and the acceptable level of false positives and false negatives.

4\. The number of records returned as a result of a query shall not exceed ten per Member State. Additional restrictions on the number of records returned may be imposed, where appropriate.

5\. Except where otherwise provided for in Regulation (EU) 2019/816, the central authorities shall at all times have access to all the data entered by them into ECRIS-TCN, including access to multiple data records at the same time.

6\. The lists of profiles of staff authorised to access ECRIS-TCN, established by the competent authorities in accordance with Articles 12(1)(d) and 15 of Regulation (EU) 2019/816, as well as their updates shall be provided to eu-LISA.

## Article 6 — Keeping and accessing logs

1\. eu-LISA and the competent authorities shall be responsible for providing the necessary infrastructure and tools for logging data processing operations in ECRIS-TCN in accordance with Article 31 of Regulation (EU) 2019/816, and in particular the tools for aggregating and searching logs.

eu-LISA, in consultation with the ECRIS-TCN Advisory Group referred to in Article 39 of Regulation (EU) 2019/816 (‘ECRIS-TCN Advisory Group’), and the competent authorities, shall also be responsible for specifying their respective logging standards, practices and procedures, including the specific format of the logging records and the procedure for sharing log records.

2\. eu-LISA and the competent authorities shall be responsible for implementing their respective standards and procedures referred to in paragraph 1. That implementation shall include:

(a) inspecting the logs in reaction to incidents and where possible in a proactive manner,

(b) the logs management tasks such as archiving, safe storage, high availability and protection against unauthorised access in accordance with Article 19 of Regulation (EU) 2019/816.

3\. eu-LISA shall be responsible for making the logs available to the competent authorities, on request, in accordance with the procedure specified in accordance with paragraph 1, second subparagraph.

4\. The competent authorities shall be responsible for keeping their respective logs referred to in Article 31 of Regulation (EU) 2019/816, managing them and providing them to eu-LISA, on request, in accordance with the procedure specified in accordance with paragraph 1, second subparagraph.

5\. Each data processing operations log of ECRIS-TCN shall, as a minimum, contain a chronological record that provides documentary evidence of the sequence of activities that have affected at any time a specific operation, procedure, or event.

6\. eu-LISA and the competent authorities shall each define the list of staff authorised to access the data processing operations logs of ECRIS-TCN and their profiles in accordance with Article 31 of Regulation (EU) 2019/816.

## Article 7 — Statistics

1\. The Central Repository for Reporting and Statistics, established and implemented by eu-LISA in accordance with Article 39(2) of Regulation (EU) 2019/818, and the ECRIS reference implementation shall produce statistics relating to the recording, storage and exchange of information extracted from criminal records through ECRIS-TCN and the ECRIS reference implementation, referred to in Article 32 of Regulation (EU) 2019/816.

2\. The statistics referred to in paragraph 1 shall include in particular the following business statistics:

(a) as concerns system usage indicators:

(i) number of data records created for TCN and for dual (TCN/EU) nationals;

(ii) number of data records modified for TCN and for dual (TCN/EU) nationals;

(iii) number of data records erased for TCN and for dual (TCN/EU) nationals;

(iv) number of viewings by central authorities of their own data records in accordance with Article 5(5);

(v) number of queries with respect to TCN and with respect to dual (TCN/EU) nationals;

(b) as concerns data indicators:

(i) number of records in the database;

(ii) number of records containing fingerprints;

(iii) number of records containing flags established in accordance with Article 5(1), point (c), of Regulation (EU) 2019/816 for the convictions of a terrorist offence or of any other criminal offence listed in the Annex to Regulation (EU) 2018/1240;

(iv) report on presence of alphanumeric data;

(v) report on accuracy of birth date;

(vi) number of records not accepted for inclusion;

(vii) number of fingerprint data not accepted for inclusion pursuant to Article 4(7) of this Decision;

(viii) number of records containing facial image;

(ix) number of records containing facial image not accepted for inclusion pursuant to Article 4a(2) of this Decision;

(c) as concerns matching efficiency indicators:

(i) number of records returned when performing an exact search for convicting Member States;

(ii) number of records returned when performing an inexact search for convicting Member States;

(iii) number of exact searches performed using alphanumeric data or fingerprints, or both;

(iv) number of inexact searches performed using alphanumeric data or fingerprints, or both;

(v) number of exact search hits, based on the subsequent ECRIS requests;

(vi) number of inexact search hits, based on the subsequent ECRIS requests;

(d) other indicators:

(i) which competent authority performed the search;

(ii) purpose of the searches in accordance with Article 7 of Regulation (EU) 2019/816, specified per competent authority that performed the search.

3\. Where relevant, the statistics referred to in paragraph 2 shall be produced separately for each competent authority.

4\. The statistics referred to in paragraph 1 shall include in particular the following technical statistics, as concerns quality of service indicators:

(a) success/failure ratio of requests;

(b) system availability;

(c) response time statistics for every use case supported by the system.

5\. The statistics referred to in paragraphs 1to 4 shall be produced daily.

6\. The Member States that use their national ECRIS implementation software, as provided for in Article 4(4) to (7) of Regulation (EU) 2019/816, shall ensure that their national ECRIS implementation software allows for producing the same statistics as the ECRIS reference implementation.

## Article 8 — Performance requirements of ECRIS-TCN

1\. Performance requirements of the ECRIS-TCN central system for creating, modifying, erasing and viewing data records as well as for searching a convicting Member State are set out in Section III of the Annex.

2\. eu-LISA shall monitor fingerprint data accuracy performance in ECRIS-TCN centrally on the data entered by the Member States in ECRIS-TCN, based on a representative sample of cases.

3\. The monitoring referred to in paragraph 2 shall be carried out on a regular basis, and at least once per month. eu-LISA shall disseminate reports of that monitoring to the Member States.

4\. The process to measure fingerprint data accuracy performance shall be automated to the highest possible extent and shall not allow for individual identification. That process shall be determined after carrying out the relevant tests referred to in Article 11(1) of Regulation (EU) 2019/816 during the implementation phase.

5\. The accuracy indicator ‘Failure To Enrol Rate’, concerning the proportion of registrations with insufficient quality, shall be applied in the process of fingerprints data accuracy monitoring.

The accuracy target for that indicator shall be determined after carrying out the relevant tests referred to in Article 11(1) of Regulation (EU) 2019/816 during the implementation phase.

## Article 9 — Availability and recoverability requirements of ECRIS-TCN

1\. The ECRIS-TCN central system shall have an availability ratio of at least 97,6 %, calculated over a year. The planned maintenance shall take place outside the office hours of eu-LISA and the central authorities.

2\. ECRIS-TCN operations shall be maintained in case of any potential disturbing event or adverse situation in accordance with the Recovery Time Objective values approved by eu-LISA and the Member States following a Business Impact Analysis process run on an annual basis.

3\. eu-LISA shall ensure that data included in ECRIS-TCN can be restored in case of any potential disturbing event or adverse situation, in accordance with the Recovery Point Objective values approved by eu-LISA and the Member States as specified in a Business Impact Analysis process run on an annual basis).

## Article 10 — Communication infrastructure for ECRIS-TCN

1\. The communication infrastructure referred to in Article 4(1)(d) shall be the Trans European Services for Telematics between Administrations (TESTA) EuroDomain Network, composed of the TESTA EuroDomain Access Point (TAP) and the TESTA European backbone. Any further developments thereof or any alternative secure network shall ensure that the communication infrastructure in place continues to fulfil the necessary security requirements set in accordance with the principles contained in the design of the physical architecture of ECRIS-TCN referred to in Article 11(3) of Regulation (EU) 2019/816, as well as in the ECRIS-TCN Regulation itself.

2\. In accordance with paragraph 1 of this Article and Articles 3(15) and 4(1)(d) of the ECRIS-TCN Regulation, as long as the communication infrastructure for ECRIS-TCN is the TESTA EuroDomain Network, the national central access point for ECRIS-TCN shall be understood as the TESTA EuroDomain Access Point (TAP).

## Article 11 — Interface software

The technical specifications of the interface software shall be set in accordance with the principles contained in the design of the physical architecture of ECRIS-TCN referred to in Article 11(3) of Regulation (EU) 2019/816.

## Article 12 — Development of the technical specifications

eu-LISA, in consultation with the ECRIS-TCN Advisory Group, shall be responsible for the development of detailed technical specifications of ECRIS-TCN referred to in Articles 1, 2(3), 4(5)(g), 5(3), 5(4), 8(4), 8(5) and 11 in accordance with the requirements set out in this Decision.

## Article 13 — Entry into force

This Decision shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

## ANNEX

**I. Entering data into ECRIS-TCN data model for the ‘Send data’ message**

The central authority of the convicting Member State shall use the data model set out in the table below when entering or modifying the data in ECRIS-TCN in accordance with Regulation (EU) 2019/816. Additional technical elements may be included as well as required.

<table>
<tbody><tr><td>Data element</td><td>Type of data</td><td>‘Unknown’ value possible</td></tr>
<tr><td>[Convicting Member State]: Member State</td><td>Mandatory</td><td>N/A (1)</td></tr>
<tr><td>[Convicting Member State]: Member States Central Authorities</td><td>Mandatory</td><td>N/A</td></tr>
<tr><td>[Contact person]: First name(s)</td><td>Optional</td><td>N/A</td></tr>
<tr><td>[Contact person]: Surname</td><td>Optional</td><td>N/A</td></tr>
<tr><td>[Contact person]: Second surname</td><td>Optional</td><td>N/A</td></tr>
<tr><td>[Contact person]: Phone</td><td>Optional</td><td>N/A</td></tr>
<tr><td>[Contact person]: Fax</td><td>Optional</td><td>N/A</td></tr>
<tr><td>[Contact person]: Email</td><td>Mandatory</td><td>N/A</td></tr>
<tr><td>Username of official</td><td>Mandatory</td><td>N/A</td></tr>
<tr><td>Member State Reference Code (*1)</td><td>Mandatory</td><td>No</td></tr>
<tr><td>Unique Identifier (2)</td><td>Mandatory</td><td>No</td></tr>
<tr><td>Timestamp of sending the data record from ECRIS RI or national implementation software to the ECRIS-TCN central system</td><td>Mandatory</td><td>N/A</td></tr>
<tr><td>Surname(s) (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>First name(s) (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Full name (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Birth date (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Birth place: [Place]: Country (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Birth place: [Place]: Town name (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Birth place: [Place]: Country subdivision (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Birth place: [Place]: Town code (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Nationality or nationalities (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Gender (*1)</td><td>Mandatory</td><td>Yes</td></tr>
<tr><td>Previous surname(s) (*1)</td><td>Mandatory if applicable (3)</td><td>Yes</td></tr>
<tr><td>Previous first name(s) (*1)</td><td>Mandatory if applicable (4)</td><td>Yes</td></tr>
<tr><td>Mother’s surname(s) (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Mother’s first name(s) (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Father’s surname(s) (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Father’s first name(s) (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Identity number (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Identification document]: Identification category (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Identification document]: Identification document number (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Identification document]: Identification document type (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Identification document]: Name of the issuing authority of the identification document</td><td>Optional</td><td>No</td></tr>
<tr><td>[Identification document]: Where relevant, 3-letter code of the issuing country (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Travel document] (5): Travel document number (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Travel document]: Travel document type (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Travel document]: Name of the issuing authority of the travel document (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Travel document]: Where relevant, 3-letter code of the issuing country (*1)</td><td>Optional</td><td>No</td></tr>
<tr><td>Pseudonym</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias first name(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias surname(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias full name</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias gender</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: Country</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: Town name</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: Country subdivision</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: Town code</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Birth date</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias nationality or nationalities</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Mother first name(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Mother surname(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Father first name(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias Father surname(s)</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Number of the identification document</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Type of identification document</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Name of the issuing authority of the identification document</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Travel document number</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Travel document type</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Name of the issuing authority of the travel document</td><td>Optional</td><td>No</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td><td>No</td></tr>
<tr><td>Fingerprint digital images (the NIST file)</td><td>Optional</td><td>No</td></tr>
<tr><td>Reference number of fingerprint digital image</td><td>Mandatory if the fingerprint digital images are provided</td><td>No</td></tr>
<tr><td colspan="3"></td></tr>
<tr><td>Facial image (the NIST file)</td><td>Optional</td><td>No</td></tr>
<tr><td>Reference number of facial image</td><td>Mandatory if the facial image is provided</td><td>No</td></tr>
<tr><td colspan="3"></td></tr>
<tr><td>Parameter indicating a data record created in accordance with Article 5(5) of Regulation (EU) 2019/816 (legacy data parameter)</td><td>Mandatory if the fingerprint digital images are provided</td><td>No</td></tr>
<tr><td>Flag established in accordance with Article 5(1), point (c), of Regulation (EU) 2019/816</td><td>Optional</td><td>No</td></tr>
<tr><td colspan="3">(1)  N/A means ‘not applicable’.  (2)  The combination of the Member State Reference Code and ISO code of the convicting Member State  (3)  Concerns only cases when a person has previous name(s) or surname(s), e.g. maiden name.  (4)  Idem  (5)  Travel document means a passport or other equivalent document entitling the holder to cross the external borders and to which a visa may be affixed, as listed in Decision 1105/2011/EU of the European Parliament and of the Council of 25 October 2011 on the list of travel documents which entitle the holder to cross the external borders and which may be endorsed with a visa and on setting up a mechanism for establishing this list (OJ L 287, 4.11.2011, p. 9).  (*1)  alphanumeric data element of an existing data record, which shall be compared with a respective data element of the data record to be created in accordance with Article 3(4). </td></tr>
</tbody>
</table>

**II. Accessing and querying ECRIS-TCN – data model for the ‘Search a convicting Member State’ message**

The competent authorities shall use the data model set out in the table below when using ECRIS-TCN to identify the Member States holding criminal records information on a third-country national in accordance with Article 7 of Regulation (EU) 2019/816.

<table>
<tbody><tr><td>Data element</td><td>Type of data</td></tr>
<tr><td>Requesting competent authority</td><td>Mandatory</td></tr>
<tr><td>Username of official</td><td>Mandatory</td></tr>
<tr><td>Purpose of the search message</td><td>Mandatory</td></tr>
<tr><td>Member State Reference Code</td><td>Optional</td></tr>
<tr><td>Timestamp of sending the search data from ECRIS RI or national implementation software to the ECRIS-TCN central system</td><td>Mandatory</td></tr>
<tr><td>Exact search/Inexact search</td><td>Mandatory</td></tr>
<tr><td>Surname(s) (*1)</td><td>Optional</td></tr>
<tr><td>First name(s) (*1)</td><td>Optional</td></tr>
<tr><td>Full name</td><td>Optional</td></tr>
<tr><td>Birth date (*1)</td><td>Optional</td></tr>
<tr><td>Birth place: [Place]: country (*1)</td><td>Optional</td></tr>
<tr><td>Birth place: [Place]: town name</td><td>Optional</td></tr>
<tr><td>Birth place: [Place]: Country subdivision</td><td>Optional</td></tr>
<tr><td>Birth place: [Place]: Town code</td><td>Optional</td></tr>
<tr><td>Nationality or nationalities (*1)</td><td>Optional</td></tr>
<tr><td>Gender</td><td>Optional</td></tr>
<tr><td>Previous surname(s) (*1)</td><td>Optional</td></tr>
<tr><td>Previous first name(s) (*1)</td><td>Optional</td></tr>
<tr><td>Mother’s surname(s)</td><td>Optional</td></tr>
<tr><td>Mother’s first name(s)</td><td>Optional</td></tr>
<tr><td>Father’s surname(s)</td><td>Optional</td></tr>
<tr><td>Father’s first name(s)</td><td>Optional</td></tr>
<tr><td>Identity number (*1)</td><td>Optional</td></tr>
<tr><td>[Identification document]: Identification category</td><td>Optional</td></tr>
<tr><td>[Identification document]: Identification document number</td><td>Optional</td></tr>
<tr><td>[Identification document]: Identification document type</td><td>Optional</td></tr>
<tr><td>[Identification document]: Name of the issuing authority of the identification document</td><td>Optional</td></tr>
<tr><td>[Identification document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td></tr>
<tr><td>[Travel document]: Travel document number</td><td>Optional</td></tr>
<tr><td>[Travel document]: Travel document type</td><td>Optional</td></tr>
<tr><td>[Travel document]: Name of the issuing authority of the travel document</td><td>Optional</td></tr>
<tr><td>[Travel document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td></tr>
<tr><td>Pseudonym</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias first name(s) (*1)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias surname(s) (*1)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias full name</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias gender</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: country</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: town name</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Birth place: [Place]: country subdivision</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Birth place: [Place]: Town code</td><td>Optional</td></tr>
<tr><td>[Alias]: Birth date</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias nationality or nationalities</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Mother first name(s)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Mother surname(s)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Father first name(s)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias Father surname(s)</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Number of the identification document</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Type of identification document</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Name of the issuing authority of the identification document</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Identification document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Travel document number</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Travel document type</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Name of the issuing authority of the travel document</td><td>Optional</td></tr>
<tr><td>[Alias]: Alias [Travel document]: Where relevant, 3-letter code of the issuing country</td><td>Optional</td></tr>
<tr><td>Fingerprint digital images (the NIST file)</td><td>Optional</td></tr>
<tr><td colspan="2">(*1)  data element that might be chosen in accordance with Article 5(2) as one of the three minimum data elements for querying ECRIS-TCN system. </td></tr>
</tbody>
</table>

**III. Performance requirements for ECRIS-TCN**

The performance requirements for ECRIS-TCN should be better than or equal to the values listed in the table below.

<table>
<tbody><tr><td>Use Case</td><td>Response time based on atomic operations for 95 % of the requests</td><td>Maximum response time based on atomic operations</td></tr>
<tr><td>Create/Modify TCN data record (without fingerprints)</td><td>30 sec</td><td>60 sec</td></tr>
<tr><td>Create/Modify TCN data record (with fingerprints)</td><td>Acknowledgement: 30 sec Completion: 5 min </td><td>Acknowledgement: 60 sec Completion: 10 min </td></tr>
<tr><td colspan="3"></td></tr>
<tr><td>Create/Modify TCN data record (with facial image)</td><td>Acknowledgement: 30 sec Completion: 5 min </td><td>Acknowledgement: 60 sec Completion: 10 min </td></tr>
<tr><td colspan="3"></td></tr>
<tr><td>Erase TCN data record (with or without fingerprints)</td><td>30 sec</td><td>60 sec</td></tr>
<tr><td>View data record created by the same Member State (with or without fingerprints)</td><td>15 sec</td><td>30 sec</td></tr>
<tr><td>Search convicting Member State (exact search; without fingerprints)</td><td>15 sec</td><td>30 sec</td></tr>
<tr><td>Search convicting Member State (with fingerprints)</td><td>30 sec</td><td>60 sec</td></tr>
<tr><td>Search convicting Member State (inexact search; with or without fingerprints)</td><td>30 sec</td><td>60 sec</td></tr>
<tr><td>Verify the fingerprint data quality</td><td>10 sec</td><td>20 sec</td></tr>
</tbody>
</table>
