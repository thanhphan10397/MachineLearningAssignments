import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

boston_data = load_boston()

#print(boston_data['DESCR'])

#take the boston data
data = boston_data['data']

#working with two of features: INDUS and RM
x_input = data[:, [2,5]]
y_target = boston_data['target']
print(x_input.shape)
print(y_target.shape)

#plot data for two features
plt.title("Industrialness vs Med House Price")
plt.scatter(x_input[:, 0], y_target)
plt.xlabel('Industrialness')
plt.ylabel('Med House Price')
plt.show()

plt.title('Avg Nb of Rooms vs Med House Price')
plt.scatter(x_input[:,1], y_target)
plt.xlabel('Avg Nb of Room')
plt.ylabel('Med House Price')
plt.show()

def cost(w1, w2, b, X, y):
	#input X and target y, and weight w1, w2, b

	costs = 0
	for i in range(len(y)):
		y_predict = w1*X[i,0] + w2*X[i,1] + b
		costs += (y_predict - y[i])**2
	return (0.5/len(y))*costs
#a = cost(3,5,20, x_input,y_target)
#print(a)


#Vectprizing the cost function
def cost_vectorized(w1, w2, b, X, y):
	w = np.array([w1, w2])
	y_predict = np.dot(X,w) + b*np.ones(len(y))

	return (0.5/len(y))*np.sum((y_predict - y)**2)
#b = cost_vectorized(3,5,20, x_input,y_target)
#print(b)


#Compare Speed
import time
t0 = time.time()
print(cost(3,5,20, x_input,y_target))
t1 = time.time()
print(t1-t0)

t2 = time.time()
print(cost_vectorized(3,5,20, x_input,y_target))
t3 = time.time()
print(t3-t2)

#Plotting cost in weight space
w1s = np.arange(-1.0, 0.0, 0.01)
w2s = np.arange(6.0, 10.0, 0.1)
z_cost = []

for w2 in w2s:
	z_cost.append([cost_vectorized(w1, w2, -22, x_input, y_target) for w1 in w1s])
z_cost = np.array(z_cost)
W1, W2 = np.meshgrid(w1s, w2s)

CS = plt.contour(W1, W2, z_cost, 25)
plt.clabel(CS, inline = 1)
plt.title('Costs for various values of w1 and w2 for b = 0')
plt.xlabel('w1')
plt.ylabel('w2')
plt.plot([-0.33471389], [7.82205511], 'o') # this will be the minima that we'll find later
plt.show()



#Exact Solution using Gradient Descent
x_in = np.concatenate([x_input, np.ones([np.shape(x_input)[0], 1])], axis = 1)

def gradfn(weights, X, y):

	N, D = np.shape(X)
	y_predict = np.matmul(X, weights)
	error = y_predict - y
	return np.matmul(np.transpose(X),error)/float(N)



def solve_via_gradient_descent(X, t, print_every = 5000, niter = 100000, alpha = 0.005):
	
	X_new = np.concatenate([X, np.ones([np.shape(x_input)[0],1])], axis = 1)
	N,D = np.shape(X_new)
	w  = np.zeros([D]) 	#initialize all the weights to zeros

	for k in range (niter):
		dw = gradfn(w, X_new, t)
		w = w - alpha*dw
		if k % print_every == 0:
			print('Weight after %d interation: %s' % (k, str(w)))
	return w 

solve_via_gradient_descent( X=x_input, t=y_target)

