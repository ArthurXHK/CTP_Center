from CTPUserApiStruct import *
import gevent
from multiprocessing import Process
class StrategyCenter(object):
    
    
    def __RegisterCallback(self):
        pass
    def run(self):
        self.__process = Process(target=self.__func, args=())
        self.__process.start()
        
    def RegisterStrategy(self, func):
        self.__func = func
        
    def stop(self):
        self.__process.terminate()



def main():
    pass
if __name__ == '__main__':
    main()
        