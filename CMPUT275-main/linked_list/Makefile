CC = g++
Flag = -c -Wall -std=c++11
Name = listtest

twin_primes: $(Name).o
	$(CC) -o $(Name) $(Name).o

twin_primes.o: $(Name).cpp
	$(CC) $(Flag) $(Name).cpp

clean:
	rm -f $(Name).o $(Name) *.out