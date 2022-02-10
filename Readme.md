# Welcome to Algopyformance

A library created to aid students of ISCTE-IUL, in Portugal, to build performance 
tests for their app. This is the first version, so it is very limited and the 
plotting functionality is not as functional as I wish but improvements are 
comming soon. I am open to suggestions of features I can add and improvements to my code.

The library uses the Builder pattern to offer a simple and easy to use API to 
build performance tests. It uses pandas to store the results of the tests, 
Seaborn to plot the results and matplotlib to show the plot. To build a test you 
just need to excute 
the following 
steps:
1. Import the <b>TestStackBuilder</b> from the tests module 
2. Add <b>targets</b> which are functions that you want to execute during the 
   test (you can add multiple but keep in mind that they should contain the 
   same parameters)
3. <b>(Optional)</b> If you want to repeat the test multiple times use the 
   <b>repeat</b> 
method to pass the number of repetitions
4. <b>(Optional)</b> If you want to let the TestStackBuilder plot your data you 
   can 
add the flag to the builder using the <b>do_show_plot</b>. Keep in mind that 
   this feature doesn't work very well and 
5. Use <b>build</b> to generated a <b>TestStack</b>
6. Finally, run the test using the <b>run</b> method 
7. <b>(Optional)</b> if the plot representation doesn't suit you you can use 
   the output of the run method which is a dataframe of results from the tests 
   to build your own plot using Seaborn or Matplotlib.

The steps described above are exemplified in the code below
```Python
from sp_algopyformancelib.tests import TestStackBuilder

new_stack = TestStackBuilder()\
        .add_target(my_func_recur)\
        .add_target(my_func_iter)\
        .add_param_combinations([(x,) for x in range(20, 51, 5)])\
        .do_show_plot()\
        .build()

results = new_stack.run()

print(results)
```

<br>
<br>
<br>
<br>
<br>
Copyright © 2022 Stefan Postolache

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.