def card_cony(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('  +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} ... {x % r}')
        else:
            print(f' {x // r:{n}d} ... {x % r}')
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.:'))
            if no > 0:
                break

        while True:
            cd = int(input('어떤 진수로 변환할까요?:'))

            if 2 <= cd <= 36:
                break
            else:
                print("2~36 사이 숫자만 입력할 수 있습니다.")

        print(f'{no}를 {cd}진수로 변환하면 {card_cony(no, cd)} 입니다.')

        retry = input("한 번 더 변환할까요?(Y .... 예 / N... 아니요 ) :")
        if retry in {'N', 'n'}:
            break
