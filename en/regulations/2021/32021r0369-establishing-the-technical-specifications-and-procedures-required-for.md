---
title: "Commission Implementing Regulation (EU) 2021/369 of 1 March 2021 establishing the technical specifications and procedures required for the system of interconnection of central registers referred to in Directive (EU) 2015/849 of the European Parliament and of the Council (Text with EEA relevance)"
identifier: "32021R0369"
eli: "http://data.europa.eu/eli/reg_impl/2021/369/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2021-03-01
entry_into_force: 2021-12-07
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021R0369"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2021/369 of 1 March 2021 establishing the technical specifications and procedures required for the system of interconnection of central registers referred to in Directive (EU) 2015/849 of the European Parliament and of the Council (Text with EEA relevance)

**COMMISSION IMPLEMENTING REGULATION (EU) 2021/369**

**of 1 March 2021**

**establishing the technical specifications and procedures required for the system of interconnection of central registers referred to in Directive (EU) 2015/849 of the European Parliament and of the Council**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Directive (EU) 2015/849 of the European Parliament and of the Council of 20 May 2015 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing amending Regulation (EU) No 648/2012 of the European Parliament and of the Council, and repealing Directive 2005/60/EC of the European Parliament and of the Council and Commission Directive 2006/70/EC (1), and in particular Article 31a thereof,

Whereas:

(1) Member States are required to interconnect their national central beneficial ownership registers via the European Central Platform established by Article 22(1) of Directive (EU) 2017/1132 of the European Parliament and of the Council (2), and the interconnection should be set up in accordance with the technical specifications and procedures established by the implementing acts adopted by the Commission in accordance with Article 24 of that Directive. Nevertheless, the differences between the purpose, scope and content of the registers interconnected under Directive (EU) 2017/1132 and the central beneficial ownership registers established under Directive (EU) 2015/849 necessitate defining and adopting further technical specifications, measures and other requirements that ensure uniform conditions for the implementation of the system.

(2) The measures provided for in this Regulation are in accordance with the opinion of the Committee on the Prevention of Money Laundering and Terrorism Financing,

HAS ADOPTED THIS REGULATION:

## Article 1

The technical specifications and procedures for the system of interconnection of registers referred to in Article 30 and 31 of Directive (EU) 2015/849 shall be as set out in the Annex.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 1 March 2021.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 141, 5.6.2015, p. 73

(2) Directive (EU) 2017/1132 of the European Parliament and of the Council of 14 June 2017 relating to certain aspects of company law (OJ L 169, 30.6.2017, p. 46).

## ANNEX — Setting out the technical specifications and procedures referred to in Article 1

**1\. Subject matter**

The Beneficial Ownership Registers Interconnection System (‘BORIS’) shall be established as a decentralised system interconnecting the central national beneficial ownership registers and the European e-Justice Portal (1) through the European Central Platform (2). BORIS shall serve as a central search service making available all information related to beneficial ownership in line with the provisions of Directive (EU) 2015/849. (3)

**2\. Definitions**

(a) ‘register’ means national central registers on beneficial ownership information referred to in Articles 30 and 31 of Directive (EU) 2015/849;

(b) ‘qualified user’ means the users of BORIS referred to in points (a) and (b) of Article 30(5) and in points (a) and (b) of Article 31(4) of the Directive (EU) 2015/849;

(c) ‘minimum mandatory information’ means the common set of information with the same structure and types in all registers in the Member States;

(d) ‘additional information’ means the commonly predefined set of information that Member States may decide to share – in addition to the ‘minimum mandatory information’ – partly or entirely through BORIS;

(e) ‘national registration number’ means the individual identity number attributed under national law to a company or other legal entity, or to a trust or a similar arrangement in the beneficial ownership register.

**3\. The relationship of national registration number with the European Unique Identifier and company registration number**

|  | 3.1. | The beneficial ownership register shall share with the European Central Platform the national registration number and, for companies, the European Unique Identifier (‘EUID’) attributed to them in the Business Registers Interconnection System (‘BRIS’) (4) as well as the company registration number, in case the latter is different from the national registration number. The company registration number shall be used to attribute the EUID to companies that do not have an EUID in BRIS. For other legal entities, trusts or similar arrangements, the EUID shall be attributed based on the national registration number. |
| --- | --- | --- |

|  | 3.2. | Users of BORIS shall be able to search companies, other legal entities, trusts or similar arrangements using the national registration number and the company registration number, if different from the national registration number. |
| --- | --- | --- |

