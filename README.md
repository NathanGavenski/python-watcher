# python-watcher
I've crated this project to watch over a repo dir and execute a file after modifying anything on that same dir. Its lightweight since it only has watchdog as a dependency. Perhaps in the future, I might implement a setup so we can execute using `python -m`.

## To run this watcher you will need to inform two parameters:
  * **-d** = Folder you want the watcher to look for
  * **-f** = script that you want to run after a file is changed (probably you main.py or something similar)

  ```bash
  python <path_to_python-watcher_dir>/watcher.py -d . -f watcher.py  
  ```

## For dependencies all you need to do is run
```
pip install -r requeirements.txt
```

## Todo
- [ ] create a proper setup
