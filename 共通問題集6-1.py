#for i in range(10):
    #print('for文のプログラム')

    #10回表示

#6-2
#sum = 0
#for i in range(1,101):
    #sum +=i

#print("合計は",sum,"です",sep="")

#6-3
#for i in range(1,11):
   # print(i,end="")

6-6
sum = 0
start = int(input("開始数:"))
end = int(input("終了数:"))

for num in range(start,end+1):
    sum += num
    print("合計:",sum,sep="")
