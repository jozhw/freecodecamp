import re
def date_time_check(date_time):
    success=None
    date_regex=re.compile('\d\d\d\d-\d\d-\d\d')
    date_search=date_regex.search(date_time)
    date_search=date_search.group()
    if len(str(date_time)) == 10 or date_time == None or date_time=="":
        success=True
        return success
    else:
        seccess=False
        return success

def change_sign(trans_type,shares,price):
    if trans_type =="A" and (shares < 0 or price < 0):
        if shares < 0 and price < 0:
            shares=shares*(-1)
            price=price*(-1)
            return shares, price
        elif shares > 0 and price < 0:
            price=price*(-1)
            return shares, price
        elif shares < 0 and price > 0:
            shares=shares*(-1)
            return shares, price
    elif trans_type=="D" and (shares > 0 or price > 0):
        if shares > 0 and price > 0:
            shares=shares*(-1)
            price=price*(-1)
            return shares, price
        elif shares < 0 and price > 0:
            price=price*(-1)
            return shares, price
        elif shares > 0 and price < 0:
            shares=shares*(-1)
            return shares, price
    else:
        return shares, price




# check to see if are numbers
shares=float("50")
price=float("50")
# check to see if right type of entry A or D
trans_type=str("a").upper()
# date_time variable
date_time="5555-55-55"
if len(trans_type)==1 and (trans_type=="A" or trans_type=="D"):
    shares, price = change_sign(trans_type,shares, price)
    if date_time_check(date_time) == True:
        # name=str(entry_dic["Name of Security:"]).capitalize()
        # ticker=str(entry_dic["Ticker:"]).upper()
        # institution=str(entry_dic["Institution Name:"]).capitalize()
        date_time=date_time
        trans_type=trans_type
        shares=shares
        price=price
        print("works")
        # insert_transaction(name, ticker, institution, date_time, trans_type, shares, price)
    else:
        print("wrong date-time")
        # messagebox.showerror("Entry Error", 'Invalid entry for "Time of Transaction:" Please try again.')
else:
    print("wrong overall")
    # messagebox.showerror("Entry Error", 'Invalid entry for "Transaction Type:" Please try again. Consult the manual if needed. Note: Valid entries are A (aquire) and D (dispose).')
