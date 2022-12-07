import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    with open(f'{path}{os.sep}strat.txt') as s:
        strat = s.readlines()

    wrongScore = 0
    rightScore = 0

    for round in strat:
        o, m = round.split()
        wrongScore = wrongScore + result(o, m, wrong=True)
        rightScore = rightScore + result(o, m, wrong=False)

    print(f'Wrong score result was: {wrongScore}')
    print(f'Right score result was: {rightScore}')

def result(opp, me, wrong):
    winningThrow = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    losingThrow = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    scoring = {
        'A': 1,
        'B': 2,
        'C': 3,
        'win': 6,
        'lose': 0,
        'draw': 3
    }

    if wrong:
        translate = {
            'X': 'A',
            'Y': 'B',
            'Z': 'C'
        }
        me = translate.get(me)
        if opp == me:
            res = 'draw'
        elif winningThrow.get(opp) == me:
            res = 'win'
        else:
            res = 'lose'
    else:
        translate = {
            'X': 'lose',
            'Y': 'draw',
            'Z': 'win'
        }

        res = translate.get(me)

        if res == 'draw':
            me = opp
        elif res == 'win':
            me = winningThrow.get(opp)
        else:
            me = losingThrow.get(opp)


    return scoring.get(me) + scoring.get(res)

if __name__ == "__main__":
    main()