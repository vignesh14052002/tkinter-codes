from tkinter import *
from tkinter import ttk
from itertools import permutations

# logic behind this(overview)
# strli shows all combinations of expression with two operators and four numbers
# replace 1,2 in strli with our operators
# check if user result matches expression results for all permutations
# if matched display it

def main(a,b,c,d,r,op):
	global strli,result,possiblites,t1,l4
	a,b,c,d=int(a),int(b),int(c),int(d)
	commutative=["+","*"]
	strli=["((a1b)1c)1d","((a2b)2c)2d","((a1b)1c)2d","((a2b)1c)1d","((a1b)2c)1d","((a1b)2c)2d","((a2b)1c)2d","((a2b)2c)1d"]
	#replacing 1,2 with our operators
	strli[0]=strli[0].replace("1",str(op[0]))
	strli[1]=strli[1].replace("2",str(op[1]))
	for j in range(2,len(strli)):
		strli[j]=strli[j].replace("1",str(op[0]))
		strli[j]=strli[j].replace("2",str(op[1]))
	possiblites=[]
	def replace(a,b,c,d,i):
		global strli,possiblites
		val=strli[i].replace("a",str(a))
		val=val.replace("b",str(b))
		val=val.replace("c",str(c))
		val=val.replace("d",str(d))
		possiblites.append(val)    
	
	if r==eval(strli[0]):
		replace(a,b,c,d,0)

	if r==eval(strli[1]):
		replace(a,b,c,d,1)
	result=r
	def check(a,b,c,d):
		i=0
		if op[0] in commutative or op[1] in commutative:
			i=2
		global r,strli,possiblities

		while i<len(strli):
		 	 if eval(strli[i])==result:
		 	 	replace(a,b,c,d,i)
		 	 i+=1

	combo=list(permutations([a,b,c,d],4))
	for i in combo:
		check(*i)
	possiblites=list(set(possiblites))
	display="possiblites\n"
	for i in possiblites:
		display+=i+"\n"
	if len(possiblites)==0:
		display="possiblities\nimpossible"
	if t1==1:
		l4.destroy()
	t1=1
	l4=Label(text=display)
	l4.grid(row=7,column=0)
t1=0
def execute():
	global t
	if t==1:
		l5.destroy()
		t=0
	a,b,c,d=str(e.get()).split(" ")
	li1=[]
	for i in range(len(li)):
		if li[i]==1:
			li1.append(op[i])
	r=e1.get()
	main(a,b,c,d,int(r),li1)
def checkbox(i,v):
	#restrict to select only two checkboxes
	li[i]=v
	
	if li.count(0)<2:
		d=li.index(1)
		cb[d].deselect()
		li[d]=0
t=0

def demo():
	global t,l5,l5_text
	l5_text="enter four numbers :2 4 5 1\n select operators + -\n result 8\n possiblities\n(output when you click submit)\n((1+4)+5)-2\n((1+5)+4)-2\n((4-2)+5)+1\n((4+1)+5)-2\n((4+5)-2)+1\n((4+5)+1)-2\n((5+1)+4)-2\n((4+1)-2)+5\n((5-2)+4)+1\n((5-2)+1)+4\n((1-2)+4)+5\n((5+4)+1)-2\n((4-2)+1)+5\n((1-2)+5)+4\n((5+4)-2)+1\n((1+5)-2)+4\n((1+4)-2)+5\n((5+1)-2)+4"
	
	if t==0:
		l5=Label(text=l5_text)
		l5.grid(row=7,column=0)
		t=1
	else:
		l5.destroy()
		t=0
	
	
li=[0,0,0,0]
op=["+","-","*","//"]
w=Tk()
w.title("expression predictor")

l=Label(w,text=" enter multiple inputs space seperated")
l.grid(row=0,column=1)
l1=Label(w,text="enter four numbers :")
l1.grid(row=1,column=0)
e=Entry(w)
e.grid(row=1,column=1)
l2=Label(w,text="select two operators")
l2.grid(row=2,column=0)
v1,v2,v3,v4=IntVar(),IntVar(),IntVar(),IntVar()
c_add=Checkbutton(w,text="+",variable=v1,command=lambda:checkbox(0,v1.get()))
c_add.grid(row=3,column=0)

c_sub=Checkbutton(w,text="-",variable=v2,command=lambda:checkbox(1,v2.get()))
c_sub.grid(row=3,column=1)

c_mul=Checkbutton(w,text="*",variable=v3,command=lambda:checkbox(2,v3.get()))
c_mul.grid(row=4,column=0)

c_div=Checkbutton(w,text="//",variable=v4,command=lambda:checkbox(3,v4.get()))
c_div.grid(row=4,column=1)

l3=Label(w,text="enter result :")
l3.grid(row=5,column=0)
e1=Entry(w)
e1.grid(row=5,column=1)


cb=[c_add,c_sub,c_mul,c_div]

submit=Button(text="submit",command=execute,padx=20,pady=10,bg="#ED6B4F")
submit.grid(row=6,column=1)
show_demo=Button(text="show demo",command=demo,padx=10,pady=10,bg="#ED6B4F")
show_demo.grid(row=6,column=0)
w.mainloop()