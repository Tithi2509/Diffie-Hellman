def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            return g
p = int(input("Enter the value of p : "))
g = primitive_root(p)
print("The value of g is ", g)
a = int(input("Enter the private key of Alice : "))
b = int(input("Enter the private key of Bob : "))
x = (g**a)%p 
y = (g**b)%p

print("The public key of Alice :", x)
print("The public key of Bob :",y)

ka = (y**a)%p
kb = (x**b)%p

print("The shared key of Alice :", ka)
print("The shared key of Bob :", kb)