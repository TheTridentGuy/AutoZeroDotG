#! /usr/bin/python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pathlib


class ModificationHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".gcode"):
            f = pathlib.Path(event.src_path)
            try:
                f.rename(pathlib.Path(f.parent, "auto0.g"))
            except FileNotFoundError:
                pass  # we probably detected our own modifications


observer = Observer()
handler = ModificationHandler()


directory = "/Volumes/"
observer.schedule(handler, directory, recursive=True)
observer.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
