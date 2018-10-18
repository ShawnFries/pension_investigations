import numpy as np
from scipy import stats
import matplotlib.pyplot
NUMBER_OF_EMPLOYEES = 1000
RETIREMENT_AGE = 65
MAX_TYPICAL_LIFESPAN = 100 # The beta distribution is defined for 0 to 1, so we need to scale to 0 to 1
NUMBER_OF_YEARS = 100
EMPLOYEE_AGE = 45

#LIFESPAN_FOLLOWS_BETA_DISTRIBUTION = True # Unused for anything currently

# Note: the beta distribution has 2 parameters, alpha and beta
ALPHA_PARAMETER = 5
BETA_PARAMETER = 10
# Further note: the mean of a beta distribution is alpha / (alpha + beta) so for employee age 45 (5, 10) implies an average lifespan of 33+45 = 78

TURNOVER_PER_YEAR = 0.1  # If turnover = 1, entirely new workforce each year; if turnover is 0, workforce never changes

# With no error/variance in expected lifespan per person, number of employees who reach retirement age
print("")
employee_lifespans = np.random.beta(ALPHA_PARAMETER, BETA_PARAMETER, NUMBER_OF_EMPLOYEES) * MAX_TYPICAL_LIFESPAN + EMPLOYEE_AGE
#print(employee_lifespans)
for year_number in range(NUMBER_OF_YEARS):

    number_reaching_retirement_age = (employee_lifespans >= RETIREMENT_AGE / MAX_TYPICAL_LIFESPAN).sum()
    print("Number reaching retirement age: " + str(number_reaching_retirement_age))

    print("With sample mean: " + str(np.mean(employee_lifespans)))
    print("And sample standard deviation: " + str(np.std(employee_lifespans, ddof=1))) # The 1 takes the unbiased (sample) standard deviation
    print("And skew: " + str(stats.skew(employee_lifespans)))
    print(str(stats.skewtest(employee_lifespans)))

    # Use bin width of 1
    matplotlib.pyplot.hist(employee_lifespans, range(int(np.floor(min(employee_lifespans))), int(np.ceil(max(employee_lifespans)))))
    matplotlib.pyplot.title('Expected lifespans for population of 1000 employees all initially age 45 if everyone has the same lifespan probability distribution (those distributions are NOT normally distributed)')
    matplotlib.pyplot.show()

    np.random.shuffle(employee_lifespans)
    turnover_count = int(NUMBER_OF_EMPLOYEES * TURNOVER_PER_YEAR)
    employee_lifespans[0:turnover_count] = np.random.beta(ALPHA_PARAMETER, BETA_PARAMETER, turnover_count) * MAX_TYPICAL_LIFESPAN + EMPLOYEE_AGE