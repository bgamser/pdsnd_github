#Test Test
#This test is for the second additional changes to documentation !!
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
     
    city =['']

    while city != 'chicago' or city != 'new york' or city != 'washington':
        city = input("Hello! Let's explore some US bikeshare data!\nWhich city would you like to explore data for?\n\t1.Chicago\n\t2.New York\n\t3.Washington\n\nType the name of the city below:\n")
        
        city = city.lower()
        
        if city == 'chicago' or city =='new york' or city == 'washington':
            break


   # TO DO: get user input for month (all, january, february, ... , june)
    month = ['']
       
    while month != 'jan' or month != 'feb' or month != 'mar' or month != 'apr' or month != 'may' or month != 'jun' or month != 'all':
        
        month = input("For which months would you like to see data for:\n1.Jan\n2.Feb\n3.Mar\n4.Apr\n5.May\n6.Jun\n7.all --> No specific month (All of them)")
        
        month = month.lower()
        
        if month == 'jan' or month == 'feb' or month == 'mar' or month == 'apr' or month == 'may' or month == 'jun' or month == 'all':
            break


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ['']
      
    while day != 'sun' or day != 'mon' or day != 'tue' or day != 'wed' or day != 'thu' or day != 'fri' or day != 'sat' or day != 'all':
        
        day = input("For which days would you like to see data for:\n1.Sun\n2.Mon\n3.Tue\n4.Wed\n5.Thu\n6.Fri\n7.Sat\n8.all --> No specific day (All of them)")
        
        day = day.lower()
        #Here is where i am adding another comment for refactoring !!!
        if day == 'sun' or day == 'mon' or day == 'tue' or day == 'wed' or day == 'thu' or day == 'fri' or day == 'sat' or day == 'all':
            break            
            
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

    df = pd.read_csv(CITY_DATA[city])
    
    ans = 'yes'
    i = 5
    while ans != 'no':
    
        ans = input("would you like to see a snapshot of the first %i lines of raw data?\nAnswer by typing: No or Yes\n" %i)
        ans = ans.lower()
        
        if ans == 'no':
            break
        
        else:
            pd.set_option('display.max_columns', None)
            print(df.head(i))
            i +=5
    
#    To understand the data, needed print(df.column())
    
#    Start-time is string --> need to convert it into datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
#    Need to make column for day, month match exactly how they are inputed from the user (e.g Jan, Sat)
    df['c_month'] = df['Start Time'].dt.month_name().str.slice(stop=3)
    df['c_month']=df['c_month'].str.lower()
    df['c_day'] = df['Start Time'].dt.day_name().str.slice(stop=3)
    df['c_day']=df['c_day'].str.lower()
    df['c_hour'] = df['Start Time'].dt.hour
    
#     pd.set_option('display.max_columns', None)
#     print(df)
#   Based on research: loc is the most readable; Thus, i chose to use this kind of filter as opposed to query and dateframing a dataframe 
    if month != 'all':
            df = df.loc[(df.c_month == month)]
            
    if day != 'all':
        
        df = df.loc[(df.c_day == day)]
        
        
#     print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mc_month = df['c_month'].value_counts().idxmax()
    
    print('most common month: is: ----------'+ mc_month + '--------------')
    

    # TO DO: display the most common day of week

    
    mc_day = df['c_day'].value_counts().idxmax()
    
    print('most common day: is: ----------'+ mc_day + '--------------')
    

    # TO DO: display the most common start hour
  
    mc_hour = df['c_hour'].value_counts().idxmax()
    
    print('most common hour:', mc_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    mc_start_station = df['Start Station'].value_counts().idxmax()
    print('most common start station:', mc_start_station)
    
    # TO DO: display most commonly used end station
    
    mc_end_station = df['End Station'].value_counts().idxmax()
    print('most common end station:', mc_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip

    df['combo_dest'] = df['Start Station']+ ' --> ' + df['End Station']
    mc_combo_dest = df['combo_dest'].value_counts().idxmax()
    print('most common combo destination:', mc_combo_dest)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time :", travel_time)

    # TO DO: display mean travel time
    travel_time = df['Trip Duration'].mean()
    print("Mean time :", travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print(user_type_count)

    # TO DO: Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
        
    except KeyError:
        print('No Gender Column in Washington - Sorry !')

    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        Dob = df['Birth Year']
        mc_dob = Dob.value_counts().idxmax()
        print('most common year of birth is:', mc_dob )

        mr_dob = Dob.max()
        print('most recent year of birth is:', mr_dob )

        early_dob = Dob.min()
        print('earliest year of birth is:', early_dob )

    except KeyError:
        print('No Birth Year Column either - Sorry again !')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
