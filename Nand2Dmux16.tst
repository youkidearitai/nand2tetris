load Nand2Dmux16.hdl,
output-file Nand2Dmux16.out,
compare-to Nand2Dmux16.cmp,
output-list in%B1.16.1 sel a%B1.16.1 b%B1.16.1;

set in %B0000000000000000, set sel 0,
eval, output;

set in %B1111111111111111, set sel 0,
eval, output;

set in %B1111111111111111, set sel 1,
eval, output;
