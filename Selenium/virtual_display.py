#!/usr/bin/env python

from pyvirtualdisplay import Display

def virtual_display(status="start"):
    """Displai virtual

    Args:
        status (str, optional): "start", "stop". Defaults to "start".
    """
    if status == "start":
        # You will not see the browser.
        display = Display(visible=0, size=(800, 600))
        display.start()
    elif status == "stop":
        display.stop()



