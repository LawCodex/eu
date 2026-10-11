---
title: "Commission Implementing Decision (EU) 2017/224 of 8 February 2017 setting out the technical and operational specifications allowing the commercial service offered by the system established under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013 of the European Parliament and of the Council"
identifier: "32017D0224"
eli: "http://data.europa.eu/eli/dec_impl/2017/224/oj"
type: decision
subtype: implementing
jurisdiction: eu
language: en
date: 2017-02-08
entry_into_force: 2017-08-31
last_amended: 2024-07-31
consolidated_version: "02017D0224-20240731"
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017D0224-20240731"
retrieved: 2026-10-11
---

# Commission Implementing Decision (EU) 2017/224 of 8 February 2017 setting out the technical and operational specifications allowing the commercial service offered by the system established under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013 of the European Parliament and of the Council

**COMMISSION IMPLEMENTING DECISION (EU) 2017/224**

**of 8 February 2017**

**setting out the technical and operational specifications allowing the commercial service offered by the system established under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013 of the European Parliament and of the Council**

<table>
<tr><td rowspan="2"></td><td rowspan="2"></td><td colspan="3">Official Journal</td></tr>
<tr><td> No</td><td>page</td><td>date</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING DECISION (EU) 2018/321 of 2 March 2018 </td><td> L 62</td><td>34</td><td>5.3.2018</td></tr>
<tr><td></td><td> COMMISSION IMPLEMENTING DECISION (EU) 2024/1882 of 10 July 2024 </td><td> L 1882</td><td>1</td><td>11.7.2024</td></tr>
</table>

**COMMISSION IMPLEMENTING DECISION (EU) 2017/224**

**of 8 February 2017**

**setting out the technical and operational specifications allowing the commercial service offered by the system established under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013 of the European Parliament and of the Council**

## Article 1

The technical and operational specifications allowing the commercial service offered by the system under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013 are set out in the Annex.

## Article 2

This Decision shall enter into force on the twentieth day following its publication in the Official Journal of the European Union.

## ANNEX

**Technical and operational specifications allowing the commercial service offered by the system established under the Galileo programme to fulfil the function referred to in Article 2(4)(c) of Regulation (EU) No 1285/2013**

The commercial service (hereinafter ‘CS’) offers two major improvements compared to the open service (hereinafter ‘OS’), namely higher accuracy  in terms of geolocation (hereinafter ‘CS high accuracy  ’) and reinforced authentication capacity (hereinafter ‘CS authentication’), which can be offered to users independently of each other. The corresponding technical and operational specifications are set out in the table below:

<table>
<tbody><tr><td rowspan="2">  </td><td rowspan="2">CS high  accuracy  </td><td colspan="2">CS authentication</td></tr>
<tr><td>Specifications common to the OS and the CS: authentication of geolocation information</td><td>Specifications specific to the CS: authentication using encrypted codes</td></tr>
<tr><td>General specifications</td><td> Supply of high  accuracy   data in order to obtain a positioning error of less than two decimetres in nominal conditions of use  </td><td>Supply of authentication data for geolocation information from the OS, contained in the signals</td><td>Authentication of the signals through access to encrypted codes contained in the signals</td></tr>
<tr><td>Components of the signals used</td><td>E6, E6-B component for the supply of high  accuracy   data</td><td>E1, E1-B component for authentication data from the geolocation information</td><td> E6, E6-C component encrypted (pilot)  </td></tr>
<tr><td>Specifications of the user segment</td><td>High  accuracy   positioning obtained using precise positioning algorithms integrated into the receiver and using the data transmitted in the signals</td><td>Verification of the authenticity of the data using an asymmetrical cryptography protocol transmitted in the signals and a public cryptographic key</td><td> Verification of the authenticity of the signals by decrypting E6 codes re-encrypted with an OS data authentication key  </td></tr>
<tr><td>Geographical coverage</td><td>Global</td><td>Global</td><td>Global</td></tr>
<tr><td>System architecture</td><td>High- accuracy   data provided by one or more service providers, transmitted to users via the GNSS Service Centre (GSC), the ground segment and the satellites connected to the ground segment</td><td>Authentication data inserted into the available capacity of the EDBS field of the E1-B signal component, and disseminated by the satellites connected to the ground segment</td><td> Encryption of the E6 signal codes by the Galileo satellites, transmission of the private keys generated by the ground segment to the GNSS Service Centre (GSC), and publication of re-encrypted portions of the E6 signal codes with a future OS data authentication key  </td></tr>
<tr><td>Provision of the service</td><td>High  accuracy   data provided by one or more service providers</td><td>Authentication data provided by the system established under the Galileo programme</td><td>Encrypted signals supplied by the system operating manager</td></tr>
<tr><td>Access to the service</td><td>   — Free access   </td><td colspan="2"> Free access  </td></tr>
<tr><td>Deployment of the service</td><td>— Testing and validation phase to be concluded in 2018   — Initial signals supply phase between 2018 and 2020  — Full service supply phase from 2020   </td><td>— Testing and validation phase to be concluded in 2018 — Initial signals supply phase between 2018 and 2020  — Full service supply phase from 2020 </td><td>   — Initial signals supply phase by 2024,  — Service supply phase from 2026   </td></tr>
<tr><td>Use of EU classified information</td><td>— No use of EUCI by the Commercial Service Provider or the end user. However, if such authorisation is required it is decided in accordance with the rules on security set out in Article 17(a) of Regulation (EU) No 1285/2013.</td><td>— No use of EUCI by the Commercial Service Provider or the end user. However, if such authorisation is required it is decided in accordance with the rules on security set out in Article 17(a) of Regulation (EU) No 1285/2013.</td><td> No use of EUCI by the end user  </td></tr>
<tr><td>Further specifications</td><td>— High- accuracy   data provided for the Galileo satellites and possibly for the satellites of other constellations</td><td>— The transmission of authentication data must not lead to any deterioration in the open service — The authentication data must be provided for the Galileo satellites and possibly for the satellites of other constellations  — The users of the OS accept the risks linked to the use of authentication data </td><td>n/a</td></tr>
</tbody>
</table>

**Acronyms**

E1-B Data channel for the signal in frequency E1 of the Galileo system, on 1 575,45 MHz

E6 Frequency E6 of the Galileo system, on 1 278,75 MHz

E6-B Component of the E6 signal, corresponding to the data channel

E6-C Component of the E6 signal, corresponding to the pilot channel

EDBS External Data Broadcast Service

GNSS Global Navigation Satellite System

n/a Not applicable.

OTAR Over-The-Air Rekeying
