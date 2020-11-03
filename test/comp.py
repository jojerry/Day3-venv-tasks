l=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
 

def proper_balance(l):
    result= {x[0]:x[1] for x in l if x[1] > x[2]}
    return (result)
  
def set_of_all_balances(l):
    all_balances = {x[1] for x in l}
    return all_balances

def list_of_account_holders(l):
    Acc_holders =  {x[0] for x in l}
    return Acc_holders

def user_amount_need_fullfill(l):
    amt_need = {x[0]:x[2]-x[1] for x in l if x[1]<x[2]}
    return amt_need

def user_amount_greater_zero(l):
    amt_gr_zero = {x[0]:x[1] for x in l if x[1]>0}
    return amt_gr_zero

print(proper_balance(l))
print(set_of_all_balances(l))
print(list_of_account_holders(l))
print(user_amount_need_fullfill(l))
print(user_amount_greater_zero(l))

