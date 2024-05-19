import time
from watchdog.observers import Observer
from watchdog.events import *
from library import *
from file_mover import FileMover
from directory_creator import DirectoryCreator

create_directory = DirectoryCreator()
move_files = FileMover()


# Honestly probably going to rebuild this code here from scratch next time I open this project...



# Here we will create the event handler.
class CreateAndMove(FileSystemEventHandler):

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, sorting_directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop
            print("Something went wrong.")


class Handler(FileSystemEventHandler):
    
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        print("Something happened.")
        create_directory.create_directory()

        time.sleep(2)
        move_files.file_mover_commit()




if __name__ == "__main__":
    watch = CreateAndMove()
    watch.run()
#     path = sorting_directory
#     logging.info(f'start watching directory {path!r}')
#     event_handler = CreateAndMove()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while observer.is_alive():
#             observer.join(1)
#     finally:
#         observer.stop()
#         observer.join()



    #     self.commit_create()
    #     time.sleep(2)
    #     self.commit_move



