def curency_EU_USD(eur=int) -> int:
    return round(eur * 1.09, 2)


def curency_EU_JPY(eur=int) -> int:
    return round(eur * 164.62, 2)


if __name__ == "__main__":
    print(curency_EU_USD(100))
    print(curency_EU_JPY(112.12))