|  | 3.3. | Member States may choose not to provide national registration numbers for trusts or similar legal arrangements. With regard to trusts or similar legal arrangements created under the law of the Member State where they are held in the beneficial ownership register, this derogation only applies for a period of five years counted from the date on which BORIS becomes operational. |
| --- | --- | --- |

**4\. Methods of communication**

BORIS shall use service-based methods of electronic communication, such as web-services, for the purpose of interconnection of registers.

The communication between the portal and the platform, and between a register and the platform, shall be one-to-one communication.

**5\. Communication protocols**

Secure internet protocols, such as HTTPS, shall be used for the communication between the portal, the platform and the registers.

Standard communication protocols, such as Simple Object Access Protocol (SOAP), shall be used for the transmission of data and metadata.

**6\. Security standards**

For the communication and distribution of information via BORIS, the technical measures for ensuring minimum information technology security standards shall include:

(a) measures to ensure confidentiality of information, including by using secure channels, such as HTTPS;

(b) measures to ensure the integrity of data while being exchanged;

(c) measures to ensure the non-repudiation of origin of the sender of information within BORIS and the non-repudiation of receipt of information;

(d) measures to ensure logging of security events in line with recognised international recommendations for information technology security standards;

(e) measures to ensure the authentication and authorisation of any qualified users and measures to verify the identity of systems connected to the portal, the platform or the registers within BORIS;

(f) where necessary, measures to protect against automated searches and copying of registers, such as limiting the results returned by each register to a maximum number and using a CAPTCHA (5) functionality.

**7\. Data to be exchanged in the framework of BORIS**

|  | 7.1. | The set of information in the national registers concerning a corporate or other legal entity, or a trust or a similar type of legal arrangement is referred to as ‘BO record’. The ‘BO record’ includes data on the profile of the entity or arrangement concerned, on the person of the beneficial owner or owners of that entity or arrangement, as well as on the beneficial interest(s) held by those owners. |
| --- | --- | --- |

|  | 7.2. | In relation to a company or other legal entity, as well as in relation to a trust or a similar arrangement, data on the profile shall include information on the name, legal form, as well as the registration address and the national registration number, if any. |
| --- | --- | --- |

|  | 7.3. | Each Member State shall have the possibility to extend the minimum mandatory information with additional information. With regard to the beneficial owner and the beneficial interest held by him/her, minimum mandatory information shall consist of the data set out in the second subparagraph of Article 30(5) and in the second subparagraph of Article 31(4) of Directive (EU) 2015/849. With regard to the identity of the beneficial owner, additional information shall include at least the date of birth or contact details, as set out in the last sentence of Article 30(5) and third subparagraph of Article 31(4). The data from the BO record shall be modelled based on the established interface specification. |
| --- | --- | --- |

|  | 7.4. | The exchange of information shall also include messages necessary for the operation of the system, such as for acknowledgement of receipt, logging and reporting. |
| --- | --- | --- |

**8\. Structure of the standard message format**

The exchange of information between the registers, the platform and the portal shall be based on standard data-structuring methods and shall be expressed in a standard message format such as XML (6).

**9\. Data for the platform**

|  | 9.1. | In accordance with the interoperability requirements the services to be exposed by each register shall be unified and present the same interface in order to enable the interaction by the calling application, such as the platform, with one single kind of interface exposing a common set of data elements. Member States shall align their internal data structure using mapping tables or similar technical implementation to meet the requirements of the interface specifications to be provided by the Commission. |
| --- | --- | --- |

<table>
<tbody><tr><td></td><td>9.2.</td><td>The following type of data shall be provided for the platform to perform its functions:<table><tbody><tr><td>(a)</td><td>data allowing for the identification of systems that are connected to the platform. Those data could consist of URLs or any other number or code uniquely identifying each system within BORIS;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>any other operational data that is necessary for the platform to ensure the proper and efficient functioning of the search service and the interoperability of the registers with the platform. Those data may include code lists, reference data, glossaries and related translations of those metadata, as well as logging and reporting data.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

|  | 9.3. | The data and metadata handled by the platform shall be processed and stored in line with the security standards set out in Section 5. |
| --- | --- | --- |

**10\. Methods of operation of the system and information technology services provided by the platform**

|  | 10.1 | For the distribution and exchange of information, the system shall be based on the following technical method of operation: [image] |
| --- | --- | --- |

