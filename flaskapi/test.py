customer_Details = {
    1:
    {'name':'Jothi',
     'account_no':1,
     'contact_info':123456},

    2:
    {'name':'Jerry',
     'account_no':2,
     'contact_info':99999}
}


def get_name(name):
    for x,y in customer_Details.items():
        if y['name']==name:
            print({x:y})
get_name('Jerry')

