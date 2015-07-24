load Nand2Xor.hdl,
output-file Nand2Xor.out,
compare-to Nand2Xor.cmp,
output-list a b out;

set a 0, set b 0,
eval, output;
set a 0, set b 1,
eval, output;
set a 1, set b 0,
eval, output;
set a 1, set b 1,
eval, output;
