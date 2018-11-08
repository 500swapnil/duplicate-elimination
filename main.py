import sys
import hash
import btree


if len(sys.argv) < 5:
	print("Input Format : python3 main.py relation, no_attributes, no_blocks, type_of_index (hash/btree)")
	sys.exit(0)

R = sys.argv[1]
n = int(sys.argv[2])
M = int(sys.argv[3])
type_of_index = sys.argv[4]
B = 100

if type_of_index=='hash':
    time_taken = hash.main(R,n,M)
    print(time_taken)

elif type_of_index == 'btree':
    time_taken = btree.main(R,n,M)
    print(time_taken)