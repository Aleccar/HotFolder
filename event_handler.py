import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import *
from hot_folder_library import files_in_directory
from hot_folder_library import sorting_directory
from hot_folder_library import sorting_dict
from file_mover import FileMover
from directory_creator import DirectoryCreator

create_directory = DirectoryCreator()
move_files = FileMover()


class AnyEventHandler(FileSystemEventHandler):
    
    def dispatch(self, event: FileSystemEvent) -> None:
        """Dispatches events to the appropriate methods.

        :param event:
            The event object representing the file system event.
        :type event:
            :class:`FileSystemEvent`
        """
        self.on_any_event(event)
        {
            EVENT_TYPE_CREATED: self.on_created,
            EVENT_TYPE_DELETED: self.on_deleted,
            EVENT_TYPE_MODIFIED: self.on_modified,
            EVENT_TYPE_MOVED: self.on_moved,
            EVENT_TYPE_CLOSED: self.on_closed,
            EVENT_TYPE_OPENED: self.on_opened,
        }[event.event_type](event)

    def commit_create(self, event):
        if event.is_directory:
            return None
        else:
            create_directory.create_directory()

# class EventMove(LoggingEventHandler):
#     def commit_move(self, event):
#         if event.is_directory:
#             return None
#         else:
#             time.sleep(2)
#             move_files.file_mover_0commit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sorting_directory
    logging.info(f'start watching directory {path!r}')
    event_handler = AnyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


