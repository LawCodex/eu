---
title: "Commission Implementing Regulation (EU) 2025/1325 of 7 July 2025 amending Implementing Regulation (EU) 2015/2378 as regards the standard forms and computerised formats to be used for the mandatory automatic exchange of information under Council Directive 2011/16/EU as amended by Council Directive (EU) 2025/872"
identifier: "32025R1325"
eli: "http://data.europa.eu/eli/reg_impl/2025/1325/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2025-07-07
entry_into_force: 2026-01-01
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R1325"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2025/1325 of 7 July 2025 amending Implementing Regulation (EU) 2015/2378 as regards the standard forms and computerised formats to be used for the mandatory automatic exchange of information under Council Directive 2011/16/EU as amended by Council Directive (EU) 2025/872

**COMMISSION IMPLEMENTING REGULATION (EU) 2025/1325**

**of 7 July 2025**

**amending Implementing Regulation (EU) 2015/2378 as regards the standard forms and computerised formats to be used for the mandatory automatic exchange of information under Council Directive 2011/16/EU as amended by Council Directive (EU) 2025/872**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Council Directive 2011/16/EU of 15 February 2011 on administrative cooperation in the field of taxation and repealing Directive 77/799/EEC (1), and in particular Article 20(4) thereof,

Whereas:

(1) Council Directive (EU) 2025/872 (2) amended Directive 2011/16/EU to provide for the mandatory automatic exchange of information reported by the multinational enterprise groups and the large-scale domestic groups that fall within the scope of Council Directive (EU) 2022/2523 (3).

(2) In accordance with Directive 2011/16/EU, it is necessary to lay down the practical arrangements to facilitate the communication of the information referred to in Article 8ae(2) of that Directive. In particular, the automatic exchange of information pursuant to Article 8ae(5) of Directive 2011/16/EU should be carried out using a standard computerised format.

(3) Commission Implementing Regulation (EU) 2015/2378 (4) should therefore be amended accordingly.

(4) The measures provided for in this Regulation are in accordance with the opinion of the Committee on Administrative Cooperation for Taxation,

HAS ADOPTED THIS REGULATION:

## Article 1

Implementing Regulation (EU) 2015/2378 is amended as follows:

(1) in Article 2, the following paragraph 4 is added:

‘4. The computerised format to be used for the mandatory automatic exchange of information pursuant to Article 8ae(5) of Directive 2011/16/EU shall comply with Annex XVII to this Regulation.’

;

(2) the text set out in the Annex to this Regulation is added as Annex XVII.

## Article 2

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 7 July 2025.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 64, 11.3.2011, p. 1, ELI: http://data.europa.eu/eli/dir/2011/16/oj.

