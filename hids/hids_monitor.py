import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HIDSHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")

    def on_created(self, event):
        print(f"File created: {event.src_path}")

if __name__ == "__main__":
    event_handler = HIDSHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/path/to/important/files', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()