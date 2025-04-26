From this project, we learned a few main lessons.

- We learned that githooks can be extremely helpful for identifying issues at incremental points in the software development process.
In a real world scenario, the speed of development can be highly improved with githooks. Githooks make it so that you don't have to manually run commands before commits, and they can help you catch issues before you push them.

- We learned about how to create workflows which run in github. We learned that we needed to install packages within the github environment that are created for the code to be able to run there. The packages you install locally do not affect what is in the github environment at all. In the yml for the workflow, you need to ensure that packages are installed before running the code so that everything works properly in the github environment.

- We learned about how to manage and create virtual environments using docker. When we were learning how to run our project properly, we found that we needed to copy our files from our local space to our docker image so that the execution reflected the local changes. We also learned that it was neccesary to make sure the neccesary packages were installed in the docker image as well.


Report of Errors Caught by fuzzing tool:
  (screenshots named accordingly)
- fuzzing_failure_1.png: update json paths had no instanceof check to see what kind of data is passed in. This meant a crash could easily occur if a wrong typed object was passed in.

- For the other methods fuzzed, no more bugs were found.


