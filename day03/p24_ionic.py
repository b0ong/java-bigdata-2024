# file: p24_ionic.py
# desc: 클래스 상속

from p22_carClass import Car

class Ionic(Car): # 상속. Car 클래스를 상속받아 ionic
    __fuelRate = 0.0 # 연비
    
    def setFuelRate(self, rate):
        self.__fuelRate = rate
        
    def getFuelRate(self) -> float:
        return self.__fuelRate
    
    def getCarNum(self) -> str: # 함수 오버라이딩(재정의)
        return f'소중한 제차는{super().getCarNum()} 입닌다.'


myCar = Ionic('23나 2345')
myCar.company = '기아'
myCar.setFuelRate(23.5)
print(myCar)
print(f'내차 연비는 {myCar.getFuelRate()} km/h 입니다')