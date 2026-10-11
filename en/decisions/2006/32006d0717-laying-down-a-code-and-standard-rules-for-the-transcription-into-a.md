---
title: "2006/717/EC: Commission Decision of 4 September 2006 laying down a code and standard rules for the transcription into a machine-readable form of the data of the basic surveys of areas under vines (notified under document number C(2006) 3881) (Codified version)"
identifier: "32006D0717"
eli: "http://data.europa.eu/eli/dec/2006/717/oj"
type: decision
subtype: addressed
jurisdiction: eu
language: en
date: 2006-09-04
entry_into_force: 2006-09-20
status: in_force
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006D0717"
retrieved: 2026-10-11
---

# 2006/717/EC: Commission Decision of 4 September 2006 laying down a code and standard rules for the transcription into a machine-readable form of the data of the basic surveys of areas under vines (notified under document number C(2006) 3881) (Codified version)

**COMMISSION DECISION**

**of 4 September 2006**

**laying down a code and standard rules for the transcription into a machine-readable form of the data of the basic surveys of areas under vines**

**(notified under document number C(2006) 3881)**

**(Codified version)**

**(2006/717/EC)**

THE COMMISSION OF THE EUROPEAN COMMUNITIES,

Having regard to the Treaty establishing the European Community,

Having regard to Council Regulation (EEC) No 357/79 of 5 February 1979 on statistical surveys of areas under vines (1), and in particular Article 4(2) and (4) and Article 6(7) thereof,

Whereas:

(1) Commission Decision 79/491/EEC of 17 May 1979 laying down a code and standard rules for the transcription into a machine-readable form of the data of the basic surveys of areas under vines (2) has been substantially amended several times (3). In the interests of clarity and rationality, the said Decision should be codified.

(2) Regulation (EEC) No 357/79 requires the Member States to submit to the Commission the information collected in the framework of the basic surveys of areas under vines in the form of a schedule of tables broken down by geographical units which are to be fixed in accordance with the procedure laid down in Article 8 of the said Regulation, i.e. by a Commission Decision following an opinion from the Standing Committee on Agricultural Statistics.

(3) Those Member States which process their survey results electronically of areas under vines should submit these results to the Commission in a machine-readable form. These codes for transmitting survey results are also determined in accordance with the procedure laid down in Article 8 of Regulation (EEC) No 357/79.

(4) The measures provided for in this Decision are in accordance with the opinion of the Standing Committee on Agricultural Statistics,

HAS ADOPTED THIS DECISION:

## Article 1

The machine-readable form for submission of the data provided for in Article 2 of Regulation (EEC) No 357/79 by those Member States which process their survey results electronically shall be magnetic tape.

## Article 2

The codes and rules governing the transcription on to magnetic tape of the data provided for in Article 2 of Regulation (EEC) No 357/79 shall be as set out in Annexes I, II and III to this Decision.

## Article 3

Decision 79/491/EEC is repealed.

References to the repealed Decision shall be construed as references to this Decision and shall be read in accordance with the correlation table set out in Annex V.

## Article 4

This Decision is addressed to the Member States.

Done at Brussels, 4 September 2006.

For the Commission

The President

José Manuel BARROSO

(1) OJ L 54, 5.3.1979, p. 124. Regulation as last amended by Regulation (EC) No 1882/2003 of the European Parliament and of the Council (OJ L 284, 31.10.2003, p. 1).

(2) OJ L 129, 28.5.1979, p. 9. Decision as last amended by Decision 1999/661/EC (OJ L 261, 7.10.1999, p. 42).

(3) See Annex IV.

## ANNEX I

**MAGNETIC TAPE SPECIFICATION FOR THE DELIVERY TO EUROSTAT OF THE DATA OF THE BASIC SURVEYS OF THE AREAS UNDER VINES**

**(Regulation (EEC) No 357/79)**

**GENERAL PROVISIONS**

