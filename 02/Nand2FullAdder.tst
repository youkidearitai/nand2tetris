load Nand2FullAdder.hdl,
output-file Nand2FullAdder.out,
compare-to Nand2FullAdder.cmp,
output-list a b c carry sum;

set a 0, set b 0, set c 0,
eval, output;
set a 0, set b 0, set c 1,
eval, output;
set a 0, set b 1, set c 0,
eval, output;
set a 0, set b 1, set c 1,
eval, output;

set a 1, set b 0, set c 0,
eval, output;
set a 1, set b 0, set c 1,
eval, output;
set a 1, set b 1, set c 0,
eval, output;
set a 1, set b 1, set c 1,
eval, output;

