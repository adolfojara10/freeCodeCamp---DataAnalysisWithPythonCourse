import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    data = pd.read_csv("Exercise 2 - Demographic Data Analyzer/adult.data.csv")
    races = data['race'].unique()
    quantity = []

    for i in range(len(races)):
        n = data[data['race'] == races[i]].count()[0]
        quantity.append(n)
        
    race_count = pd.Series(quantity, index=races)

    # What is the average age of men?
    men = data[data['sex'] == 'Male']
    ages = men['age']
    ag = np.array(ages)
    
    average_age_men = ag.mean()

    # What is the percentage of people who have a Bachelor's degree?
    bach = data[data['education'] == 'Bachelors'].count()[0]
    
    percentage_bachelors = (bach/32561)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    mon = data[data['education'] == 'Bachelors']
    mas = data[data['education'] == 'Masters']
    doc = data[data['education'] == 'Doctorate']
    number = mon[mon['salary'] == '>50K'].count()[0]
    number += mas[mas['salary'] == '>50K'].count()[0]
    number += doc[doc['salary'] == '>50K'].count()[0]
    l = data[(data['education'] == 'Bachelors') | (data['education'] == 'Masters') | (data['education'] == 'Doctorate')].count()[0]
    
    ppp =data[(data['education'] != 'Bachelors') & (data['education'] != 'Masters') & (data['education'] != 'Doctorate')]
    numPP = ppp[ppp['salary'] == '>50K'].count()[0]
    nop = ppp.count()[0]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = number
    lower_education = numPP

    # percentage with salary >50K
    higher_education_rich = (number/l)*100
    lower_education_rich = (numPP/nop)*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hours = np.array(data['hours-per-week'])
    min_work_hours = work_hours.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    people_above_50 = data[(data['hours-per-week'] == work_hours.min()) & (data['salary'] == '>50K')].count()[0]
    
    num_min_workers = data[data['hours-per-week'] == work_hours.min()].count()[0]

    rich_percentage = (people_above_50/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    countries = data['native-country'].unique()
    above_50 = data[data['salary'] == '>50K']
    
    number_people = []

    for i in range(len(countries)):
        number_people.append(above_50[above_50['native-country'] == countries[i]].count()[0])
    
    dataframe = pd.DataFrame(number_people, index=countries)
    col = ['Number']

    dataframe.columns = col 
    dataframe['%'] = (dataframe['Number']/above_50.count()[0])*100
    
    maximo = dataframe['%'].max() 
    country = dataframe[dataframe['%'] == maximo]
    country = country.reset_index()
    pays = str(country['index'][0])
    
    highest_earning_country = pays
    highest_earning_country_percentage = maximo

    # Identify the most popular occupation for those who earn >50K in India.
    india = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    jobs = india['occupation'].unique()
    
    list_india = []

    for i in range(len(jobs)):
        list_india.append(india[india['occupation'] == jobs[i]].count()[0])
    
    serie_india = pd.Series(list_india, index=jobs)
    maximo_india = serie_india.max()
    occupation = str(serie_india[serie_india == maximo_india])
    
    top_IN_occupation = occupation

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
