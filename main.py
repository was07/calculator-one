import os
import colorama as clr


class SavedCalculation:
    def __init__(self, inp, res):
        self.inp = str(inp).strip()
        self.res = str(res).strip()
    
    def as_text(self):
        return f"{clr.Fore.LIGHTBLACK_EX}{self.inp.ljust(25)} {clr.Fore.LIGHTBLACK_EX}= {clr.Style.RESET_ALL}{self.res.rjust(9)}{clr.Style.RESET_ALL}"
    
    def as_text_special(self):
        inp_size = 25 if len(self.res) < 9 else 25-(len(self.res)-9)
        inp = self.inp if len(self.inp) < inp_size else f"{self.inp[:inp_size - 2]}.."

        return f"{inp.ljust(25)} {clr.Fore.LIGHTBLACK_EX}= {clr.Fore.CYAN}{self.res.rjust(9)}{clr.Style.RESET_ALL}"


class Calculator:
    def __init__(self):
        self.reses: list[SavedCalculation] = []
        self.mainloop()
    
    def mainloop(self):
        while True:
            self.show()

    def show(self):
        os.system("cls")
        width = 41
        sep = '─' * (width - 2)
        print(f'╭{sep}╮')

        fillers = 11 - len(self.reses)
        print('\n'.join([('│' + ' ' * (width - 2) + '│')] * fillers))
        if self.reses:
            if len(self.reses) > 1:
                print('\n'.join([f'│ {c.as_text()} │' for c in self.reses[:-1]]))
            print(f'├{sep}┤')
            print(f'│ {self.reses[-1].as_text_special()} │')
        else:
            print(f'├{sep}┤')

        print(f'╰{sep}╯')
        try:
            inp = input(f'{clr.Fore.CYAN}: {clr.Fore.BLUE}')
        except KeyboardInterrupt:
            print(f"{clr.Fore.RED}Quitted{clr.Style.RESET_ALL}")
            exit()
        print(clr.Style.RESET_ALL)

        if inp.strip() == 'q':
            exit()
        elif inp.strip() == 'clr':
            self.reses.clear()
            return

        self.calculate(inp)
    
    def add(self, inp, res):
        self.reses.append(
            SavedCalculation(inp, res)
        )
        if len(self.reses) > 11:
            self.reses = self.reses[-11:]
    
    def _replace_operators(self, op):
        return {'+': '+', '-': '-', '*': '×', '/': '/'}[op]
    
    def calculate(self, raw_inp: str) -> int:
        if not raw_inp: return 1
        parts = []
        temp = ""
        for c in raw_inp:
            if c in ('+', '-', '*', '/'):
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
            res = eval()
        except Exception:
            return 1

        self.add(' '.join(parts), str(res))
        return 0


if __name__ == '__main__':
    os.system('cls')
    print(f"""    {clr.Fore.RED}Controls{clr.Style.RESET_ALL}
    {clr.Fore.CYAN}: q{clr.Style.RESET_ALL}     -> exit
    {clr.Fore.CYAN}: clr{clr.Style.RESET_ALL}   -> clear history
    {clr.Fore.RED}Press enter to continue{clr.Style.RESET_ALL}
    """)
    i = input()
    if i == 'q': exit()
    Calculator()
