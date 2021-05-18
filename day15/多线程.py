import threading
import time

#电脑管家杀毒
class PCmanager(threading.Thread):
    def run(self) -> None:
        for i in range(50):
            time.sleep(0.1)
            print("电脑管家已经杀了",i,"个毒！")


#360管家杀毒
class Manager360(threading.Thread):
    def run(self) -> None:
        for i in range(50):
            time.sleep(0.1)
            print("360管家已经杀了",i,"个毒！")


#运行线程
pc = PCmanager()
manager = Manager360()

pc.start()
manager.start()

























