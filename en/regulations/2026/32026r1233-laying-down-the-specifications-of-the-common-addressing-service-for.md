---
title: "Commission Implementing Regulation (EU) 2026/1233 of 11 June 2026 laying down the specifications of the common addressing service for the European Maritime Single Window environment"
identifier: "32026R1233"
eli: "http://data.europa.eu/eli/reg_impl/2026/1233/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2026-06-11
entry_into_force: 2026-09-22
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1233"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2026/1233 of 11 June 2026 laying down the specifications of the common addressing service for the European Maritime Single Window environment

**COMMISSION IMPLEMENTING REGULATION (EU) 2026/1233**

**of 11 June 2026**

**laying down the specifications of the common addressing service for the European Maritime Single Window environment**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2019/1239 of the European Parliament and of the Council of 20 June 2019 establishing a European Maritime Single Window environment and repealing Directive 2010/65/EU (1), and in particular Article 13 thereof,

After consulting the Digital Transport and Trade Facilitation Committee,

Whereas:

(1) In the context of the European Maritime Single Window environment established by Regulation (EU) 2019/1239, declarants and data service providers (senders) can fulfil their reporting obligations via a system-to-system connection to the reporting interface module (RIM) of the maritime national single windows (MNSW).

(2) The RIM, developed in accordance with the specifications laid down in the Commission Implementing Regulation (EU) 2023/2790 (2) ensures technical interoperability and the use of a harmonised set of messages for data exchange with the MNSWs. Before senders exchange data with MNSW through the RIM, the connection details have to be manually configured. This is also required in the case connection details change. The common addressing service should overcome this issue by way of facilitating the automatic configuration of the direct system-to-system connection.

(3) The common addressing service should use dynamic discovery that ensures flexibility and scalability to the network of MNSWs. Senders should be able to use the common addressing service to initiate direct system-to-system data connection between their AS4 access point and a RIM by way of automatically retrieving the latest connection details of a RIM.

(4) The common addressing service should minimise the need for human interventions and should, therefore, proportionally reduce costs and risks of errors, making the network flexible when there is a change in connection details of its participants, such as endpoint information and public certificate.

(5) To ensure interoperability and reduction of implementing costs, the common addressing service should be based on the same technologies and standards used for the RIM.

(6) The central locator node should contain participants’ identifiers and the publisher nodes location, and it should be hosted centrally to ensure that such data is kept up to date in the public Domain Name System (DNS).

(7) To enhance the resilience of the service and mitigate the risk of a single point of failure, each Member State should host its own publisher node that should contain all necessary connection details of the corresponding RIM.

(8) To ensure scalability and flexibility also to the authorities of the Member States managing the MNSWs, Member States should also be able to store in their publisher nodes the connection details of the AS4 access points of senders, in alternative of manually pre-configuring those in their RIM.

(9) To make its publisher node discoverable to common addressing service users, to ensure the correctness and availability of the publisher node address in the public DNS and to prevent common addressing service users in discovering de-commissioned or non-existent publisher nodes, Member States should be able to register, update and delete its publisher node details through the central locator node.

(10) The Maritime National Single Windows constitutes a cross-border digital public service in the meaning of the Regulation (EU) 2024/903 of the European Parliament and of the Council (3) (‘Interoperable Europe Act’). This Regulation introduces new binding requirements affecting the aforementioned digital public service(s), and, as such, is subject to the interoperability assessment obligation under Article 3 of the Interoperable Europe Act. Accordingly, an interoperability assessment has been carried out, and the resulting report is to be published on the Interoperable Europe Portal,

HAS ADOPTED THIS REGULATION:

## Article 1

For the purposes of this Regulation, the definitions in Article 1 of Commission Implementing Regulation (EU) 2023/2790 shall apply.

The following definitions shall also apply:

(1) ‘dynamic discovery’ means a mechanism that enables both AS4 access points of senders and RIMs to automatically obtain connection details about each other to initiate direct connection;

(2) ‘eDelivery’ means a set of technical specifications and standards for electronic message exchange developed by the Commission;

(3) ‘central locator node’ means a Service Metadata Locator (SML) compliant with the eDelivery profile specifications (4) that facilitates dynamic discovery via the public Domain Name System (DNS);

(4) ‘publisher node’ means a Service Metadata Publisher (SMP) compliant with the eDelivery profile specifications (5) that holds the connection details of the reporting interface modules (RIMs) and the AS4 access points of the senders;

