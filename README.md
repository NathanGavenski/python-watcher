# python-watcher
I've crated this project to watch over a repo dir and execute a file after modifying anything on that same dir. 
Its lightweight since it only has watchdog as a dependency. 
Perhaps in the future, I might implement a setup so we can execute direct from the command line.

## To run this watcher you will need to inform two parameters:
```
-d or --dir (required): 
    Folder you want the watcher to look for changes
-f or --file (required): 
    Script that you want to run after a file is changed (probably you main.py or something similar)
-t or --time (optional):
    Time delay to run again (good when saving constantly)
--test (optional):
    If the watcher should run a pytest command instead of python
```

```bash
python -m watcher -d . -f watcher.py  
```

## For dependencies all you need to do is run
```
pip install -e .
```

## Todo
- [x] create a proper setup
- [ ] make it executable from command line
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
