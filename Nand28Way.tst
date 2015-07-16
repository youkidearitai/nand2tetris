load Nand2Or8Way.hdl,
output-file Nand2Or8Way.out,
compare-to Nand2Or8Way.cmp,
output-list in sel a b;

set in 0, set sel 0,
eval, output;
set in 0, set sel 1,
eval, output;
set in 1, set sel 0,
eval, output;
set in 1, set sel 1,
eval, output;
