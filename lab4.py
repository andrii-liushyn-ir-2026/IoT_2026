class TouristVoucher:
    def __init__(self, country="Україна", duration=1, price=0.0, voucher_code="default-000", discount_percent=0.0):
        self.__country = country
        self.__duration = duration
        self.__price = price

        self.voucher_code = voucher_code
        self.discount_percent = discount_percent

    def getCountry(self):
        return self.__country

    def getDuration(self):
        return self.__duration

    def getPrice(self):
        return self.__price

    def __str__(self):
        return (f"Путівка в {self.__country} | "
                f"Тривалість: {self.__duration} днів | "
                f"Ціна: {self.__price}€ | Код: {self.voucher_code} | "
                f"Знижка: {self.discount_percent}%")

    def __repr__ (self):
        return (f"TouristVoucher(country='{self.__country}', duration={self.__duration}, "
                f"price={self.__price}, voucher_code='{self.voucher_code}', "
                f"discount_percent={self.discount_percent})")

    def __del__(self):
        print(f"Об'єкт TouristVoucher ({self.voucher_code}) видалено з пам'яті.")

def main():
    voucher1 = TouristVoucher()
    voucher2 = TouristVoucher("Єгипет", 7, 450.50, "EGY-2026", 10.0)
    voucher3 = TouristVoucher("Італія", 10, 899.99, "ITA-777", 5.0)
    voucher4 = TouristVoucher(price=100.0)
    print(voucher4.getPrice())
    

    vouchers = [voucher1, voucher2, voucher3]

    print("=== Виведення об'єктів через __str__ ===")
    for v in vouchers:
        print(v)

    print("\n=== Виведення об'єктів через __repr__ ===")
    for v in vouchers:
        print(repr(v))

    print("\n=== Виведення полів окремо (геттери + публічні поля) ===")
    for i, v in enumerate(vouchers, 1):
        print(f"Об'єкт №{i}:")
        print(f"  Країна (геттер): {v.getCountry()}")
        print(f"  Тривалість (геттер): {v.getDuration()} днів")
        print(f"  Ціна (геттер): {v.getPrice()}€")
        print(f"  Код путівки (публічне поле): {v.voucher_code}")
        print(f"  Знижка (публічне поле): {v.discount_percent}%\n")

if __name__ == "__main__":
    main()
