"""import wx
def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

def area(heigth,width):
    return heigth * width

app = wx.App()
win = wx.Frame(None,title='Simple Editor',size=(410,335))
#win.Show()
loadButton = wx.Button(win,label='Open',pos=(225,5),size=(80,25))
loadButton.Bind(wx.EVT_BUTTON,load)

saveButton = wx.Button(win,label='Save',pos=(315,5),size=(80,25))
saveButton.Bind(wx.EVT_BUTTON,save)
filename = wx.TextCtrl(win,pos=(5,5),size=(210,25))
contents = wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE | wx.HSCROLL)
win.Show()
app.MainLoop()"""

import random, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()

result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def task_q():
    return task_queue

def result_q():
    return result_queue

QueueManager.register('get_task_queue',callable=task_q)
QueueManager.register('get_result_queue',callable=result_q)

manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')

if __name__ == '__main__':
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0,10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result:%s' % r)

    manager.shutdown()
    print('master exit.')



