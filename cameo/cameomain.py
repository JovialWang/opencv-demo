'''
Created on 2017年8月8日

@author: wangjuewei
'''
import cv2
from cameo import filters
from cameo.managers import WindowManager, CaptrueManager

class Cameo(object):
    
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptrueManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.FindEdgesFilter()
        
    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            
            # TODO: Filter the frame
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
            
    
    def onKeypress(self, keycode):
        """Handle a keypress.
                  
        space  -> Take a screenshot.
        tab    -> Start/top recording a screencast.
        escape -> Quit
        
        """
        if keycode == 32: # space
            self._captureManager.writeImage('/Users/wangjuewei/Desktop/screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('/Users/wangjuewei/Desktop/screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()
            
if __name__=="__main__":
    Cameo().run()
        
        