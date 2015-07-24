load Nand2DMux4Way.hdl,
output-file Nand2DMux4Way.out,
compare-to Nand2DMux4Way.cmp,
output-list in sel%B1.2.1 a b c d;

set in 1, set sel %B00,
eval, output;

set in 1, set sel %B01,
eval, output;

set in 1, set sel %B10,
eval, output;

set in 1, set sel %B11,
eval, output;
