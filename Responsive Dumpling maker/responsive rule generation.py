def exchange(s):
    l = []
    s = s.split()
    for i in range(len(s)):
        temp = ""
        for j in s[i]:
            a = "["+str.upper(j)+"|"+j+"]"
            temp += a
        l.append(temp)
    b = " ".join(i for i in l)
    return b


def ww(s):
    l = []
    b = s[0]
    for i in s:
        a = "\"" +exchange(i) + "\"" + " : " + "\"" + "#"+ b + " dumpling#"+ "\""
        l.append(a)
    return l


s0 = ["not meat", "no meat", "unmeat", "meat free", "meat"]
s1 = ["vegetarian","vegan","gluten free","GF"]

s2 = ["not veggie" , "no veggie", "unveggie", 'veggie free', "meat only", "only meat", "veggie"]
s3 = ["not beef", "no beef", "unbeef", "beef free", "beef"]

s4 = ["not chicken", "no chicken", "unchicken", "chicken free", "chicken"]
s5 = ["not pork", "no pork", "unpork", "pork free", "pork"]

s6 = ["not seafood", "no seafood", "unseafood", "seafood free", "seafood"]

s7 = ["not spicy", "no spicy", "unspicy", "spicy free", "spicy"]

s8 = ["not single", "no single", "unsingle", "single"]
s9 = ["not double", "no double", "undouble", "double"]
s10 = ["not salty", "no salty", "unsalty", "salty"]
ss = ["dumpling"]
ww(ss)
