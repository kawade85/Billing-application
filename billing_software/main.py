
from tkinter import *
import tkinter as tk 
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk #pip install pillow
import random,os
from tkinter import messagebox
import tempfile
from time import strftime



class bill_app: # defining a constructor 
    def __init__(self, root): # main window => root
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Application")
        self.tax = 0.1  # Assuming a tax rate of 10%



        ############ creating some variables ############
        self.c_name = StringVar()
        self.c_phn = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_mail = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.prices = IntVar()  #for calculation
        self.qty = IntVar()    #for calculation
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

      # defining category list before using them
        
        #  list of product categories:
        self.Category = ["Clothing","lifestyle","Accessories","food stuffs"]
      
      # Clothing subcategory
        self.subcategory_Clothing = ["Pants","T-shirts","Shirts"]
        self.pants = ["Lee Cooper","Levi's","Spykar","Calvin Klien"]
        self.price_LeeCooper = 6000
        self.price_Levis = 5000
        self.price_Spyker = 8000
        self.price_Calvinklien = 7000

        self.Tshirts = ["Polo","jacknjones","Adidas","Levi's"]
        self.price_Polo = 2000
        self.price_jacknjones = 5000
        self.price_Adidas = 3000
        self.price_Levis = 5000

        self.shirts = ["Van Heusen","Raymond"]
        self.price_Vanheusan = 5000
        self.price_Raymond = 5000

        # lifestyle subcategory

        self.subcategory_Lifestyle = ["Cosmetics","Hair Oil", "Perfumes"]
        self.Cosmetics = ["Foundations","Compact powders","Lipstics"]
        self.price_Foundations = 699
        self.price_Compactpowders = 599
        self.price_Lipstics = 450

        self.HairOil = ["Jasmine","Almand","Olive"]
        self.price_Jasmine = 100
        self.price_Almond = 129
        self.price_Olive = 299

        self.Perfumes = ["Bella Vita","Fogg","Denver"]
        self.price_Bellavita = 565
        self.price_Fogg = 390
        self.price_Denver = 311

        # accessory subcategory
        self.subcategory_Accessories = ["Handbags","Sunglasses","Earrings","Neckless"]
        self.Handbags = ["Tote","mini","longchain"]
        self.price_Tote = 500
        self.price_mini = 250
        self.price_longchain = 999

        self.Sunglasses = ["All Types"]
        self.price_alltypes = 300

        self.Earring = ["Tops","Jhumka","String"]
        self.price_tops = 60
        self.price_jhumka = 150
        self.price_string = 130

        self.Neckless = ["Short","Long"]
        self.price_short = 300
        self.price_long = 600

        #food stuffs

        self.subcategory_Foodstuffs = ["Drinks","Chips/kurkure","cakes"]
        self.Drinkd = ["Pepsi","Coca-cola","Fruity"]
        self.price_Pepsi = 70
        self.price_Cocacola = 75
        self.price_Fruity = 60

        self.Chips = ["Doritos","Balaji chips","Lays","Kurkure"]
        self.price_Doritos = 30
        self.price_Balaji = 20
        self.price_Lays = 30
        self.price_kurkure = 30

        self.cakes = ["strawberry","Pineapple","chocolate"]
        self.price_strawberry = 60
        self.price_Pineapple = 30
        self.price_chocolate = 40



        # Load and display the first image
        img1 = Image.open("image/picture1.jpg")
        img1 = self.resize_image(img1, (500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = tk.Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=0, y=0, width=500, height=130)


        # Load and display the seconnd image
        img2 = Image.open("image/picture4.png")
        img2 = self.resize_image(img2, (500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = tk.Label(self.root, image=self.photoimg2)
        lbl_img2.place(x=1000, y=0, width=500, height=130)


         # Load and display the middle image
        img3 = Image.open("image/shopping.jpg")
        img3 = self.resize_image(img3, (500, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = tk.Label(self.root, image=self.photoimg3)
        lbl_img3.place(x=500, y=0, width=500, height=130)


        lbl_title = Label(self.root, text="* Billing Software *", font=("times new roman", 32, "bold"), bg="cyan", fg="green")
        lbl_title.place(x=0, y=130, width=1530, height=45)

        # creating time clock in our  bill
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(lbl_title,font = ("times new roman", 16,'bold'),background = "cyan",foreground= "blue")
        lbl.place(x=0,y=0,width=120,height=55)
        time() 


        #main frame
        #creating a main frame for our window
        main_frame = Frame(self.root,bd=5,relief=GROOVE,bg="yellow")
        main_frame.place(x=0,y=175,width=1530,height=620)


        #frame for customer info
        cust_frame = LabelFrame(main_frame,text="Customer",font=("times new roman", 12, "bold"),bg="white",fg="red")
        cust_frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob = Label(cust_frame,text = "Mobile No.:",font=("times new roman",12,"bold"), bg="white")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.enter_mob = ttk.Entry(cust_frame,textvariable=self.c_phn,font=("times new roman",10,"bold"),width=24)
        self.enter_mob.grid(row=0,column=1)

#
        self.lbl_CustName = Label(cust_frame,text = "Customer Name:",font=("arial",12,"bold"), bg="white", bd=4)
        self.lbl_CustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_CustName = ttk.Entry(cust_frame,textvariable=self.c_name,font=("arial",10,"bold"),width=24)
        self.txt_CustName.grid(row=1,column=1, sticky=W,padx=5,pady=2)

#
        self.lblEmail = Label(cust_frame,text = "Email:",font=("arial",12,"bold"), bg="white", bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail = ttk.Entry(cust_frame,textvariable=self.c_mail,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)




        # frame for products info
        prod_frame = LabelFrame(main_frame,text= "Products", font = ("times new roman",12,"bold"),bg = "white", fg="red")
        prod_frame.place(x=370,y=5,width=660,height=140)

        #category
        self.lbl_category = Label(prod_frame,font=("arial",12,"bold"),bg="white",text="Select Categories:",bd=4)
        self.lbl_category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category = ttk.Combobox(prod_frame,value = self.Category ,font = ("arial",10,"bold"),width = 24, state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.Catagories)

        #subcategory
        self.lbl_subcategory = Label(prod_frame,font=("arial",12,"bold"),bg="white", text="Subcategory:",bd=4)
        self.lbl_subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_subcategory = ttk.Combobox(prod_frame,value = [""],font = ("arial",10,"bold"),width=24,state="readonly")
        self.combo_subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)

        
        #Product Names:
        self.lbl_product = Label(prod_frame,font=("arial",12,"bold"),bg="white",text="Product Name:",bd=4)
        self.lbl_product.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_product = ttk.Combobox(prod_frame,textvariable=self.product,state="readonly", font = ("arial",10,"bold"),width=24)
        self.combo_product.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_product.bind("<<ComboboxSelected>>",self.price)

        #Price
        self.lbl_price = Label(prod_frame,text="Price:",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbl_price.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_price = ttk.Combobox(prod_frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.combo_price.grid(row=0,column=3,sticky=W,padx=5,pady=2)


        #Quantity of products
        self.lbl_Qty = Label(prod_frame,text="Quantity:",font=("arial",12,"bold"),bg="white",bd="4")
        self.lbl_Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.combo_Qty = ttk.Entry(prod_frame,textvariable=self.qty,font=("arial",10,"bold"),width=24)
        self.combo_Qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)
        

                             
        #creating a frame to right side-
        #inside the main frame
        rightlabelframe = LabelFrame(main_frame, text = "Bill Counter",font = ("times new roman",12,"bold"),bg="white",fg="red")
        rightlabelframe.place(x=1037,y=5,width=480,height=478)

        scroll_yy = Scrollbar(rightlabelframe,orient=VERTICAL)
        self.textarea = Text(rightlabelframe,yscrollcommand =  scroll_yy.set,bg = "white",fg="blue",font=("times new roman",12,"bold"))
        scroll_yy.pack(side = RIGHT,fill=Y)
        scroll_yy.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        # bill taxes/bottom frame creation
        bottom_frame = LabelFrame(main_frame,text= "=> Tax Column", font = ("times new roman",12,"bold"),bg = "white", fg="red")
        bottom_frame.place(x=0,y=485,width=1520,height=125)


        self.lbl_subtotal = Label(bottom_frame,text="Sub-Total:",font=("arial",12,"bold"),bg="white",bd="4")
        self.lbl_subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_subtotal = ttk.Entry(bottom_frame,font=("arial",10,"bold"),width=24)
        self.entry_subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

#####

        self.lbl_tax = Label(bottom_frame,font=("arial",12,"bold"),bg="white",text="Tax:",bd = 4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_tax = ttk.Entry(bottom_frame,font=("arial",10,"bold"),width=24)
        self.entry_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

#####

        self.lbl_amtotal = Label(bottom_frame,font=("arial",12,"bold"),text="Amount Total:",bg="white",bd=4)
        self.lbl_amtotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_amtotal = ttk.Entry(bottom_frame,font=("arial","10","bold"),width=24)
        self.entry_amtotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)
    

    #### Creating a button frame ####

        btn_frame = Frame(bottom_frame,bd=2,bg="white")
        btn_frame.place(x=320,y=0)

        self.addtocart = Button(btn_frame,command=self.add_item,text="Add to Cart",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.addtocart.grid(row=0,column=0)

        self.gen_bill = Button(btn_frame,command=self.generate_bill,text="Generate Bill",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.gen_bill.grid(row=0,column=1)

        self.save = Button(btn_frame,command=self.save_bill,text="Save",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.save.grid(row=0,column=2)

        self.print = Button(btn_frame,command=self.iprint,text="Print",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.print.grid(row=0,column=3)

        self.clear = Button(btn_frame,command=self.cclear,text="CLEAR",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.clear.grid(row=0,column=4)

        self.exit= Button(btn_frame,command=self.root.destroy,text="Exit!",font=("arial",15,"bold"),bg="black",fg="white",height=4,width=15,cursor="hand2")
        self.exit.grid(row=0,column=5)



        ####________****________######
        #    middle frame
        midd_frame = Frame(main_frame,bd=10)
        midd_frame.place(x=10,y=150,width=1020,height=330)
        
        #inserting image
        img8 = Image.open("image/lucky.png")
        img8 = self.resize_image(img8, (500, 310))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lbl_img8 = tk.Label(midd_frame, image=self.photoimg8)
        lbl_img8.place(x=0, y=0, width=500, height=310)


        img9 = Image.open("image/ring.jpg")
        img9 = self.resize_image(img9, (500, 310))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        lbl_img9 = tk.Label(midd_frame, image=self.photoimg9)
        lbl_img9.place(x=500, y=0, width=500, height=310)





        #search column
        search_frame = Frame(main_frame,bd=2,bg="white")
        search_frame.place(x=0,y=445,width=445,height=38)

        self.lbl_bill = Label(search_frame,font=("arial",12,"bold"),fg="white",bg="red",text="Bill Number:")
        self.lbl_bill.grid(row=0,column=0,sticky=W,padx=1)


        self.entry_search = ttk.Entry(search_frame,textvariable = self.search_bill,font=("arial",10,"bold"),width=24)
        self.entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.srbutton = Button(search_frame,command = self.find_bill,text="Search",font=("arial",12,"bold"),bg="grey",fg="black",width=15,cursor="hand2")
        self.srbutton.grid(row=0,column=2)
        self.welcome()


        self.l = []
        #================================Function Declaration===============================

    def add_item(self):
        tax = 0.1  # Assuming a tax rate of 10%
    
    # Get selected product and quantity
        product = self.product.get()
        qty = self.qty.get()
        price = self.prices.get()
    
    # Check if a product is selected
        if product == "":
            messagebox.showerror("Error!", "Please select a product.")
            return
    
    # Calculate item price
        item_price = qty * price
    
    # Display item details
        self.textarea.insert(END, f"\n{product}\t\t{qty}\t\t{item_price}")
    
    # Update subtotal
        self.l.append(item_price)
        self.sub_total.set(f'Rs.{sum(self.l):.2f}')
    
    # Calculate and update tax
        tax = (sum(self.l) - price) * tax
        self.tax_input.set(f'Rs.{tax:.2f}')
    
    # Calculate and update total
        total = sum(self.l) + tax
        self.total.set(f'Rs.{total:.2f}')

   

    def generate_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add To Cart")
        else:
            text = self.textarea.get(10.0,(10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n==================================================")
            self.textarea.insert(END,f"\n Sub Total-Amount : \t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount : \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount : \t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n==================================================")
            # Update the Amount Total field

            self.entry_amtotal.delete(0, END)  # Clear any previous value

            self.entry_amtotal.insert(0, self.total.get())

        # Update the Gov. Tax field

            self.entry_tax.delete(0, END)  # Clear any previous value

            self.entry_tax.insert(0, self.tax_input.get())

        # Update the Sub-Total field

            self.entry_subtotal.delete(0, END)  # Clear any previous value

            self.entry_subtotal.insert(0, self.sub_total.get())
        

    def save_bill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save bill ?")
        if op>0:
            self.bill_date = self.textarea.get(1.0,END)
            f1 =  open('Bills/'+str(self.bill_no.get())+".txt",'w')
            op = messagebox.showinfo("Saved!!",f"Bill N0.:{self.bill_no.get} Saved Successfully!!")
            f1.write(self.bill_date)
            f1.close

    def iprint(self):
        q = self.textarea.get(1.0,"end-1c")
        filename = tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def cclear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_mail.set("")
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.c_phn.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set('')
        self.welcome()


#search box
    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f'bills.{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found = "yes"

        if found == 'no':
            messagebox.showerror("Error!!","Invalid Bill Number!!")




    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t Welcome to Lucky Shopping Mini-Mall")
        self.textarea.insert(END, f"\n\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number : {self.c_phn.get()}")
        self.textarea.insert(END, f"\n Email : {self.c_mail.get()}")
        self.textarea.insert(END, "\n==================================================")
        self.textarea.insert(END, f"\n Products:\t\t\t Qty:\t Price:")
        self.textarea.insert(END, "\n==================================================\n")




    def Catagories(self,event = ""):
        if  self.combo_category.get()=="Clothing":
            self.combo_subcategory.config(value = self.subcategory_Clothing)
            self.combo_subcategory.current(0)

        
        if  self.combo_category.get()=="lifestyle":
            self.combo_subcategory.config(value = self.subcategory_Lifestyle)
            self.combo_subcategory.current(0)


        if  self.combo_category.get()=="Accessories":
            self.combo_subcategory.config(value = self.subcategory_Accessories)
            self.combo_subcategory.current(0)


        if  self.combo_category.get()=="food stuffs":
            self.combo_subcategory.config(value = self.subcategory_Foodstuffs)
            self.combo_subcategory.current(0)


    def Product_add(self,event=""):
        # clothing
        if self.combo_subcategory.get()=="Pants":
            self.combo_product.config(value = self.pants)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="T-shirts":
            self.combo_product.config(value = self.Tshirts)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shirts":
            self.combo_product.config(value = self.shirts)
            self.combo_product.current(0)

        # lifestyle
        if self.combo_subcategory.get()=="Cosmetics":
            self.combo_product.config(value = self.Cosmetics)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Hair Oil":
            self.combo_product.config(value = self.HairOil)

        if self.combo_subcategory.get()=="Perfumes":
            self.combo_product.config(value = self.Perfumes)
            self.combo_product.current(0)
            self.combo_product.current(0)

        # Accessories
        #"Handbags","Sunglasses","Earrings","Neckless"
        if self.combo_subcategory.get()=="Handbags":
            self.combo_product.config(value = self.Handbags)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Sunglasses":
            self.combo_product.config(value = self.Sunglasses)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Earrings":
            self.combo_product.config(value = self.Earring)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Neckless":
            self.combo_product.config(value = self.Neckless)
            self.combo_product.current(0)
        


        # food stuffs
        #"Drinks","Chips/kurkure","cakes"
        if self.combo_subcategory.get()=="Drinks":
            self.combo_product.config(value = self.Drinkd)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Chips/kurkure":
            self.combo_product.config(value = self.Chips)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="cakes":
            self.combo_product.config(value = self.cakes)
            self.combo_product.current(0)

        

    def price(self,event = ""):
        #pant   ["Pants","T-shirts","Shirts"]
        #self.pants = ["Lee Cooper","Levi's","Spykar","Calvin Klien"]
        if self.combo_product.get() == "Levi's":
            self.combo_price.config(value = self.price_Levis)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Lee Cooper":
            self.combo_price.config(value = self.price_LeeCooper)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Spykar":
            self.combo_price.config(value = self.price_Spyker)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Calvin Klien":
            self.combo_price.config(value = self.price_Calvinklien)  
            self.combo_price.current(0)
            self.qty.set(1) 

        #  Tshirts
        #"Polo","jacknjones","Adidas","Levi's

        if self.combo_product.get() == "Polo":
            self.combo_price.config(value = self.price_Polo)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "jacknjones":
            self.combo_price.config(value = self.price_jacknjones)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Adidas":
            self.combo_price.config(value = self.price_Adidas)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Levi's":
            self.combo_price.config(value = self.price_Levis)  
            self.combo_price.current(0)
            self.qty.set(1) 

        #shirts
        #Van Heusen","Raymond

        if self.combo_product.get() == "Van Heusen":
            self.combo_price.config(value = self.price_Vanheusan)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Raymond":
            self.combo_price.config(value = self.price_Raymond)  
            self.combo_price.current(0)
            self.qty.set(1) 

        
        # Lifestyle = ["Cosmetics","Hair Oil", "Perfumes"]
        #cosmetics 
        if self.combo_product.get() == "Foundations":
            self.combo_price.config(value = self.price_Foundations)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Compact Powders":
            self.combo_price.config(value = self.price_Compactpowders) 
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Lipstics":
            self.combo_price.config(value = self.price_Lipstics)  
            self.combo_price.current(0)
            self.qty.set(1) 

        #hair oil
        if self.combo_product.get() == "Jasmine":
            self.combo_price.config(value = self.price_Jasmine)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Almond":
            self.combo_price.config(value = self.price_Almond)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Olive":
            self.combo_price.config(value = self.price_Olive)  
            self.combo_price.current(0)
            self.qty.set(1) 

        # perfumes
        if self.combo_product.get() == "Bella Vita":
            self.combo_price.config(value = self.price_Bellavita)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Fogg":
            self.combo_price.config(value = self.price_Fogg)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Denver":
            self.combo_price.config(value = self.price_Denver)  
            self.combo_price.current(0)
            self.qty.set(1) 


        #Accessories = ["Handbags","Sunglasses","Earrings","Neckless"]
        # handbags

        if self.combo_product.get() == "Tote":
            self.combo_price.config(value = self.price_Tote)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "mini":
            self.combo_price.config(value = self.price_mini)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Longchain":
            self.combo_price.config(value = self.price_longchain)  
            self.combo_price.current(0)
            self.qty.set(1) 

        # sunglasses
        if self.combo_product.get() == "All Types":
            self.combo_price.config(value = self.price_alltypes)  
            self.combo_price.current(0)
            self.qty.set(1) 

        # Earrings

        if self.combo_product.get() == "Tops":
            self.combo_price.config(value = self.price_tops)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Jhumka":
            self.combo_price.config(value = self.price_jhumka)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "String":
            self.combo_price.config(value = self.price_string)  
            self.combo_price.current(0)
            self.qty.set(1) 

# neckless
        if self.combo_product.get() == "Long":
            self.combo_price.config(value = self.price_long)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Short":
            self.combo_price.config(value = self.price_short)  
            self.combo_price.current(0)
            self.qty.set(1) 
        

        # food stuffs     
        #Foodstuffs = ["Drinks","Chips/kurkure","cakes"]
        
        #drinks
        if self.combo_product.get() == "Pepsi":
            self.combo_price.config(value = self.price_Pepsi)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Coca-cola":
            self.combo_price.config(value = self.price_Cocacola)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Fruity":
            self.combo_price.config(value = self.price_Fruity)  
            self.combo_price.current(0)
            self.qty.set(1) 

        # chips
        if self.combo_product.get() == "Doritos":
            self.combo_price.config(value = self.price_Doritos)  
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get() == "Balaji chips":
            self.combo_price.config(value = self.price_Balaji)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Lays":
            self.combo_price.config(value = self.price_Lays)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Kurkure":
            self.combo_price.config(value = self.price_kurkure)  
            self.combo_price.current(0)
            self.qty.set(1) 

        # vakes
        if self.combo_product.get() == "strawberry":
            self.combo_price.config(value = self.price_short)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "Pineapple":
            self.combo_price.config(value = self.price_short)  
            self.combo_price.current(0)
            self.qty.set(1) 

        if self.combo_product.get() == "chocolate":
            self.combo_price.config(value = self.price_short)  
            self.combo_price.current(0)
            self.qty.set(1) 
        


    def new_method(self):
        return 10





        

    
    def resize_image(self, img, size):
        return img.resize(size)


root = tk.Tk()
app = bill_app(root)
root.mainloop()








