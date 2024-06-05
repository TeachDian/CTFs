import sys

primes = []
with open("primes1.txt") as file:
    for line in file:
        primes += [int(num) for num in line.split()]
        
print('\n'.join([str(p) for p in primes[int(sys.argv[1]):int(sys.argv[2])]]))
file = open("primes", "w")
file.write('\n'.join([str(p) for p in primes[int(sys.argv[1]):int(sys.argv[2])]])+'\n')
file.close()
