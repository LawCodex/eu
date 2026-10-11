---
title: "Commission Implementing Regulation (EU) 2017/2169 of 21 November 2017 concerning the format and arrangements for the transmission of European Statistics on natural gas and electricity prices pursuant to Regulation (EU) 2016/1952 of the European Parliament and of the Council (Text with EEA relevance. )"
identifier: "32017R2169"
eli: "http://data.europa.eu/eli/reg_impl/2017/2169/oj"
type: regulation
subtype: implementing
jurisdiction: eu
language: en
date: 2017-11-21
entry_into_force: 2017-01-01
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R2169"
retrieved: 2026-10-11
---

# Commission Implementing Regulation (EU) 2017/2169 of 21 November 2017 concerning the format and arrangements for the transmission of European Statistics on natural gas and electricity prices pursuant to Regulation (EU) 2016/1952 of the European Parliament and of the Council (Text with EEA relevance. )

**COMMISSION IMPLEMENTING REGULATION (EU) 2017/2169**

**of 21 November 2017**

**concerning the format and arrangements for the transmission of European Statistics on natural gas and electricity prices pursuant to Regulation (EU) 2016/1952 of the European Parliament and of the Council**

**(Text with EEA relevance)**

THE EUROPEAN COMMISSION,

Having regard to the Treaty on the Functioning of the European Union,

Having regard to Regulation (EU) 2016/1952 of the European Parliament and of the Council of 26 October 2016 concerning European statistics on natural gas and electricity prices and repealing Directive 2008/92/EC (1), and in particular Article 5(2) thereof

Whereas:

(1) Regulation (EU) 2016/1952 establishes the common framework for producing comparable European statistics on natural gas and electricity prices for household and final non-household customers in the Union.

(2) In accordance with Article 5(2) of Regulation (EU) 2016/1952 Member States should transmit the statistical data in electronic form, in order to conform to an appropriate technical format to be laid down by the Commission.

(3) The Statistical Data and Metadata exchange (SDMX) provides statistical and technical standards for the exchange of official statistics. A technical format in accordance with these standards should therefore be established by the Commission (Eurostat) within the European Statistical System in close cooperation with Member States.

(4) The measures provided for in this Regulation are in accordance with the opinion of the European Statistical System Committee,

HAS ADOPTED THIS REGULATION:

## Article 1

The data on natural gas and electricity prices for household and final non-household customers in the Union shall be provided to Eurostat through the single entry point to enable the Commission (Eurostat) to retrieve those data by electronic means.

## Article 2

The structure used for transmitting data to the Commission (Eurostat) is set out in the Annexes.

## Article 3

This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in all Member States.

Done at Brussels, 21 November 2017.

For the Commission

The President

Jean-Claude JUNCKER

(1) OJ L 311, 17.11.2016, p. 1.

## ANNEX I

**The structure for transmitting statistical data on natural gas price**

Information to be included in the transmission files:

**General Information**

| Field | Remarks | Reporting Frequency |
| --- | --- | --- |
| Country | Name of the reporting country | Semester |
| Organisation | Name of the reporting organisation | Semester |
| Contact person | Name of the reporting officer | Semester |
| Email address | Email address of the reporting officer | Semester |
| Year | Reference year for the data (2017, 2018 etc.) | Semester |
| Semester | 1 or 2 | Semester |

For every consumption band the fields in Tables 1, 2 and 4 are to be transmitted.

The bands for the household consumers are:

— Band-D1 (small): annual consumption below 20 GJ;

— Band-D2 (medium): annual consumption 20 or more but less than 200 GJ;

— Band-D3 (large): annual consumption 200 GJ or more.

The bands for the non-household consumers are:

— Band-I1: annual consumption below 1 000 GJ;

— Band-I2: annual consumption 1 000 or more but less than 10 000 GJ;

— Band-I3: annual consumption 10 000 or more but less than 100 000 GJ;

— Band-I4: annual consumption 100 000 or more but less than 1 000 000 GJ;

— Band-I5: annual consumption 1 000 000 or more but less than 4 000 000 GJ;

— Band-I6: annual consumption 4 000 000 GJ or more.

Data in Table 3 are to be specified as averages covering all consumption bands together.

