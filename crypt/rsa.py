#coding:utf-8
#分解n，知道e、c求m
def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
      raise Exception('modular inverse does not exist')
    else:
      return x % m

n=2811372585084629351009313697163126066330687280313472384381
e=65537
c=987336460127302980611521813060916433876991011122463417552

p=320644954422610049929
q=8767867843568934765983476584376578389
d = modinv(e, (p-1)*(q-1))
print d

	
m = pow(c,d,n)
print m
