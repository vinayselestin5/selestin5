import matplotlib.pyplot as plt
vinay=[1,2,3,4,5]
varsha=[10,20,30,40,15,]
tick_label=['one','two','three','foure','five']
plt.bar(vinay, varsha, tick_label= tick_label, 
	    width = 0.5,color = ['blue','black','red'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('cl1 bar')
plt.show()