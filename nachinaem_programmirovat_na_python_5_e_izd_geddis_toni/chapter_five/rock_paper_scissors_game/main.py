import computer_choice
import utils
import player_choice
import rock_paper_scissors

def main():
    result = rock_paper_scissors.TIE

    while result == rock_paper_scissors.TIE:
        computer = computer_choice.choiceInt()
        player = player_choice.choiceInt()
        print("Компьютер выбрал: ", utils.choiceString(computer))
        print("Игрок выбрал: ", utils.choiceString(player))

        result = rock_paper_scissors.rockPaperScissors(player, computer)

        if result == rock_paper_scissors.TIE:
            print('Вы сделали тот же выбор, что и компьютер. Попробуем еще раз')

    if (result == rock_paper_scissors.COMPUTER_WINS):
        print ('Компьютер победил')
    elif result == rock_paper_scissors.PLAYER_WINS:
        print ('Вы победили')
    else:
        print ('Вы сделали недопустимый выбор. Победителя нет')

main()
