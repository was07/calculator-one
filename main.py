import os
import colorama


class Calc:
    def __init__(self, inp, res):
        self.inp = str(inp).strip()
        self.res = str(res).strip()
    
    def as_text(self):
        return f"{self.inp.ljust(25)} {colorama.Fore.LIGHTBLACK_EX}= {colorama.Fore.CYAN}{self.res.rjust(9)}{colorama.Style.RESET_ALL}"


class Calculator:
    def __init__(self):
        self.reses: list[Calc] = []
        self.mainloop()
    
    def mainloop(self):
        while True:
            self.show()

    def show(self):
        os.system("cls")
        width = 41
        sep = '─' * (width - 2)
        print('╭' + sep + '╮')

        fillers = 11 - len(self.reses)
        print('\n'.join([('│' + ' ' * (width - 2) + '│')] * fillers))
        if self.reses:
            if len(self.reses) > 1:
                print('\n'.join(
                    ['│ ' + c.as_text() + ' │' for c in self.reses[:-1]]
                ))
            print('├' + sep + '┤')
            print('│ ' + self.reses[-1].as_text() + ' │')
        else:
            print('├' + sep + '┤')

        print('╰' + sep + '╯')
        try:
            inp = input( colorama.Fore.CYAN + ': ' + colorama.Fore.BLUE)
        except KeyboardInterrupt:
            print(colorama.Fore.RED + "Quitted" + colorama.Style.RESET_ALL)
            exit()
        print(colorama.Style.RESET_ALL)

        if inp.strip() == 'q':
            exit()
        elif inp.strip() == 'clr':
            self.reses.clear()
            return

        self.calculate(inp)
    
    def add(self, inp, res):
        self.reses.append(
            Calc(inp, res)
        )
        if len(self.reses) > 11:
            self.reses = self.reses[-11:]
    
    def _replace_operators(self, op):
        return {'+': '+', '-': '-', '*': '×', '/': '/', '^': '^'}[op]
    
    def calculate(self, raw_inp: str) -> int:
        if not raw_inp: return 1
        parts = []
        temp = ""
        for c in raw_inp:
            if c in ('+', '-', '*', '/', '^'):
                if temp: parts.append(temp.strip())
                else: return 1
                parts.append(self._replace_operators(c))
                temp = ""
            elif c not in '1234567890. ':
                return 1
            elif c:
                temp += c
        if temp: parts.append(temp.strip())
        
        try:
            res = eval(raw_inp)
        except:
            return 1

        self.add(' '.join(parts), str(res))
        return 0


if __name__ == '__main__':
    os.system('cls')
    print(f"""    {colorama.Fore.RED}Controls{colorama.Style.RESET_ALL}

    {colorama.Fore.CYAN}: q{colorama.Style.RESET_ALL}     -> exit
    {colorama.Fore.CYAN}: clr{colorama.Style.RESET_ALL}   -> clear history

    {colorama.Fore.RED}Press enter to continue{colorama.Style.RESET_ALL}
    """)
    i = input()
    if i == 'q': exit()
    Calculator()
