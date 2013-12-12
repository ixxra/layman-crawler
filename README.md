#Layman Crawler
##Basic web crawler written in python3

This is a very basic web crawler I wrote in python for my students on numerical Analysis.
This crawler is meant to be an utility which aims to help implement the **pagerank** algorithm as described in [Cleve Moler's book](http://www.mathworks.com/moler/exm/chapters/pagerank.pdf)

###Google Page Rank

the file **network_topology.txt** represents a subset for [www.matematicas.uady.mx](http://www.matematicas.uady.mx) topology in a format suitable to analyze with numpy. The format for the file is

* First line: A space separated list of urls.
* Next lines: a square matrix representing the network connectivity.

Each row is a space separated list of `0` and `1` representing `true` of `false` according to wether site `j` contains a link to site `i`. If such a link exists, it is assumed that in the matrix it is represented by the entry `(i, j)`.
