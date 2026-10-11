---
title: "Commission Implementing Decision (EU) 2026/1065 of 8 June 2026 laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of police records through EPRIS"
identifier: "32026D1065"
eli: "http://data.europa.eu/eli/dec_impl/2026/1065/oj"
type: decision
subtype: implementing
jurisdiction: eu
language: en
date: 2026-06-08
entry_into_force: 2026-09-30
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026D1065"
retrieved: 2026-10-11
---

# Commission Implementing Decision (EU) 2026/1065 of 8 June 2026 laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of police records through EPRIS

**COMMISSION IMPLEMENTING DECISION (EU) 2026/1065**

**of 8 June 2026**

**laying down rules for the application of Regulation (EU) 2024/982 of the European Parliament and of the Council as regards the automated search and exchange of police records through EPRIS**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2024/982 of the European Parliament and of the Council of 13 March 2024 on the automated search and exchange of data for police cooperation, and amending Council Decisions 2008/615/JHA and 2008/616/JHA and Regulations (EU) 2018/1726, (EU) 2019/817 and (EU) 2019/818 of the European Parliament and of the Council (the Prüm II Regulation) (1), and in particular Article 31 and Article 44(6) thereof,

Whereas:

(1) Regulation (EU) 2024/982 establishes a framework for the automated search and exchange of certain categories of data for cross-border police cooperation.

(2) Pursuant to Regulation (EU) 2024/982, the Commission is to specify the technical procedure for automated search and exchange of police records to be done via the European Police Record Index System (EPRIS).

(3) Establishment of uniform technical and operational specifications for the functioning of EPRIS is necessary to ensure the effective, secure and interoperable exchange of police records. Such specifications should define the procedures, formats, protocols, and security requirements to guarantee a consistent and reliable automated information exchange under Regulation (EU) 2024/982.

(4) The EPRIS central routing infrastructure to be operated by Europol is to serve as a trusted intermediary for the exchange of queries and results between national police record indexes. The technical design of that infrastructure should ensure end-to-end encryption, pseudonymisation of data and strict segregation between routing functions and data content, thereby preserving data protection and confidentiality throughout all EPRIS transactions.

(5) To maintain operational continuity and mutual trust between participating entities, it is necessary to establish common requirements for system availability, configuration management and logging, as well as procedures for error handling and statistical reporting. These requirements should support the monitoring, evaluation and improvement of EPRIS performance in line with the principles of accountability, transparency and data minimisation.

(6) In accordance with Articles 1 and 2 of Protocol No 22 on the position of Denmark, annexed to the Treaty on European Union and to the Treaty on the Functioning of the European Union, Denmark did not take part in the adoption of Regulation (EU) 2024/982 and is not bound by it or subject to its application. Denmark is therefore not bound by this Decision or subject to its application.

(7) Ireland is bound by Regulation (EU) 2024/982 and is therefore bound by this Decision.

(8) EPRIS contributes to the provision of a cross-border digital public service. As this Decision introduces binding requirements affecting its development, an interoperability assessment is required under Article 3 of Regulation (EU) 2024/903 of the European Parliament and of the Council (2) (Interoperable Europe Act). The assessment has been carried out, and the resulting report will be published on the Interoperable Europe Portal.

(9) The European Data Protection Supervisor delivered an opinion on 27 January 2026.

(10) The measures provided for in this Decision are in accordance with the opinion of the Prüm II Committee, established by Article 77 of Regulation (EU) 2024/982.

HAS ADOPTED THIS DECISION:

## Article 1

For the purposes of this Decision, the following definitions apply::

(a) ‘entity’ means either a Member State or Europol;

(b) ‘requesting entity’ means a Member State or Europol that initiates a query;

(c) ‘requested entity’ means a Member State that receives a search;

(d) ‘transaction’ means one query, converted into one or several searches and its corresponding results;

(e) ‘query’ means the input initiated and sent by a requesting entity to the query service deployed in its own infrastructure;

(f) ‘search’ means a message sent by the query service of a requesting entity to the search service of requested entities to retrieve a list of results;