(2) Council Directive (EU) 2025/872 of 14 April 2025 amending Directive 2011/16/EU on administrative cooperation in the field of taxation (OJ L, 2025/872, 6.5.2025, ELI: http://data.europa.eu/eli/dir/2025/872/oj).

(3) Council Directive (EU) 2022/2523 of 15 December 2022 on ensuring a global minimum level of taxation for multinational enterprise groups and large-scale domestic groups in the Union (OJ L 328, 22.12.2022, p. 1, ELI: http://data.europa.eu/eli/dir/2022/2523/oj).

(4) Commission Implementing Regulation (EU) 2015/2378 of 15 December 2015 laying down detailed rules for implementing certain provisions of Council Directive 2011/16/EU on administrative cooperation in the field of taxation and repealing Implementing Regulation (EU) No 1156/2012 (OJ L 332, 18.12.2015, p. 19, ELI: http://data.europa.eu/eli/reg_impl/2015/2378/oj).

## ANNEX

Annex XVII to Implementing Regulation (EU) 2015/2378 is added as follows:

**‘ANNEX XVII**

**Computerised format to be used for the mandatory automatic exchange of information pursuant to Article 8ae(5)**

&lt;?xml version="1.0" encoding="UTF-8"?>

&lt;!-- edited with XMLSpy v2013 rel. 2 sp1 (x64) (http://www.altova.com) by Accounting Division (OECD) -->

&lt;xsd:schema xmlns:globe="urn:oecd:ties:globe:v2" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:stf="urn:oecd:ties:globestf:v5" xmlns:iso="urn:oecd:ties:isoglobetypes:v1" targetNamespace="urn:oecd:ties:globe:v2" elementFormDefault="qualified" attributeFormDefault="unqualified" version="1.0">

&lt;xsd:import namespace="urn:oecd:ties:isoglobetypes:v1" schemaLocation="isoglobetypes_v1.1.xsd"/>

&lt;xsd:import namespace="urn:oecd:ties:globestf:v5" schemaLocation="oecdglobetypes_v5.0.xsd"/>

&lt;!--+++++++++++++++++++++++ Reusable Simple types ++++++++++++++++++++++++++++++++++++++ -->

&lt;!-- Message type definitions -->

&lt;xsd:simpleType name="MessageType_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Message type defines the type of reporting&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR"/>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!-- MessageTypeIndic – 101 to 103 -->

&lt;xsd:simpleType name="MessageTypeIndic_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">The MessageTypeIndic defines the type of message sent&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR101">

&lt;xsd:annotation>

&lt;xsd:documentation>The message contains new information&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR102">

&lt;xsd:annotation>

&lt;xsd:documentation>The message contains corrections for previously sent information&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR103">

&lt;xsd:annotation>

&lt;xsd:documentation>The message advises there is no data to report&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #2 Set of Enumerations – 201 to 205 – ID Type – Rules-->

&lt;xsd:simpleType name="IDTypeRules_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">ID Type – Rules&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR201">

&lt;xsd:annotation>

&lt;xsd:documentation>QIIR applicable to Low-Taxed Constituent Entities located in other jurisdictions only&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR202">

&lt;xsd:annotation>

&lt;xsd:documentation>QIIR applicable to both Low-Taxed Constituent Entities located in other jurisdictions and in the jurisdiction of the Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR203">

&lt;xsd:annotation>

&lt;xsd:documentation>QUTPR&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR204">

&lt;xsd:annotation>

&lt;xsd:documentation>QDMTT&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR205">

&lt;xsd:annotation>

&lt;xsd:documentation>Not applicable&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #3 Set of Enumerations – 301 to 317 – ID Type – GloBEStatus-->

&lt;xsd:simpleType name="IDTypeGloBEStatus_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">ID Type – GloBEStatus&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR301">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR302">

&lt;xsd:annotation>

&lt;xsd:documentation>Flow-Through Entity – Tax Transparent&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR303">

&lt;xsd:annotation>

&lt;xsd:documentation>Flow-Through Entity – Reverse Hybrid&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR304">

&lt;xsd:annotation>

&lt;xsd:documentation>Hybrid Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR305">

&lt;xsd:annotation>

&lt;xsd:documentation>Permanent Establishment&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR306">

&lt;xsd:annotation>

&lt;xsd:documentation>Main Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR307">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR308">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Subsidiary&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR309">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR310">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR311">

&lt;xsd:annotation>

&lt;xsd:documentation>Insurance Investment Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR312">

&lt;xsd:annotation>

&lt;xsd:documentation>Securitisation Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR313">

&lt;xsd:annotation>

&lt;xsd:documentation>JV&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR314">

&lt;xsd:annotation>

&lt;xsd:documentation>JV Subsidiary&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR315">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Material Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR316">

&lt;xsd:annotation>

&lt;xsd:documentation>Excluded Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR317">

&lt;xsd:annotation>

&lt;xsd:documentation>Parent Entity required to apply a QIIR under Article 10.3.5&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR318">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-group Member&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #4 Set of Enumerations – 401 to 405 – FilingInfo – FilingCE – Role-->

&lt;xsd:simpleType name="FilingCERole_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">FilingInfo – FilingCE – Role&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR401">

&lt;xsd:annotation>

&lt;xsd:documentation>Ultimate Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR402">

&lt;xsd:annotation>

&lt;xsd:documentation>Designated Filing Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR403">

&lt;xsd:annotation>

&lt;xsd:documentation>Designated Local Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR404">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR405">

&lt;xsd:annotation>

&lt;xsd:documentation>Other&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #5 Set of Enumerations – 501 to 504 – FilingInfo – AccountingInfo – CFsofUPE-->

&lt;xsd:simpleType name="FilingCECofUPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">FilingInfo – AccountingInfo – CFsofUPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR501">

&lt;xsd:annotation>

&lt;xsd:documentation>Subparagraph a&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR502">

&lt;xsd:annotation>

&lt;xsd:documentation>Subparagraph b&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR503">

&lt;xsd:annotation>

&lt;xsd:documentation>Subparagraph c&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR504">

&lt;xsd:annotation>

&lt;xsd:documentation>Subparagraph d&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #6 Set of Enumerations – 601 to 606 – Excluded UPE – Type-->

&lt;xsd:simpleType name="ExcludedUPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Excluded Entity – Type&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR601">

&lt;xsd:annotation>

&lt;xsd:documentation>Governmental Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR602">

&lt;xsd:annotation>

&lt;xsd:documentation>International Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR603">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-profit Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR604">

&lt;xsd:annotation>

&lt;xsd:documentation>Pension Fund&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR605">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Fund that is an UPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR606">

&lt;xsd:annotation>

&lt;xsd:documentation>Real Estate Investment Vehicle that is an UPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #7 Set of Enumerations – 701 to 721 – GlobeStatus-->

&lt;xsd:simpleType name="IDGlobeStatus_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Subgroup – TypeofSubGroup&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR701">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR702">

&lt;xsd:annotation>

&lt;xsd:documentation>Flow-Through Entity – Tax Transparent&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR703">

&lt;xsd:annotation>

&lt;xsd:documentation>Flow-Through Entity – Reverse Hybrid&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR704">

&lt;xsd:annotation>

&lt;xsd:documentation>Hybrid Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR705">

&lt;xsd:annotation>

&lt;xsd:documentation>Permanent Establishment&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR706">

&lt;xsd:annotation>

&lt;xsd:documentation>Main Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR707">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR708">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Subsidiary&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR709">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR710">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR711">

&lt;xsd:annotation>

&lt;xsd:documentation>Insurance Investment Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR712">

&lt;xsd:annotation>

&lt;xsd:documentation>Securitisation Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR713">

&lt;xsd:annotation>

&lt;xsd:documentation>JV&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR714">

&lt;xsd:annotation>

&lt;xsd:documentation>JV Subsidiary&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR715">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Material Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR716">

&lt;xsd:annotation>

&lt;xsd:documentation>POPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR717">

&lt;xsd:annotation>

&lt;xsd:documentation>Intermediate Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR718">

&lt;xsd:annotation>

&lt;xsd:documentation>Ultimate Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR719">

&lt;xsd:annotation>

&lt;xsd:documentation>Excluded Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR720">

&lt;xsd:annotation>

&lt;xsd:documentation>Parent Entity required to apply a QIIR under Art. 10.3.5&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR721">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Group member&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #8 Set of Enumerations – 801 to 806 – OwnershipType-->

&lt;xsd:simpleType name="OwnershipType_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Ownership Type&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR801">

&lt;xsd:annotation>

&lt;xsd:documentation>UPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR802">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR803">

&lt;xsd:annotation>

&lt;xsd:documentation>JVs&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR804">

&lt;xsd:annotation>

&lt;xsd:documentation>JV Subsidiaries&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR805">

&lt;xsd:annotation>

&lt;xsd:documentation>Excluded Entities (aggregate)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR806">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Group members (aggregate)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #9 Set of Enumerations – 901 to 903 – POPE IPE-->

&lt;xsd:simpleType name="POPEIPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">POPE IPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR901">

&lt;xsd:annotation>

&lt;xsd:documentation>POPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR902">

&lt;xsd:annotation>

&lt;xsd:documentation>Intermediate Parent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR903">

&lt;xsd:annotation>

&lt;xsd:documentation>Parent Entity required to apply a QIIR under Art. 10.3.5&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #10 Set of Enumerations – 1001 to 1008 – Excluded Entity – Type-->

&lt;xsd:simpleType name="ExcludedEntity_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Excluded Entity – Type&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1001">

&lt;xsd:annotation>

&lt;xsd:documentation>Governmental Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1002">

&lt;xsd:annotation>

&lt;xsd:documentation>International Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1003">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-profit Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1004">

&lt;xsd:annotation>

&lt;xsd:documentation>Pension Fund&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1005">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Fund that is an UPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1006">

&lt;xsd:annotation>

&lt;xsd:documentation>Real Estate Investment Vehicle that is an UPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1007">

&lt;xsd:annotation>

&lt;xsd:documentation>Entity owned by Excluded Entities under Article 1.5.2(a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1008">

&lt;xsd:annotation>

&lt;xsd:documentation>Entity owned by Excluded Entities under Article 1.5.2(b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #11 Set of Enumerations – 1101 to 1106 – Type of Subgroup-->

&lt;xsd:simpleType name="TypeofSubGroup_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Type of Subgroup&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1101">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1102">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Subgroup&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1103">

&lt;xsd:annotation>

&lt;xsd:documentation>Standalone MOCEs&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1104">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1105">

&lt;xsd:annotation>

&lt;xsd:documentation>JV Group&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1106">

&lt;xsd:annotation>

&lt;xsd:documentation>Stateless Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #12 Set of Enumerations – 1201 to 1209 – SafeHarbour-->

&lt;xsd:simpleType name="SafeHarbour_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Summary – SafeHarbour&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1201">

&lt;xsd:annotation>

&lt;xsd:documentation>De minimis Exclusion&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1202">

&lt;xsd:annotation>

&lt;xsd:documentation>QDMTT safe harbour&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1203">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional CbCR Safe Harbour – De minimis test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1204">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional CbCR Safe Harbour – ETR test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1205">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional CbCR Safe Harbour – Routine profit test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1206">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional UTPR Safe Harbour&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1207">

&lt;xsd:annotation>

&lt;xsd:documentation>Permanent Safe Harbour – De minimis test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1208">

&lt;xsd:annotation>

&lt;xsd:documentation>Permanent Safe Harbour – ETR test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1209">

&lt;xsd:annotation>

&lt;xsd:documentation>Permanent Safe Harbour – Routine profit test&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #13 Set of Enumerations – 1301 to 1314 – ETR Range -->

&lt;xsd:simpleType name="ETRRange_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Summary – ETR Range&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1301">

&lt;xsd:annotation>

&lt;xsd:documentation>below 2.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1302">

&lt;xsd:annotation>

&lt;xsd:documentation>2.5% or above but below 5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1303">

&lt;xsd:annotation>

&lt;xsd:documentation>5% or above but below 7.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1304">

&lt;xsd:annotation>

&lt;xsd:documentation>7.5% or above but below 10%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1305">

&lt;xsd:annotation>

&lt;xsd:documentation>10% or above but below 12.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1306">

&lt;xsd:annotation>

&lt;xsd:documentation>12.5% or above but below 15%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1307">

&lt;xsd:annotation>

&lt;xsd:documentation>15% or above but below 17.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1308">

&lt;xsd:annotation>

&lt;xsd:documentation>17.5% or above but below 20%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1309">

&lt;xsd:annotation>

&lt;xsd:documentation>20% or above but below 22.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1310">

&lt;xsd:annotation>

&lt;xsd:documentation>22.5% or above but below 25%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1311">

&lt;xsd:annotation>

&lt;xsd:documentation>25% or above but below 27.5%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1312">

&lt;xsd:annotation>

&lt;xsd:documentation>27.5% or above but below 30%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1313">

&lt;xsd:annotation>

&lt;xsd:documentation>30% or above&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1314">

&lt;xsd:annotation>

&lt;xsd:documentation>Section 3.2 not completed&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #14 Set of Enumerations – 1401 to 1409 – QDMTTTut-->

&lt;xsd:simpleType name="QDMTTuT_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">QDMTTTut&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1401">

&lt;xsd:annotation>

&lt;xsd:documentation>No Top-up Tax payable&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1402">

&lt;xsd:annotation>

&lt;xsd:documentation>below EUR 1 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1403">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 1 million to below EUR 5 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1404">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 5 million to below EUR 25 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1405">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 25 million to below EUR 50 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1406">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 50 million to below EUR 75 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1407">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 75 million to below EUR 100 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1408">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 100 million to below EUR 250 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1409">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 250 million or above&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #15 Set of Enumerations – 1501 to 1509 – GlobeTuT -->

&lt;xsd:simpleType name="GlobeTuT_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Globe TuT&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1501">

&lt;xsd:annotation>

&lt;xsd:documentation>No Top-up Tax payable&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1502">

&lt;xsd:annotation>

&lt;xsd:documentation>below EUR 1 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1503">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 1 million to below EUR 5 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1504">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 5 million to below EUR 25 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1505">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 25 million to below EUR 50 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1506">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 50 million to below EUR 75 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1507">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 75 million to below EUR 100 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1508">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 100 million to below EUR 250 million&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1509">

&lt;xsd:annotation>

&lt;xsd:documentation>EUR 250 million or above&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #16 Set of Enumerations – 1601 to 1609 – Type of Subgroup-->

&lt;xsd:simpleType name="ETRTypeofSubGroup_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Type of SubGroup&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1601">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1602">

&lt;xsd:annotation>

&lt;xsd:documentation>Minority-Owned Subgroup&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1603">

&lt;xsd:annotation>

&lt;xsd:documentation>Standalone MOCEs&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1604">

&lt;xsd:annotation>

&lt;xsd:documentation>Investment Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1605">

&lt;xsd:annotation>

&lt;xsd:documentation>JV Group&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1606">

&lt;xsd:annotation>

&lt;xsd:documentation>Stateless Constituent Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1607">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional CbCR Safe Harbour-Constituent Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1608">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional CbCR Safe Harbour- JV Group (specify which JV Group)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1609">

&lt;xsd:annotation>

&lt;xsd:documentation>Transitional UTPR Safe Harbour&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #17 Set of Enumerations – 1701 to 1704 – MainEntityPEandFTEBasis-->

&lt;xsd:simpleType name="MainEntityPEandFTEBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">MainEntityPEandFTEBasis&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1701">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1702">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.5.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1703">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.5.1(a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1704">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.5.1(b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #18 Set of Enumerations – 1801 to 1802 – CrossBorderAdjustments-->

&lt;xsd:simpleType name="CrossBorderAdjustments_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Cross Border Adjustments&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1801">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.2.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1802">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.2.7&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #19 Set of Enumerations – 1901 to 1910 – UPEAdjustmentsBasis-->

&lt;xsd:simpleType name="UPEAdjustmentsBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">UPE Adjustment Basis&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR1901">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.1.1 (a)(i)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1902">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.1.1 (a)(ii)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1903">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.1.1 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1904">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.1.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1905">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.1 (a)(i)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1906">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.1 (a)(ii)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1907">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.1 (a)(iii)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1908">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.1 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1909">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR1910">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.2.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #20 Set of Enumerations – 2001 to 2026 – 3.2.1.1 Computation of GloBE Income (Loss) – Adjustment Items -->

&lt;xsd:simpleType name="AdjustmentItem_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">3.2.1.1 Computation of GloBE Income (Loss)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2001">

&lt;xsd:annotation>

&lt;xsd:documentation>Net Taxes Expense – Article 3.2.1 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2002">

&lt;xsd:annotation>

&lt;xsd:documentation>Excluded Dividends – Article 3.2.1 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2003">

&lt;xsd:annotation>

&lt;xsd:documentation>Excluded Equity Gain or Loss – Article 3.2.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2004">

&lt;xsd:annotation>

&lt;xsd:documentation>Included Revaluation Method Gain or Loss – Article 3.2.1 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2005">

&lt;xsd:annotation>

&lt;xsd:documentation>Gain or loss from disposition of assets and liabilities excluded under Article 6.3 – Article 3.2.1 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2006">

&lt;xsd:annotation>

&lt;xsd:documentation>Asymmetric Foreign Currency Gains or Losses – Article 3.2.1 (f)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2007">

&lt;xsd:annotation>

&lt;xsd:documentation>Policy Disallowed Expenses – Article 3.2.1 (g)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2008">

&lt;xsd:annotation>

&lt;xsd:documentation>Prior Period Errors – Article 3.2.1 (h)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2009">

&lt;xsd:annotation>

&lt;xsd:documentation>Changes in Accounting Principles – Article 3.2.1 (h)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2010">

&lt;xsd:annotation>

&lt;xsd:documentation>Accrued Pension Expense – Article 3.2.1 (i)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2011">

&lt;xsd:annotation>

&lt;xsd:documentation>Debt releases – Article 3.2.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2012">

&lt;xsd:annotation>

&lt;xsd:documentation>Stock-based compensation – Article 3.2.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2013">

&lt;xsd:annotation>

&lt;xsd:documentation>Arm’s length adjustments – Article 3.2.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2014">

&lt;xsd:annotation>

&lt;xsd:documentation>Qualified Refundable Tax Credit or Marketable Transferable Tax Credit – Article 3.2.4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2015">

&lt;xsd:annotation>

&lt;xsd:documentation>Election for Gains and losses using realisation principle – Article 3.2.5&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2016">

&lt;xsd:annotation>

&lt;xsd:documentation>Election for Adjusted Asset Gain – Article 3.2.6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2017">

&lt;xsd:annotation>

&lt;xsd:documentation>Intragroup Financing Arrangement expense – Article 3.2.7&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2018">

&lt;xsd:annotation>

&lt;xsd:documentation>Election for intragroup transactions in same jurisdiction – Article 3.2.8&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2019">

&lt;xsd:annotation>

&lt;xsd:documentation>Insurance company taxes charged to policyholders – Article 3.2.9&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2020">

&lt;xsd:annotation>

&lt;xsd:documentation>Increase/decrease to equity attributed to Additional Tier One and Restricted Tier One Capital distributions paid/payable or received/receivable – Article 3.2.10&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2021">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entities joining and leaving an MNE Group – Article 3.2.11 and 6.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2022">

&lt;xsd:annotation>

&lt;xsd:documentation>Reduction of GloBE Income of the UPE that is a Flow-through Entity – Article 3.2.11 and 7.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2023">

&lt;xsd:annotation>

&lt;xsd:documentation>Reduction of GloBE Income of the UPE that is subject to a Deductible Dividend Regime – Article 3.2.11 and 7.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2024">

&lt;xsd:annotation>

&lt;xsd:documentation>Taxable Distribution Method election – Article 3.2.11 and 7.6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2025">

&lt;xsd:annotation>

&lt;xsd:documentation>International Shipping Income – Article 3.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2026">

&lt;xsd:annotation>

&lt;xsd:documentation>Transactions between Constituent Entities – Article 9.1.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #21 Set of Enumerations – 2101 to 2106 – International Shipping Category-->

&lt;xsd:simpleType name="IntShipCategory_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">International Shipping Category&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2101">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.a&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2102">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.b&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2103">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.c&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2104">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.d&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2105">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.e&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2106">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.2.f&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #22 Set of Enumerations – 2201 to 2205 – Qualified Ancillary Shipping Income -->

&lt;xsd:simpleType name="ANCShipCategory_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Qualified Ancillary Shipping Income&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2201">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.3.a&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2202">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.3.b&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2203">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.3.c&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2204">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.3.d&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2205">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.3.3.e&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #23 Set of Enumerations – 2301 to 2309 – Adjusted Basis-->

&lt;xsd:simpleType name="AdjustedBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Adjusted Basis&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2301">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2302">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2303">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2304">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2305">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2306">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.3 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2307">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.3 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2308">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2309">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.3.2(c) – Blended CFC regime&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #24 Set of Enumerations – 2401 to 2417 – 3.2.1.2 Computation of Adjusted Covered Taxes-->

&lt;xsd:simpleType name="CurrentAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">3.2.1.2 Computation of Adjusted Covered Taxes&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2401">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Tax accrued as an expense in the profit before taxation in the financial accounts – Article 4.1.2 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2402">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes for uncertain tax position recorded as a reduction to Covered Taxes in prior year – Article 4.1.2 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2403">

&lt;xsd:annotation>

&lt;xsd:documentation>Qualified Refundable Tax Credit or Marketable Transferable Tax Credits recorded as a reduction to current tax expense – Article 4.1.2 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2404">

&lt;xsd:annotation>

&lt;xsd:documentation>Qualified Flow-through Tax Benefits of Qualified Ownership Interests – Article 3.2.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2405">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense on income excluded from GloBE Income or Loss – Article 4.1.3 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2406">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Qualified Refundable Tax Credit, Non-Marketable Transferable Tax Credit or Other Tax Credits not recorded as a reduction to current tax expense – Article 4.1.3 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2407">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes refunded or credited (except for any Qualified Refundable Tax Credit, or Marketable Transferable Tax Credits) not treated as an adjustment to current tax expense – Article 4.1.3 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2408">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense related to uncertain tax position– Article 4.1.3 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2409">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense not expected to be paid within three years – Article 4.1.3 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2410">

&lt;xsd:annotation>

&lt;xsd:documentation>Post-filing adjustments – Article 4.6.1.&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2411">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes relating to Net Asset Gain or Net Asset Loss – Article 3.2.6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2412">

&lt;xsd:annotation>

&lt;xsd:documentation>Reduction of Covered Taxes of the UPE that is a Flow-through Entity – Article 7.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2413">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes for GloBE Income of the UPE that is reduced under a Deductible Dividend Regime – Article 7.2.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2414">

&lt;xsd:annotation>

&lt;xsd:documentation>Deemed Distribution Tax – Article 7.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2415">

&lt;xsd:annotation>

&lt;xsd:documentation>Taxable Distribution Method election – Article 7.6 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2416">

&lt;xsd:annotation>

&lt;xsd:documentation>Total Deferred Tax Adjustment Amount – Article 4.4.1(b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2417">

&lt;xsd:annotation>

&lt;xsd:documentation>Increase or decrease in Covered Taxes recorded in equity or Other Comprehensive Income relating to amounts included in GloBE Income or Loss that will be subject to tax under local tax rules – Article 4.1.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #25 Set of Enumerations – 2501 to 2516 – 3.2.2 Jurisdictional computations relating to deferred tax accounting-->

&lt;xsd:simpleType name="DeferredAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">3.2.2 Jurisdictional computations relating to deferred tax accounting&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2501">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense related to items excluded from GloBE Income or Loss – Article 4.4.1 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2502">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense related to Disallowed Accruals– Article 4.4.1 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2503">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense related to Unclaimed Accruals – Article 4.4.1 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2504">

&lt;xsd:annotation>

&lt;xsd:documentation>Valuation adjustment or accounting recognition adjustment related to a deferred tax asset – Article 4.4.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2505">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense arising from a re-measurement related to changes in the tax rate – Article 4.4.1 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2506">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense related to the generation and use of tax credits – Article 4.4.1 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2507">

&lt;xsd:annotation>

&lt;xsd:documentation>Substitute Loss Carry Forward DTA or deemed Substitute Loss Carry Forward DTA – Article 4.4.1 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2508">

&lt;xsd:annotation>

&lt;xsd:documentation>Disallowed Accruals or Unclaimed Accruals paid during the fiscal year – Article 4.4.2 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2509">

&lt;xsd:annotation>

&lt;xsd:documentation>Recapture Deferred Tax Liability paid during the fiscal year– Article 4.4.2 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2510">

&lt;xsd:annotation>

&lt;xsd:documentation>Recognition of a loss Deferred Tax Asset not included in the financials – Article 4.4.2 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2511">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense adjustment resulting from a reduction to a tax rate – Article 4.6.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2512">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense adjustment resulting from an increase to a tax rate – Article 4.6.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2513">

&lt;xsd:annotation>

&lt;xsd:documentation>Constituent Entities joining and leaving an MNE Group – Article 6.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2514">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense of the UPE that is a Flow-through Entity – Article 7.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2515">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax expense of the UPE that is subject to Deductible Dividend Regime – Article 7.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2516">

&lt;xsd:annotation>

&lt;xsd:documentation>Deferred tax adjustment resulting from transactions between Constituent Entities – Article 9.1.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #26 Set of Enumerations – 2601 to 2606 -->

&lt;xsd:simpleType name="NonArt415_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">3.2.2 Jurisdictional computations relating to deferred tax accounting&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2601">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 3.2.6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2602">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.4.4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2603">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.6.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2604">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 4.6.4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2605">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.3.5&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2606">

&lt;xsd:annotation>

&lt;xsd:documentation>Article 7.3.7&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #27 Set of Enumerations – 2701 to 2720 – 3.2.1.2 Computation of Adjusted Covered Taxes-->

&lt;xsd:simpleType name="FinalAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">3.2.1.2 Computation of Adjusted Covered Taxes&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2701">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Tax accrued as an expense in the profit before taxation in the financial accounts – Article 4.1.2 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2702">

&lt;xsd:annotation>

&lt;xsd:documentation>GloBE Loss Deferred Tax Asset established under Article 4.5.1 or used – Article 4.1.2 (b) combined with Article 4.5.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2703">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes for uncertain tax position recorded as a reduction to Covered Taxes in prior year – Article 4.1.2 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2704">

&lt;xsd:annotation>

&lt;xsd:documentation>Qualified Refundable Tax Credit or Marketable Transferable Tax Credits recorded as a reduction to current tax expense – Article 4.1.2 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2705">

&lt;xsd:annotation>

&lt;xsd:documentation>Qualified Flow-through Tax Benefits of Qualified Ownership Interests – Article 3.2.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2706">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense on income excluded from GloBE Income or Loss – Article 4.1.3 (a)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2707">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-Qualified Refundable Tax Credit, Non-Marketable Transferable Tax Credit or Other Tax Credits not recorded as a reduction to current tax expense – Article 4.1.3 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2708">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes refunded or credited (except for any Qualified Refundable Tax Credit, or Marketable Transferable Tax Credits) not treated as an adjustment to current tax expense – Article 4.1.3 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2709">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense related to uncertain tax position– Article 4.1.3 (d)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2710">

&lt;xsd:annotation>

&lt;xsd:documentation>Current tax expense not expected to be paid within three years – Article 4.1.3 (e)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2711">

&lt;xsd:annotation>

&lt;xsd:documentation>Post-filing adjustments – Article 4.6.1.&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2712">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes relating to Net Asset Gain or Net Asset Loss – Article 3.2.6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2713">

&lt;xsd:annotation>

&lt;xsd:documentation>Reduction of Covered Taxes of the UPE that is a Flow-through Entity – Article 7.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2714">

&lt;xsd:annotation>

&lt;xsd:documentation>Covered Taxes for GloBE Income of the UPE that is reduced under a Deductible Dividend Regime – Article 7.2.2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2715">

&lt;xsd:annotation>

&lt;xsd:documentation>Deemed Distribution Tax – Article 7.3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2716">

&lt;xsd:annotation>

&lt;xsd:documentation>Taxable Distribution Method election – Article 7.6 (b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2717">

&lt;xsd:annotation>

&lt;xsd:documentation>Total Deferred Tax Adjustment Amount – Article 4.4.1(b)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2718">

&lt;xsd:annotation>

&lt;xsd:documentation>Increase or decrease in Covered Taxes recorded in equity or Other Comprehensive Income relating to amounts included in GloBE Income or Loss that will be subject to tax under local tax rules – Article 4.1.1 (c)&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2719">

&lt;xsd:annotation>

&lt;xsd:documentation>Excess Negative Tax Expense Carry Forward generated – Article 4.1.5 and 5.2.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2720">

&lt;xsd:annotation>

&lt;xsd:documentation>Decrease in Covered Taxes (but not below zero) by the remaining balance of the Excess Negative Tax Expense Carry-forward – Article 4.1.5 and 5.2.1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #28 Set of Enumerations – 2801 to 2805 -->

&lt;xsd:simpleType name="ExTypeOfEntity_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Enumeration options for Entity Owners&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2801">

&lt;xsd:annotation>

&lt;xsd:documentation>Governmental Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2802">

&lt;xsd:annotation>

&lt;xsd:documentation>International Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2803">

&lt;xsd:annotation>

&lt;xsd:documentation>Non-profit Organisation&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2804">

&lt;xsd:annotation>

&lt;xsd:documentation>Pension Fund&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2805">

&lt;xsd:annotation>

&lt;xsd:documentation>Pension Fund that is not a Pension Services Entity&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #29 Set of Enumerations – 2901 to 2902 – Basis for Deminimis-SimplifiedNMCECalculation-->

&lt;xsd:simpleType name="DeminimisSimpleBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">POPE IPE&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR2901">

&lt;xsd:annotation>

&lt;xsd:documentation>De minimis election&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR2902">

&lt;xsd:annotation>

&lt;xsd:documentation>Simplified Calculation for Non-material Constituent Entities&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #30 Set of Enumerations – 3001 to 3004 TIN Type-->

&lt;xsd:simpleType name="TIN_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">TIN Type&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR3001">

&lt;xsd:annotation>

&lt;xsd:documentation>Tax Identification Number&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR3002">

&lt;xsd:annotation>

&lt;xsd:documentation>Functionally equivalent number&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR3003">

&lt;xsd:annotation>

&lt;xsd:documentation>Agreed GIR designated number&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR3004">

&lt;xsd:annotation>

&lt;xsd:documentation>Not required to be reported&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--GLOBE #31 Set of Enumerations – 3101 to 3102 -->

&lt;xsd:simpleType name="Currency_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">TIN Type&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:restriction base="xsd:string">

&lt;xsd:enumeration value="GIR3101">

&lt;xsd:annotation>

&lt;xsd:documentation>Local&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;xsd:enumeration value="GIR3102">

&lt;xsd:annotation>

&lt;xsd:documentation>CFS&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:enumeration>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;xsd:simpleType name="percentage">

&lt;xsd:restriction base="xsd:decimal">

&lt;xsd:minInclusive value="0"/>

&lt;xsd:maxInclusive value="1"/>

&lt;xsd:fractionDigits value="4"/>

&lt;/xsd:restriction>

&lt;/xsd:simpleType>

&lt;!-- -->

&lt;!--++++++++++++++++++ Reusable Complex types +++++++++++++++++++++++++++++++++++++ -->

&lt;!-- Message specification: Data identifying and describing the message as a whole -->

&lt;!-- -->

&lt;!--Message specification: Data identifying and describing the message as a whole-->

&lt;xsd:complexType name="MessageSpec_Type">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">Information in the message header identifies the Tax Administration that is sending the message. It specifies when the message was created, what period (normally a year) the report is for, and the nature of the report (original, corrected, supplemental, etc.).

&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;xsd:sequence>

&lt;xsd:element name="SendingEntityIN" type="stf:StringMin1Max200_Type" minOccurs="0"/>

&lt;xsd:element name="TransmittingCountry" type="iso:CountryCode_Type"/>

&lt;!-- modified for GLOBE -->

&lt;xsd:element name="ReceivingCountry" type="iso:CountryCode_Type"/>

&lt;xsd:element name="MessageType" type="globe:MessageType_EnumType"/>

&lt;xsd:element name="Warning" type="stf:StringMin1Max4000_Type" minOccurs="0"/>

&lt;xsd:element name="Contact" type="stf:StringMin1Max4000_Type" minOccurs="0"/>

&lt;xsd:element name="MessageRefId" type="stf:StringMin1Max170_Type"/>

&lt;xsd:element name="MessageTypeIndic" type="globe:MessageTypeIndic_EnumType"/>

&lt;xsd:element name="ReportingPeriod" type="xsd:date"/>

&lt;xsd:element name="Timestamp" type="xsd:dateTime"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;!-- -->

&lt;!-- TIN -->

&lt;xsd:complexType name="TIN_Type">

&lt;xsd:simpleContent>

&lt;xsd:extension base="stf:StringMin1Max200_Type">

&lt;xsd:attribute name="issuedBy" type="iso:CountryCode_Type" use="optional"/>

&lt;xsd:attribute name="unknown" type="xsd:boolean" use="optional"/>

&lt;xsd:attribute name="TypeOfTIN" type="globe:TIN_EnumType"/>

&lt;/xsd:extension>

&lt;/xsd:simpleContent>

&lt;/xsd:complexType>

&lt;!-- -->

&lt;!-- GlobeOECD File Message structure -->

&lt;xsd:complexType name="GLOBEBody_Type">

&lt;xsd:sequence>

&lt;xsd:element name="FilingInfo">

&lt;xsd:complexType>

&lt;xsd:complexContent>

&lt;xsd:extension base="globe:FilingInfo">

&lt;xsd:sequence>

&lt;xsd:element name="DocSpec" type="stf:DocSpec_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:extension>

&lt;/xsd:complexContent>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="GeneralSection" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:complexContent>

&lt;xsd:extension base="globe:GeneralSectionType">

&lt;xsd:sequence>

&lt;xsd:element name="DocSpec" type="stf:DocSpec_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:extension>

&lt;/xsd:complexContent>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Summary" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:complexContent>

&lt;xsd:extension base="globe:SummaryType">

&lt;xsd:sequence>

&lt;xsd:element name="DocSpec" type="stf:DocSpec_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:extension>

&lt;/xsd:complexContent>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="JurisdictionSection" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:complexContent>

&lt;xsd:extension base="globe:JurisdictionSectionType">

&lt;xsd:sequence>

&lt;xsd:element name="DocSpec" type="stf:DocSpec_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:extension>

&lt;/xsd:complexContent>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UTPRAttribution" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:complexContent>

&lt;xsd:extension base="globe:UTPRAttributionType">

&lt;xsd:sequence>

&lt;xsd:element name="DocSpec" type="stf:DocSpec_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:extension>

&lt;/xsd:complexContent>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;!--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Schema element ++++++++++++++++++++++++++++++++++++++++++++ -->

&lt;!-- -->

&lt;!-- GLOBE Message structure -->

&lt;xsd:element name="GLOBE_OECD">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="MessageSpec" type="globe:MessageSpec_Type"/>

&lt;xsd:element name="GLOBEBody" type="globe:GLOBEBody_Type" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;xsd:attribute name="version" type="stf:StringMin1Max10_Type">

&lt;xsd:annotation>

&lt;xsd:documentation xml:lang="en">GLOBE Version&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:attribute>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:complexType name="CorporateStructureType">

&lt;xsd:sequence>

&lt;xsd:element name="UPE" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="ExcludedUPE">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ExcludedUPEStatus" type="globe:ExcludedUPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #6&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Art10.3.5" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:sequence>

&lt;xsd:element name="ID" type="globe:ExcludedUPE_ID_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="OtherUPE">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ID" type="globe:ID_Type"/>

&lt;xsd:element name="Art10.3.5" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="CE" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ID" type="globe:ID_Type"/>

&lt;xsd:element name="OwnershipChange" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ChangeDate" type="xsd:date"/>

&lt;xsd:element name="PreGlobeStatus" type="globe:IDGlobeStatus_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #7&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="PreOwnership" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="OwnershipType" type="globe:OwnershipType_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #8&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="PreOwnershipPercentage" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Ownership" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="OwnershipType" type="globe:OwnershipType_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Emumeration #8&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="OwnershipPercentage" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="QIIR" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="POPE-IPE" type="globe:POPEIPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #9&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Exception" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ExceptionRule">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="Art2.1.3" type="xsd:boolean"/>

&lt;xsd:element name="Art2.1.5" type="xsd:boolean"/>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="QUTPR" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Art9.3" type="xsd:boolean"/>

&lt;xsd:element name="AggOwnership" type="globe:percentage" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="UPEOwnership" type="xsd:boolean" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ExcludedEntity" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Name" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="Type" type="globe:ExcludedEntity_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #10&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Change" type="xsd:boolean"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UnreportChangeCorpStr" type="xsd:boolean" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="ETRType">

&lt;xsd:sequence>

&lt;xsd:element name="SubGroup" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="TypeofSubGroup" type="globe:ETRTypeofSubGroup_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #16&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ETRStatus">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ETRException" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Deminimis-SimplifiedNMCECalc" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Basis" type="globe:DeminimisSimpleBasis_EnumType"/>

&lt;xsd:element name="FinancialData" maxOccurs="3">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Year" type="xsd:date" minOccurs="1"/>

&lt;xsd:element name="Revenue" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="GlobeRevenue" type="xsd:integer"/>

&lt;xsd:element name="NetGlobeIncome" type="xsd:integer"/>

&lt;xsd:element name="FANIL" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Average">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Revenue" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="GlobeRevenue" type="xsd:integer"/>

&lt;xsd:element name="NetGlobeIncome" type="xsd:integer"/>

&lt;xsd:element name="FANIL" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TransitionalCbCRSafeHarbour" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Revenue" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Profit" type="xsd:integer"/>

&lt;xsd:element name="IncomeTax" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UTPRSafeHarbour" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="CITRate" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ETRComputation" type="globe:ETRComputationType" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Election" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Art3.2.6" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art4.1.5" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art4.6.1" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art5.3.1" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art3.2.2" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence>

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art3.2.5" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art3.2.8" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="NoDefTaxAllocation" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence>

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art4.5" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art3.2.1.c" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence>

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;xsd:element name="QualOwnerIntentBalance" type="xsd:integer"/>

&lt;xsd:element name="Additions" type="xsd:integer"/>

&lt;xsd:element name="Reductions" type="xsd:integer"/>

&lt;xsd:element name="OutstandingBalance" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="SimplifiedReporting" type="xsd:boolean" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="ID_Type">

&lt;xsd:sequence>

&lt;xsd:element name="Name" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="TIN" type="globe:TIN_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="Rules" type="globe:IDTypeRules_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="GlobeStatus" type="globe:IDTypeGloBEStatus_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="ExcludedUPE_ID_Type">

&lt;xsd:sequence>

&lt;xsd:element name="Name" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" minOccurs="0" maxOccurs="unbounded"/>

&lt;xsd:element name="TIN" type="globe:TIN_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="Rules" type="globe:IDTypeRules_EnumType" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="GlobeStatus" type="globe:IDTypeGloBEStatus_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="FilingInfo">

&lt;xsd:sequence>

&lt;xsd:element name="FilingCE">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="Name" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="Role" type="globe:FilingCERole_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #4&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AccountingInfo">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="CFSofUPE" type="globe:FilingCECofUPE_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #11&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="FAS" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="Currency" type="iso:currCode_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Period">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Start" type="xsd:date"/>

&lt;xsd:element name="End" type="xsd:date"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="NameMNE" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="AdditionalInfo" type="stf:StringMin1Max4000_Type" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="ETRComputationType">

&lt;xsd:sequence>

&lt;xsd:element name="CEComputation" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="AdjustedFANIL">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="FANIL" type="xsd:integer"/>

&lt;xsd:element name="Adjustment" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="MainEntityPEandFTE" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Basis" type="globe:MainEntityPEandFTEBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #17&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="OtherTIN" type="globe:TIN_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:element name="Additions" type="xsd:integer"/>

&lt;xsd:element name="Reductions" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="CrossBorderAdjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Basis" type="globe:CrossBorderAdjustments_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #18&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="OtherTIN" type="globe:TIN_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:element name="Additions" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Reductions" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UPEAdjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Basis" type="globe:UPEAdjustmentsBasis_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #19&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Reductions" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;xsd:element name="Exception" type="xsd:boolean"/>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="IdentificationOfOwners" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="OwnershipPercentage" type="globe:percentage"/>

&lt;xsd:choice>

&lt;xsd:element name="IndOwners">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NumOfOwners" type="xsd:integer"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:element name="TaxRate" type="globe:percentage" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="EntityOwner">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="TaxRate" type="globe:percentage" minOccurs="0"/>

&lt;xsd:element name="ExTypeOfEntity" type="globe:ExTypeOfEntity_EnumType" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:choice>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="NetGlobeIncome">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Adjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer" maxOccurs="2"/>

&lt;xsd:element name="AdjustmentItem" type="globe:AdjustmentItem_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #20&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="IntShippingIncome" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="InternationalShipIncome">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="Category" type="globe:IntShipCategory_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #21&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Revenue" type="xsd:integer"/>

&lt;xsd:element name="Costs" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="QualifiedAncShipIncome">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="Category" type="globe:ANCShipCategory_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #22&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Revenue" type="xsd:integer"/>

&lt;xsd:element name="Costs" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="SubstanceExclusion">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="PayrollCosts" type="xsd:integer"/>

&lt;xsd:element name="TangibleAssets" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="CoveredTaxes" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AdjustedIncomeTax">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="IncomeTax" type="xsd:integer"/>

&lt;xsd:element name="CrossAllocation" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Basis" type="globe:AdjustedBasis_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #23&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="OtherTIN" type="globe:TIN_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="Additions" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Reductions" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AdjustedCoveredTax">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Adjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer" maxOccurs="2"/>

&lt;xsd:element name="AdjustmentItem" type="globe:CurrentAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #24&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="DeferTaxAdjustAmt">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="DeferTaxExpense" type="xsd:integer"/>

&lt;xsd:element name="Adjustment" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer" maxOccurs="2"/>

&lt;xsd:element name="AdjustmentItem" type="globe:DeferredAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #25&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Recast" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Higher" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Lower" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="Elections" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Art1.5.3" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="SimplCalculations" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art3.2.1" type="xsd:boolean" minOccurs="0"/>

&lt;xsd:element name="Art3.2.1b" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art3.2.1c" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art6.3.4" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="FYTriggerEvent" type="xsd:date"/>

&lt;xsd:element name="Inclusion">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="Art6.3.4.c.i" type="xsd:boolean"/>

&lt;xsd:element name="Art6.3.4.c.ii" type="xsd:boolean"/>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AggregatedReporting" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TaxConsolGroupTIN" type="globe:TIN_Type"/>

&lt;xsd:element name="EntityTIN" type="globe:TIN_Type" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art4.4.7" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art4.5.6" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art7.5" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence minOccurs="0">

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;xsd:element name="CEOwnerTIN" type="globe:TIN_Type" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art7.6" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence>

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;xsd:element name="ActualDeemedDist" type="xsd:integer"/>

&lt;xsd:element name="LocalCreditableTaxGross" type="xsd:integer"/>

&lt;xsd:element name="ShareOfUndistNetGlobeInc" type="globe:percentage"/>

&lt;xsd:element name="InvestmentEntityTIN" type="globe:TIN_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="OtherFAS" type="stf:StringMin1Max200_Type" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="OverallComputation" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="FANIL" type="xsd:integer"/>

&lt;xsd:element name="AdjustedFANIL" type="xsd:integer"/>

&lt;xsd:element name="NetGlobeIncome">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Adjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;xsd:element name="AdjustmentItem" type="globe:AdjustmentItem_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #1&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="IntShippingIncome" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="TotalIntShipIncome" type="xsd:integer"/>

&lt;xsd:element name="FiftyPercentCap" type="xsd:integer"/>

&lt;xsd:element name="TotalQualifiedAncIncome" type="xsd:integer"/>

&lt;xsd:element name="ExcessOfCap" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="IncomeTaxExpense" type="xsd:integer"/>

&lt;xsd:element name="ETRRate" type="globe:percentage"/>

&lt;xsd:element name="TopUpTaxPercentage" type="globe:percentage"/>

&lt;xsd:element name="AdjustedCoveredTax" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="AggregrateCurrentTax" type="xsd:integer"/>

&lt;xsd:element name="Adjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;xsd:element name="AdjustmentItem" type="globe:FinalAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #2&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="PostFilingAdjust" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="DeferTaxAsset">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="AmountAttributed" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Year" type="xsd:date"/>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="CoveredTaxRefund">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="AmountAttributed" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Year" type="xsd:date"/>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="DeemedDistTax" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Election" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Recapture" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Year" type="xsd:date"/>

&lt;xsd:element name="StartAmount" type="xsd:integer"/>

&lt;xsd:element name="DDTYear-0" type="xsd:integer"/>

&lt;xsd:element name="DDTYear-1" type="xsd:integer"/>

&lt;xsd:element name="DDTYear-2" type="xsd:integer"/>

&lt;xsd:element name="DDTYear-3" type="xsd:integer"/>

&lt;xsd:element name="TotalDDT" type="xsd:integer"/>

&lt;xsd:element name="EndAmount" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Reduction" type="xsd:integer"/>

&lt;xsd:element name="IncrementalTopUpTax" type="xsd:integer"/>

&lt;xsd:element name="Ratio" type="globe:percentage"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="DeferTaxAdjustAmt" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="DefTaxAmt" type="xsd:integer"/>

&lt;xsd:element name="DiffCarryValue" type="xsd:integer"/>

&lt;xsd:element name="GLoBEValue" type="xsd:integer"/>

&lt;xsd:element name="BefRecastAdjust" type="xsd:integer"/>

&lt;xsd:element name="TotalAdjust" type="xsd:integer"/>

&lt;xsd:element name="PreRecast" type="xsd:integer"/>

&lt;xsd:element name="Recast" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Higher" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Lower" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Adjustments" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:sequence>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;xsd:element name="AdjustmentItem" type="globe:DeferredAdjustedTax_EnumType">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #3&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;xsd:element name="RecaptureDeferred">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="DTLRFYMinus5" type="xsd:integer"/>

&lt;xsd:element name="RecapDTLRFYMinus5" type="xsd:integer"/>

&lt;xsd:element name="DTLRFY" type="xsd:integer"/>

&lt;xsd:element name="AggregateDTL">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ReportingFiscalYear">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="AmountPreTransition" type="xsd:integer"/>

&lt;xsd:element name="AmountOutBalance" type="xsd:integer"/>

&lt;xsd:element name="AmountUnjustified" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="PriorFiscalYear">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="AmountPreTransition" type="xsd:integer"/>

&lt;xsd:element name="AmountOutBalance" type="xsd:integer"/>

&lt;xsd:element name="AmountUnjustified" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Transition" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Year" type="xsd:date"/>

&lt;xsd:element name="DeferredTaxLiabilityStart" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="DeferredTaxLiabilityRecast" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="DeferredTaxAssets" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="DeferredTaxAssetStart" type="xsd:integer"/>

&lt;xsd:element name="DeferredTaxAssetRecast" type="xsd:integer"/>

&lt;xsd:element name="DeferredTaxAssetExcluded" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Disposal" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="NetDTADTL" type="xsd:integer"/>

&lt;xsd:element name="CarryingValue" type="xsd:integer"/>

&lt;xsd:element name="TaxPaid" type="xsd:integer"/>

&lt;xsd:element name="DTADTL" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AltJurisdiction" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TransBlendCFC" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="CFCJur" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Jurisdiction" type="iso:CountryCode_Type"/>

&lt;xsd:element name="Allocation">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="SubGroupTIN" type="globe:TIN_Type"/>

&lt;xsd:element name="AggAllocTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="SubstanceExclusion" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:sequence>

&lt;xsd:element name="PayrollCost" type="xsd:integer"/>

&lt;xsd:element name="PayrollMarkUp" type="globe:percentage"/>

&lt;xsd:element name="TangibleAssetValue" type="xsd:integer"/>

&lt;xsd:element name="TangibleAssetMarkup" type="globe:percentage"/>

&lt;xsd:element name="PEAllocation" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="JurOfOwners">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="UPE" type="xsd:boolean"/>

&lt;xsd:element name="NotApplicable" type="xsd:boolean"/>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="PayrollCost">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Allocation" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TangibleAssetValue">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Allocation" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="FTEAllocation" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="JurOfOwners">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="UPE" type="xsd:boolean"/>

&lt;xsd:element name="NotApplicable" type="xsd:boolean"/>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="PayrollCost">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Allocation" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TangibleAssetValue">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Total" type="xsd:integer"/>

&lt;xsd:element name="Allocation" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ExcessProfits" type="xsd:integer"/>

&lt;xsd:element name="AdditionalTopUpTax" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NONArt4.1.5" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Articles" type="globe:NonArt415_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #17&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Year" type="xsd:date">

&lt;xsd:annotation>

&lt;xsd:documentation>&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="Previous">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NetGlobeIncome" type="xsd:integer"/>

&lt;xsd:element name="AdjustedCoveredTax" type="xsd:integer"/>

&lt;xsd:element name="ETRRate" type="globe:percentage"/>

&lt;xsd:element name="ExcessProfits" type="xsd:integer"/>

&lt;xsd:element name="TopUpTaxPercentage" type="globe:percentage"/>

&lt;xsd:element name="TopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Recalculated">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NetGlobeIncome" type="xsd:integer"/>

&lt;xsd:element name="AdjustedCoveredTax" type="xsd:integer"/>

&lt;xsd:element name="ETRRate" type="globe:percentage"/>

&lt;xsd:element name="ExcessProfits" type="xsd:integer"/>

&lt;xsd:element name="TopUpTaxPercentage" type="globe:percentage"/>

&lt;xsd:element name="TopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AdditionalTopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Art4.1.5" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="AdjustedCoveredTax" type="xsd:integer"/>

&lt;xsd:element name="GlobeLoss" type="xsd:integer"/>

&lt;xsd:element name="ExpectedAdjustedCoveredTax" type="xsd:integer"/>

&lt;xsd:element name="AdditionalTopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="QDMTT" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="FAS" type="stf:StringMin1Max200_Type"/>

&lt;xsd:element name="Amount" type="xsd:integer"/>

&lt;xsd:element name="MinRate" type="globe:percentage" minOccurs="0"/>

&lt;xsd:element name="BasisforBlending" type="stf:StringMin1Max4000_Type" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>Free text&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="SBIEAvailable" type="xsd:boolean"/>

&lt;xsd:element name="DeMinAvailable" type="xsd:boolean"/>

&lt;xsd:element name="Currency" type="iso:currCode_Type"/>

&lt;xsd:element name="CurrencyElection" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="Status" type="xsd:boolean"/>

&lt;xsd:sequence>

&lt;xsd:element name="ElectionYear" type="xsd:date"/>

&lt;xsd:element name="RevocationYear" type="xsd:date" minOccurs="0"/>

&lt;xsd:element name="Currency" type="globe:Currency_EnumType"/>

&lt;/xsd:sequence>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="TopUpTax" type="xsd:integer"/>

&lt;xsd:element name="ExcessNegTaxExpense">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="PriorYearBalance" type="xsd:integer"/>

&lt;xsd:element name="GeneratedInRFY" type="xsd:integer"/>

&lt;xsd:element name="UtilizedInRFY" type="xsd:integer"/>

&lt;xsd:element name="Remaining" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Non-MaterialCE" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="RFY">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TotalRevenue" type="xsd:integer"/>

&lt;xsd:element name="AggregateSimplified" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="RFY-1" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TotalRevenue" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="RFY-2" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TotalRevenue" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="Average">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TotalRevenue" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ID" type="globe:ID_Type"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="LowTaxJurisdictionType">

&lt;xsd:sequence>

&lt;xsd:element name="TopUpTaxAmount" type="xsd:integer"/>

&lt;xsd:element name="LTCE" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="IIR" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NetGlobeIncome" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="TopUpTax" type="xsd:integer"/>

&lt;xsd:element name="ParentEntity" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="OtherOwnershipAllocation" type="xsd:integer"/>

&lt;xsd:element name="InclusionRatio" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="TopUpTaxShare" type="xsd:integer"/>

&lt;xsd:element name="IIROffSet" type="xsd:integer"/>

&lt;xsd:element name="TopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UTPR" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:choice>

&lt;xsd:element name="UTPRSafeHarbour">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="CITRate" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="UTPRCalculation">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TotalUTPRTopUpTax" type="xsd:integer"/>

&lt;xsd:element name="Article 2.5.1TopUpTax" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:choice>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="InitialIntActivityType">

&lt;xsd:sequence>

&lt;xsd:element name="StartDate" type="xsd:date"/>

&lt;xsd:element name="ReferenceJurisdiction">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="TangibleAssetValue" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="OtherJurisdiction" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type" maxOccurs="5"/>

&lt;xsd:element name="TangibleAssetValue" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="RFYNumberOfJurisdictions" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="RFYSumTangibleAssetValue" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="GLOBETax">

&lt;xsd:sequence>

&lt;xsd:element name="ETR" type="globe:ETRType" minOccurs="0" maxOccurs="unbounded"/>

&lt;xsd:element name="InitialIntActivity" type="globe:InitialIntActivityType" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="GeneralSectionType">

&lt;xsd:sequence>

&lt;xsd:element name="RecJurCode" type="iso:CountryCode_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="CorporateStructure" type="globe:CorporateStructureType"/>

&lt;xsd:element name="AdditionalDataPoint" type="globe:AdditionalDataPointType" minOccurs="0" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="JurisdictionSectionType">

&lt;xsd:sequence>

&lt;xsd:element name="RecJurCode" type="iso:CountryCode_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="Jurisdiction" type="iso:CountryCode_Type"/>

&lt;xsd:element name="JurWithTaxingRights" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="JurisdictionName" type="iso:CountryCode_Type"/>

&lt;xsd:element name="Subgroup" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="TypeofSubGroup" type="globe:TypeofSubGroup_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #11&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="ReportDifference" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ETRDifference" type="globe:percentage" minOccurs="0"/>

&lt;xsd:element name="AdjCoveredTaxDifference" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="AggCurrentTaxExpense" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="QRTCExpense" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="OtherTaxCredits" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="DeferTaxExpense" type="xsd:integer" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="NetGLoBEDifference" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="SBIEDifference" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="AddCurrentTuTDifference" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="TuTDifference" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="ElectionsDifference" type="stf:StringMin1Max4000_Type" minOccurs="0"/>

&lt;xsd:element name="QRTCIncome" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="ExcessNegTaxCarryForw" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="TransitionDifference" type="xsd:boolean" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="LocalCurrency" type="iso:currCode_Type" minOccurs="0"/>

&lt;xsd:element name="GLoBETax" type="globe:GLOBETax"/>

&lt;xsd:element name="LowTaxJurisdiction" type="globe:LowTaxJurisdictionType" minOccurs="0"/>

&lt;xsd:element name="AdditionalDataPoint" type="globe:AdditionalDataPointType" minOccurs="0" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="UTPRAttributionType">

&lt;xsd:sequence>

&lt;xsd:element name="RecJurCode" type="iso:CountryCode_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="Attribution" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="ResCountryCode" type="iso:CountryCode_Type"/>

&lt;xsd:element name="UTPRTopUpTaxCarryForward" type="xsd:integer"/>

&lt;xsd:element name="Employees" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="TangibleAssetValue" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="UTPRPercentage" type="globe:percentage">

&lt;xsd:annotation>

&lt;xsd:documentation>%&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="UTPRTopUpTaxAttributed" type="xsd:integer"/>

&lt;xsd:element name="AddCashTaxExpense" type="xsd:integer"/>

&lt;xsd:element name="UTPRTopUpTaxCarriedForward" type="xsd:integer"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="AdditionalDataPoint" type="globe:AdditionalDataPointType" minOccurs="0" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="SummaryType">

&lt;xsd:sequence>

&lt;xsd:element name="RecJurCode" type="iso:CountryCode_Type" maxOccurs="unbounded"/>

&lt;xsd:element name="Jurisdiction">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="JurisdictionName" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:element name="Subgroup" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="TIN" type="globe:TIN_Type"/>

&lt;xsd:element name="TypeofSubGroup" type="globe:TypeofSubGroup_EnumType" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #11&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="JurWithTaxingRights" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="JurisdictionName" type="iso:CountryCode_Type" minOccurs="0"/>

&lt;xsd:element name="DiffDomesticTut" type="globe:GlobeTuT_EnumType" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="SafeHarbour" type="globe:SafeHarbour_EnumType" minOccurs="0" maxOccurs="unbounded">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #12&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="ETRRange" type="globe:ETRRange_EnumType" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #13&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="SBIE" minOccurs="0">

&lt;xsd:complexType>

&lt;xsd:sequence>

&lt;xsd:element name="NotApplicable" type="xsd:boolean"/>

&lt;xsd:element name="NoTut" type="xsd:boolean"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:element>

&lt;xsd:element name="QDMTTut" type="globe:QDMTTuT_EnumType" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #14&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="GLoBETut" type="globe:GlobeTuT_EnumType" minOccurs="0">

&lt;xsd:annotation>

&lt;xsd:documentation>Enumeration #15&lt;/xsd:documentation>

&lt;/xsd:annotation>

&lt;/xsd:element>

&lt;xsd:element name="AdditionalDataPoint" type="globe:AdditionalDataPointType" minOccurs="0" maxOccurs="unbounded"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;xsd:complexType name="AdditionalDataPointType">

&lt;xsd:sequence>

&lt;xsd:element name="Description" type="stf:StringMin1Max170_Type" minOccurs="0"/>

&lt;xsd:element name="Amount" type="xsd:integer" minOccurs="0"/>

&lt;xsd:element name="Percentage" type="globe:percentage" minOccurs="0"/>

&lt;xsd:element name="Text" type="stf:StringMin1Max4000_Type" minOccurs="0"/>

&lt;xsd:element name="Boolean" type="xsd:boolean" minOccurs="0"/>

&lt;/xsd:sequence>

&lt;/xsd:complexType>

&lt;/xsd:schema>

’

ELI: http://data.europa.eu/eli/reg_impl/2025/1325/oj

ISSN 1977-0677 (electronic edition)
