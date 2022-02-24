with open("my_f.txt", "w", encoding="utf-8") as my_f:
    stop = False

    while not stop:
        cur_str = input('Введите строку, q - окончание ввода: ')
        if cur_str == 'q':
            stop = True
        else:
            for el in cur_str.split(' '):
                my_f.write(el)
                if not stop:
                    my_f.write('\n')