(g) ‘result’ means the information sent from the search service of a requested entity to the query service of a requesting entity following a search, indicating either a match, including its related details, or a no-match outcome;

(h) ‘response’ means the aggregation of all results related to a query;

(i) ‘query service’ means a micro-service to query entities;

(j) ‘search service’ means a micro-service to manage and search the index(es).

## Article 2

The specifications relating to the technical rules for automated search and exchange of police records via EPRIS shall be as set out in the Annex.

## Article 3

This Decision shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

Done at Brussels, 10.6.2026.

For the Commission

The President

Ursula VON DER LEYEN

(1) OJ L 2024/982, 5.4.2024, ELI: http://data.europa.eu/eli/reg/2024/982/oj.

(2) Regulation (EU) 2024/903 of the European Parliament and of the Council of 13 March 2024 laying down measures for a high level of public sector interoperability across the Union (Interoperable Europe Act) (OJ L, 2024/903, 22.3.2024, ELI: http://data.europa.eu/eli/reg/2024/903/oj).

## ANNEX — Technical rules for automated search and exchange of police records via EPRIS as referred to in Article 2

**CHAPTER 1**

**EPRIS**

**1\. Entities code table**

The requesting and requested entities shall be identified by a two-letter code from ISO 3166. Where the entity has no reserved ISO-code, this document defines one in Table 1.

**Table 1**

**List of entity codes used in Prüm II automated exchanges**

| Entity name | Code |
| --- | --- |
| Austria | AT |
| Belgium | BE |
| Bulgaria | BG |
| Cyprus | CY |
| Czechia | CZ |
| Germany | DE |
| Estonia | EE |
| Spain | ES |
| Finland | FI |
| France | FR |
| Greece | GR |
| Croatia | HR |
| Hungary | HU |
| Ireland | IE |
| Italy | IT |
| Lithuania | LT |
| Luxembourg | LU |
| Latvia | LV |
| Malta | MT |
| Netherlands | NL |
| Poland | PL |
| Portugal | PT |
| Romania | RO |
| Sweden | SE |
| Slovenia | SI |
| Slovakia | SK |
| Europol | EP |

**2\. The technical procedure for EPRIS to query Member States’ police record indexes**

EPRIS shall use the network interconnections agreed between Europol and Member States for the exchange of data with the entities. EPRIS and the entities shall exchange data via transactions using a central routing infrastructure. This service provided by Europol shall be known as the ‘EPRIS central routing infrastructure’ and its technical details shall be determined by Europol.

Each participating Member State shall deploy: (i) at least one national police record index; (ii) micro-services to manage and search the index(es) (search services); and (iii) micro-services to query entities (query services).

Europol shall deploy services to query entities (query service).

The EPRIS central routing infrastructure and services shall be provided with respect to the infrastructure of Member States.

The workflow for an EPRIS transaction shall have the following steps:

(1) The requesting entity initiates a query that is sent to its query service.

(2) The query service of the requesting entity shall pseudonymize the query parameters and shall send a search to the search service of each requested entity via the EPRIS central routing infrastructure.

(3) The search service of each requested entity shall proceed to a search of its national police record index in an automated manner. If a requested entity uses multiple national indexes, a search proxy shall receive and dispatch the query to the multiple national search services, and collect the results.

(4) The search service (or the search proxy if applicable) of the requested entities shall send the results via the EPRIS central routing infrastructure to the query service of the requesting entity.

(5) The query service of the requesting entity shall collect the results in a response.

Each query of a requesting entity to the query service deployed in its own infrastructure shall include the search parameters and information regarding requested entities as determined by Europol.

A requesting entity may initiate several queries within a single interaction to its query service.

Each search sent by the query service of the requesting entity shall include specific routing information as defined in the technical documentation on the implementation of EPRIS. The routing information shall be added to the query by the query service based on configuration data.

The search parameters within the data payload of a search shall be pseudonymised in accordance with Article 25(2) of Regulation (EU) 2024/982.

The data-payload for the search and subsequent result is encrypted via a security certificate before being exchanged, except for the routing information.

The query service of the requesting entity shall validate the data payload.

The EPRIS central routing infrastructure shall not be able to read or validate the data-payload as it is encrypted.

The search service of the requested entity shall validate the data-payload to ensure it can be processed correctly.

If the search service of the requested entity is unable to process the data-payload correctly, an error shall be sent back to the requesting entity through the EPRIS central routing infrastructure. The format and details of these errors shall be determined by Europol, notably error-codes related to the webservices and the EPRIS central routing infrastructure.

**3\. Search concepts**

EPRIS shall support at least two search concepts which allow to compare the pseudonymised police records in an exact manner (strict search) and an inexact manner (tolerant search). The search concepts shall be determined by Europol.

The requesting entity shall decide which search concepts to use in each individual case.

**4\. The format and maximum number of replies**

Each search and its subsequent result as described in Article 28 of Regulation (EU) 2024/982 shall be identified by a Transaction Identifier (TId) consisting of the requesting entity’s two-letter code followed by a unique code identifying the transaction, which shall be linked to the date and time in the query service logs. The receiving search service shall log the transaction retaining the TId for traceability.

All searches sent by the query service which are based on a single query initiated by the requesting entity shall have the same TId.

Each result sent back to the query service of the requesting entity shall reference the TId from the search.

Only one result per search shall be sent back by each requested entity.

The result shall include the total number of matches, the Data Reference Number (DRN) of the police records from the requested entities on which the match was returned and information about the quality of the match, including the quality of the match for each parameter used in the search. The data reference numbers and information about the quality of the match shall be returned for a maximum of 10 best matches per requested entity.

The maximum number of matches returned per result by each national police record index through the EPRIS central routing infrastructure shall be 100. The threshold of 100 matches constitutes the technical capping of the system. Europol may further adjust this threshold if operational or technical reasons would require doing so. If the threshold of 100 matches is exceeded, the search service of the requested entity shall neither report a match nor return any candidate. EPRIS shall instead report an error message stating there are too many candidates. In this case, the requesting entity shall refine its query.

**5\. Availability of the system**

The EPRIS central routing infrastructure shall be built and managed as a high-availability system with full redundancy.

In accordance with Article 46(1) of Regulation (EU) 2024/982, where it is technically impossible to use EPRIS to query one or several national police record indexes because of a failure of Europol’s infrastructure, Europol shall notify Member States in an automated manner. Europol shall take measures to address the technical impossibility of using EPRIS without delay.

Europol shall verify at regular intervals if the search services of the entities are available. Europol shall determine the process to check the availability of the entities’ search services.

Each entity shall monitor the availability of their own search and query services and act in accordance with Article 46(2) of Regulation (EU) 2024/982.

In case of the technical unavailability of a search service of more than 24 hours, Europol shall contact the entity concerned in order to assist and find a solution to this unavailability.

**6\. Configuration Data**

All parameters necessary for EPRIS to function correctly shall be managed in the global configuration data and in the local configuration data.

Global configuration data shall be regularly checked and actively managed by Europol. It includes the list of participants, common search parameters (such as thresholds, traffic lights, colour mixing table, valid nationalities), common name handling configuration, provision of pseudonymisation parameters and other elements. Common search parameters, common name handling configuration, pseudonymisation parameters and timeout values shall be determined by Europol.

Global configuration data is published centrally and available to the entities. All entities shall use the exact same set of global configuration data. Pseudonymisation parameters shall be changed in a regular timeframe, and without any delay after a security incident related to the pseudonymisation parameters.

Local configuration data shall be managed by participating entities and shall include the connection details to the local services, the national infrastructure, the source databases and others.

**7\. Target processing time**

For the searching of police records, queries shall be processed by a fully automated procedure. Results shall be dispatched so as to reach the requesting entity in line with the response time limits to be determined by Europol.

**8\. Logs collection**

All queries and responses shall be logged in a structured and uniform manner by each entity, whether a requesting or a requested entity, at national level, in a decentralised approach.

In accordance with Article 45(1) of Regulation (EU) 2024/982, the logs shall include:

(a) the requesting entity;

(b) the date and time of the search;

(c) the date and time of the result;

(d) the national index(es) to which a search was sent;

(e) the national index(es) that provided a result.

The following additional fields shall be included in the logs:

(f) the transaction identifier (TId);

(g) the number of matches or no match information provided.

The log elements listed in letters a) to g) shall be used for statistical purpose.