<table>
<tbody><tr><td></td><td>I.</td><td>The information recorded in accordance with the characteristics referred to in Article 2 of Regulation (EEC) No 357/79 is to be delivered to Eurostat in the following form by those Member States which process their survey information electronically:<table><tbody><tr><td>1.</td><td>The information shall refer to summaries of holdings if the survey is exhaustive (or to raised summaries of holdings if the survey is based on random sampling) and not to individual holdings.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>2.</td><td>The information shall be delivered on nine-track magnetic tape/1 600 BPI (630 bytes/cm) standard label.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>3.</td><td>The information shall be of fixed record length consisting of 308 positions, and shall be recorded in EBCDIC.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>4.</td><td>The first two fields of each record shall contain information to permit identification. The first field (three positions) identifies the geographical unit, the codification of which is given in the detailed provisions and in Annex II.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>5.</td><td>The second field (two positions) identifies the table in the schedule of tables provided for in Regulation (EEC) No 357/79. The codification of these tables is given in the detailed provisions.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>6.</td><td>The number and size of the fields in each record vary according to the table. If all the 308 positions are not filled in the case of certain tables, the record shall be completed by blanks.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>7.</td><td>The information shall be entered right justified in each field.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>8.</td><td>Surface area data shall be given in hectares to two decimal places with a virtual point.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>9.</td><td>Member States shall have a choice as to blocking factor and Eurostat must be informed as to what blocking factor has been used.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>10.</td><td>The records shall be sorted according to geographical unit, table, and size classes or variety, in that order.</td></tr>
</tbody>
</table>
<table><tbody><tr><td>11.</td><td>Standard administrative procedures governing the transmission of the magnetic tape files to Eurostat shall be established jointly by Eurostat and the Member States.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

<table>
<tbody><tr><td></td><td>II.</td><td>The following pages give for each table and for the various items of a record:<table><tbody><tr><td>(a)</td><td>the codes which are to be used;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(b)</td><td>the maximum number of digits required for the item in question;</td></tr>
</tbody>
</table>
<table><tbody><tr><td>(c)</td><td>the consecutive numbering of the positions for the various items.</td></tr>
</tbody>
</table>
</td></tr>
</tbody>
</table>

**DETAILED PROVISIONS**

The first two fields of each record contain the following information:

<table>
<tbody><tr><td></td><td>Code</td><td>Number of digits</td><td>Byte number on tape</td></tr>
<tr><td><table><tbody><tr><td>1.</td><td>Geographical unit</td></tr>
</tbody>
</table>
</td><td>See Annex II</td><td>3 </td><td>1-3</td></tr>
<tr><td><table><tbody><tr><td>2.</td><td>Tables</td></tr>
</tbody>
</table>
</td><td></td><td>2 </td><td>4-5</td></tr>
<tr><td>1</td><td>10 </td><td></td><td></td></tr>
<tr><td>2.1</td><td>21 </td><td></td><td></td></tr>
<tr><td>2.2</td><td>22 </td><td></td><td></td></tr>
<tr><td>2.3</td><td>23 </td><td></td><td></td></tr>
<tr><td>2.4</td><td>24 </td><td></td><td></td></tr>
<tr><td>2.5</td><td>25 </td><td></td><td></td></tr>
<tr><td>2.6</td><td>26 </td><td></td><td></td></tr>
<tr><td>3</td><td>30 </td><td></td><td></td></tr>
<tr><td>4</td><td>40 </td><td></td><td></td></tr>
<tr><td>5 (1)</td><td>50 </td><td></td><td></td></tr>
</tbody>
</table>

The following list gives the record specifications by tables:

<table>
<tbody><tr><td></td><td>Code</td><td>Number of digits</td><td>Byte number on tape</td></tr>
<tr><td>Table 1</td></tr>
<tr></tr>
<tr><td><table><tbody><tr><td>1.1.</td><td>Size classes of area under vines (ha)</td></tr>
</tbody>
</table>
</td><td></td><td>2 </td><td>6-7</td></tr>
<tr><td>≤ 0·10</td><td>01 </td><td></td><td></td></tr>
<tr><td>0·10 ≤ 0·20</td><td>02 </td><td></td><td></td></tr>
<tr><td>0·20 ≤ 0·30</td><td>03 </td><td></td><td></td></tr>
<tr><td>0·30 ≤ 0·50</td><td>04 </td><td></td><td></td></tr>
<tr><td>0·50 ≤ 1</td><td>05 </td><td></td><td></td></tr>
<tr><td>1 ≤ 2</td><td>06 </td><td></td><td></td></tr>
<tr><td>2 ≤ 3</td><td>07 </td><td></td><td></td></tr>
<tr><td>3 ≤ 5</td><td>08 </td><td></td><td></td></tr>
<tr><td>5 ≤ 10 (b)</td><td>11 </td><td></td><td></td></tr>
<tr><td>10 ≤ 20 (a)(b)</td><td>12 </td><td></td><td></td></tr>
<tr><td>20 ≤ 30 (a)(b)</td><td>13 </td><td></td><td></td></tr>
<tr><td>≥ 30 (a)(b)</td><td>14 </td><td></td><td></td></tr>
<tr><td>≥ 10</td><td>21 </td><td></td><td></td></tr>
<tr><td>≥ 5</td><td>31 </td><td></td><td></td></tr>
<tr><td>All classes</td><td>41 </td><td></td><td></td></tr>
</tbody>
</table>

