---
title: "Regulation (EU) 2015/1599 of the European Central Bank of 10 September 2015 amending Regulation (EU) No 1333/2014 concerning statistics on the money markets (ECB/2015/30)"
identifier: "32015R1599"
eli: "http://data.europa.eu/eli/reg/2015/1599/oj"
type: regulation
jurisdiction: eu
language: en
date: 2015-09-10
entry_into_force: 2015-04-22
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R1599"
retrieved: 2026-10-11
---

# Regulation (EU) 2015/1599 of the European Central Bank of 10 September 2015 amending Regulation (EU) No 1333/2014 concerning statistics on the money markets (ECB/2015/30)

**REGULATION (EU) 2015/1599 OF THE EUROPEAN CENTRAL BANK**

**of 10 September 2015**

**amending Regulation (EU) No 1333/2014 concerning statistics on the money markets (ECB/2015/30)**

THE GOVERNING COUNCIL OF THE EUROPEAN CENTRAL BANK,

Having regard to the Statute of the European System of Central Banks and of the European Central Bank, and in particular Article 5 thereof,

Having regard to Council Regulation (EC) No 2533/98 of 23 November 1998 concerning the collection of statistical information by the European Central Bank (1), and in particular Articles 5(1) and 6(4) thereof,

Whereas:

(1) Regulation (EU) No 1333/2014 of the European Central Bank (ECB/2014/48) (2) requires the reporting of statistical data by reporting agents in order that the European System of Central Banks, in the fulfilment of its tasks, may produce statistics on money market transactions.

(2) A set of reporting instructions setting out detailed parameters for the reporting of statistical information under Regulation (EU) No 1333/2014 (ECB/2014/48) will be issued to national central banks. As the reporting instructions refine a number of significant terms appearing in that Regulation, consistency requires that it should also reflect those changes.

(3) Therefore, Regulation (EU) No 1333/2014 (ECB/2014/48) should be amended accordingly,

HAS ADOPTED THIS REGULATION:

## Article 1 — Amendments

1\. Annex I to Regulation (EU) No 1333/2014 (ECB/2014/48) is replaced by Annex I to this Regulation.

2\. Annexes II and III to Regulation (EU) No 1333/2014 (ECB/2014/48) are amended in accordance with Annex II to this Regulation.

## Article 2 — Final provisions

This Regulation shall enter into force on the twentieth day following its publication in the Official Journal of the European Union.

This Regulation shall be binding in its entirety and directly applicable in the Member States in accordance with the Treaties.

Done at Frankfurt am Main, 10 September 2015.

For the Governing Council of the ECB

The President of the ECB

Mario DRAGHI

(1) OJ L 318, 27.11.1998, p. 8.

(2) Regulation (EU) No 1333/2014 of the European Central Bank of 26 November 2014 concerning statistics on the money markets (ECB/2014/48) (OJ L 359, 16.12.2014, p. 97).

## ANNEX I — ‘ANNEX I

**Reporting scheme for money market statistics relating to secured transactions**

**PART 1**

**TYPE OF INSTRUMENTS**

Reporting agents report to the European Central Bank (ECB) or the relevant national central bank (NCB) all repurchase agreements and transactions entered into thereunder, including tri-party repo transactions, which are denominated in euro with a maturity of up to and including one year (defined as transactions with a maturity date of not more than 397 days after the settlement date) between the reporting agent and other monetary financial institutions (MFIs), other financial intermediaries (OFIs), insurance corporations, pension funds, general government or central banks for investment purposes as well as with non-financial corporations classified as “wholesale” according to the Basel III LCR framework.

**PART 2**

**TYPE OF DATA**

**1\. Type of transaction-based data (1) to be reported for each transaction:**

