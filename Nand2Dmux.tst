load Nand2Dmux.hdl,
output-file Nand2Dmux.out,
compare-to Nand2Dmux.cmp,
output-list in sel a b;

set in 0, set sel 0,
eval, output;
set in 0, set sel 1,
eval, output;
set in 1, set sel 0,
eval, output;
set in 1, set sel 1,
eval, output;
