load Nand2Mux4Way16.hdl,
output-file Nand2Mux4Way16.out,
compare-to Nand2Mux4Way16.cmp,
output-list a%B1.16.1 b%B1.16.1 c%B1.16.1 d%B1.16.1 sel%B1.2.1 out%B1.16.1;

set a %B1111000000000000, set b %B0000000000000000, set c %B0000000000000000, set d %B0000000000000000, set sel %B00,
eval, output;

set a %B0000000000000000, set b %B1111000000000000, set c %B0000000000000000, set d %B0000000000000000, set sel %B01,
eval, output;

set a %B0000000000000000, set b %B0000000000000000, set c %B1111000000000000, set d %B0000000000000000, set sel %B10,
eval, output;

set a %B0000000000000000, set b %B0000000000000000, set c %B0000000000000000, set d %B1111000000000000, set sel %B11,
eval, output;