(a) For the geographical units, the use of a single size class ‘≥ 10 ha’ is optional for France and Italy.

(b) For the geographical units, the use of a single size class ‘≥ 5 ha’ is optional for Germany, Greece and Luxembourg.

<table>
<tbody><tr><td></td><td>Code</td><td>Number of digits</td><td>Byte number on tape</td></tr>
<tr><td>1.2.  Total </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>8-14</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>15-24</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>25-33</td></tr>
<tr><td>1.3.  Wine-grape varieties </td></tr>
<tr></tr>
<tr><td>Total</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>34-40</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>41-50</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>51-59</td></tr>
<tr><td>Quality wines psr</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>60-66</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>67-76</td></tr>
<tr><td>Area</td><td></td><td>9 </td><td>77-85</td></tr>
<tr><td>Other wines</td></tr>
<tr></tr>
<tr><td>Total</td><td></td><td></td><td></td></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>86-92</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>93-102</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>103-111</td></tr>
<tr><td>Of which for spirits</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>112-118</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>119-128</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>129-137</td></tr>
<tr><td>1.4.  Table grapes </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>138-144</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>145-154</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>155-163</td></tr>
<tr><td>1.5.  Planted rootstock for grafting </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>164-170</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>171-180</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>181-189</td></tr>
<tr><td>1.6.  Area for propagation </td></tr>
<tr></tr>
<tr><td>Nurseries</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>190-196</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>197-206</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>207-215</td></tr>
<tr><td>Parent vines</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>216-222</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>223-232</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>233-241</td></tr>
<tr><td>1.7.  Grapes for drying </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>242-248</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>249-258</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>259-267</td></tr>
<tr><td>Table 2 (Tables 2.1 to 2.6)</td></tr>
<tr></tr>
<tr><td><table><tbody><tr><td>2.1.</td><td>Size classes of area under vines (ha) (See Table 1)</td></tr>
</tbody>
</table>
</td><td>See Table 1</td><td>2 </td><td>6-7</td></tr>
<tr><td>2.2.  Total </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>8-14</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>15-24</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>25-33</td></tr>
<tr><td>&gt; 0 ≤ 10</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>34-40</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>41-50</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>51-59</td></tr>
<tr><td>10 ≤ 25</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>60-66</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>67-76</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>77-85</td></tr>
<tr><td>25 ≤ 50</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>86-92</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>93-102</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>103-111</td></tr>
<tr><td>50 ≤ 75</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>112-118</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>119-128</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>129-137</td></tr>
<tr><td>75 ≤ 90</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>138-144</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>145-154</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>155-163</td></tr>
<tr><td>≥ 90</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>164-170</td></tr>
<tr><td>UAA (ha)</td><td></td><td>10 </td><td>171-180</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>181-189</td></tr>
<tr><td>Table 3</td></tr>
<tr></tr>
<tr><td><table><tbody><tr><td>3.1.</td><td>Size classes of area under vines (see Table 1)</td></tr>
</tbody>
</table>
</td><td>See Table 1</td><td>2 </td><td>6-7</td></tr>
<tr><td>3.2.  Total </td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>8-14</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>15-23</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>24-32</td></tr>
<tr><td>0</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>33-39</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>40-48</td></tr>
<tr><td>Quality wines psr (ha) (the value must be 0)</td><td></td><td>9 </td><td>49-57</td></tr>
<tr><td>&gt; 0 ≤ 10</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>58-64</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>65-73</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>74-82</td></tr>
<tr><td>10 ≤ 25</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>83-89</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>90-98</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>99-107</td></tr>
<tr><td>25 ≤ 50</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>108-114</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>115-123</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>124-132</td></tr>
<tr><td>50 ≤ 75</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>133-139</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>140-148</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>149-157</td></tr>
<tr><td>75 ≤ 90</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>158-164</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>165-173</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>174-182</td></tr>
<tr><td>90 ≤ 100</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>183-189</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>190-198</td></tr>
<tr><td>Quality wines psr (ha)</td><td></td><td>9 </td><td>199-207</td></tr>
<tr><td>100</td></tr>
<tr></tr>
<tr><td>Holdings</td><td></td><td>7 </td><td>208-214</td></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>215-223</td></tr>
<tr><td>Quality wines psr (ha) (equals preceding field)</td><td></td><td>9 </td><td>224-232</td></tr>
<tr><td>Table 4</td></tr>
<tr><td>There are three varieties per record; the three varieties have the same structure</td></tr>
<tr><td>4.1.  First variety </td></tr>
<tr></tr>
<tr><td>4.1.1.  Variety </td></tr>
<tr></tr>
<tr><td>The variety codes are given in Annex III</td><td>See Annex III</td><td>4 </td><td>6-9</td></tr>
<tr><td>4.1.2.  Age classes </td></tr>
<tr></tr>
<tr><td>All</td></tr>
<tr></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>10-18</td></tr>
<tr><td>Age class 1</td></tr>
<tr></tr>
<tr><td>Classification</td><td>10 </td><td>2 </td><td>19-20</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>21-29</td></tr>
<tr><td>Age class 2</td></tr>
<tr></tr>
<tr><td>Classification</td><td>20 </td><td>2 </td><td>30-31</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>32-40</td></tr>
<tr><td>Age class 3</td></tr>
<tr></tr>
<tr><td>Classification</td><td>30 </td><td>2 </td><td>41-42</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>43-51</td></tr>
<tr><td>Age class 4</td></tr>
<tr></tr>
<tr><td>Classification</td><td>40 </td><td>2 </td><td>52-53</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>54-62</td></tr>
<tr><td>Age class 5</td></tr>
<tr></tr>
<tr><td>Classification</td><td>41 </td><td>2 </td><td>63-64</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>65-73</td></tr>
<tr><td>Age class 6</td></tr>
<tr></tr>
<tr><td>Classification</td><td>45 </td><td>2 </td><td>74-75</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>76-84</td></tr>
<tr><td>Age class 7</td></tr>
<tr></tr>
<tr><td>Classification</td><td>21 </td><td>2 </td><td>85-86</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>87-95</td></tr>
<tr><td>Age class 8</td></tr>
<tr></tr>
<tr><td>Classification</td><td>22 </td><td>2 </td><td>96-97</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>98-106</td></tr>
<tr><td>4.2.  Second variety </td></tr>
<tr></tr>
<tr><td><table><tbody><tr><td>4.2.1.</td><td>Variety</td></tr>
</tbody>
</table>
</td><td>See Annex III</td><td>4 </td><td>107-110</td></tr>
<tr><td>4.2.2.  Age classes </td></tr>
<tr></tr>
<tr><td>All (ha)</td><td></td><td>9 </td><td>111-119</td></tr>
<tr><td>Age classes 1 to 8</td></tr>
<tr></tr>
<tr><td>Classification</td><td></td><td>8 fields of 2</td><td rowspan="2">120-207</td></tr>
<tr><td>Area (ha)</td><td></td><td>8 fields of 9</td></tr>
<tr><td>4.3.  Third variety </td></tr>
<tr></tr>
<tr><td><table><tbody><tr><td>4.3.1.</td><td>Variety</td></tr>
</tbody>
</table>
</td><td>See Annex III</td><td>4 </td><td>208-211</td></tr>
<tr><td>4.3.2.  Age classes </td></tr>
<tr></tr>
<tr><td>All (ha)</td><td></td><td>9 </td><td>212-220</td></tr>
<tr><td>Age classes 1 to 8</td></tr>
<tr></tr>
<tr><td>Classification</td><td></td><td>8 fields of 2</td><td rowspan="2">221-308</td></tr>
<tr><td>Area (ha)</td><td></td><td>8 fields of 9</td></tr>
</tbody>
</table>

