import comp

list1=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
def test_proper_balance():
    assert comp.proper_balance(list1) == {'Guido': 2000, 'Brandon': 2000}

def test_set_of_all_balances():
    assert comp.set_of_all_balances(list1) == {2000, 900, -52}

def test_list_of_account_holders():
    assert comp.list_of_account_holders(list1) == {'Brandon', 'Guido', 'Raymond', 'Jack'}

def test_user_amount_need_fullfill():
    assert comp.user_amount_need_fullfill(list1) == {'Raymond': 1052, 'Jack': 100}

def test_user_amount_greater_zero():
    assert comp.user_amount_greater_zero(list1) == {'Guido': 2000, 'Jack': 900, 'Brandon': 2000}


