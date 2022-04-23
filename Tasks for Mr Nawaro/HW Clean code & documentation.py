import pandas as pd


#Ex.1

def fizz_buzz():
    '''
    Function  iterates over a list of numbers from 1 to 100, but multiples of 3 and
    of 5 should be replaced with  “Fizz” and “Buzz” respectively.
     For numbers which are multiples of both 3 and 5 print “FizzBuzz”.
     '''

    for i in range (1,101):
        #checking whether a number is divisible by 3 and not divisible by 5 in the same time
        if i%3 == 0 and i%5 != 0:
            print('Fizz')
        # checking whether a number is divisible by 5 and not divisible by 3 in the same time
        elif i%5== 0 and i%3 != 0:
            print('Buzz')
        # checking whether a number is divisible by 5 and 3 in the same time
        elif i%5== 0 and i%3== 0:
            print('FizzBuzz')
        #printing a number as it is in all other cases
        else:
            print(str(i))

fizz_buzz()

#Ex. 2a - no solution :(


#Ex.3

#reading an imported from the internet dataset into a pd dataframe
us_dataset = pd.read_csv('uscities.csv')

#checking the column names to see how the column with the names of states is called
print(us_dataset.columns)

#storing unique list of states names in a list
us_states = us_dataset['state_name'].unique()

#putting the name of the states in upper and lowercase to a pandas data frame
d = pd.DataFrame({'upper':[state.upper() for state in us_states], 'lower':[state.lower() for state in us_states ]})

#saving a file in a .csv format
d.to_csv('states.csv')


#Ex. 4

#importing a dataset
studPerformance = pd.read_csv('StudentsPerformance.csv')

# print mean math score for each group of students by their race/ethnicity
print(studPerformance.groupby("race/ethnicity")['math score'].mean())


# print mean math, reading, and writing scores for students who completed the
# test preparation course and their parent obtained a degree
degree_test = studPerformance.loc[(studPerformance['test preparation course'] == 'completed') & (studPerformance['parental level of education'].isin(["associate's degree", "bachelor's degree", "master's degree"]))]

for column in ['math score', 'reading score', 'writing score']:
    print(column, degree_test[column].mean())


# As I don't have a better idea how to improve  the plot, I would leave it as it is.





