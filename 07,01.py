class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for Le in self.my_list:
            for i in Le:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for k in range(len(other.my_list[i])):
                self.my_list[i][k] = self.my_list[i][k] + other.my_list[i][k]
        return Matrix.__str__(self)


m = Matrix([[-2, 1, 3], [-5, 0, 8], [4, 1, -6], [9, 0, -3]])
new_m = Matrix([[8, 0, -2], [3, 9, -5], [-3, 4, 6], [-9, 0, 5]])
print(m.__str__())
print(m.__add__(new_m))
