import argparse
import time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def __init__(self, params):
        self.params = params
        self.last_trigger = time.time()

    def on_modified(self, event):
        delta = time.time() - self.last_trigger
        if 'swp' not in event.src_path and delta > self.params.time:
            os.system('clear')
            print(f'Event type: {str(event.event_type).upper()}\nPath : {event.src_path}')
            print(f'Running {self.params.file}...')
            os.system(f'python {self.params.dir}/{self.params.file}')
            self.last_trigger = time.time() 
        

def get_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Args for watching over a file")
    parser.add_argument('-d', '--dir', type=str, help='Dir the file is located')
    parser.add_argument('-f', '--file', type=str, help='File name')
    parser.add_argument('-t', '--time', type=int, default=1, help='Time delta between saves (save processing if constant saving')
    return parser.parse_args()


if __name__ == "__main__":
    params = get_args()

    os.system('clear')
    print(f'Watching over {params.dir}/{params.file}')
    event_handler = MyHandler(params)
    observer = Observer()
    observer.schedule(event_handler, path=params.dir, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