| Field | Description of data | Alternative reporting option (if any) and other qualifications |
| --- | --- | --- |
| Transaction identifier | The internal unique transaction identifier used by the reporting agent for each transaction. | The transaction identifier is unique for any transaction reported on a given reporting date for any money market segment. |
| Reporting date | The date on which the data are submitted to the ECB or the NCB. |  |
| Electronic time stamp | The time at which a transaction is concluded or booked. |  |
| Counterparty code | An identification code used to recognise the counterparty of the reporting agent for the reported transaction. | Where transactions are conducted via a central clearing counterparty (CCP), the CCP legal entity identifier (LEI) must be provided. Where transactions are undertaken with non-financial corporations, OFIs, insurance corporations, pension funds, general government, and central banks and for any other reported transaction for which the counterparty LEI is not provided, the counterparty class must be provided. |
| Counterparty code ID | An attribute specifying the type of individual counterparty code transmitted. | To be used in all circumstances. An individual counterparty code will be provided. |
| Counterparty location | International Organisation for Standardisation (ISO) country code of the country in which the counterparty is incorporated. | Mandatory if the individual counterparty code is not provided. Otherwise optional. |
| Transaction nominal amount | The amount initially borrowed or lent. |  |
| Collateral nominal amount | The nominal amount of the security pledged as collateral. | Except for tri-party repos and any other transaction in which the security pledged is not identified via a single International Securities Identification Number (ISIN). |
| Trade date | The date on which the parties enter into the financial transaction. |  |
| Settlement date | The purchase date, i.e. the date on which the cash is due to be paid by the lender to the borrower and the security is to be transferred by the borrower to the lender. | In the case of open basis repurchase transactions, this is the date on which the rollover settles (even if no exchange of cash takes place). |
| Maturity date | The repurchase date, i.e. the date on which the cash is due to be repaid by the borrower to the lender. | In the case of open basis repurchase transactions, this is the date on which principal and interest owed is to be repaid if the transaction is not rolled over further. |
| Transaction sign | Borrowing of cash in the case of repos or lending of cash in the case of reverse repos. |  |
| ISIN of the collateral | The ISIN assigned to securities issued in financial markets, composed of 12 alphanumeric characters, which uniquely identifies a security (as defined by ISO 6166). | To be reported with exceptions for certain collateral types. |
| Collateral type | To identify the asset class pledged as collateral where no individual ISIN is provided. | To be provided in all cases where no individual ISIN is provided. |
| Collateral Issuer Sector | To identify the sector of the issuer of the collateral when no individual ISIN is provided | To be provided where no individual ISIN is provided. |
| Special collateral flag | To identify all repurchase transactions conducted against general collateral and those conducted against special collateral. Optional field to be provided only if it is feasible for the reporting agent. | Reporting of this field is optional. |
| Deal rate | The interest rate expressed in accordance with the ACT/360 money market convention at which the repo was concluded and at which the cash lent is remunerated. |  |
| Collateral haircut | A risk control measure applied to underlying collateral whereby the value of that underlying collateral is calculated as the market value of the assets reduced by a certain percentage (haircut). For reporting purposes the collateral haircut is calculated as 100 minus the ratio between the cash lent/borrowed and the market value including accrued interest of the collateral pledged. | Reporting of this field is only required for single collateral transactions. |
| Counterparty code of the tri-party agent | The counterparty code identifier of the tri-party agent. | To be reported for tri-party repos. |
| Tri-party agent code ID | An attribute specifying the type of individual tri-party agent code transmitted. | To be used in all circumstances where an individual tri-party agent code will be provided. |

**2\. Materiality threshold**

Transactions undertaken with non-financial corporations should only be reported when undertaken with non-financial corporations classified as wholesale on the basis of the Basel III LCR Framework (2).

**3\. Exceptions**

Intra-group transactions should not be reported.’

(1) The electronic reporting standards and the technical specifications for the data are laid down separately. They are available on the ECB's website at: www.ecb.europa.eu.

(2) See “Basel III: The liquidity coverage ratio and liquidity risk monitoring tools”, Basel Committee on Banking Supervision, January 2013, pp. 23 to 27, available on the Bank for International Settlements' website at: www.bis.org.

## ANNEX II

Annexes II and III to Regulation (EU) No 1333/2014 (ECB/2014/48) are amended as follows:

1\. in Annex II, Part 1 is replaced by the following:

**‘PART 1**

**TYPE OF INSTRUMENTS**

<table>
<tbody><tr><td></td><td>1.</td><td>Reporting agents report to the European Central Bank (ECB) or the relevant national central bank (NCB):<table><tbody><tr><td>(a)</td><td>all borrowing using the instruments defined in the table below, which are denominated in euro with a maturity of up to and including one year (defined as transactions with a maturity date of not more than 397 days after the settlement date), of the reporting agent from other monetary financial institutions (MFIs), other financial intermediaries (OFIs), insurance corporations, pension funds, general government or central banks for investment purposes as well as from non-financial corporations classified as “wholesale” according to the Basel III LCR framework;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>all lending to other credit institutions with a maturity of up to and including one year (defined as transactions with a maturity date of not more than 397 days after the settlement date) via unsecured deposits or call accounts, or via the purchase from the issuing credit institutions of commercial paper, certificates of deposit, floating rate notes and other debt securities with a maturity of up to one year.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td></td><td>2.</td><td>The table below provides a detailed standard description of the instrument categories for transactions which reporting agents are required to report to the ECB. In the event that the reporting agents are required to report the transactions to their NCB, the relevant NCB should transpose these descriptions of instrument categories at national level in accordance with this Regulation.<table><tbody><tr><td>Instrument type</td><td>Description</td></tr>
<tr><td>Deposits</td><td>Unsecured interest-bearing deposits (including call accounts but excluding current accounts) which are either redeemable at notice or have a maturity of not more than one year and which are either taken (borrowing) or placed by the reporting agent.</td></tr>
<tr><td>Call accounts</td><td>Cash accounts with daily changes in the applicable interest rate, giving rise to interest payments or calculations at regular intervals, and a notice period to withdraw money.</td></tr>
<tr><td>Certificate of deposit</td><td>A fixed-rate debt instrument issued by an MFI entitling the holder to a specific fixed rate of interest over a defined fixed term of up to one year.</td></tr>
<tr><td>Commercial paper</td><td>A debt instrument that is either unsecured or backed by collateral provided by the issuer, which has a maturity of not more than one year and is either interest-bearing or discounted.</td></tr>
<tr><td>Floating rate note</td><td>A debt instrument for which the periodic interest payments are calculated on the basis of the value, i.e. through fixing of an underlying reference rate such as Euribor on predefined dates known as fixing dates, and which has a maturity of not more than one year.</td></tr>
<tr><td>Other short-term debt securities</td><td>Unsubordinated securities other than equity of up to one year maturity issued by reporting agents, which are instruments usually negotiable and traded on secondary markets or which can be offset on the market and which do not grant the holder any ownership rights over the issuing institution. This item includes:<table><tbody><tr><td>(a)</td><td>securities that give the holder an unconditional right to a fixed or contractually determined income in the form of coupon payments and/or a stated fixed sum at a specific date (or dates) or starting from a date defined at the time of issue;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>non-negotiable instruments issued by reporting agents that subsequently become negotiable and are reclassified as “debt securities”.’</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

