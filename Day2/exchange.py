from collections import Counter

def holiday_test(string):
    '''
    INPUT: string
    OUTPUT: boolian

    Given a string of the trading/exchange information, returns True if that date was a Bank holiday.
    '''
    if 'Bank holiday' in string:
        return True
    else:
        return False


def rate_change(yesterday_str, today_str):
    '''
    INPUT: string, string
    OUTPUT: float

    Given the strings showing the rate and exchange information for two consecutive trading days (bank holidays must be already excluded), return the overnight change in the exchange rate.
    '''
    yesterday_rate = float(yesterday_str[16:22])
    today_rate = float(today_str[16:22])
    return round(today_rate - yesterday_rate, 4)

def extract_dates_n_rates(filename):
    '''
    INPUT: string (filename)
    OUTPUT: dict

    Take the filename of exchange data, extract the dates and corresponding exchange rate change (including removing bank holidays), compile them in a dict, and return it.
    '''
    dates_n_rates = {}
    i = 1
    yesterday = ''
    today = ''

    with open(filename) as f:
        for line in f:
            yesterday = line
            if not holiday_test(yesterday):
                if i > 4:
                    dates_n_rates[today[0:10]] = rate_change(yesterday, today)
                today = yesterday
            i += 1

    return dates_n_rates


def exchange_trends(filename):
    '''
    INPUT: string (filename):
    OUTPUT: a printed summation of the exchange rate information in input file, including the frequency of specific changes in exchange rate, and the date of maximum change.
    '''
    dates_n_rates = extract_dates_n_rates(filename)

    max_date = max(dates_n_rates, key=lambda i: dates_n_rates[i])
    max_rate = dates_n_rates[max_date]

    forex_frequency = Counter()

    for date in dates_n_rates:
        forex_frequency[round(dates_n_rates[date],2)] += 1

    print '\n'.join(str(item) + ': ' + str(forex_frequency[item]) for item in sorted(forex_frequency))
    print 'Day(s) with biggest gain ({}): {}'.format(max_rate, max_date)
    return
