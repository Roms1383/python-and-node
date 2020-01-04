# python-and-node

Demonstrate how to communicate between Python and Node.js

## How to test ?

*  Run `python caller.py` to output the result from `rest.js`
*  Run `node caller.js` to output the result from `rest.py`

## About the files ?

*  `rest.py` and `rest.js` are bare implementation of API call
*  `callable.js` and `callable.py` are the abstraction files to call underlying `rest.py` and `rest.js` respectively, expecting function name and parameter
*  `caller.js` and `caller.py` are the test files to call underlying `callable.py` and `callable.js` respectively, dynamically with parameter

## More informations

A more detailed explanation can be found on [Medium](https://medium.com/@romain.kelifa/python-node-js-communication-a990e56ebc10) !
