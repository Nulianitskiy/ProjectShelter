import random

class RSA():
    def __init__(self) -> None:
        self.public_key, self.private_key = self.create_keys()
        

    def create_keys(self):
        p = self.random_prime()
        q = self.random_prime()

        if p == q :
            q = self.random_prime()

        n = p*q
        f = (p-1)*(q-1)

        e = self.find_e(f)
        _, x, _ = self.gcdExtended(e,f)
        d = ((x%e+e)%e)

        return [e, n], [d, n] #public, private
    

    def gcdExtended(self,a, b):
        if a == 0 :
            return b,0,1
        gcd,x1,y1 = self.gcdExtended(b%a, a)
        x = y1 - (b//a) * x1
        y = x1
        return gcd,x,y
    
    def find_e(self,f):
        while True:
            e = random.randint(2,f)
            if self.GCD(f,e) == 1:
                return e


    def GCD(self, x, y):
        while(y):
            x, y = y, x % y
        return abs(x)


    def random_prime(self):
        n = random.randint(100, 1000)
        while True:
            if self.mil_rab(n,2):
                return n
            else:
                n+= 1


    def mil_rab(self, n, a): # n - число, a - основание
        m = 0
        k = 0 # максимальное число шагов
        while True:
            if n % pow(a,k) == 0:
                k += 1
            else:
                m = n // pow(a,k)
                break

        t = pow(a,m) % n # инициализация

        for _ in range(k-1): # итерация
            t = pow(t,a) % n
        
        if t== n-1:
            return True # если t = -1 - то оно простое
        else:
            return False # если t = 1 - то оно составное
        

    def encode(self, text):
        code = []
        for let in text:
            l = ord(let)
            code.append((l**self.public_key[0])%self.public_key[1])

        return code
    
    def encode_by_key(self, key, text):
        code = []
        for let in text:
            l = ord(let)
            code.append((l**key[0])%key[1])

        return code
    
    def decode(self, code):
        text = []
        for let in code:
            l = (let**self.private_key[0])% self.private_key[1]
            text.append(chr(l))

        return text
    

# key = RSA()

# word = key.encode("aboba")
# print(word)
# print(key.decode(word))