The zones for each variety in the record must always be completed by zeros when all the classes are not used.

If there is only one variety (or two varieties) in the last record, the information relating to the missing variety (varieties) is to be indicated by zeros (bytes 107-308, or 208-308).

<table>
<tbody><tr><td></td><td>Code</td><td>Number of digits</td><td>Byte number on tape</td></tr>
<tr><td>Table 5</td></tr>
<tr></tr>
<tr><td>5.1.  All </td></tr>
<tr></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>6-14</td></tr>
<tr><td>5.2.  Quality wines psr </td></tr>
<tr></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>15-23</td></tr>
<tr><td>Yield class I</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>2 </td><td>24-25</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>26-34</td></tr>
<tr><td>Yield class II</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>2 </td><td>35-36</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>37-45</td></tr>
<tr><td>Yield class III</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>2 </td><td>46-47</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>48-56</td></tr>
<tr><td>Yield class IV</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>2 </td><td>57-58</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>59-67</td></tr>
<tr><td>Yield class V</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>2 </td><td>68-69</td></tr>
<tr><td>Area (ha)</td><td></td><td>9 </td><td>70-78</td></tr>
<tr><td>5.3.  Other wines </td></tr>
<tr></tr>
<tr><td>Total (ha)</td><td></td><td>9 </td><td>79-87</td></tr>
<tr><td>Yield classes I to V</td></tr>
<tr></tr>
<tr><td>Classification (2)</td><td></td><td>5 fields of 2</td><td rowspan="2">88-142</td></tr>
<tr><td>Area (ha)</td><td></td><td>5 fields of 9</td></tr>
</tbody>
</table>

