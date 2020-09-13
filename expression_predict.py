from tkinter import *
from tkinter import ttk
from itertools import permutations,product

# logic behind this(overview)
# strli shows all combinations of expression with two operators and four numbers
# replace 1,2 in strli with our operators
# check if user result matches expression results for all permutations
# if matched display it

def main(num,r,op):
	global strli,result,possiblites,t1,l4,opinions
	n=len(num)
	oper=list(product(op,repeat=n-1))
	number=list(permutations(num,n))
	strli=[]
	possiblities=[]
	t=0
	for x in number:
		
		for a in oper:
			func="("*(n-1)
			func+=x[0]+a[0]+x[1]+")"
			for i,j in zip(x[2:],a[1:]):
				func+=j+i+')'	
			if eval(func)==r:
				possiblities.append(func)
			if opinions[0] and len(possiblities)==1:
				t=1
				break
		if t:
			break
	
	possiblities=list(set(possiblities))
	display="possiblites\n"
	for i in possiblities:
		display+=i+"\n"
	if len(possiblities)==0:
		display="possiblities\nimpossible"
	if t1==1:
		l4.destroy()
	t1=1
	l4=Label(text=display)
	l4.grid(row=8,column=0)
t1=0
def execute():
	global t
	if t==1:
		l5.destroy()
		t=0
	num=str(e.get()).split(" ")
	li1=[]
	for i in range(len(li)):
		if li[i]==1:
			li1.append(op[i])
	r=e1.get()
	main(num,int(r),li1)
	print(num,int(r),li1)

def checkbox(i,v):
	li[i]=v
t=0
def opinion(i,v):
	opinions[i]=v

def demo():
	global t,l5,l5_text
	l5_text="enter numbers :2 4 5 1\n select operators + -\n result 8\n possiblities\n(output when you click submit)\n((1+4)+5)-2\n((1+5)+4)-2\n((4-2)+5)+1\n((4+1)+5)-2\n((4+5)-2)+1\n((4+5)+1)-2\n((5+1)+4)-2\n((4+1)-2)+5\n((5-2)+4)+1\n((5-2)+1)+4\n((1-2)+4)+5\n((5+4)+1)-2\n((4-2)+1)+5\n((1-2)+5)+4\n((5+4)-2)+1\n((1+5)-2)+4\n((1+4)-2)+5\n((5+1)-2)+4"
	
	if t==0:
		l5=Label(text=l5_text)
		l5.grid(row=7,column=0)
		t=1
	else:
		l5.destroy()
		t=0
	
	
li=[0,0,0,0]
opinions=[0]
op=["+","-","*","//"]
w=Tk()
w.title("expression predictor")

l=Label(w,text=" enter multiple inputs space seperated")
l.grid(row=0,column=1)
l1=Label(w,text="enter numbers :")
l1.grid(row=1,column=0)
e=Entry(w)
e.grid(row=1,column=1)
l2=Label(w,text="select operators")
l2.grid(row=2,column=0)
v1,v2,v3,v4,v5=IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
c_add=Checkbutton(w,text="+",variable=v1,command=lambda:checkbox(0,v1.get()))
c_add.grid(row=3,column=0)

c_sub=Checkbutton(w,text="-",variable=v2,command=lambda:checkbox(1,v2.get()))
c_sub.grid(row=3,column=1)

c_mul=Checkbutton(w,text="*",variable=v3,command=lambda:checkbox(2,v3.get()))
c_mul.grid(row=4,column=0)

c_div=Checkbutton(w,text="//",variable=v4,command=lambda:checkbox(3,v4.get()))
c_div.grid(row=4,column=1)
# o for opinion
c_o=Checkbutton(w,text="display only one output",variable=v5,command=lambda:opinion(0,v5.get()))
c_o.grid(row=6,column=1)


l3=Label(w,text="enter result :")
l3.grid(row=5,column=0)
e1=Entry(w)
e1.grid(row=5,column=1)


cb=[c_add,c_sub,c_mul,c_div]

submit=Button(text="submit",command=execute,padx=20,pady=10,bg="#ED6B4F")
submit.grid(row=7,column=1)
show_demo=Button(text="show demo",command=demo,padx=10,pady=10,bg="#ED6B4F")
show_demo.grid(row=7,column=0)
w.mainloop()