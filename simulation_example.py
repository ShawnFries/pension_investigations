# Requires numpy and scipy
# TODO: add graphs

import numpy as np
from scipy import stats
NUMBER_OF_EMPLOYEES = 1000
#TURNOVER_PER_YEAR = 0 # Currently unused
RETIREMENT_AGE = 65
MAX_LIFESPAN = 100 # The beta distribution is defined for 0 to 1, so we need to scale to 0 to 1
NUMBER_OF_SIMULATIONS = 100

LIFESPAN_FOLLOWS_BETA_DISTRIBUTION = True # Unused for anything currently

# Note: the beta distribution has 2 parameters, alpha and beta
ALPHA_PARAMETER = 20
BETA_PARAMETER = 5
# Further note: the mean of a beta distribution is alpha / (alpha + beta)

# With no error/variance in expected lifespan per person, number of employees who reach retirement age
print("")
print("Number making it to retirement if everyone has the same lifespan probability distribution (NOT normally distributed)")
array_of_number_making_retirement_age = []
for repetition_number in range(NUMBER_OF_SIMULATIONS):
    number_reaching_retirement_age = (np.random.beta(ALPHA_PARAMETER, BETA_PARAMETER, NUMBER_OF_EMPLOYEES) >= RETIREMENT_AGE / MAX_LIFESPAN).sum()
    array_of_number_making_retirement_age = np.append(array_of_number_making_retirement_age, number_reaching_retirement_age)
    print(number_reaching_retirement_age)

print("With sample mean: " + str(np.mean(array_of_number_making_retirement_age)))
print("And sample standard deviation: " + str(np.std(array_of_number_making_retirement_age, ddof=1))) # The 1 takes the unbiased (sample) standard deviation
print("And skew: " + str(stats.skew(array_of_number_making_retirement_age)))
print(str(stats.skewtest(array_of_number_making_retirement_age)))


# With normal errors/variance in expected lifespan per person
# For varying lifespan by person (assuming error terms are themselves normally distributed)
ALPHA_PARAMETER_RANDOM_ERROR_MEAN = 0
ALPHA_PARAMETER_RANDOM_ERROR_ST_DEV = 4
BETA_PARAMETER_RANDOM_ERROR_MEAN = 0
BETA_PARAMETER_RANDOM_ERROR_ST_DEV = 1

alpha_parameter_errors = np.random.normal(ALPHA_PARAMETER_RANDOM_ERROR_MEAN, ALPHA_PARAMETER_RANDOM_ERROR_ST_DEV, NUMBER_OF_EMPLOYEES)
beta_parameter_errors = np.random.normal(BETA_PARAMETER_RANDOM_ERROR_MEAN, BETA_PARAMETER_RANDOM_ERROR_ST_DEV, NUMBER_OF_EMPLOYEES)

# With random error per person, number of employees who reach retirement age
# Also ensures the person makes it to at least 1 year old
print("")
print("Number making it to retirement if people's lifespans have normally distributed errors")

array_of_number_making_retirement_age = []
for repetition_number in range(NUMBER_OF_SIMULATIONS):
    number_reaching_retirement_age = 0
    for i in range(NUMBER_OF_EMPLOYEES):
        if np.random.beta(max(ALPHA_PARAMETER + alpha_parameter_errors[i], 0.01), max(BETA_PARAMETER + beta_parameter_errors[i], 0.01)) > RETIREMENT_AGE / MAX_LIFESPAN:
            number_reaching_retirement_age += 1
    array_of_number_making_retirement_age = np.append(array_of_number_making_retirement_age, number_reaching_retirement_age)
    print(number_reaching_retirement_age)
print("With sample mean: " + str(np.mean(array_of_number_making_retirement_age)))
print("And sample standard deviation: " + str(np.std(array_of_number_making_retirement_age, ddof=1))) # The 1 takes the unbiased (sample) standard deviation
print("And skew: " + str(stats.skew(array_of_number_making_retirement_age)))
print(str(stats.skewtest(array_of_number_making_retirement_age)))

# With exponential errors/variance in expected lifespan per person
# For varying lifespan by person (assuming error terms are themselves normally distributed)
ALPHA_PARAMETER_RANDOM_ERROR_LAMBDA = 4
BETA_PARAMETER_RANDOM_ERROR_LAMBDA = 4

alpha_parameter_errors = np.random.exponential(ALPHA_PARAMETER_RANDOM_ERROR_LAMBDA, NUMBER_OF_EMPLOYEES)
beta_parameter_errors = np.random.exponential(BETA_PARAMETER_RANDOM_ERROR_LAMBDA, NUMBER_OF_EMPLOYEES)

# With random error per person, number of employees who reach retirement age
# Also ensures the person makes it to at least 1 year old
print("")
print("Number making it to retirement if people's lifespans have exponentially distributed errors")

array_of_number_making_retirement_age = []
for repetition_number in range(NUMBER_OF_SIMULATIONS):
    number_reaching_retirement_age = 0
    for i in range(NUMBER_OF_EMPLOYEES):
        if np.random.beta(max(ALPHA_PARAMETER + alpha_parameter_errors[i], 0.01), max(BETA_PARAMETER + beta_parameter_errors[i], 0.01)) > RETIREMENT_AGE / MAX_LIFESPAN:
            number_reaching_retirement_age += 1
    array_of_number_making_retirement_age = np.append(array_of_number_making_retirement_age, number_reaching_retirement_age)
    print(number_reaching_retirement_age)
print("With sample mean: " + str(np.mean(array_of_number_making_retirement_age)))
print("And sample standard deviation: " + str(np.std(array_of_number_making_retirement_age, ddof=1))) # The 1 takes the unbiased (sample) standard deviation
print("And skew: " + str(stats.skew(array_of_number_making_retirement_age)))
print(str(stats.skewtest(array_of_number_making_retirement_age)))

# Keep lifespans the same for .9 of population that preserves, .1 turnover rate with new population each time.. or variable turnover (if varies 100% each time should exhibit central limit theorem)
# With 100% turnover, should give skewed distribution right? exact distribution of skewed amount
# Make plots for this
# Make github repo for this
# Explore assumption that errors cancel out