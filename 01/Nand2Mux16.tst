load Nand2Mux16.hdl,
output-file Nand2Mux16.out,
compare-to Nand2Mux16.cmp,
output-list a%B1.16.1 b%B1.16.1 sel out%B1.16.1;

set a %B0000000000000000, set b %B1111111111111111, set sel 0,
eval, output;

set a %B0000000000000000, set b %B1111111111111111, set sel 1,
eval, output;

set a %B1111111111111111, set b %B0000000000000000, set sel 0,
eval, output;

set a %B1111111111111111, set b %B0000000000000000, set sel 1,
eval, output;

set a %B1010101010101010, set b %B0101010101010101, set sel 0,
eval, output;

set a %B1010101010101010, set b %B0101010101010101, set sel 1,
eval, output;

set a %B0011110011000011, set b %B1100001100111100, set sel 0,
eval, output;

set a %B0011110011000011, set b %B1100001100111100, set sel 1,
eval, output;

set a %B0001001000110100, set b %B1110110111001011, set sel 0,
eval, output;

set a %B0001001000110100, set b %B1110110111001011, set sel 1,
eval, output;