(5) ‘common addressing service’ means the service referred to in Article 2(10) of Regulation (EU) 2019/1239.

## Article 2

The functional and technical specifications, quality control mechanisms and procedures for deploying, maintaining and employing the common addressing service are set out in the Annex to this Regulation.

## Article 3

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 11 June 2026.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 198, 25.7.2019, p. 64. ELI: http://data.europa.eu/eli/reg/2019/1239/oj.

(2) Commission Implementing Regulation (EU) 2023/2790 of 14 December 2023 laying down functional and technical specifications for the reporting interface module of the Maritime National Single Windows (OJ L, 2023/2790, 18.12.2023, ELI: http://data.europa.eu/eli/reg_impl/2023/2790/oj.

(3) Regulation (EU) 2024/903 of the European Parliament and of the Council of 13 March 2024 laying down measures for a high level of public sector interoperability across the Union (Interoperable Europe Act) (OJ L, 2024/903, 22.3.2024, ELI: http://data.europa.eu/eli/reg/2024/903/oj).

(4) https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/SML+service.

(5) https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/SMP+software.

## ANNEX

**DEPLOYMENT, MAINTENANCE AND USAGE OF THE COMMON ADDRESSING SERVICE**

The common addressing service shall consist of a central locator node, operated and maintained by the Commission, and publisher nodes operated and maintained by each Member State in compliance with the eDelivery specifications.

Senders may use the common addressing service to initiate direct system-to-system data connection between their AS4 access point and a reporting interface module using the dynamic discovery instead of a manually pre-configured connection details of the reporting interface module in their AS4 access point.

To retrieve RIM connection details, the sender’s AS4 access point shall contact a publisher node, which stores the relevant connection information. Connection details of a particular RIM or an AS4 access point shall be stored exclusively in a single publisher node. The central locator node shall facilitate this process by managing publisher nodes in the public DNS and enabling dynamic discovery.

In alternative of manually pre-configuring the connection details of the senders AS4 access point in the reporting interface module, Member States may use their publisher node to store the connection details of the AS4 access points of senders.

**FUNCTIONAL AND TECHNICAL SPECIFICATIONS**

**Central locator node**

Central locator node shall provide the following functionalities:

| ID | Name | Description |
| --- | --- | --- |
| C1 | Network address directory and lookup | The central locator node shall act as a central directory of RIM and AS4 access points identifiers and their respective publisher nodes identifiers and make them discoverable via public DNS. |
| C2 | Central management of publisher nodes | The central locator node shall register, update and delete metadata of publisher nodes in the public DNS. Member States shall be able to manage their publisher node details directly through the system-to-system interface of the central locator node. |
| C3 | Trust and Security | The central locator node shall only allow the registration and communication through publisher nodes that present a valid mutual Transport Layer Security (mTLS) certificate issued by a recognized and trusted public certificate authority in accordance with eDelivery guidelines on digital certificates. |

**Publisher nodes**

Publisher nodes shall provide the following functionalities:

| ID | Name | Description |
| --- | --- | --- |
| D4 | Metadata provision | The publisher node shall store and provide the RIM or sender AS4 access point connection details upon request. |
| D5 | Trust and Security | Publisher nodes shall be accessible over internet using a valid TLS certificate issued by a recognized and trusted public certificate authority in accordance with eDelivery guidelines on digital certificates. |
| D6 | Managing records | Publisher node shall provide the possibility to manage (register, update, remove or migrate) RIM and sender AS4 access point connection details stored in the publisher node. Updates related to this information and of a publisher node that requires modification in DNS records shall be synchronised with the central locator node. |

The publisher node shall store at least the following information:

| ID | Name | Description |
| --- | --- | --- |
| E1 | Endpoint information | The RIM or AS4 access point technical addresses to which the AS4 messages are sent. |
| E2 | Public certificate | The public trusted certificate required for the AS4 message encryption. |

**QUALITY CONTROL MECHANISMS**

| ID | Name | Description |
| --- | --- | --- |
| L1 | Logging and monitoring information | The central locator and publisher nodes shall offer the logging and monitoring capabilities for quality control purposes. |
| L2 | Exception handling | The central locator and publisher nodes shall be able to detect and handle exceptions and errors and report when they occur. |

ELI: http://data.europa.eu/eli/reg_impl/2026/1233/oj

ISSN 1977-0677 (electronic edition)