To support the generation of statistics for operational and technical purposes, further information may be included in the logs, such as:

(h) the search mode used;

(i) the colour of the best match returned;

(j) the national index(es) that returned an error and the type of error;

(k) the national index(es) that returned too many candidates;

(l) the parameters combination that was used in the search.

**9\. Statistics collection and reporting**

Statistical data shall be recorded locally by all entities.

In accordance with Article 72(3) and (4) of Regulation (EU) 2024/982, Europol shall collect and store the following anonymised statistical data from requesting entities:

(a) the number of queries per requesting entity;

(b) the number of searches to each requested entity;

(c) the number of matches or no match information returned by each requested entity.

Further anonymised statistical data (such as response time, system availability, search mode used, colour of the best match returned, type of error returned in case of error, too many candidates, parameters combination used in the search) may be collected for operational and technical purposes.

Europol shall create and manage a centralised platform to collect these statistical data from each entity. The centralised platform shall produce customisable reports and statistics as requested by the Member States’ competent authorities, the Commission and Europol.

**10\. Protocols and standards to be used for encryption**

The Mutual Transport Layer Security (mTLS) protocol shall be used to authenticate the webservices and to encrypt the data. Other standards may be used additionally to ensure the security of the webservices.

**11\. Security standards and data protection**

In accordance with Article 53(3), point (g), of Regulation (EU) 2024/982, Europol shall ensure, by means of individual user identities and secure access modes only, that each member of Europol staff authorised to access EPRIS has access only to the data covered by their access authorisation.

