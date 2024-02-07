class SFA:
    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def calculate_gini(self):
        """
        gini = value/100 if value<100 else 0
        """
        return self.value / 100 if self.value < 100.0 else 0.0


ram = SFA("ltv_100", 68)
gini = ram.calculate_gini()
print(f"Gini of the provided risk driver: {gini}")
