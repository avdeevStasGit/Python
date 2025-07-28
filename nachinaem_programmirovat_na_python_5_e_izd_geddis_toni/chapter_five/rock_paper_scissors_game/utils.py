import rock_paper_scissors

def choiceString(choice):
    if choice == rock_paper_scissors.ROCK:
        return "Камень"
    elif choice == rock_paper_scissors.PAPER:
        return "Бумага"
    elif choice == rock_paper_scissors.SCISSORS:
        return "Ножницы"
    else:
        return "Ошибка"