def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_hasta(limite):
    return [n for n in range(2, limite+1) if es_primo(n)]

if __name__ == "__main__":
    limite = int(input("Hasta qué número quieres ver primos? "))
    print(primos_hasta(limite))