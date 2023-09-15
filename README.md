# python-watcher
I've crated this project to watch over a repo dir and execute a file after modifying anything on that same dir. 
Its lightweight since it only has watchdog as a dependency. 

## Parameters for running
```
-d or --dir (required): 
    Folder you want the watcher to look for changes. Defaults to "."
-f or --file (required): 
    Script that you want to run after a file is changed (probably you main.py or something similar)
-t or --time (optional):
    Time delay to run again (good when saving constantly). Defaults to 1.
--test (optional):
    If the watcher should run a pytest command instead of python. Defaults to False.
```

## To run

Watching and executing a python script:
```bash
watcher -d . -f watcher.py  
```
Watching and executing pytest
```
watcher --test
```


## For dependencies all you need to do is run
```
pip install -e .
```

## Use cases
Although trivial, there are some uses cases that made me create this package:

* Run pytest when saving a file.
* Run pylint when making corrections.
* Run smaller scripts after every modification.

Mostly I was tired off having to tab out from vim just to run pytest/pylint/python on the terminal.

## Todo
- [x] create a proper setup
- [x] make it executable from command line
- [ ] be able to pass parameters
- [ ] read parameters from yaml file
- [x] only watch a single file changes
- [x] run pytest
- [ ] run pylint
    - [ ] to run pylint there has to be a folder to run pylint over
    - [ ] fail with some threshold
- [ ] Spawn a new process to close if needed (more control over running process)
- [ ] Create documentation
- [x] Create tests
- [ ] Publish
- [ ] Fix pytest not working on GitHub actions
