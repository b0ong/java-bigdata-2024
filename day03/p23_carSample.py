# file: p23_carSample.py
# desc: Car클래스 사용해보기

# from p22_carClass import Car

# myCar = Car() # 클래스를 사용, 객체를 하나 생성 (instance)
# yourCar = Car()


# myCar = Car('226나 2059')
# yourCar = Car('11호 8744')
# # print(myCar)
# # print(yourCar)
# # myCar.__carNum = '226나 2059'       # 더이상 불가
# myCar.company = '현대'
# myCar.fuelType = '가솔린'
# myCar.carType = '하이브리드'
# myCar.color = '흰색'
# myCar.releaseYear = 2019
# # yourCar.__carNum = '11호 8744'
# print(myCar)

# myCar.getColor()
# myCar.start()
# myCar.accel()
# yourCar.start()
# myCar.turnRight()
# myCar.turnLeft()
# myCar.brake()

from p22_carClass import Car

myCar = Car('54라 9538') #클래스를 사용, 객체를 하나 생성(instance)
yourCar = Car('98호 8733')

# print(myCar)
# print(yourCar)
myCar.__carNum = '54라 9538'
myCar.company = '현대자동차'
myCar.fuelType = '가솔린'
myCar.carType = '하이브리드'
myCar.color = '흰색'
myCar.releaseYear =  2018
yourCar.__carNum= '87호 8733'
print(myCar)

myCar.getCarColor()
myCar.start()
myCar.accel()
yourCar.start()
myCar.turnRight()
myCar.turnLeft()
myCar.brake() 