Member States shall also ensure, by means of individual user identities and secure access modes only, that the staff of its competent authorities authorised to access EPRIS has access only to the data covered by their access authorisation.

**CHAPTER 2**

**National police record indexes**

**1\. Index management procedure**

Member States shall update at least every 24 hours their national police record index in a fully automated procedure.

In accordance with Article 74(7) of Regulation (EU) 2024/982, participating Member States shall notify the other Member States, the Commission and Europol of the content of their national police record indexes (such as the number of records, the number of data subjects indexed, the status of the data subjects, the type of criminal offences, the set of data included in the index, the number of the index…) and of the national source databases used for the establishment of those indexes, and the conditions for automated searches.

Additionally, Europol shall centralise and provide information about the content of all national police record indexes connected to all participating entities.

**2\. Data reference number**

Each police record is created by the entity in the national police record index(es) and uniquely labelled with a Data Reference Number (DRN) in accordance with Article 27 of Regulation (EU) 2024/982. The DRN is a unique sequence of alphanumeric characters which is persistent over time, uniquely identifying the police record.

The DRN shall not expose any personal data. Member States shall be responsible for the composition of their reference numbers. Member States shall use their country code at the beginning of all their reference numbers. DRN shall be irrevocably linked to a single record in the national police record index.

In accordance with Article 27 of Regulation (EU) 2024/982, the reference numbers for police records shall be the combination of the following:

(a) a reference number allowing Member States, in the event of a match, to retrieve biographical data and other information in their national police record indexes or source database(s) in order to supply them or it to one, several or all of the other Member States;

(b) a code to indicate the Member State which holds the police records.

In accordance with Article 28(2), point (e), of Regulation (EU) 2024/982, the DRN of the police record on which there has been a match shall be returned in the response.

The DRN shall be used when submitting a follow-up request via SIENA.

ELI: http://data.europa.eu/eli/dec_impl/2026/1065/oj

ISSN 1977-0677 (electronic edition)
