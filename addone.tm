#adds one to a big-endian number
start > > > start
start 0 0 > right
start 1 1 > all_one
start # 1 < halt
all_one 0 0 > right
all_one 1 1 > all_one
all_one # 0 < clear
right 0 0 > right
right 1 1 > right
right # # < carry
clear > > > put_one
clear 1 0 < clear
put_one 0 1 < halt
carry 0 1 < halt
carry 1 0 < carry
TAPE >1
TAPE >10
TAPE >111111111111111
TAPE >10001
TAPE >101010
TAPE >1100101001011111111111111111111111111
