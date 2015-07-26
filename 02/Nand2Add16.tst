load Nand2Add16.hdl,
output-file Nand2Add16.out,
compare-to Nand2Add16.cmp,
output-list a%B1.16.1 b%B1.16.1 out%B1.16.1;

set a %B0000000000000000, set b %B0000000000000000,
eval, output;
set a %B0000000000000001, set b %B0000000000000010,
eval, output;
set a %B0000000000000011, set b %B0000000000000010,
eval, output;
set a %B0111111111111111, set b %B0000000000000001,
eval, output;
