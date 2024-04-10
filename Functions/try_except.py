# data = {
#     1: "One",
#     2: "Two",
#     3: "Tree"
# }
# def enter_numbers():
#     while True:
#         try: # gaudom klaidas
#             value = int(input("input number: "))
#             print((data[value]))
#         except ValueError: # tikimes buten sitos klaidos
#             raise ValueError("iveskite tik skaiciu") # iskeliam klaida i
#         except KeyError:
#             raise KeyError("Neteisingas raktas")
#             continue
#
#         if value > 10:
#             print("daugiau uz 10")
#         elif value < 10:
#             print("maziau uz 10")
#
#
# # enter_numbers()
#
# dalyba = lambda a, b : a / b
# daugyba = lambda a, b : a * b
# def sum(*args):
#     return sum(args)
#
# def belekas(fun, *args):
#     return
