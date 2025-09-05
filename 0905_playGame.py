class Human :
    """사람 이름 포함"""
    def __init__(self, name) :
        self.name = name
        self.money = 0
        print(f"{self.name}님 안녕하세요")

class Game :
    def start(self) :
        i = 0
        while i < 5 :
            user = input('가나다라마바사 따라 치세요 : ')
            if user == '가나다라마바사' :
                i +=1
            else :
                print("똑바로 치세요^^")
        return 10000
    
class Slave(Human) :
    '''Human 상속, Game 상관'''
    budget = 10000
    
    def work(self) :
        self.money += Game().start()
        print("돈 얼마나 벌었을까요?^^ 잔액체크로 확인하세요^^")
    
    def fire(self) :
        if self.money > Slave.budget :
            result =  "축하합니다 은퇴하셔도 됩니다!"
            print(result)
        else :
            print(f"잔액 체크 비용 10000원입니다. 기존 잔액은 {self.money}이었지만")
            self.money -= 10000
            print(f"당신의 잔액이 {self.money}원 되었네요^^")
            print("열심히 일해보세요^^")

def main() :
    '''콘솔창에서 게임 열심히 하는 방법'''
    name = input('당신의 이름을 입력하세요 : ')
    player = Slave(name)
    print(f'당신은 {player.budget}원을 초과할 때 까지 돈을 벌고 일하셔야합니다. \n')
    while True :
        user_choice = input('1 : 일하기 \t 2 : 잔액체크하기 [입력] : ')
        if user_choice == '끝' :
            break
        elif user_choice == "1" :
            player.work()
        elif user_choice == "2" :
            player.fire()
            if player.money > player.budget :
                break
        else :
            print("선택지를 잘 고르세요^^")

if __name__ == "__main__" :
    main()