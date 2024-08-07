
# Exercise 1  (note the interference also of the constant in the models)

import statsmodels.formula.api as smf
est_both = smf.ols(formula='target ~ RAD + TAX', data=boston).fit()

est_both.summary()  # For me, RAD beta is 0.2762, TAX is -0.0386 (nearly zero)

est_rad = smf.ols(formula='target ~ RAD', data=boston).fit()
est_rad.summary()  # RAD coeff = -0.4031

est_tax = smf.ols(formula='target ~ TAX', data=boston).fit()
est_tax.summary()  # TAX coeff = -0.0256

# Exercise 2

Y = np.random.random(1000)

X1 = Y * 3 + 5
X2 = Y / 2

data = pd.Series({"X1": X1, "X2": X2, "Y": Y})

est_corr = smf.ols(formula="Y ~ X1 + X2", data=data).fit()
est_corr.summary()  # note how the sum of the beta values is about 1 - they are interfering with each other


''' copied from exercise where we detrend wheat and gold data
from sklearn.linear_model import LinearRegression
X=np.arange(len(prices)).reshape(-1,1)
y1=prices['gold']
reg1 = LinearRegression().fit(X,y1)
y2=prices['wheat']
reg2 = LinearRegression().fit(X,y2)

det1=reg1.predict(X)
plt.plot(prices.index,det1)
plt.plot(prices['gold'])
det2=reg2.predict(X)
plt.plot(prices.index,det2)
plt.plot(prices['wheat'])

detrended_prices=pd.DataFrame(data=np.vstack((det1,det2)).T,index=prices.index,columns=prices.columns)
detrended_prices=prices-detrended_prices
detrended_prices.plot()
'''