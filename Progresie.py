class Progresie:
    def __init__(self, numere):
        self.numere = numere

    def verificare_progresie(self):

        # Verificăm dacă este o progresie aritmetică
        diff_aritmetica = self.numere[1] - self.numere[0]
        is_aritmetica = all(self.numere[i] - self.numere[i - 1] == diff_aritmetica for i in range(2, len(self.numere)))

        # Verificăm dacă este o progresie geometrică
        ratie_geometrica = self.numere[1] / self.numere[0]
        is_geometrica = all(self.numere[i] / self.numere[i - 1] == ratie_geometrica for i in range(2, len(self.numere)))

        # Returnăm rezultatul în funcție de tipul de progresie identificat
        if is_aritmetica:
            return f"A({diff_aritmetica})"
        elif is_geometrica:
            return f"G({ratie_geometrica})"
        else:
            return "N"
