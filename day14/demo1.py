#老手机类
class Oidphone:
    __name = None

    def setOidphone(self,name):
        self.__name = name
    def getOidphone(self):
        return self.__name

    def ringup(self,phone):
        print("正在给",phone,"打电话...")

#新手机类
class Newphone(Oidphone):

    def ringup(self,phone):
        print("语音拨号中...")
        super().ringup(phone)

    def call(self):
        print("品牌为：",self.getOidphone(),"的手机很好用...")

new = Newphone()
new.setOidphone("🍎")
new.ringup("🍐")
new.call()





























