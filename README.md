# RISC-V Single Cycle Processor 
## Supporting RV32I Base Integer Instructions


### Testing the code with Pytest
To maintain and keeping track of the correctness of the implementation, we are using the package Pytest. The testing should be done from the root directory.

To run all pytests, simply write in the terminal:

```$ pytest```

To run a specific test, give the name of the sub directory and the file name:

```$ pytest py_tests\<file name>.py```

To compress the test output to a single line per test, add the following flags at the end:

```$ pytest py_tests\<file name>.py --tb=line```