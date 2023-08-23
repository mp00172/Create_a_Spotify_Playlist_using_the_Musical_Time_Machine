from gui import Gui
import config


program = Gui()
program.authenticate_with_spotify()
program.create_main_window(
    size=config.MAIN_WINDOW_SIZE,
    title=config.MAIN_WINDOW_TITLE
)
program.create_labelframe_upper()
program.fill_labelframme_upper()

program.main_window.mainloop()