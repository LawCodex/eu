---
title: "Commission Implementing Decision (EU) 2026/1066 of 8 June 2026 laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of vehicle registration data"
identifier: "32026D1066"
eli: "http://data.europa.eu/eli/dec_impl/2026/1066/oj"
type: decision
subtype: implementing
jurisdiction: eu
language: en
date: 2026-06-08
entry_into_force: 2026-09-22
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026D1066"
retrieved: 2026-10-11
---

# Commission Implementing Decision (EU) 2026/1066 of 8 June 2026 laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of vehicle registration data

**COMMISSION IMPLEMENTING DECISION (EU) 2026/1066**

**of 8 June 2026**

**laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of vehicle registration data**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2024/982 of the European Parliament and of the Council of 13 March 2024 on the automated search and exchange of data for police cooperation, and amending Council Decisions 2008/615/JHA and 2008/616/JHA and Regulations (EU) 2018/1726, (EU) 2019/817 and (EU) 2019/818 of the European Parliament and of the Council (the Prüm II Regulation) (1), and in particular Article 17(3) and Article 31 thereof,

Whereas:

(1) Regulation (EU) 2024/982 establishes a framework for the automated search and exchange of certain categories of data for cross-border police cooperation, including vehicle registration data between Member States for the purpose of preventing, detecting and investigating criminal offences.

(2) Pursuant to Regulation (EU) 2024/982, the Commission is to specify technical rules for automated search and exchange of vehicle registration data to be carried out via the European Vehicle and Driving Licence Information System (EUCARIS).

(3) It is therefore necessary to lay down technical rules governing the automated searches and exchanges of such data in order to ensure interoperability, reliability and a uniform level of security across all Member States.

(4) Article 16 of Regulation (EU) 2024/982 distinguishes between different types of automated searches. Technical rules should be specified for the two types of searches to be implemented for vehicle registration data, namely searches conducted with vehicle-related data to identify the owner or holder and searches conducted with owner- or holder-related data to identify all vehicles associated with that person.

(5) To ensure a consistent approach in the exchange of vehicle registration data and an appropriate quality level of the data exchanged, it is necessary to define the mandatory data elements to be exchanged and the optional data elements that may be exchanged, the corresponding search parameters and the communication mechanisms through EUCARIS. Member States should be encouraged to exchange optional data elements when available in their national databases, to enhance the completeness and usefulness of cross-border information exchange.

(6) In accordance with Articles 1 and 2 of Protocol No 22 on the position of Denmark, annexed to the Treaty on European Union and to the Treaty on the Functioning of the European Union, Denmark did not take part in the adoption of Regulation (EU) 2024/982 and is not bound by it or subject to its application. Denmark is therefore not bound by this Decision or subject to its application.

(7) Ireland is bound by Regulation (EU) 2024/982 and is therefore bound by this Decision.

(8) The European Data Protection Supervisor delivered an opinion on 27 January 2026.

(9) The measures provided for in this Decision are in accordance with the opinion of the Prüm II Committee, established by Article 77 of Regulation (EU) 2024/982,

HAS ADOPTED THIS DECISION:

## Article 1

For the purposes of this Decision, the following definitions apply:

(a) ‘mandatory (M)’ means mandatory communication of the data element when available in any national register of a Member State;

(b) ‘optional (O)’ means optional communication of the data element when available in a national database of a Member State.;

(c) ‘entity’ means either a Member State or Europol;

(d) ‘requesting entity’ means a Member State or Europol that initiates a query;

(e) ‘reference date and time’ means a specific moment in time determined by the requesting entity and used to retrieve the data registered at that specific date and time;

(f) ‘current date and time’ means the moment in time used to retrieve the data currently registered.

## Article 2

The specifications relating to the technical rules for the automated search and exchange of vehicle registration data shall be as set out in the Annex.

## Article 3

This Decision shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

