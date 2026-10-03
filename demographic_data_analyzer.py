import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read the data
    df = pd.read_csv(
        "adult.data.csv",
        skipinitialspace=True
    )

    # 1. Number of people of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(),
        1
    )

    # 3. Percentage of people who have a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # 4. Percentage of people with higher education
    # who earn more than 50K
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )

    higher_education_rich = round(
        (df[higher_education]["salary"] == ">50K").mean() * 100,
        1
    )

    # 5. Percentage of people without higher education
    # who earn more than 50K
    lower_education = ~higher_education

    lower_education_rich = round(
        (df[lower_education]["salary"] == ">50K").mean() * 100,
        1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people who work the minimum number
    # of hours and earn more than 50K
    min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (min_workers["salary"] == ">50K").mean() * 100,
        1
    )

    # 8. Country with the highest percentage of people
    # earning more than 50K
    country_rich = df[
        df["salary"] == ">50K"
    ].groupby("native-country").size()

    country_total = df.groupby(
        "native-country"
    ).size()

    country_percentage = (
        country_rich / country_total * 100
    ).dropna()

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(
        country_percentage.max(),
        1
    )

    # 9. Most popular occupation in India
    # among people earning more than 50K
    india_rich = df[
        (df["native-country"] == "India") &
        (df["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_rich["occupation"]
        .value_counts()
        .idxmax()
    )

    # Print results
    if print_data:
        print("Number of each race:")
        print(race_count)

        print("Average age of men:", average_age_men)

        print(
            "Percentage of people with a Bachelor's degree:",
            percentage_bachelors
        )

        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )

        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )

        print(
            "Min work time:",
            min_work_hours,
            "hours/week"
        )

        print(
            "Percentage of rich among min workers:",
            rich_percentage
        )

        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )

        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )

        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }