CXX=g++

all: syncer

syncer: main.o dirs.o compare.o
	g++ -o syncer main.o dirs.o compare.o

dirs.o: include/dirs.hpp src/dirs.cpp
	g++ -c -g src/dirs.cpp

compare.o: include/compare.hpp src/compare.cpp
	g++ -c -g src/compare.cpp

main.o: src/main.cpp
	g++ -c -g src/main.cpp

