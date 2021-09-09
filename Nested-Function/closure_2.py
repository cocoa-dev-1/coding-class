def start_compplex_at(x):
    one = 1
    def increment_by(y):
        added = x + y + one
        def multiply_by(z):
            return added * z
        return multiply_by
    return increment_by

c1 = start_compplex_at(2)
c2 = c1(3)
c3 = c2(4)
print(c3)