Done at Brussels, 8 June 2026.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L, 2024/982, 5.4.2024, ELI: http://data.europa.eu/eli/reg/2024/982/oj.

## ANNEX — Technical rules for the automated search and exchange of vehicle registration data as referred to in Article 2

**CHAPTER 1**

**Searches for vehicle registration data exchange**

**1\. Types of searches**

In accordance with Article 16 of Regulation (EU) 2024/982 (Prüm II), two types of searches shall be implemented for vehicle registration data, namely a search with data relating to the vehicle to find the owner or holder, and a search with data relating to the owner or holder to find all vehicles of that owner or holder.

**2\. Search on vehicle to find owner/holder**

**2.1. Description of the search**

There are two different ways to search for the information on the owner or holder of a vehicle:

— by a complete Chassis Number/Vehicle Identification Number (VIN), Reference Date and Time,

— by a complete License Plate Number, Reference Date and Time.

If the Reference Date and Time is not provided, the system shall automatically use the Current Date and Time as the reference for the search. When a search is made with a Reference Date and Time and historical information is not available in the register of a given Member State because no such information is registered, the information at the Current Date and Time may be returned with an indication that the data correspond to the current situation.

By means of these search criteria, information related to one and sometimes more vehicles will be returned. If information for only one vehicle is to be returned, the complete data set listed in point 2.2.2 shall be returned in one response.

If more than one vehicle is found, all the data elements necessary for the refinement of the search as described in point 2.2.1, shall be returned.

When the search is conducted by Chassis Number/Vehicle Identification Number and Reference Date and Time, the request shall be sent to one, some or all Member States.

When the search is conducted by License Plate Number and Reference Date and Time, the request shall be sent to one specific Member State of registration.

If the Member State of registration is uncertain, the request shall be sent to some or all Member States and the search shall be carried out on a hit/no hit basis. In the reply, the requesting entity shall receive a hit/no hit indication per requested Member State.

Member States shall provide up-to-date data. When a search is made at the Current Date and Time, the current situation shall be provided. Where the vehicle has been de-registered, the Member State of registration shall provide the information that the vehicle has been de-registered. The last known registration shall be provided upon request.

Entities shall indicate via a flag if the data relating to the holder of the vehicle, the data relating to the owner of the vehicle, the data relating to insurance and/or the last known registration, are requested to be included in the data set returned as a result of the search.

**2.2. Data sets**

**2.2.1. Mandatory data elements to be provided for the refinement of the search**

