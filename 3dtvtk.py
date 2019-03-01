from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI

s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
'''r = tvtk.Renderer(background=(0,0,0))
r.add_actor(a)
w = tvtk.RenderWindow(size=(300,300))
w.add_renderer(r)
i = tvtk.RenderWindowInteractor(render_window=w)
i.initialize()
i.start()'''
gui = GUI()
win = ivtk.IVTKWithCrustAndBrowser()
win.open()
win.scene.add_actor(a)

dialog = win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0X00000000))
dialog.show()

gui.start_event_loop()