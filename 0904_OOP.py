class Vehicle :
    """자동차 대표 클래스"""
    Vehicle_num = 0 # 전체 instance 개수를 체크하는 스태틱 변수
    def __init__(self, color : str, engine : str, fuel : int) :
        self.color = color
        self.engine = engine
        Vehicle.Vehicle_num +=1
    
    def __str__(self) :
        return f"{self.color}색 {self.engine} 성능 자동차"

my_car = Vehicle('red','v4',200)
print(my_car)
print(my_car.car_num)
print(Vehicle.car_num)

class SportsCar(Vehicle) :
    ''' 
    Car 클래스를 상속받아서 SportsCar를 구현
    '''
    def __init__(self, color:str, engine:str, fuel : int) :
        self.color = color
        self.engine = engine
        self.fuel = fuel
        self.types = "스포츠카"
        self.engine_state = False
        Vehicle.Vehicle_num +=1
    
    def engine_start(self) :
        self.engine_state = True
        return f"{self.types} 시동 {self.fuel} 남음"
    
    def run(self, fuel_using : int) :
        if self.engine_state == True :
            self.fuel = self.fuel - fuel_using
            return f"{self.fuel}사용, 연비까지 대입하면 얼마나 이동했는 지 알 수 있습니다."
        else :
            return "시동 먼저 키세요 : engine_start() 함수 활용"
    
    def engine_off(self) :
        if self.engine_state == True :
            self.engine_state = False
            return f"{self.fuel} 리터 남은 {self.types} 정지"
        else :
            return "시동이 켜진 적 없습니다"
    
my_sportscar = SportsCar('red','v8',200)
print(my_sportscar)
print(my_sportscar.engine_start())
print(my_sportscar.run(45))
print(my_sportscar.engine_off())
print(my_sportscar.run(45))
print(my_sportscar.engine_off())
print(Vehicle.car_num)
print(my_sportscar.car_num)