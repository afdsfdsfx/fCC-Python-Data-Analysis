import pandas as pd
import numpy as np


def calculate_demographic_data(print_data = True):
    # Read data from file
    df = pd.read_csv('demographic_data.csv',
                     header = 0
                     )

    # 1. How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race']
    race_count.index = df['race']

    race_count = df['race'].value_counts()

    race_count = pd.Series(race_count)


    # 2. What is the average age of men?
    male_only = df[df['sex'] == 'Male']
    np_male_age = np.array(male_only['age'])

    np_ave_male_age = np_male_age.mean()

    average_age_men = np.around(np_ave_male_age,
                                decimals = 1)
    

    # 3. What is the percentage of people who have a Bachelor's degree?
    total_population = np.array(df['education'].value_counts()).sum()
    
    bachelors_only = df[df['education'] == 'Bachelors']
    bachelors_only = np.array(bachelors_only['education'].value_counts()).sum()
    
    percentage_bachelors = (bachelors_only / total_population) * 100
    
    percentage_bachelors = np.around(percentage_bachelors, 
                                    decimals = 1)


    # 4. What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? 
    adv_ed = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    
    total_adv_ed = np.array(adv_ed['education'].value_counts()).sum()
    
    adv_ed_high_salary = adv_ed[adv_ed['salary'] == '>50K']
    total_adv_ed_high_salary = np.array(adv_ed_high_salary['salary'].value_counts()).sum()
    percent_adv_ed_high_salary = (total_adv_ed_high_salary / total_adv_ed) * 100
    
    higher_education_rich = np.around(percent_adv_ed_high_salary, 
                                      decimals = 1)


    # 5. What percentage of people without advanced education make more than 50K?
    
    not_adv_ed = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    
    wo_adv_ed_total = np.array(not_adv_ed['education'].value_counts()).sum()
    
    wo_adv_ed_high_salary = not_adv_ed[not_adv_ed['salary'] == '>50K']
    wo_adv_ed_high_salary_total = np.array(wo_adv_ed_high_salary['education'].value_counts()).sum()
    percent_wo_adv_ed_high_salary = (wo_adv_ed_high_salary_total/wo_adv_ed_total) * 100
    
    lower_education_rich = np.around(percent_wo_adv_ed_high_salary, decimals = 1)


    # 6. What is the minimum number of hours a person works per week (hours-per-week feature)?
    hrs_per_wk = df['hours-per-week']
    
    min_work_hours = np.array(hrs_per_wk).min()


    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_df = df[df['hours-per-week'] == min_work_hours]

    min_hours_high_salary = min_hours_df[min_hours_df['salary'] == '>50K']['salary'].value_counts()
    np_rich = np.array(min_hours_high_salary)
    np_rich_total = np.array(min_hours_df['salary'].value_counts()).sum()

    rich_percentage = (np_rich/np_rich_total) * 100
    rich_percentage = np.around(rich_percentage, 
                                decimals = 1)

    # 8. What country has the highest percentage of people that earn >50K?
    rich_country = {}

    country_list = df['native-country']

    for i in country_list.value_counts().index:
        country = df[df['native-country'] == i]

        high_salary = country[country['salary'] == '>50K'].value_counts()
        np_high = np.array(high_salary).sum()

        all_salary = country['salary'].value_counts()
        np_all = np.array(all_salary).sum()

        percentage = (np_high/np_all) * 100
        earn_percent = np.around(percentage, 
                                decimals = 1)
        
        rich_country.update({**rich_country, i:earn_percent})
        
    rich_country_series = pd.Series(rich_country)

    highest_earning_country_percentage = rich_country_series.max()
    highest_earning_country = rich_country_series[rich_country_series == rich_country_series.max()].index[0]


    # 9. Identify the most popular occupation for those who earn >50K in India.
    india = df[df['native-country'] == 'India']
    indian_works_high_salary = india[india['salary'] == '>50K']
    
    popular_india = pd.Series(indian_works_high_salary['occupation'].value_counts())
    
    top_IN_occupation = popular_india.index[0]


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
