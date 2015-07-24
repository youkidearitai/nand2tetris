load Nand2And16.hdl,
output-file Nand2And16.out,
compare-to Nand2And16.cmp,
output-list a%B1.16.1 b%B1.16.1 out%B1.16.1;

set a %B0000000000000000, set b %B1111111111111111,
eval, output;

set a %B1111111111111111, set b %B0000000000000000,
eval, output;

set a %B1010101010101010, set b %B0101010101010101,
eval, output;

set a %B0011110011000011, set b %B1100001100111100,
eval, output;

set a %B0001001000110100, set b %B1110110111001011,
eval, output;

set a %B1111111111111111, set b %B1111111111111111,
eval, output;