|  | 10.2. | For the delivery of messages in the relevant language version, the European e-Justice Portal shall provide reference data artefacts, such as code lists, controlled vocabularies and glossaries. Where relevant, these shall be translated into the official languages of the Union. Where possible, recognised standards and standardised messages shall be used. |
| --- | --- | --- |

|  | 10.3. | The Commission shall share with the Member State further details on the technical method of operation and the implementation of the information technology services provided by the platform. |
| --- | --- | --- |

**11\. Search criteria**

|  | 11.1. | At least one country shall be selected when running a search. |
| --- | --- | --- |

<table>
<tbody><tr><td></td><td>11.2.</td><td>The portal shall provide the following harmonised criteria for the search:<table><tbody><tr><td>(a)</td><td>with regard to the companies or other legal entities, the trusts or similar arrangements:<table><tbody><tr><td>(i)</td><td>Name of the legal entity or arrangement;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(ii)</td><td>National registration number. The search criteria under (i) and (ii) can be used alternatively. </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>with regard to persons as beneficial owners:<table><tbody><tr><td>(i)</td><td>First name and surname of the beneficial owner;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(ii)</td><td>Date of birth of the beneficial owner. The search criterion under (i) and (ii) shall be used cumulatively. </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

|  | 11.3. | Further search criteria may be available on the portal. |
| --- | --- | --- |

**12\. Payment modalities and online registration**

|  | 12.1. | For the particular data for which Member States charge fees and which are made available on the portal via BORIS, the system shall allow users to pay online by using widely used payment methods such as credit and debit cards. |
| --- | --- | --- |

|  | 12.2. | BORIS shall contain measures to ensure a possibility for an online registration in accordance with Article 30(5a) and Article 31(4a) of Directive (EU) 2015/849. |
| --- | --- | --- |

**13\. Availability of services**

|  | 13.1. | The service shall available be 24h/7 days, with an availability rate of BORIS of at least 98 % excluding scheduled maintenance. |
| --- | --- | --- |

<table>
<tbody><tr><td></td><td>13.2.</td><td>Member States shall notify the Commission of maintenance activities as follows:<table><tbody><tr><td>(a)</td><td>5 working days in advance for maintenance operations that may cause an unavailability period of up to 4 hours;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>10 working days in advance for maintenance operations that may cause an unavailability period of up to 12 hours;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(c)</td><td>30 working days in advance for infrastructure computer room maintenance, which may cause up to 6 days unavailability period per year. To the extent possible, maintenance operations shall be planned outside working hours (19.00–8.00 CET). </td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

|  | 13.3. | Where Member States have fixed weekly service windows, they shall inform the Commission of the time and day of the week when such fixed weekly windows are planned. Without prejudice to the obligations in points (a) to (c) of the second paragraph, where Member State systems become unavailable during such a fixed window, Member States may choose not to notify the Commission. |
| --- | --- | --- |

|  | 13.4. | In case of unexpected technical failure causing unavailability of more than half an hour of the systems of Member States, they shall inform the Commission without delay during working hours (9.00–16.00 CET) of their system unavailability, and, if known, of the projected resuming of the service. |
| --- | --- | --- |

|  | 13.5. | In case of unexpected failure of the central platform or of the portal, the Commission shall inform Member States without delay during working hours (9.00–16.00 CET) of the unavailability of the platform or the portal, and if known, of the expected resuming of the service. |
| --- | --- | --- |

**14\. Rules of transcription and transliteration**

Each Member State shall transcribe or transliterate the search requests targeted to them and the returned results in accordance with their national standards.

(1) Hereinafter: the portal.

(2) The European Central Platform (hereinafter: the platform) is established by Article 22(1) of Directive (EU) 2017/1132 of the European Parliament and of the Council of 14 June 2017 relating to certain aspects of company law (OJ L 169, 30.6.2017, p. 46).

(3) This being without prejudice to any additional functionalities BORIS might acquire in the future.

(4) Article 16(1) of Directive (EU) 2017/1132 of the European Parliament and of the Council of 14 June 2017 relating to certain aspects of company law and Article 8 of the Annex to Commission Implementing Regulation (EU) 2015/884 of 8 June 2015 establishing technical specifications and procedures required for the system of interconnection of registers established by Directive 2009/101/EC of the European Parliament and of the Council.

(5) ‘Completely Automated Public Turing test to tell Computers and Humans Apart’.

(6) Extensible Markup Language.
