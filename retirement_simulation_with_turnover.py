import numpy as np
from scipy import stats
import matplotlib.pyplot
MONTE_CARLO_SIMULATION_NUMBER = 1000
NUMBER_OF_EMPLOYEES = 1000
RETIREMENT_AGE = 65
MAX_TYPICAL_LIFESPAN = 100 # The beta distribution is defined for 0 to 1, so we need to scale to 0 to 1
NUMBER_OF_YEARS = 10000
EMPLOYEE_AGE = 45
P_VALUE_FOR_SKEW_MIN = 0.025
P_VALUE_FOR_SKEW_MAX = 0.975

#LIFESPAN_FOLLOWS_BETA_DISTRIBUTION = True # Unused for anything currently

# Note: the beta distribution has 2 parameters, alpha and beta
ALPHA_PARAMETER = 5
BETA_PARAMETER = 10
# Further note: the mean of a beta distribution is alpha / (alpha + beta) so for employee age 45 (5, 10) implies an average lifespan of 33+45 = 78

TURNOVER_PER_YEAR = 0.1  # If turnover = 1, entirely new workforce each year; if turnover is 0, workforce never changes

# With no error/variance in expected lifespan per person, number of employees who reach retirement age
print("")
turnover_count = int(NUMBER_OF_EMPLOYEES * TURNOVER_PER_YEAR)
employee_lifespans = []
number_reaching_retirement_age = []
employee_lifespans.append(np.random.beta(ALPHA_PARAMETER, BETA_PARAMETER, NUMBER_OF_EMPLOYEES) * MAX_TYPICAL_LIFESPAN + EMPLOYEE_AGE)

years_required_to_reach_symmetry = 0
for simulation_run in range(MONTE_CARLO_SIMULATION_NUMBER):
    for year_number in range(NUMBER_OF_YEARS):

        number_reaching_retirement_age.append((employee_lifespans[-1] >= RETIREMENT_AGE).sum())

        #print("With sample mean of number expected to reach retirement: " + str(np.mean(number_reaching_retirement_age)))
        #print("And sample standard deviation of number expected to reach retirement : " + str(np.std(number_reaching_retirement_age, ddof=1))) # The 1 takes the unbiased (sample) standard deviation
        #print("And skew of number expected to reach retirement: " + str(stats.skew(number_reaching_retirement_age)))
        if year_number > 7:  # Skewtest requires at least 8 samples
            skewtest = stats.skewtest(number_reaching_retirement_age)[1]
            if skewtest < P_VALUE_FOR_SKEW_MIN or skewtest >= P_VALUE_FOR_SKEW_MAX:
                years_required_to_reach_symmetry += year_number
                break

        employee_lifespans.append(employee_lifespans[-1])
        np.random.shuffle(employee_lifespans[-1])
        employee_lifespans[-1][0:turnover_count] = np.random.beta(ALPHA_PARAMETER, BETA_PARAMETER, turnover_count) * MAX_TYPICAL_LIFESPAN + EMPLOYEE_AGE

        # Uncomment below to show graphs
        # Use bin width of 1
        """if year_number == 1 or year_number > 100 and year_number % 9 == 0:
            matplotlib.pyplot.hist(number_reaching_retirement_age, range(int(np.floor(min(number_reaching_retirement_age))), int(np.ceil(max(number_reaching_retirement_age)))))
            matplotlib.pyplot.title('Expected lifespans for population of ' + str(NUMBER_OF_EMPLOYEES) + ' employees all initially age ' + str(EMPLOYEE_AGE) + ' if everyone has the same lifespan probability distribution (those individual distributions are skewed)')
            matplotlib.pyplot.show()"""

print(years_required_to_reach_symmetry / MONTE_CARLO_SIMULATION_NUMBER)  # average years to reach symmetry


# TODO: Try another function for life expectancy (e.g. from wikipedia)
# TODO: Think more analytically about the longitudinal analysis/"mixture problem" aspect
# TODO: Solve numerically for years to approach normality (or no skew i.e. symmetry)
# TODO: Incorporate aging
