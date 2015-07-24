load Nand2Or8Way.hdl,
output-file Nand2Or8Way.out,
compare-to Nand2Or8Way.cmp,
output-list in%B1.8.1 out;

set in %B00000000,
eval, output;

set in %B11111111,
eval, output;

set in %B00000100,
eval, output;
