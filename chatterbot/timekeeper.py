import time


class TimeKeeper(object):
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.pause_time = None
        self.time_paused = 0

    def now(self):
    	if self.pause_time:
    		return self.pause_time
    	else: 
    		return time.time()

    def start(self):
        self.start_time = self.now()

    def pause (self):
    	self.pause_time = self.now()

    def resume (self):
    	self.time_paused += time.time() - self.pause_time
    	self.pause_time = None

    def elapsed(self):
        return self.now() - self.start_time - self.time_paused
