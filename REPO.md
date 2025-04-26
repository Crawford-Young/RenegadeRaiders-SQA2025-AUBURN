From this project, we learned a few main lessons.

- We learned that githooks can be extremely helpful for identifying issues at incremental points in the software development process.
In a real world scenario, the speed of development can be highly improved with githooks. Githooks make it so that you don't have to manually run commands before commits, and they can help you catch issues before you push them.

- We learned about how to create workflows which run in github. We learned that we needed to install packages within the github environment that are created for the code to be able to run there. The packages you install locally do not affect what is in the github environment at all. In the yml for the workflow, you need to ensure that packages are installed before running the code so that everything works properly in the github environment.

- We learned about how to manage and create virtual environments using docker. When we were learning how to run our project properly, we found that we needed to copy our files from our local space to our docker image so that the execution reflected the local changes. We also learned that it was neccesary to make sure the neccesary packages were installed in the docker image as well.

- We learned how to effectively manage a project has a team. We made pull requests in many scenarios and had to handle merge conflicts on a few occasions.

Report of Errors Caught by fuzzing tool:
  (screenshots named accordingly)
- fuzzing_failure_1.png: update json paths had no instanceof check to see what kind of data is passed in. This meant a crash could easily occur if a wrong typed object was passed in.

- For the other methods fuzzed, no more bugs were found.

For forensic logging, we logged in 5 locations.

- line 71 in main.py -> shows program starting and location for results
- line 23 in graphtaint.py -> showing all found yaml files
- line 31 in graphtaint.py -> showing that helm string was constructed for particular tuples
- line 643 in scanner.py -> showing that scanner has started running on a directory
- line 745 in scanner.py -> showing that scanner has finished running on a directory

For fuzzing, we fuzzed 5 functions with many different values for each method. We printed the results of each run of each method. We created these functions to perform the fuzzing on the corresponding methods.
    - fuzz_keyMiner()
    - fuzz_getKeyRecursively()
    - fuzz_getValuesRecursively()
    - fuzz_getValsFromKey()
    - fuzz_update_json_paths()  

For git hooks, we copied the format from workshop 8 for most of the githook, and then we also only ran bandit if python files were changed.


