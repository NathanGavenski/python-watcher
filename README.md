# python-watcher
This is a watcher to rerun scripts after you change them

## To run this watcher you will need to inform two parameters:
  * **-d** => Folder you want the watcher to look for
  * **-f** => script that you want to run after a file is changed (probably you main.py or something similar)

  ```
  python watcher -d . -f watcher.py  
  ```