from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, PatternMatchingEventHandler

start_directory =  "C:\\"


class HandlerFile(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            print("An event has ocurred on directory.")
        else:
            print("An event has ocurred on file.")
        #if event.is_directory:
        #    return None

        if event.event_type == 'created':
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)

    def on_created(self,event):
        filename = Path(event.src_path).name
        print(f"{event.src_path} has been created.")
    # Do things when a file is deleted
    def on_deleted(self,event):
        print(f"{event.src_path} deleted!")

    def on_modified(self,event):
        print(f"{event.src_path} has been modified.")

    def on_moved(self,event):
        print(f"moved {event.src_path} to {event.dest_path}")
             

class HandlerPattern(PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        patterns = ["*.tnd"]
        ignore_patterns = None
        ignore_directories = True
        case_sensitive = False
        PatternMatchingEventHandler.__init__(self, patterns, ignore_patterns, ignore_directories, case_sensitive)
 
    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now
 
    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now
 




class Watcher:
    # Set the directory on watch
    watchDirectory = r"C:\watching"
  
    print(f"watching for changes at {watchDirectory}.")
 
    def __init__(self):
        # Setup the observation for defined directory
        self.observer = Observer()
 
    def run(self):
        event_handler = HandlerPattern()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        # Start it
        self.observer.start()
        try:
            while self.observer.is_alive():
                self.observer.join(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")
 
        self.observer.join()



if __name__ == '__main__':
    w = Watcher()
    w.run()

