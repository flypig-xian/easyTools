#-*- coding:utf-8 -*-
from pymouse import PyMouse
from threading import Thread
import time,pythoncom, pyHook
def OnKeyboardEvent(event):
  print(event.Key)
  if("Space" == event.Key):
    print("enter Space!")
    #True开始运行新线程 
    task = threadPlayTask()
    t = Thread(target=task.run,args=[15,])
    t.start()
    #反之，开始终止线程运行  
  if("F7" == event.Key): 
    print("Thread killed!")
    t.terminate()
    
class threadPlayTask:
  def __init__(self):
    self.testHandle = autoPlay()
    self.running = True
  def run(self,nums):
    while(self.running and nums):
      self.testHandle.autoClick()
      nums = nums - 1
      
  def terminate(self):
    self.running = False
class autoPlay:
  def __init__(self):
    self.m = PyMouse()
  def autoClick(self):
      self.x,self.y = self.m.position()
      self.m.click(self.x,self.y)
      time.sleep(0.1)

if __name__ == '__main__':
  hm = pyHook.HookManager()
  # watch for all mouse events
  hm.KeyDown = OnKeyboardEvent
  # set the hook
  hm.HookKeyboard()
  # wait forever
  pythoncom.PumpMessages()

  #testHandle = autoPlay()
  #testHandle.autoClicks()