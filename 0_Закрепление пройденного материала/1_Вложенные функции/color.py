def color() -> None:
    g = 'green'

    def grey() -> None:
        global g
        g = 'grey'
        print(g)

    grey()
    print(g)


color()