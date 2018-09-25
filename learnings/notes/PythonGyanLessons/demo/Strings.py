s1 = "a"
s2 = "b"
i1=3

s1+s2

# s1+i1
s1*i1

ss1 = "Welcome to India"
ss2 = "0123456789"

len(ss1)

ss1[-1]

ss1[:-1]

ss2[1::2]

list(range(1,10,2))


'Welcome' in ss1

'Welcome' not in ss1


"tim" == "tie"
"free" != "freedom"
"arrow" > "aron"
"right" >= "left"
"teeth" < "tee"
"yellow" <= "fellow"
"abc" > ""
'a' > 'A'
'1'<'a'


chr(97)
ord('a')
ord('A')


for i in range(200):
    print(chr(i))



":"<'@'

my_var = "aAbB^@:?90"

min(my_var)







for i in range(200):
    if chr(i) in "aAbB^@:?90":
        print(str(i), " : ", chr(i))

my_india = "India is great!!"
for i in my_india:
    # print(i, end="\n")  #this is default behavior
    # print(i, end="")    # print string without a newline
    print(i, end="#")

print(list(my_india))




















