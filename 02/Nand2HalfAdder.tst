load Nand2HalfAdder.hdl,
output-file Nand2HalfAdder.out,
compare-to Nand2HalfAdder.cmp,
output-list a b carry sum;

set a 0, set b 0,
eval, output;
set a 0, set b 1,
eval, output;
set a 1, set b 0,
eval, output;
set a 1, set b 1,
eval, output;
