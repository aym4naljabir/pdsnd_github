import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']
MONTHS = ['all' , 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True :
        city = input("Please type the desired city (Chicago,New york,Washington) : ").lower()
        if city in CITIES :
            break
        else : 
                print("You enterd a wrong city please try again (from cities above): ")
               
    
    while True :
        month = input("Please type the desired month : ").lower()
        if month in MONTHS :
            break
        else : 
                print("You enterd a wrong month please try again : ")
               

    
    while True :
        day = input("Please type the desired day : ").lower()
        if day in DAYS :
            break
        else : 
                print("You enterd a wrong day please try again : ")

    print('-'*80)
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

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

    
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    
    return df
def convert_hours(hour):
    if hour >= 12  :
        if hour == 12:
            return("12 PM")
        else:
            return( str(hour - 12) + " PM")
    else:
        if hour == 0 :
            return("12 AM")
        else:
            return(str(hour)+ " AM")
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", MONTHS[int(most_common_month)].capitalize())

    
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day is :", most_common_day.capitalize())

    
    most_common_hour = df['hour'].value_counts().idxmax()
    print("The most common hour is :", convert_hours(int(most_common_hour)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

   
    most_common_start_end_station = df['Start End'] = df['Start Station'].map(str) + " " + 'and,' + " " + df['End Station']
    popular_start_end = df['Start End'].value_counts().idxmax()
    print("the most popular Start and End Stations were : " ,popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_travel = df['Trip Duration'].sum()
    print("Total travel time in seconds  :", int(total_travel) , "Sec.")

    
    mean_travel = df['Trip Duration'].mean()
    print("Averge travel in seconds is :", int(mean_travel) , "Sec.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    print("Counts of the users types:\n")
    user_counts = df['User Type'].value_counts()
    
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
 
    
    print('-'*80)

    if 'Gender' in df.columns:
        usg(df)
    print('-'*80)
    
    if 'Birth Year' in df.columns:
        usb(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)
def convert_hours(hour):
    if hour >= 12  :
        if hour == 12:
            return("12 PM")
        else:
            return( str(hour - 12) + " PM")
    else:
        if hour == 0 :
            return("12 AM")
        else:
            return(str(hour)+ " AM")
def usg(df):
    """Displays statistics of analysis based on the gender of bikeshare users."""

    
    print("Counts of gender:\n")
    gcs = df['Gender'].value_counts()
    
    for index,gc   in enumerate(gcs):
        print("  {}: {}".format(gcs.index[index], gc))
    
    print()
def usb(df):
    """Displays statistics of analysis based on the birth years of bikeshare users."""

    
    by = df['Birth Year']
    
    yr = by.value_counts().idxmax()
    print("The most common birth year is : ", int(yr))
    
    mr = by.max()
    print("The most recent birth year is : ", int(mr))
    
    ey = by.min()
    print("The earliest birth year is : ", int(ey))
def display_data(df):
    hd = 0
    tl = 5
    while True:
        raw_data = input('Would you like to see 5 rows of raw data?\nPlease enter yes or no : ').lower()
        if raw_data == 'yes':
            print(df[df.columns[0:-1]].iloc[hd:tl])
            hd += 5
            tl += 5
        else:
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
if __name__ == "__main__":
	main()
