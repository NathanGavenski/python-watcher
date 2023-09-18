# python-watcher
I've crated this project to watch over a repo dir and execute a file after modifying anything on that same dir. 
Its lightweight since it only has watchdog as a dependency. 

## Parameters for running
```
-d or --dir (str, required): 
    Folder you want the watcher to look for changes. Defaults to "."
-f or --file (str, required): 
    Script that you want to run after a file is changed (probably you main.py or something similar)
-t or --time (int, optional):
    Time delay to run again (good when saving constantly). Defaults to 1.
--test (bool, optional):
    If the watcher should run pytest command instead of python. Defaults to False.
--lint (bool, optional):
    If the watcher should run pylint command instead of python. Defaults to False.
--lint_src (str, optional):
    where the linter should be run (so it does not run into unwanted files).
--lint_threshold (float, optional):
    Threshold for Pylint to fail. Defaults to None (no threshold).
```

## To run

Watching and executing a python script:

```bash
# watch changes in the directory "." and execute watcher.py
watcher -d . -f watcher.py

# watch changes only in the file watcher.py
watcher -f watcher.py

# watching and executing pytest
watcher --test

# watching and executing pylint only for "src" directory with a threshold with 90%
watcher --lint --lint_src src --lint_threshold 9
```

## For dependencies all you need to do is run

Install from `PyPi`
```
pip install watcher-cli
```

Or from source:
```
git clone https://github.com/NathanGavenski/python-watcher
cd python-watcher
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
- [x] run pylint
    - [x] to run pylint there has to be a folder to run pylint over
    - [x] fail with some threshold
- [x] Spawn a new process to close if needed (more control over running process)
- [ ] Create documentation
- [x] Create tests
- [ ] Publish
- [ ] Fix pytest not working on GitHub actions
