CC = g++
CCFlags = -c -Wall -std=c++11 -g
Name1= server/server
Name2 = server/dijkstra
Name3 = server/digraph


run: $(Name1) client/client.py
	gnome-terminal -- ./server/server
	python3 client/client.py

clean:
	rm -f $(Name1) $(Name1).o $(Name2).o $(Name3).o inpipe outpipe *.out

