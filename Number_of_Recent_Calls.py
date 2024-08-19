import queue

class RecentCounter:

    def __init__(self):
        #queue allows for easy popping at front because time can only increase and we will only pop from the front
        self.pings = queue.Queue()

    def ping(self, t: int) -> int:
        while not self.pings.empty() and self.pings.queue[0] < t - 3000:
            self.pings.get()
        self.pings.put(t)
        return self.pings.qsize()