class Calc:
    def sum(self, x: int, y: int) -> int:
        return x + y

    def devide(self, x: int, y: int) -> float:
        return round((x / y), 2)

    def substract(self, x: int, y: int) -> int:
        return x - y

    def multiply(self, x: int, y: int) -> int:
        return x * y

    def input_math(self) -> list:
        while True:
            a = input("Enter number math logic, or EXIT to finnish: ")
            if len(a.split()) == 3:
                return a.split()
            elif a.upper() == "EXIT":
                break
            else:
                print("Enter symbols separedet by space or EXIT to finnish")

    def calculation(self):
        while True:

            value = self.input_math()

            if value is None:
                break

            elif value[1] == "/":

                print(self.devide(float(value[0]), float(value[2])))

            elif value[1] == "+":

                print(self.sum(float(value[0]), float(value[2])))

            elif value[1] == "-":

                print(self.substract(float(value[0]), float(value[2])))

            elif value[1] == "*":

                print(self.multiply(float(value[0]), float(value[2])))


if __name__ in "__main__":

    calculator = Calc()

    calculator.calculation()