**Table 1: Main price levels**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality Status</td><td></td><td>Semester</td></tr>
<tr><td>Price without taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include only the energy and supply component and the network component.</td><td>Semester</td></tr>
<tr><td>Price excluding VAT and other recoverable taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include the energy and supply component, the network component and taxes, fees, levies and charges considered as non-recoverable for final non-household customers. For household customers this price level shall include the energy and network components and taxes, fees, levies and charges but excludes VAT.</td><td>Semester</td></tr>
<tr><td>Price including all taxes and VAT (recoverable and non-recoverable)<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include the energy and supply component, the network component, and all recoverable and non-recoverable taxes, fees, levies and charges, including VAT.</td><td>Semester</td></tr>
</tbody>
</table>

Values are specified in national currency per gigajoule (gross calorific value).

Confidentiality and observation status are set using standard code lists.

**Table 2: Detailed breakdown of prices in components and sub-components**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Energy and supply price<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This component shall include the commodity price for natural gas paid by the supplier or the price of natural gas at the point of entry into the transmission system, including, if applicable, the following end-user costs: storage costs plus costs relating to the sale of natural gas to final customers.</td><td>Annual</td></tr>
<tr><td>Network price<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>The network price shall include the following end-user costs: transmission and distribution tariffs, transmission and distribution losses, network costs, after-sale service costs, system service costs and meter rental and metering costs.</td><td>Annual</td></tr>
<tr><td>Value added tax<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Value added tax as defined in Council Directive 2006/112/EC (1)</td><td>Annual</td></tr>
<tr><td>Renewable taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to the promotion of renewable energy sources, energy efficiency and CHP (combined heat and power) generation.</td><td>Annual</td></tr>
<tr><td>Capacity taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to strategic stockpiles, capacity payments and energy security; taxes on natural gas distribution; stranded costs and levies on financing energy regulatory authorities or market and system operators.</td><td>Annual</td></tr>
<tr><td>Environmental taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to air quality and for other environmental purposes; taxes on emissions of CO2 or other greenhouse gases.</td><td>Annual</td></tr>
<tr><td>Other taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>All other taxes, fees, levies or charges not covered by any of the previous four categories: support for district heating; local or regional fiscal charges; island compensation; concession fees relating to licences and fees for the occupation of land and public or private property by networks or other devices.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for all components and all sub-components is annual.

Values are specified in national currency per gigajoule (GJ), based on gross calorific value (GCV).

Confidentiality and observation status are set using standard code lists.

**Table 3: Network costs**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Transmission costs<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Average relative share of transmission costs for household customers and average relative share of transmission costs for final non-household customers, expressed as a percentage of total network costs.</td><td>Annual</td></tr>
<tr><td>Distribution costs<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Average relative share of distribution costs for household customers and average relative share of distribution costs for final non-household customers, expressed as a percentage of total network costs.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for the transmission and distribution costs is annual.

Values are specified in percentages.

Confidentiality and observation status are set using standard code lists.

**Table 4: Consumption volumes**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Consumption volumes<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Relative share of natural gas in each consumption band based on the total volume to which the prices refer.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for the consumption volumes is annual.

Values are specified in percentages.

Confidentiality and observation status are set using standard code lists.

(1) Council Directive 2006/112/EC of 28 November 2006 on the common system of value added tax (OJ L 347, 11.12.2006, p. 1).

## ANNEX II

**The structure for transmitting statistical data on electricity price**

Information to be included in the transmission files:

**General Information**

| Field | Remarks | Reporting Frequency |
| --- | --- | --- |
| Country | Name of the reporting country | Semester |
| Organisation | Name of the reporting organisation | Semester |
| Contact person | Name of the reporting officer | Semester |
| Email address | Email address of the reporting officer | Semester |
| Year | Reference year for the data (2017, 2018 etc.) | Semester |
| Semester | 1 or 2 | Semester |

For every consumption band, the fields in Tables 1, 2 and 4 are to be transmitted.

The bands for the household consumers are:

— Band-DA (very small): annual consumption below 1 000 kWh;

— Band-DB (small): annual consumption 1 000 or more but less than 2 500 kWh;

— Band-DC (medium): annual consumption 2 500 or more but less than 5 000 kWh;

— Band-DD (large): annual consumption 5 000 or more but less than 15 000 kWh;

— Band-DE (very large): annual consumption 15 000 kWh or more.

The bands for the non-household consumers are:

— Band-IA: annual consumption below 20 MWh;

— Band-IB: annual consumption 20 or more but less than 500 MWh;

