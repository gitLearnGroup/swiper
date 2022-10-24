class A:

    def __init__(self):
        self.text = '111111111111'

    def abc(self):
        print(self.text)


def rt(self):
    print(f"{self.text}22222222222")


if __name__ == '__main__':
    A.abc_old = A.abc
    A.abc = rt
    a = A()
    a.abc()


OUTPUT: 11111111111122222222222