2\. in Annex III, Part 1 is replaced by the following:

**‘PART 1**

**TYPE OF INSTRUMENTS**

Reporting agents report to the European Central Bank (ECB) or the relevant national central bank (NCB):

(a) all foreign exchange swaps transactions, in which euro are bought/sold spot against a foreign currency and re-sold or re-bought at a forward date at a pre-agreed foreign exchange forward rate with a maturity of up to and including one year (defined as transactions with a maturity date of not more than 397 days after the settlement date of the spot leg of the foreign exchange swap transaction), between the reporting agent and other monetary financial institutions (MFIs), other financial intermediaries (OFIs), insurance corporations, pension funds, general government or central banks for investment purposes as well as with non-financial corporations classified as “wholesale” according to the Basel III LCR framework;

(b) overnight index swaps (OIS) transactions denominated in euro between the reporting agent and other MFIs, OFIs, insurance corporations, pension funds, general government or central banks for investment purposes as well as with non-financial corporations classified as “wholesale” according to the Basel III LCR framework.’;

3\. in Annex III, the table in paragraph 1 of Part 2 is replaced by the following:

| ‘Field | Description of data | Alternative reporting option (if any) and other qualifications |
| --- | --- | --- |
| Transaction identifier | The internal unique transaction identifier used by the reporting agent for each transaction. | The transaction identifier is unique for any transaction reported on a given reporting date for any money market segment. |
| Reporting date | The date on which the data are submitted to the ECB or the NCB. |  |
| Electronic time stamp | The time at which a transaction is concluded or booked. |  |
| Counterparty code | An identification code to be used to recognise the counterparty of the reporting agent for the reported transaction. | Where transactions are conducted via a central clearing counterparty (CCP), the CCP legal entity identifier (LEI) must be provided. Where transactions are undertaken with non-financial corporations, OFIs, insurance corporations, pension funds, general government, and central banks and for any other reported transaction for which the counterparty LEI is not provided, the counterparty class must be provided. |
| Counterparty code ID | An attribute specifying the type of individual counterparty code transmitted. | To be used in all circumstances. An individual counterparty code will be provided. |
| Counterparty location | International Organisation for Standardisation (ISO) country code of the country in which the counterparty is incorporated. | Mandatory if the individual counterparty code is not provided. Otherwise optional. |
| Trade date | The date on which the parties enter into the reported financial transaction. |  |
| Spot value date | The date on which one party sells to the other a specified amount of a specified currency against payment of an agreed amount of a specified different currency based on an agreed foreign exchange rate known as a foreign exchange spot rate. |  |
| Maturity date | The date on which the foreign exchange swap transaction expires and the currency sold on the spot value date is repurchased. |  |
| Transaction sign | To be used to identify whether the euro amount reported under the transactional nominal amount is bought or sold on the spot value date. | This should refer to euro spot, i.e. whether euro is bought or sold on the spot value date. |
| Transaction nominal amount | The amount of euro bought or sold on the spot value date. |  |
| Foreign currency code | The international three-digit ISO code of the currency bought/sold in exchange for euro. |  |
| Foreign exchange spot rate | The foreign exchange rate between the euro and the foreign currency applicable to the spot leg of the foreign exchange swap transaction. |  |
| Foreign exchange forward points | The difference between the foreign exchange spot rate and the foreign exchange forward rate expressed in basis points quoted in accordance with the prevailing market conventions for the currency pair.’ |  |