— Band-IC: annual consumption 500 or more but less than 2 000 MWh;

— Band-ID: annual consumption 2 000 or more but less than 20 000 MWh;

— Band-IE: annual consumption 20 000 or more but less than 70 000 MWh;

— Band-IF: annual consumption 70 000 or more but less than 150 000 MWh;

— Band-IG: annual consumption 150 000 MWh or more.

Data in Table 3 are to be specified as averages covering all consumption bands.

**Table 1: Main price levels**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality Status</td><td></td><td>Semester</td></tr>
<tr><td>Price without taxes:<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include only the energy and supply component and the network component.</td><td>Semester</td></tr>
<tr><td>Price excluding VAT and other recoverable taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include the energy and supply component, the network component and taxes, fees, levies and charges considered as non-recoverable for final non-household customers. For household customers this price level shall include the energy and the network components and taxes, fees, levies and charges but excludes VAT.</td><td>Semester</td></tr>
<tr><td>Price including all taxes and VAT (recoverable and non-recoverable)<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>This price level shall include the energy and supply component, the network component, and all recoverable and non-recoverable taxes, fees, levies and charges, including VAT.</td><td>Semester</td></tr>
</tbody>
</table>

Values are specified in national currency per kilowatt-hour.

Confidentiality and observation statuses are set using standard code lists.

**Table 2: Detailed breakdown of prices in components and sub-components**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Energy and supply price<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>The component of the total price that deals with energy and supply, excluding taxes. This component shall include the following end-user costs: generation, aggregation, balancing energy, supplied energy costs, customer services, after-sales management and other supply costs. </td><td>Annual</td></tr>
<tr><td>Network price<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>The component of the total price that deals with network prices, excluding taxes. The network price shall include the following end-user costs: transmission and distribution tariffs, transmission and distribution losses, network costs, after-sale service costs, system service costs, and meter rental and metering costs. </td><td>Annual</td></tr>
<tr><td>Value added tax<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Value added tax as defined in Directive 2006/112/EC.</td><td>Annual</td></tr>
<tr><td>Renewable taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to the promotion of renewable energy sources, energy efficiency and CHP generation.</td><td>Annual</td></tr>
<tr><td>Capacity taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to capacity payments, energy security and generation adequacy; taxes on coal industry restructuring; taxes on electricity distribution; stranded costs and levies on financing energy regulatory authorities or market and system operators.</td><td>Annual</td></tr>
<tr><td>Environmental taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to air quality and for other environmental purposes; taxes on emissions of CO2 or other greenhouse gases.</td><td>Annual</td></tr>
<tr><td>Nuclear taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Taxes, fees, levies or charges relating to the nuclear sector, including nuclear decommissioning, inspections and fees for nuclear installations.</td><td>Annual</td></tr>
<tr><td>Other taxes<table><tbody><tr><td>—</td><td>value</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>All other taxes, fees, levies or charges not covered by any of the previous five categories: support for district heating; local or regional fiscal charges; island compensation; concession fees relating to licences and fees for the occupation of land and public or private property by networks or other devices.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for all components and all sub-components is annual.

Values are specified in national currency per kilowatt-hour.

Confidentiality and observation statuses are set using standard code lists.

**Table 3: Network costs**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Transmission costs<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Average relative share of transmission costs for household customers and average relative share of transmission costs for final non-household customers, expressed as a percentage of total network costs.</td><td>Annual</td></tr>
<tr><td>Distribution costs<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Average relative share of distribution costs for household customers and average relative share of distribution costs for final non-household customers, expressed as a percentage of total network costs.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for the transmission and distribution costs is annual.

Values are specified in percentages.

Confidentiality and observation statuses are set using standard code lists.

**Table 4: Consumption volumes**

<table>
<tbody><tr><td>Field</td><td>Remarks</td><td>Reporting Frequency</td></tr>
<tr><td>Confidentiality status</td><td></td><td></td></tr>
<tr><td>Consumption volumes<table><tbody><tr><td>—</td><td>percentage</td></tr>
</tbody>
</table>
<table><tbody><tr><td>—</td><td>observation status</td></tr>
</tbody>
</table>
</td><td>Relative share of electricity in each consumption band based on the total volume to which the prices refer.</td><td>Annual</td></tr>
</tbody>
</table>

The reference period for the consumption volumes is annual.

Values are specified in percentages.

Confidentiality and observation statuses are set using standard code lists.
