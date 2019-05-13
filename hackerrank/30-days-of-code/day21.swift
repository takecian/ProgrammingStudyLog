# https://www.hackerrank.com/challenges/30-generics/problem

import Foundation

struct Printer<T> {
	/**
	*    Name: printArray
	*    Print each element of the generic array on a new line. Do not return anything.
	*    @param A generic array
	**/

	// Write your code here
	func printArray(array: [T]) {
        for t in param {
    	    print(t)
        }
	}

}