(1) For these tables, it would be desirable for Member States which process their basic survey information electronically to send the information provided for in Article 6(2) of Regulation (EEC) No 357/79 to Eurostat on magnetic tape.

(2) The codes for this yield classification (number and limits) will be established subsequently.

## ANNEX II

**GEOGRAPHICAL UNITS LAID DOWN BY ARTICLE 4(3) OF REGULATION (EEC) No 357/79**

|  | Code |
| --- | --- |
| GERMANY (wine-growing regions) | 100 |
| Ahr | 101 |
| Mittelrhein | 102 |
| Mosel-Saar-Ruwer | 103 |
| Nahe | 104 |
| Rheinhessen | 105 |
| Pfalz | 106 |
| Hessische Bergstraße | 107 |
| Rheingau | 108 |
| Württemberg | 109 |
| Baden | 110 |
| Franken | 111 |
| Saale-Unstrut | 112 |
| Sachsen | 113 |
| GREECE | 600 |
| Ανατολική Μακεδονία, Θράκη | 601 |
| Κεντρική Μακεδονία | 602 |
| Δυτική Μακεδονία | 603 |
| Ήπειρος | 604 |
| Θεσσαλία | 605 |
| Ιόνια Νησιά | 606 |
| Δυτική Ελλάδα | 607 |
| Στερεά Ελλάδα | 608 |
| Αττική | 609 |
| Πελοπόννησος | 610 |
| Βόρειο Αιγαίο | 611 |
| Νότιο Αιγαίο | 612 |
| Κρήτη | 613 |
| SPAIN (provinces or autonomous regions) | 700 |
| Galicia | 701 |
| Principado de Asturias | 702 |
| Cantabria | 703 |
| País Vasco A (Territorio Histórico de Álava) | 704 |
| País Vasco B (Territorios Históricos de Guipúzcoa y Vizcaya) | 705 |
| Navarra | 706 |
| La Rioja | 707 |
| Aragón A (provincia de Zaragoza) | 708 |
| Aragón B (provincias de Huesca y Teruel) | 709 |
| Catalunya A (provincia de Barcelona) | 710 |
| Catalunya B (provincia de Tarragona) | 711 |
| Catalunya C (provincias de Girona y Lleida) | 712 |
| Illes Balears | 713 |
| Castilla y León A (provincia de Burgos) | 714 |
| Castilla y León B (provincia de León) | 715 |
| Castilla y León C (provincia de Valladolid) | 716 |
| Castilla y León D (provincia de Zamora) | 717 |
| Castilla y León E (provincias de Ávila, Palencia, Salamanca, Segovia y Soria) | 718 |
| Comunidad de Madrid | 719 |
| Castilla-La Mancha A (provincia de Albacete) | 720 |
| Castilla-La Mancha B (provincia de Ciudad Real) | 721 |
| Castilla-La Mancha C (provincia de Cuenca) | 722 |
| Castilla-La Mancha D (provincia de Guadalajara) | 723 |
| Castilla-La Mancha E (provincia de Toledo) | 724 |
| Comunidad Valenciana A (provincia de Alicante) | 725 |
| Comunidad Valenciana B (provincia de Castellón) | 726 |
| Comunidad Valenciana C (provincia de Valencia) | 727 |
| Región de Murcia | 728 |
| Extremadura A (provincia de Badajoz) | 729 |
| Extremadura B (provincia de Cáceres) | 730 |
| Andalucía A (provincia de Cádiz) | 731 |
| Andalucía B (provincia de Córdoba) | 732 |
| Andalucía C (provincia de Huelva) | 733 |
| Andalucía D (provincia de Málaga) | 734 |
| Andalucía E (provincias de Almería, Granada, Jaén y Sevilla) | 735 |
| Canarias | 736 |
| FRANCE (departments or groups of departments) | 200 |
| Aude | 201 |
| Gard | 202 |
| Hérault | 203 |
| Lozère | 204 |
| Pyrénées-Orientales | 205 |
| Var | 206 |
| Vaucluse | 207 |
| Bouches-du-Rhône | 208 |
| Gironde | 209 |
| Gers | 210 |
| Charente | 211 |
| Charente-Maritime | 212 |
| Ardèche | 213 |
| Aisne | 214 |
| Seine-et-Marne | 215 |
| Ardenne, Aube, Marne, Haute-Marne | 250 |
| Cher, Eure-et-Loir, Indre, Indre-et-Loire, Loir-et-Cher, Loiret | 251 |
| Côte-d'Or, Nièvre, Saône-et-Loire, Yonne | 252 |
| Meurthe-et-Moselle, Meuse, Moselle, Vosges | 253 |
| Bas-Rhin, Haut-Rhin | 254 |
| Doubs, Jura, Haute-Saône, Territoire-de-Belfort | 255 |
| Loire-Atlantique, Maine-et-Loire, Sarthe, Vendée | 256 |
| Deux-Sèvres, Vienne | 220 |
| Dordogne, Landes, Lot-et-Garonne, Pyrénées-Atlantiques | 221 |
| Ariège, Aveyron, Haute-Garonne, Lot, Hautes-Pyrénées, Tarn, Tarn-et-Garonne | 222 |
| Corrèze, Haute-Vienne | 223 |
| Ain, Drôme, Isère, Loire, Rhône, Savoie, Haute-Savoie | 224 |
| Cantal, Allier, Haute-Loire, Puy-de-Dôme | 257 |
| Alpes-de-Haute-Provence, Hautes-Alpes, Alpes-Maritimes | 225 |
| Corse-du-Sud, Haute-Corse | 258 |
| ITALY (provinces) | 300 |
| Torino | 301 |
| Vercelli | 302 |
| Novara | 303 |
| Cuneo | 304 |
| Asti | 305 |
| Alessandria | 306 |
| Biella | 307 |
| Verbano-Cusio-Ossola | 308 |
| Aosta | 309 |
| Imperia | 310 |
| Savona | 311 |
| Genova | 312 |
| La Spezia | 313 |
| Varese | 314 |
| Como | 315 |
| Sondrio | 316 |
| Milano | 317 |
| Bergamo | 318 |
| Brescia | 319 |
| Pavia | 320 |
| Cremona | 321 |
| Mantova | 322 |
| Lecco | 323 |
| Lodi | 324 |
| Bolzano-Bozen | 325 |
| Trento | 326 |
| Verona | 327 |
| Vicenza | 328 |
| Belluno | 329 |
| Treviso | 330 |
| Venezia | 331 |
| Padova | 332 |
| Rovigo | 333 |
| Pordenone | 334 |
| Udine | 335 |
| Gorizia | 336 |
| Trieste | 337 |
| Piacenza | 338 |
| Parma | 339 |
| Reggio nell'Emilia | 340 |
| Modena | 341 |
| Bologna | 342 |
| Ferrara | 343 |
| Ravenna | 344 |
| Forlì | 345 |
| Rimini | 346 |
| Massa Carrara | 347 |
| Lucca | 348 |
| Pistoia | 349 |
| Firenze | 350 |
| Livorno | 351 |
| Pisa | 352 |
| Arezzo | 353 |
| Siena | 354 |
| Grosseto | 355 |
| Prato | 356 |
| Perugia | 357 |
| Terni | 358 |
| Pesaro e Urbino | 359 |
| Ancona | 360 |
| Macerata | 361 |
| Ascoli Piceno | 362 |
| Viterbo | 363 |
| Rieti | 364 |
| Roma | 365 |
| Latina | 366 |
| Frosinone | 367 |
| Caserta | 368 |
| Benevento | 369 |
| Napoli | 370 |
| Avellino | 371 |
| Salerno | 372 |
| L'Aquila | 373 |
| Teramo | 374 |
| Pescara | 375 |
| Chieti | 376 |
| Campobasso | 377 |
| Isernia | 378 |
| Foggia | 379 |
| Bari | 380 |
| Taranto | 381 |
| Brindisi | 382 |
| Lecce | 383 |
| Potenza | 384 |
| Matera | 385 |
| Cosenza | 386 |
| Catanzaro | 387 |
| Reggio di Calabria | 388 |
| Crotone | 389 |
| Vibo Valentia | 390 |
| Trapani | 391 |
| Palermo | 392 |
| Messina | 393 |
| Agrigento | 394 |
| Caltanissetta | 395 |
| Enna | 396 |
| Catania | 397 |
| Ragusa | 398 |
| Siracusa | 399 |
| Sassari | 400 |
| Nuoro | 401 |
| Cagliari | 402 |
| Oristano | 403 |
| LUXEMBOURG (constitutes a single geographical unit) | 500 |
| AUSTRIA | 900 |
| Burgenland | 901 |
| Niederösterreich | 902 |
| Steiermark | 903 |
| Wien und die anderen Bundesländer | 904 |
| PORTUGAL | 800 |
| Entre Douro e Minho | 801 |
| Trás-os-Montes | 802 |
| Beira Litoral | 803 |
| Beira Interior | 804 |
| Ribatejo e Oeste | 805 |
| Alentejo | 806 |
| Algarve | 807 |
| Região Autónoma dos Açores | 808 |
| Região Autónoma da Madeira | 809 |
| UNITED KINGDOM (constitutes a single geographical unit) | 550 |

