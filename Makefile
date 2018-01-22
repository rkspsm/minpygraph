
all : _cgraph.so

_cgraph.so : cgraph.cpp
	g++ -fPIC -shared -std=c++17 -Wno-write-strings `pkg-config --cflags --libs libcgraph` -o _cgraph.so cgraph.cpp

demo : demo.png

demo.png : demo.gv
	dot -Tpng demo.gv >demo.png

demo.gv : _cgraph.so demo.py
	python3 demo.py

clean :
	rm -f _cgraph.so demo.gv demo.png

