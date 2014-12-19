#Description 

This is a python 3 implementation of a 
[Locality Sensitive Hashing (LSH)](http://en.wikipedia.org/wiki/Locality-sensitive_hashingscheme)
that makes use of the 
[Goemans-Williamson SDP rounding](http://en.wikipedia.org/wiki/Semidefinite_programming#Example_3_.28Goemans-Williamson_MAX_CUT_approximation_algorithm.29)
 technique for approximating MAXCUT. A LSH scheme maps "close" strings to the same 
bucket. The notion of closeness depends on the way the data is mapped to
vectors (for instance the characteristic vector if it is a text, or the 
frequency vector). The Goemans-Williamson rounding technique samples a n-variate
Gaussian x (n being the dimension of the data) and rounds the data vector v to 1
if <v,x> >= 0 and to 0 otherwise. Here we map an n-bit vector to a log^2(n) bit vector
with the probability of collision being:

```
	(1-a/\pi)^{(log n)^2} 

```

where a is the angle between the two vectors. Note that if the machine precision is k

(typically a constant in n) then the probability of collision is atleast

```

	(1-1/(2^k*\pi))^{(log n)^2}

```
which is asymptotically inverse super-polynomial in n.

#Usage

* The ** convert_text.py ** file converts a text file to its frequency vector and writes to a file named * data *

* The ** generate_example.py ** file generates a random collection of vectors to be hashed. One can specify the dimension
of the data and the number of data points.

* The ** hash.py ** file uses this hashing scheme to hash it to a file of your choosing. It also outputs the number
of collisions observed. 

A sample data file is also included in the repository. 

# Reference

 http://www.cs.princeton.edu/courses/archive/spring04/cos598B/bib/CharikarEstim.pdf 
