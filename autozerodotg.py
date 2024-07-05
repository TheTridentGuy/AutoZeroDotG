from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pathlib


class CreationHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".gcode"):
            print(f"Detected creation of gcode file: {event.src_path}")
            f = pathlib.Path(event.src_path)
            f.rename(pathlib.Path(f.parent, "auto0.g"))


observer = Observer()
handler = CreationHandler()


directory = "/Volumes/"
observer.schedule(handler, directory, recursive=True)
observer.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
