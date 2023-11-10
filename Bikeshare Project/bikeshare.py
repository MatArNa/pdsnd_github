import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   # Get user input for city (chicago, new york city, washington).
 
    print('To start please choose between the next options: ')
    print('1.Chicago 2. New York City 3. Washington')
    print('Note: The valid way to input the city is by the complete name, for example: new york city')
    
    #Input variable to start the function    
    city = ''
    city_input = ''
        
    while city not in ['chicago', 'new york city', 'washington']:
        #To avoid an error if the user use upper case or another letter.
        city = input().lower()         
        
        #Condition to request the user to try again
        if city not in ['chicago', 'new york city', 'washington']:         
            print('So sorry, it appears that you input a wrong city name, to continue   please choose between the next options: ')
            print('1. Chicago 2. New York City 3. Washington')
            
        elif city == 'chicago':
            city_input = 'chicago.csv'
            
        elif city == 'new york city':
            city_input = 'new_york_city.csv'
            
        elif city == 'washington':
            city_input = 'washington.csv'
            
    #Text to validate the choice of the user        
    print('Well done you have input a valid option!')
    print('We\'ll proceed with {}'.format(city))
    
    
    # Get user input for month (all, january, february, ... , june)
    
    print('For the next step, please choose a month between the next options: ')
    print('1. January 2. February 3. March 4. April 5. May 6. June 7. All')
    print('Note: The valid way to input the month is by the complete name, for example: May')
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ''
    
    while month not in months:
          month = input().lower()
          
          if month not in months:
                print('So sorry, it appears that you input a wrong month, to continue please choose between the next options: ')
                print('1. January 2. February 3. March 4. April 5. May 6. June 7. All') 
                
    print('Well done you have input a valid option!')
    print('We\'ll proceed with {}'.format(month))

    # Get user input for day of week (all, monday, tuesday, ... sunday)

    print('For the next step, please choose a day between the next options: ')
    print('1. Monday 2. Tuesday 3. Wednesday 4. Thursday 5. Friday 6. Saturday 7. Sunday 8. All')
    print('Note: The valid way to input the day is by the complete name, for example: Sunday')
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = ''
    
    while day not in days:
        
            day = input().lower()
            
            if day not in days:
                
                print('So sorry, it appears that you input a wrong day, to continue please choose between the next options: ')
                print('1. Monday 2. Tuesday 3. Wednesday 4. Thursday 5. Friday 6. Saturday 7. Sunday 8. All')
    
    print('Well done you have input a valid option!')
    print('We\'ll proceed with {}'.format(day))
    
    print('-'*40)
    return city, month, day ,city_input


def load_data(city, month, day, city_input):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #Load data file into dataframe
    
    df = pd.read_csv(city_input)
    
    #Convert Start Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extract month and day of week from Start Time to Create new columns
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #filter by month if applicable
    
    if month != 'all':
        
        #use the index of the months list to get the corresponding int
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #filter by month to create the new dataframe
        
        df = df[df['month'] == month]
        
    #filter by day of week if applicable
    
    if day != 'all':
        
        #filter by day of week yo create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month - Mode Statistic

    mode_month = df['month'].mode()[0]
    
    print('The most popular month is: {}'.format(mode_month))

    # Display the most common day of week - Mode Statistic

    mode_dow = df['day_of_week'].mode()[0]
    
    print('The most popular day of week is {}'.format(mode_dow))

    # Convert the Start Time column to create an hour column
    
    df['hour'] = df['Start Time'].dt.hour
    
    # Display the most common start hour - Mode Statistic
    
    mode_hour = df['hour'].mode()[0]
    
    print('The most popular hour is {}'.format(mode_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display the most common start station - Mode Statistic
    
    mode_start_station = df['Start Station'].mode()[0]
    
    print('The most common start station is: {}'.format(mode_start_station))

    # Display the most common end station - Mode Statistic
    
    mode_end_station = df['End Station'].mode()[0]
    
    print('The most common end station is: {}'.format(mode_end_station))

    # New column creation with the combination of start to end
    
    df['start_end_comb'] = df['Start Station'].astype(str) + ' - ' + df['End Station'].astype(str)
    
    # Display the most common start and end station - Mode Statistic
    
    mode_start_end = df['start_end_comb'].mode()[0]
    
    print('The most common combination of start and end station is : {}'.format(mode_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display of the total duration of the trip - Sum Statistic
    
    sum_travel = df['Trip Duration'].sum()
    
    print('The total travel duration for the trip is: {}'.format(sum_travel))

    # Display of the mean of the trip - Mean Statistic
    
    avg_travel = df['Trip Duration'].mean()
    
    print('The average travel duration for the trip is: {}'.format(avg_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Diplay the count of the user types - Count Statistic
          
    user_count = df['User Type'].value_counts()
          
    print('The value count of every user type are: {}'.format(user_count))

    # Probe if the column Gender exist
          
    try:
        count_gender = df['Gender'].value_counts()
    
    except:
        print('There is no gender in this document')
    
     # Diplay the count of Gender Type - Count Statistic
          
    else:
        print('The value of count of every gender are: {}'.format(count_gender))        
          

    # Probe if the column Birth Year exist
          
    try:
        earliest_birth = df['Birth Year'].min()
        recent_birth =  df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
    
    except:
        print('Sorry there is no birth year in this document')
    
    # Display the earliest, most recent, and most common year of birth
          
    else:
        print('''
          The earliest birth is: {} 
          The most recent birth is: {}
          The most common birth is: {}
          '''.format(earliest_birth, recent_birth, common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
                
    
def main():
    while True:
        city, month, day, city_input = get_filters()
        df = load_data(city, month, day, city_input)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
