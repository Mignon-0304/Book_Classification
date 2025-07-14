import os

with open('category_all.txt', 'r', encoding='utf-8') as c:
    ctg = c.readlines()


print("輸入類別號碼和書名以歸類書籍。")
print("新增類別：按111" + '\n' + "修改類別名：按222" + '\n' + "查看類別總覽：按333" + '\n' + "查詢書籍分類：按555")

while True:
    try:
        a = int(input("輸入類別號碼(輸入0結束)："))
        break
    except ValueError:
        print("輸入錯誤！請重新輸入。")
    

choose = 2
outside = "/Users/mignon/Desktop/github/書籍歸類"
inside = "/Users/mignon/Desktop/github/書籍歸類/categories"

os.chdir(outside)


while a != 0:
    if a == 111:
        os.chdir(inside)
        a = int(input("輸入新類別號碼："))
        new = input("請輸入新類別名：")
        ctg.append(new)
        open(new + '.txt', 'a', encoding='utf-8').close()
        os.chdir(outside)
        with open('category_all.txt', 'a') as f:
            f.write(new + '\n')
        print("已建立新類別 " + ctg[a-1])

    elif a == 222:
        os.chdir(inside)
        a = int(input("輸入欲修改之類別號碼："))
        name = ctg[a-1].strip()
        with open(name + '.txt', 'r', encoding='utf-8') as source: #讀取原檔案內容
            content = source.read()
        os.remove(name + '.txt')
        new = input("目前類別名為：" + name + '\n' + "請輸入新類別名：")
        ctg[a-1] = new + '\n'
        with open(new + '.txt', 'w', encoding='utf-8') as target:
            target.write(content)
        os.chdir(outside)
        with open("category_all.txt", "w", encoding="utf-8") as f:
            pass
        with open("category_all.txt", 'a') as f:
            for i in ctg:
                f.write(i)
        with open("each_ctg.txt", 'a', encoding='utf-8') as f:
            all = [new + '\n' if i.strip() == new else i for i in all]
        with open("each_ctg.txt", 'w', encoding='utf-8') as f:
            f.writelines(all)
        print("已修改類別為 " + ctg[a-1])

    elif a == 333:
        for i in range(len(ctg)):
            print(str(i+1) + " " + ctg[i], end = '')
        print('\n')

    elif a == 555:
        book = input("輸入欲查詢書名：")
        with open("book_all.txt", 'r', encoding='utf-8') as f:
            all = f.readlines()
        if book+'\n' in all:
            for i, element in enumerate(all, start = 0):
                if element.strip() == book:
                    with open("each_ctg.txt", 'r', encoding='utf-8') as file:
                        each_ctg = file.readlines()
                        print("該書被歸類於 " + each_ctg[i].strip() + " 類")
                    break
        else:
            print("查無此書")
                    
        
    elif a > len(ctg) or a < 0:
        print("查無此類別，請重新輸入")
        a = int(input("輸入類別號碼(輸入0結束)："))
        continue

    else:
        book = input("輸入作品名稱(欲跳出輸入0)：")
        if book != "0":
            with open("book_all.txt", 'r', encoding="utf-8") as file:
                r = file.readlines()
                if book+'\n' in r:
                    for i, element in enumerate(r, start = 0):
                        if element.strip() == book:
                            print("hi")
                            with open("each_ctg.txt", 'r') as f:
                                each_ctg = f.readlines()
                            print("該書籍已被歸類於 " + each_ctg[i], end = '')
                else:
                    os.chdir(inside)
                    path = ctg[a-1].strip() + ".txt"
                    with open(path, 'a', encoding='utf-8') as f:
                        f.write(book + '\n')
                    os.chdir(outside)
                    with open("book_all.txt", 'a') as f:
                        f.write(book + '\n')
                    with open("each_ctg.txt", 'a', encoding='utf-8') as f:
                        f.write(ctg[a-1])
                    print("已將《" + book + "》加入「" + ctg[a-1].strip() + "」")

    os.chdir(outside)
    while True:
        try:
            a = int(input("輸入類別號碼(輸入0結束)："))
            break
        except ValueError:
            print("輸入錯誤！請重新輸入。")

print("歸類完畢。")
os.chdir(inside)

for i in range(len(ctg)):
    try:
        os.chdir(inside)
        with open(ctg[i].strip() + '.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        print(ctg[i].strip() + " 類：" + str(len(lines)) + "本")
        
    except FileNotFoundError:
        print(ctg[i].strip() + " 類 尚未建立檔案")

os.chdir(outside)
with open('book_all.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("總共已記錄 " + str(len(lines)) + " 本書")
