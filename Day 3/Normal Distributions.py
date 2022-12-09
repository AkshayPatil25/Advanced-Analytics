from scipy.stats import norm

#eg.1 Female Height
norm.cdf(58,64,4)

#eg.2 Weight of males
norm.sf(200,180,30)


# Amount Exceed 2000 
norm.sf(2000,1678,500)

# Daily Amount
#Top 10 %
norm.ppf(0.9,1678,500)

# Between 1000 to 1900
norm.cdf(1900,1678,500) - norm.cdf(1000,1678,500)


################################################################
# Fast food restaurant
norm.ppf(0.98,313,57)

norm.ppf(0.9,93,22)

p_a=norm.sf(450,313,57)
p_b=norm.sf(150,93,22)
p_a + p_b - p_a * p_b