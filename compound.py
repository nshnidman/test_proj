#!/usr/bin/python

salary = 175000 # Initial salary
p = 100000# Principal
i = .05 # Interest Rate
y = 25 # Number of years
cr = 0.15 # Contribution rate
yr = .03
print "Contribution Rate", cr, "Interest Rate", i, \
    "Number of Years", y
for nn in range(1,y+1):
    c = cr*salary # Contribution amount
    p = p*(1+i)+c # Principal grows with interest plus new contribution
    print "Current salary is", salary, "in year", nn, \
    "; Contribution is", c
    salary = salary*(1+yr) # Raise per year
print "Compounded Ammount", p
