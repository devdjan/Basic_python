# Gauss functions
import math


def pdf(x, mu = 0.0, sigma = 1.0):
    x = float(x - mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0 * math.pi) / sigma

def cdf(z, mu= 0.0, sigma = 1.0):
    z = float(z - mu) / sigma
    if z < -8.0: return 0.0
    if z > +8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term  *= z * z / i
        i += 2
    return 0.5 + total * pdf(z)
# Executing our function
z = 2
mu = 4.0
sigma = 2.0
print(cdf(z, mu, sigma))

# What our functions are doing? Explaining in russian:
# Реализуем Гауссову (нормальную) птлтность вероятностей (pdf) и кумулятивное распределние (cdf)
# функции которых не реализованы в библитеке math - мы сами написали. Реализация функции pdf()
# следует непостредвенно их определения, а реализвация функции cdf() использует ряд Тейлора
# и такєе візівает функцию pdf()
#
# Чуть позже перепишу функцию для многократнного использования.
#