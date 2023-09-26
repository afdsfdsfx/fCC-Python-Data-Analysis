'''
Project No.: 2
Project Title: Demographic Data Analyzer	
Date Completed: 2023-02-21



Instructions: 
	In this challenge, you must analyze demographic data using Pandas. You are given a dataset of demographic data that was extracted from the 1994 Census database. Here is a sample of what the data looks like:

		|    |   age | workclass        |   fnlwgt | education   |   education-num | marital-status     | occupation        | relationship   | race   | sex    |   capital-gain |   capital-loss |   hours-per-week | native-country   | salary   |
		|---:|------:|:-----------------|---------:|:------------|----------------:|:-------------------|:------------------|:---------------|:-------|:-------|---------------:|---------------:|-----------------:|:-----------------|:---------|
		|  0 |    39 | State-gov        |    77516 | Bachelors   |              13 | Never-married      | Adm-clerical      | Not-in-family  | White  | Male   |           2174 |              0 |               40 | United-States    | <=50K    |
		|  1 |    50 | Self-emp-not-inc |    83311 | Bachelors   |              13 | Married-civ-spouse | Exec-managerial   | Husband        | White  | Male   |              0 |              0 |               13 | United-States    | <=50K    |
		|  2 |    38 | Private          |   215646 | HS-grad     |               9 | Divorced           | Handlers-cleaners | Not-in-family  | White  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
		|  3 |    53 | Private          |   234721 | 11th        |               7 | Married-civ-spouse | Handlers-cleaners | Husband        | Black  | Male   |              0 |              0 |               40 | United-States    | <=50K    |
		|  4 |    28 | Private          |   338409 | Bachelors   |              13 | Married-civ-spouse | Prof-specialty    | Wife           | Black  | Female |              0 |              0 |               40 | Cuba             | <=50K    |

        
	You must use Pandas to answer the following questions:

		- How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
		- What is the average age of men?
		- What is the percentage of people who have a Bachelor's degree?
		- What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
		- What percentage of people without advanced education make more than 50K?
		- What is the minimum number of hours a person works per week?
		- What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
		- What country has the highest percentage of people that earn >50K and what is that percentage?
		- Identify the most popular occupation for those who earn >50K in India.
	
    Update the code so all variables set to "None" are set to the appropriate calculation or code. Round all decimals to the nearest tenth.
'''


# Importing necessary libraries
import pandas as pd
import numpy as np





# Creating the required function
def calculate_demographic_data(print_data = True):
    
    # Read data from file
    df = pd.read_csv(
        'demographic_data.csv',
        header = 0
	    )


    # 1. How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None
    
    race_count = df['race']
    race_count.index = df['race']

    race_count = df['race'].value_counts()




    # 2. What is the average age of men?
    average_age_men = None

    df_male = df[df['sex'] == 'Male']

    average_age_men = np.round(
        df_male['age'].mean(),
        decimals = 1
        )

    


    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None
    
    total_population = df['education'].value_counts().sum()
    bachelors_only = df[df['education'] == 'Bachelors'].value_counts().sum()

    percentage_bachelors = np.round(
        bachelors_only / total_population * 100,
        decimals = 1
        )




    # 4. What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K? 
    higher_education_rich = None
    
    adv_education = df[
        (df['education'] == 'Bachelors') |
        (df['education'] == 'Masters') | 
        (df['education'] == 'Doctorate')
        ]
    
    adv_education_total_population = adv_education['education'].value_counts().sum()
    adv_education_population_50K = adv_education[adv_education['salary'] == '>50K'].value_counts().sum()

    higher_education_rich = np.round(
        adv_education_population_50K / adv_education_total_population * 100,
        decimals = 1
        )




    # 5. What percentage of people without advanced education make more than 50K?
    lower_education_rich = None
    
    wo_adv_education = df[~(
        (df['education'] == 'Bachelors') | 
        (df['education'] == 'Masters') | 
        (df['education'] == 'Doctorate')
        )]

    wo_adv_education_total_population = wo_adv_education.value_counts().sum()
    wo_adv_education_population_50K = wo_adv_education[wo_adv_education['salary'] == '>50K'].value_counts().sum()

    lower_education_rich = np.round(
        wo_adv_education_population_50K / wo_adv_education_total_population * 100,
        decimals = 1
        )




    # 6. What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    
    min_work_hours = df['hours-per-week'].min()




    # 7. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    rich_percentage = None

    df_min_hours = df[df['hours-per-week'] == min_work_hours]

    min_hours_total_population = df_min_hours.value_counts().sum()
    min_hours_50K_population = df_min_hours[df_min_hours['salary'] == '>50K'].value_counts().sum()

    rich_percentage = np.round(
        min_hours_50K_population / min_hours_total_population * 100,
        decimals = 1 
        )




    # 8. What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    rich_country = {}

    for i in df['native-country'].value_counts().index:
        country = df[df['native-country'] == i]

        high_salary = country[country['salary'] == '>50K'].value_counts().sum()
        all_salary = country['salary'].value_counts().sum()

        earn_percent = np.round(
            high_salary / all_salary * 100, 
            decimals = 1
            )
        
        rich_country.update({**rich_country, i:earn_percent})

    pd_rich_country = pd.Series(rich_country)

    highest_earning_country_percentage = pd_rich_country.max()
    highest_earning_country = pd_rich_country[pd_rich_country == pd_rich_country.max()].index[0]




    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    
    IN_50K_occupation = df[
        (df['salary'] == '>50K') & 
        (df['native-country'] == 'India')
        ]

    top_IN_occupation = IN_50K_occupation['occupation'].value_counts().index[0]




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