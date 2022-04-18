import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city.Then asking him whether he/she wants to filter by month only ,or day only or both or whether he/she doesn't need to filter at all.
    Returns:
    (str) city - name of the city to analyze.
    Then if filter is needed (by month only -by day only - or Both):
    (str) month - name of the month to filter by.
    (str) day - name of the day of week to filter by.
    Or If no filter needed (Then user writes 'none')
        """

    print('Hello! Let\'s explore some US bikeshare data!')


        # get user input for city (chicago, new york, washington).
    city= input ("Would you like to see data for Chicago, New York, or Washington?\n").lower()
    while city not in CITY_DATA:
        print ('Invalid input, please enter correct city \n')
        city= input ('Please Enter the city : ').lower()
    # get user input for filter option (by month only -by day only -by both -or no filter at all "none" )
    choices=['month','day','both','none']
    choose=input ('Would you like to filter the data by "month", "day","both" or not at all "none"? Please write your choice.\n').lower()
    while choose not in choices:
        print('Invalid Choice')
        choose=input('Please enter a valid choice from ("month","day","both","none")\n:').lower()

    if choose=='month':
        day= 'all'
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month= input ("Enter the Month from the first six months:\n").lower()
        while month not in months:
            print('Invalid input, please enter a valid month\'s name (January, February,....) from the first six months: \n')
            month=input ('Please Enter the month :').lower()

            # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

    elif choose == 'day':
        month ='all'
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','all']
        day= input("Enter the day: (Monday,Tuesday ,.... ) \n").lower()
        while day not in days:
            print('Invalid input, please enter a weekday (Saturday,Sunday,.......) \n')
            day=input ('Please Enter the day :').lower()

    elif choose == 'none':
        month ='all'
        day='all'


    elif choose =='both':
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        month=input ('Enter the Month from the first six months: :').lower()
        while month not in months:
            print('Invalid input, please enter a valid month\'s name (January, February,....) from the first six months: \n')
            month=input ('Please Enter the month :').lower()
        month = months.index(month) + 1
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','all']
        day=input ('Please Enter the day :').lower()
        while day not in days:
            print('Invalid input, please enter a weekday (Saturday,Sunday,.......) \n')
            day=input ('Please Enter the day :').lower()


    print('-'*40)
    #print(city, month, day)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by
        (str) day - name of the day of week to filter by
    Returns:
        df - Pandas DataFrame containing city data filtered by required filtration or not filtered
    """

    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()


    if month!='all':
        df = df[df['month'] == month]
    elif day!='all':
        df = df[df['day'] == day.title()]
    elif (day!='all' and month!='all'):
        df = df[df['month'] == month]
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    # display the most common month
    df['month'] = df['Start Time'].dt.month
    most_month = df['month'].mode()[0]
    print("Most Common travel month is:", months[most_month-1])


    # display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    most_day = df['day'].mode()[0]
    print("Most Common Travel day is:", most_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print("Most Common Travel Hour is:", most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("Most Commonly used Start Staion is :", most_start_station)

    # display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("Most Commonly used End Staion is", most_end_station)


    # display most frequent combination of start station and end station trip
    most_comp_station = ('from  ('+ df['Start Station']+') to ('+ df['End Station']).mode()[0]+')'
    print("Most frequent combination of Start and End stations is", most_comp_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     # display total travel time
    total_travel=int (df['Trip Duration'].sum())
    print('Total Travel Time is: ', str(total_travel) +' Seconds')

    # display mean travel time
    mean_travel=int(df['Trip Duration'].mean())
    print('Mean Travel Time is: ', str(mean_travel) +' Seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

     # Display counts of user types
    user=df['User Type'].value_counts()
    print('User Types Counts is:\n',user)

    # Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print('Gender Counts is: \n',gender)
    except:
        print ('No Gender Column')
    # Display earliest, most recent, and most common year of birth
    try:
        earliest=int (df['Birth Year'].min())
        recent=int (df['Birth Year'].max())
        common=int(df['Birth Year'].mode()[0])
        #print(earliest)
        print('Earliest Year Of Birth is:\n',earliest  ,'\nRecent Year Of Birth is:\n',recent  , '\nMost Common Year of birth is:\n', common)
    except:
        print ('No Birth Year coulmn')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    yesno=['yes','no']
    display=input ('Would you like to display some raw data? yes/no \n')
    while display not in yesno:
        display=input ('Please enter "yes" or "no":\n').lower()
    if display =='yes':
        i=0
        while (display.lower() =='yes'):
            show=df.sample(i+5)
            print(show)
            display=input('Would you like to show more data?\n')
            while display not in yesno:
                display=input ('Please enter "yes" or "no":\n').lower()
            i+=5


    elif display =='no':
        print('Thank You')





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
            break

if __name__ == "__main__":
	main()
