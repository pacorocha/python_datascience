class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        product_list = []
        for i in range(len(V1)):
            product_list.append(V1[i] * V2[i])
        print("Dot product is: ", sum(product_list))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        total = []
        for i in range(len(V1)):
            total.append(float(V1[i] + V2[i]))
        print("Add Vector is: ", total)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        total = []
        for i in range(len(V1)):
            total.append(float(V1[i] - V2[i]))
        print("Add Vector is: ", total)
