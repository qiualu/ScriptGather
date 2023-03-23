from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if button == button.left:
        if pressed:
            print('Left mouse button pressed at ({0}, {1})'.format(x, y))
        else:
            print('Left mouse button released at ({0}, {1})'.format(x, y))

with Listener(on_click=on_click) as listener:
    listener.join()
