import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:

            city_input = input("Please choose city name from this list(chicago , new york city , washington): ").lower()
            if city_input in CITY_DATA:
                city = CITY_DATA[city_input]
            while city_input not in CITY_DATA:
                city = input ('\n Invalid answer please choose one from this list(chicago , new york city , washington)').lower()

            month_input = input("Please choose month from this list(january , february , march , april , may , june ,or all): ").lower()
            if month_input in months:
                month = month_input
            while month_input not in months:
                month = input ('\n Invalid answer please choose one from this list (january , february , march , april , may , june ,or all)').lower()

            day_input = input("Please choose day from this list(monday , tuesday , wednesday , thursday , friday , saturday , sunday , or all): ").lower()
            if day_input in days:
                day = day_input
            while day_input not in days:
                day = input ('\n Invalid answer please choose one from this list(monday , tuesday , wednesday , thursday , friday , saturday , sunday , or all)')


            print("You choose " , city, month, day)
            confairming = input(" (yes or no) :").lower()
            if confairming  == 'yes' :
                break
            else :
                continue

    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start_hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0].astype(str)
    print("The most common month is : " , common_month.title())

    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is : " , common_day_of_week.title())

    common_start_hour = df['start_hour'].mode()[0]
    print("The most common start hour is : " , common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " , start)

    end = df['End Station'].mode()[0]
    print("The most commonly used end station is: " , end)

    df['combination'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    combination = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: " , combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print("The total travel hours is: " , total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel hours is: " , mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("The count of user types is: " , user_types)
    try:

        gender = df['Gender'].value_counts()
        print("The count of gender is: " , gender)

    except:
        print('there is no gender data')
        pass

    try:
        earliest_birth = df['Birth Year'].min()
        print("Earliest birth from the given fitered data is: " , earliest_birth)

        most_recent_birth = df['Birth Year'].max()
        print("Most recent birth from the given fitered data is: " , most_recent_birth)

        most_common_birth = df['Birth Year'].mode()[0]
        print("Most common birth from the given fitered data is: ", most_common_birth)
    except:
        print('there is no birth data')
        pass


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(df):
    """View 5 lines of raw data."""

    i = 0
    raw_input = input("Would you like to view next five row of raw data? Enter yes or no ").lower()
    while True:

        if raw_input == 'no':
            break


        elif raw_input == 'yes':
            print(df.iloc[i : i+5])
            raw = input("Would you like to view next five row of raw data? Enter yes or no ").lower()
            i += 5
            if raw == 'no':
                break

        else:
            raw_input = input("\n Invalid answer please try again , Enter yes or no ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("\nExplore US bike share data is done. ")
            break



if __name__ == "__main__":
	main()
