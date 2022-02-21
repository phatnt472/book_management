from tkinter import *
from book import *
from time import sleep


def add():
    clear_screen()
    book_id = entry1.get().strip()
    name = entry2.get().strip()
    year = entry3.get().strip()
    if str(book_id) != "" and name.strip() != "" and str(year) != "":
        b = Book(book_id, name, year)
        with open('data.txt','r') as f:
            data = f.readlines()
        data = [x[:-1].split("-") for  x in data]
        with open('data.txt','a') as f:
            count = 0
            for line in data:
                if  book_id in line:
                    count += 1
                
            if count == 0:
                s = f"{b.book_id}-{b.name.strip()}-{b.year}\n"
                f.writelines(s)
                list_box.insert(END,s)
            else:
                list_box.insert(END,"Mã số này đã tồn tại!")
    else:
        list_box.insert(END,"Vui lòng điền đầy đủ thông tin!")
   

   

         

def clear_screen():
    list_box.delete(0,END)

def find():
    clear_screen()
    book_id = entry1.get().strip()
    name = entry2.get().strip()
    year = entry3.get().strip()
    with open('data.txt','r') as f:
        data = f.readlines()
    data = [x[:-1].split("-") for  x in data]
    count = 0
    for line in data:
        if str(book_id) == "" and name == "" and year == "":
            list_box.insert(END,"Vui lòng nhập dữ liệu!")
            count += 1
            break
        if str(book_id) == "" or name == "" or year == "":
            if str(book_id) == line[0]:
                list_box.insert(END,f"{line[0]}-{line[1]}-{line[2]}\n")
                count += 1
            elif name == line[1]:
                list_box.insert(END,f"{line[0]}-{line[1]}-{line[2]}\n")
                count += 1
            elif str(year) == line[2]:
                list_box.insert(END,f"{line[0]}-{line[1]}-{line[2]}\n")
                count += 1
        else:
            if str(book_id) == line[0] and name == line[1] and str(year) == line[2]:
                list_box.insert(END,f"{line[0]}-{line[1]}-{line[2]}\n")
                count += 1
        

    if count == 0:
        list_box.insert(END,f"Không tìm thấy!")


def sort():
    clear_screen()
    with open('data.txt','r') as f:
        data = f.readlines()
    data = [x[:-1].split("-") for  x in data]
    data.sort()
    with open('data.txt','w') as f:
        for line  in data:
            s = f"{line[0]}-{line[1]}-{line[2]}\n"
            list_box.insert(END,s)
            f.writelines(s)

 

def create_ui():
   global entry1,entry2,entry3,list_box
   root = Tk()
   root.resizable(height=False,width=False)
   root.title("Book Management")
   root.geometry("280x350")

   label1 = Label(root,text="Quản lí sách",fg="red",font=("times",20))
   label1.grid(row=0,columnspan=2)
   label2 = Label(root,text="Mã Sách:",fg="blue",font=("times",16))
   label2.grid(row=2,column=0)
   label3 = Label(root,text="Tên Sách:",fg="blue",font=("times",16))
   label3.grid(row=3,column=0)
   label4 = Label(root,text="Năm XB:",fg="blue",font=("times",16))
   label4.grid(row=4,column=0)

   string_var1 = StringVar()
   string_var2 = StringVar()
   string_var3 = StringVar()
   entry1 = Entry(root,width=22,font=("times",16),justify=LEFT,textvariable=string_var1)
   entry1.grid(row=2,column=1)
   entry2 = Entry(root,width=22,font=("times",16),justify=LEFT,textvariable=string_var2)
   entry2.grid(row=3,column=1)
   entry3  = Entry(root,width=22,font=("times",16),justify=LEFT,textvariable=string_var3)
   entry3 .grid(row=4,column=1)
   
   


   button_frame = Frame(root)
   button1=Button(button_frame,text="Thêm",command = add).pack(side=LEFT)
   button2=Button(button_frame,text="Tìm",command=find).pack(side=LEFT)
   button3=Button(button_frame,text="Sắp xếp",command = sort).pack(side=LEFT)
   button4=Button(button_frame,text="Thoát",command=root.quit).pack(side=LEFT)
   button_frame.grid(row=5,column=1)

   list_box = Listbox(root,width=30)
   list_box.grid(row=1,columnspan=2)
   root.mainloop()
   

def main():
    create_ui()

if __name__ == '__main__':
    main()