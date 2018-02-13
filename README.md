- This program designed to be dynamic where programmer can configure and change the processing
depend on data format and specifications, the program make use itreator and strategy behavioral patterns to
identify common communication patterns between objects.

- unittest is employed to test the functionality of each package.


## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── donation-analytics.py
    │   └── Analytic	;donor analytic package
    │   	└── Contributor	;donor package
    │   	└── Percentile	;percentil package
    │   	└── Reader	;general purpose package use itreator to read input file, use strategy pattern for tokenize data recods	
    │   	└── Tokenizer	;implement tokenizer algorithms
    │   	└── Validator	;implement validator algorithms
    │   	└── Writer	;general purpose output file writer 
    ├── input
    │   └── percentile.txt
    │   └── itcont.txt
    ├── output
    |   └── repeat_donors.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── percentile.txt
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── repeat_donors.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── repeat_donors.txt