<table>
<tbody><tr><td>Data elements</td><td>M/O</td><td>Remarks</td></tr>
<tr><td colspan="3">Data relating to vehicles</td></tr>
<tr><td>Licence plate number</td><td>M</td><td>(Code A) full registration number of the vehicle (permanent number, temporary number when valid)</td></tr>
<tr><td>/Vehicle identification number (VIN)/Chassis number</td><td>M</td><td>(Code E) full vehicle identification number/chassis number of the vehicle</td></tr>
<tr><td>Member State of registration</td><td>M</td><td>Country code of the Member State of registration of the vehicle</td></tr>
<tr><td>Make</td><td>M</td><td>(Code D.1) e.g. Ford, Opel, Renault, etc.</td></tr>
<tr><td>Commercial description(s)</td><td>M</td><td>(Code D.3) e.g. Focus, Astra, Megane, etc.</td></tr>
<tr><td>EU Category Code</td><td>M</td><td>(Code J) mopeds, motorbikes, cars, etc.</td></tr>
<tr><td colspan="3"><table><tbody><tr><td>Note:</td><td>The codes are harmonised according to Annexes I and II to Council Directive 1999/37/EC (1).</td></tr>
</tbody>
</table>
 (1) Council Directive 1999/37/EC of 29 April 1999 on the registration documents for vehicles (OJ L 138, 1.6.1999, p. 57, ELI: http://data.europa.eu/eli/dir/1999/37/oj). </td></tr>
</tbody>
</table>

**2.2.2. Complete data set of data elements to be provided as a result of the search**

<table>
<tbody><tr><td>Data elements</td><td>M/O</td><td>Remarks</td></tr>
<tr><td colspan="2">Data relating to the holder of the vehicle</td><td>(Code C.1) The data refer to the holder of the specific registration certificate. The data shall be returned if requested in the search. </td></tr>
<tr><td>Type of holder</td><td>M</td><td>Natural person, legal person</td></tr>
<tr><td>Family name(s) or business name</td><td>M</td><td>(Code C.1.1.) The name can relate to a natural person or a legal person.  Separate fields are used for family name or business name, infixes and titles. They shall also be communicated in printable format  If a natural person has only one name, it is considered as a family name. </td></tr>
<tr><td>First name(s)</td><td>M</td><td>(Code C.1.2) Separate fields for first name(s) and initials. They shall also be communicated in printable format. </td></tr>
<tr><td>Address</td><td>M</td><td>(Code C.1.3) Separate fields shall be used for street, house number and annex, postal code, place of residence, country of residence, etc. and the address. They shall also be communicated in printable format. </td></tr>
<tr><td>Gender</td><td>O</td><td>Male, female, officially not specified, non-binary</td></tr>
<tr><td>Date of birth</td><td>M</td><td></td></tr>
<tr><td>Place of Birth</td><td>O</td><td></td></tr>
<tr><td>ID Number</td><td>O</td><td>An identifier that uniquely identifies the natural person or the legal person.</td></tr>
<tr><td>Type of ID Number</td><td>O</td><td>The type of ID Number (e.g. passport number).</td></tr>
<tr><td>Start date of holdership</td><td>M</td><td>Start date of the holdership of the car. This date will often be the date as printed under (I) on the registration certificate of the vehicle.</td></tr>
<tr><td>End date of holdership</td><td>M</td><td>End date of the holdership of the car.</td></tr>
<tr><td>Status of holder</td><td>O</td><td>(Code C.4) Where the owner of the vehicle (C.2) is not included in the vehicle registration certificate, reference to the fact that the holder of the registration certificate:<table><tbody><tr><td>—</td><td>is the vehicle owner,</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>is not the vehicle owner,</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>is not identified by the registration certificate as being the vehicle owner.</td></tr>
</tbody>
</table>
</td></tr>
<tr><td colspan="2">Data relating to the owner of the vehicle</td><td>(Code C.2) The data refer to the owner of the vehicle. The data shall be returned if requested in the search. </td></tr>
<tr><td>Type of owner</td><td>M</td><td>Natural person, legal person</td></tr>
<tr><td>Family name(s) or business name</td><td>M</td><td>(Code C.2.1) The name can relate to a natural person or a legal person.  Separate fields are used for family name or business name, infixes and titles. They shall also be communicated in printable format.  If a natural person has only one name, it is considered as a family name. </td></tr>
<tr><td>First name(s)</td><td>M</td><td>(Code C.2.2) Separate fields for first name(s) and initials. They shall also be communicated in printable format. </td></tr>
<tr><td>Address</td><td>M</td><td>(Code C.2.3) Separate fields shall be used for street, house number and annex, postal code, place of residence, country of residence, etc. and the address. They shall also be communicated in printable format. </td></tr>
<tr><td>Gender</td><td>O</td><td>male, female, officially not specified, non-binary</td></tr>
<tr><td>Date of birth</td><td>M</td><td></td></tr>
<tr><td>Place of Birth</td><td>O</td><td></td></tr>
<tr><td>ID Number</td><td>O</td><td>An identifier that uniquely identifies the natural person or the legal person.</td></tr>
<tr><td>Type of ID Number</td><td>O</td><td>The type of ID Number (e.g. passport number).</td></tr>
<tr><td>Start date of ownership</td><td>M</td><td>Start date of the ownership of the vehicle.</td></tr>
<tr><td>End date of ownership</td><td>M</td><td>End date of the ownership of the vehicle.</td></tr>
<tr><td colspan="3">Data relating to vehicles</td></tr>
<tr><td>Licence plate number</td><td>M</td><td>(Code A) full registration number of the vehicle</td></tr>
<tr><td>Vehicle identification number (VIN)/Chassis number</td><td>M</td><td>(Code E) full vehicle identification number/chassis number of the vehicle</td></tr>
<tr><td>Member State of registration</td><td>M</td><td>Country code of the Member State of registration of the vehicle</td></tr>
<tr><td>Make</td><td>M</td><td>(Code D.1) e.g. Ford, Opel, Renault, etc.</td></tr>
<tr><td>Commercial description(s)</td><td>M</td><td>(Code D.3) e.g. Focus, Astra, Megane, etc.</td></tr>
<tr><td>EU Category Code</td><td>M</td><td>(Code J) mopeds, motorbikes, cars, etc.</td></tr>
<tr><td>First registration data</td><td>M</td><td>(Code B) Date of first registration of the vehicle.</td></tr>
<tr><td>Start date of actual registration</td><td>M</td><td>(Code I) Date of the registration to which the certificate of the vehicle refers.</td></tr>
<tr><td>End date of registration</td><td>M</td><td>End date of the registration. This date indicates the period of validity as printed on the document (document abbreviation = H).</td></tr>
<tr><td>Status at reference date and time</td><td>M</td><td>Destructed, stolen, exported or other applicable qualifications</td></tr>
<tr><td>Start date of status</td><td>M</td><td></td></tr>
<tr><td>End date of status</td><td>M</td><td>Mandatory to provide if applicable</td></tr>
<tr><td>Maximum net power (kW)</td><td>O</td><td>(Code P.2)</td></tr>
<tr><td>Capacity</td><td>O</td><td>(Code P.1)</td></tr>
<tr><td>Type of licence number</td><td>O</td><td>Regular, transit or other types</td></tr>
<tr><td>Vehicle document ID</td><td>O</td><td>The first unique document ID as indicated on the vehicle document. A second document ID may be transmitted.</td></tr>
<tr><td>Vehicle colour</td><td>M</td><td>(Code R) Note: colours are only registered for vehicles of category M1 (i.e. cars) according to Regulation (EU) 2018/858 (2) </td></tr>
<tr><td>Mileage recordings</td><td>O</td><td>Value, date of recording, measure unity</td></tr>
<tr><td colspan="2">Data relating to insurance</td><td>The data shall be returned if requested in the search.</td></tr>
<tr><td>Insurance company name</td><td>O</td><td></td></tr>
<tr><td>Begin date of insurance</td><td>O</td><td></td></tr>
<tr><td>End date of insurance</td><td>O</td><td></td></tr>
<tr><td>Address</td><td>O</td><td>Separate fields shall be used for street, house number and annex, postal code, place of residence, country of residence, etc. and the address. They shall also be communicated in printable format.</td></tr>
<tr><td>Insurance number</td><td>O</td><td></td></tr>
<tr><td>ID number</td><td>O</td><td>An identifier that uniquely identifies the company.</td></tr>
<tr><td>Type of ID number</td><td>O</td><td>E.g. Chamber of Commerce number</td></tr>
<tr><td colspan="3">() (2) Regulation (EU) 2018/858 of the European Parliament and of the Council of 30 May 2018 on the approval and market surveillance of motor vehicles and their trailers, and of systems, components and separate technical units intended for such vehicles, amending Regulations (EC) No 715/2007 and (EC) No 595/2009 and repealing Directive 2007/46/EC (OJ L 151, 14.6.2018, p. 1, ELI: http://data.europa.eu/eli/reg/2018/858/oj). </td></tr>
</tbody>
</table>

**3\. Search for all vehicles of owner-holder**

**3.1. Description of the search**

This search aims to retrieve all vehicles held and/or owned by a specific natural person or legal person, either currently, or at a specified date and time in the past, in the Member State of registration.

In accordance with Article 16 of Regulation (EU) 2024/982, it is mandatory for entities to execute a search with:

first name(s), family name(s) and full date of birth where the owner or holder of the vehicle is a natural person;

legal person’s name where the owner or holder of the vehicle is a legal person.

Optional search parameters listed in the tables at points 3.2.1 and 3.2.2 may be used in addition to the mandatory search parameters, to allow the system to refine the result of the search to only one candidate, in case the mandatory search parameters lead to multiple candidates. The ID number, when available, shall be used in the first place to refine the result of the search, instead of the combination of first name, family name and date of birth. When the ID number is available and is used to perform the search, the result of the search shall also be returned even if one data element among family name, first name, and full date of birth does not match.

The optional search parameters used to refine the search for all vehicles of an owner or holder can be obtained from the results of a search on vehicle to find owner/holder as referred to in point 2.

The Member State of registration shall enable the search with the optional search parameters in the national vehicle register in accordance with its national legislation.

If a past situation is inquired, a Reference Date and Time shall be provided.

For the inquiry to succeed, the Member State of registration shall be able to identify a specific unique holder or owner (= Person of interest), i.e. the search should result in a unique candidate.

If no unique candidate is identified, only a description regarding the nature of the failure is returned as follows:

No natural person is registered under this combination of family name(s), first name(s) and date of birth;

Multiple natural persons with this combination of family name(s), first name(s) and date of birth are registered (please provide additional search parameters if possible);

No legal person is registered under this legal person’s name.

The ‘search for all vehicles of owner-holder’ request is always sent to the Member State of registration, i.e. the Member State providing personal data via the preceding initial search on vehicle data relating to the vehicle to find owner/holder. A Person of interest may hold or own vehicles in various Member States. In that case, the information is to be collected using separate requests in EUCARIS to the various Member States.

The identification data required to identify a Person of interest may be different per Member State because of difference in data elements that are registered. National identifiers are specific to each Member State, as well as differences in the name data of one and the same person, because of marriage, transliteration difference, or difference in the use of diacritical characters.

**3.2. Data set**

**3.2.1. Search request if the Person of interest is a natural person**

| Data elements | M/O | Remarks |
| --- | --- | --- |
| Type of Person of interest | M | Code for natural person |
| Family name(s) | M | (Code C.1.1.) or (Code C.2.1.) |
| First name(s) | M | (Code C.1.2.) or (Code C.2.2.) Contains the first name(s), or the first name plus initials |
| Date of birth | M | Full date of birth |
| ID number | O | A national identifier that uniquely identifies the natural person or the legal person. |
| Type of ID number | O | E.g. national ID number or passport number |
| Place of birth | O |  |
| Gender | O | male, female, officially not specified, non-binary |
| License plate number | O | (Code A) full registration number of the vehicle which is known to be held/owned by the Person of interest |
| Vehicle identification number (VIN)/Chassis number | O | (Code E) full vehicle identification number/chassis number of the vehicle of which it is known to be held/owned by the Person of interest |

**3.2.2. Search request if the Person of interest is a legal person**

| Data elements | M/O | Remarks |
| --- | --- | --- |
| Type of Person of interest | M | Code for legal person |
| Legal person Name | M |  |
| Legal person ID number | O |  |
| Type of ID number | O | E.g. Chamber of Commerce number |
| License plate number | O | (Code A) full registration number of the vehicle which is known to be held/owned by the Person of interest |
| Vehicle identification number (VIN)/Chassis number | O | (Code E) full vehicle identification number/chassis number of the vehicle of which it is known to be held/owned by the Person of interest |

**3.2.3. Data set returned**

A list of vehicles held or owned is returned, or a message indicating that at the Reference Date and Time, no vehicles are held or owned. The exact number of vehicles will be displayed. The data set will be returned for a maximum number of 500 vehicles. Particularly legal persons may hold/own more vehicles. In that case, a message is returned indicating that the list exceeds 500 entries and thus cannot be returned in the automated inquiry. The message will also indicate the contact details to be used to obtain the result through a manual procedure.

Per vehicle held or owned:

| Data elements | M/O | Remarks |
| --- | --- | --- |
| Vehicle Identification Number (VIN) /Chassis number | M | (Code E) full vehicle identification number/chassis number of the vehicle |
| License plate number | M | (Code A) full registration number of the vehicle |
| Indication if the Person of interest is holder of the vehicle | M | Yes or no. |
| Indication if the Person of interest is owner of the vehicle | M | Yes, no or unknown. |

**3.3. Technical specifications for the search in point 3.2.1**

| Search string number | Item |
| --- | --- |
| 1 | Type of Person of interest |
| 2 | Family name(s) |
| 3 | First name(s) |
| 4 | Date of birth |
| 5 | ID number |
| 6 | Type of ID number |
| 7 | Place of birth |
| 8 | Gender |
| 9 | License plate number |
| 10 | Vehicle identification number (VIN)/Chassis number |

Search strings 1 to 10 shall be coded into a national database query and shall not be case sensitive.

Search strings 2 and 3 shall deliver a match against the corresponding fields in the national database where there is a match on any of the strings present in the corresponding field. This is commonly expressed as: Where &lt;database-field> CONTAINS &lt;search-string>.

Where in the Member State of registration, the national database does not have separate fields for First name and Family name, the search on a ‘name field’ shall be performed using the concatenation of the First name-string and the Family name-string. Search string 2 and 3 shall be permutated by the Member State of Registration between the corresponding fields to cope with cases where it is unclear which is the First name, and which is the Family name. The search shall identify records that contain both the Family name-string AND the First name-string.

The national database query shall implement the following logical expression:

[image]

**CHAPTER 2**

**The technical procedure for EUCARIS to query Member States’ databases**

**1\. Overview**

The EUCARIS software connects all entities in a mesh network, where each entity communicates directly with another entity. There is no central component required for the communication to be established.

The EUCARIS software supports different functionalities. The ‘Prüm functionality’ is used for the automated searching of vehicle registration data under Regulation (EU) 2024/982.

Each cluster of functionalities has its own authorisation, e.g. users only under the ‘Treaty of EUCARIS (3) functionality’ may not use the ‘Prüm functionality’. Administrator services are separated from the regular end-user roles.

The EUCARIS software supports secure communication to the other entities and communicates to the back-end legacy systems of Member States. Entities exchange messages by directly sending them to the recipient. Entities are connected to the TESTA network (4) or its subsequent implementations.

The messages sent over the EUCARIS network are encrypted. Encryption technologies such as SSL (Secure Sockets Layer) or TLS (Transport Layer Security) shall be used to encrypt the messages. The connection between the EUCARIS application and the national back-end shall be in a protected environment. Therefore, the messages sent to the back-end may be clear text messages.

A client application is provided to authorised users, which can be used within an entity to query Member States’ registers. It may be used by Member States to query their own register. User management, means of authentication and possible encryption are the responsibility of each entity.

**2\. User roles**

The user group called ‘Prüm users’ shall be established for the search on vehicle to find owner/holder and for the search for all vehicles of owner-holder.

Two separate user roles shall be established for:

— the search on vehicle to find owner/holder (Prüm-Owner-Holder-Info)

— the search for all vehicles of owner-holder (Prüm-All-Vehicles-of-Holder-Owner).

The end-user may benefit from the two user roles.

(3) Treaty of 29 June 2000 concerning a European Vehicle and Driving Licence Information System (EUCARIS).

(4) The TESTA network is a secure, private, EU-wide network that enables encrypted and reliable data exchange between EU institutions, Member States’ authorities and agencies, specifically for sensitive information like law enforcement and justice data.

ELI: http://data.europa.eu/eli/dec_impl/2026/1066/oj

ISSN 1977-0677 (electronic edition)
