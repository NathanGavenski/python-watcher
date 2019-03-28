import sys, logging, time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, params):
        self.params = params

    def on_modified(self, event):
        print('event type: {type}  path : {path}'.format(type=event.event_type, path=event.src_path))
        os.system('clear')
        print('Running {file}...'.format(file=params['-f']))
        os.system('python {path}/{file}'.format(path=params['-d'], file=params['-f']))
        

if __name__ == "__main__":
    params = {}
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    for index, value in enumerate(sys.argv):
        if  index % 2 > 0 and value[0] == '-':
            params[value] = sys.argv[index + 1]

    path = params['-d']
    event_handler = MyHandler(params)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()