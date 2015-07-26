load Nand2Inc16.hdl,
output-file Nand2Inc16.out,
compare-to Nand2Inc16.cmp,
output-list in%B1.16.1 out%B1.16.1;

set in %B0000000000000000,
eval, output;
set in %B0000000000000001,
eval, output;
set in %B0000000000000011,
eval, output;
set in %B0111111111111111,
eval, output;