## ANNEX III

**CODES FOR SPECIFIED VARIETIES OF WINE GRAPES FOR THE TRANSMISSION TO EUROSTAT OF THE RESULTS OF THE STATISTICAL SURVEYS OF AREAS UNDER VINES**

**(Regulation (EEC) No 357/79)**

| Varieties | Code |
| --- | --- |
| Individual varieties (to be specified) |  |
|  |  |
| Black | 1000 -1799 |
| Total | 1800 |
| White and other colours | 2000 -2799 |
| Total | 2800 |
| Total individual varieties | 3800 |
| Other varieties |  |
|  |  |
| Black | 1900 |
| White and other colours | 2900 |
| Total | 3900 |
| All varieties |  |
|  |  |
| Black | 1999 |
| White and other colours | 2999 |
| Total | 3999 |

## ANNEX IV

**Repealed Decision with its successive amendments**

| Commission Decision 79/491/EEC | (OJ L 129, 28.5.1979, p. 9) |
| --- | --- |
| Commission Decision 85/620/EEC | (OJ L 379, 31.12.1985, p. 1) |
| Commission Decision 96/20/EC | (OJ L 7, 10.1.1996, p. 6) |
| Commission Decision 1999/661/EC | (OJ L 261, 7.10.1999, p. 42) |

## ANNEX V

**CORRELATION TABLE**

| Decision 79/491/EEC | This Decision |
| --- | --- |
| Article 1 | Article 1 |
| Article 2 | Article 2 |
| — | Article 3 |
| Article 3 | Article 4 |
| Annex I | Annex I |
| Annex II | Annex II |
| Annex III | Annex III |
| — | Annex IV |
| — | Annex V |
