#Collatz conjecture for turing machines
#uses little endian numbers to simplify programming
start > > R start
start 0 0 R fetch # Even numbers should be divided by two
start 1 1 R checkspace
start # # R halt
checkspace # # L halt
checkspace 0 0 L m3carry1
checkspace 1 1 L m3carry1
fetch2 0 0 R fetch
fetch2 1 1 R fetch
fetch2 # # R fetch
fetch 0 0 L put0
fetch 1 1 L put1
fetch # # L putspace
put0 0 0 R fetch2
put0 1 0 R fetch2
put1 0 1 R fetch2
put1 1 1 R fetch2
putspace 0 # L return
putspace 1 # L return
putspace # # L return
return > > R start
return 0 0 L return
return 1 1 L return
m3carry2 # 0 R m3carry1
m3carry2 0 0 R m3carry1
m3carry2 1 1 R m3carry2
m3carry1 # 1 L return
m3carry1 0 1 R m3carry0
m3carry1 1 0 R m3carry2
m3carry0 # # L return
m3carry0 0 0 R m3carry0
m3carry0 1 1 R m3carry1
TAPE >11
TAPE >010101
TAPE >10001
TAPE >11011
#TAPE >10101010000101010101010101101001110010101001101000011111
