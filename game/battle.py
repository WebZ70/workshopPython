from classes import Warrior as War
import random


def battle():
    list_of_war = [War('Arthas', 3), War('Uther', 3), War('Jaina', 3)]

    print('\t\t Бой скоро начнется! Готовтесь!')
    print('На поле боя:')
    for challenger in list_of_war:
        print('\t%s с атакой равной %d' % (challenger.name, challenger.attack))

    print('\n\t\t В бой!\n')
    print('========== Журнал боя ==========')
    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].get_hit(list_of_war[r2])
        if list_of_war[r1].check_death():
            del list_of_war[r1]
    print('================================')
    print('\n\t\t Бой окончен!')
    print('\tПобеждает %s!' % list_of_war.pop().name)
