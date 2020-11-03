from flask import Flask, request,jsonify
app=Flask(__name__)

customer_Details = {
    1:
    {'name':'jothi',
     'account_no':1,
     'contact_info':123456},

    2:
    {'name':'jerry',
     'account_no':2,
     'contact_info':99999}
}

@app.route('/')
def welcomepage():
    return 'Welcome to the Banking portal-updated'

@app.route('/customer-details')
def get_all_customer_details():
    return customer_Details

@app.route('/customer-details/<int:acc_id>',methods=['GET','PUT',DELETE])
def get_selected_customer_details(acc_id):
    details =  customer_Details.get(acc_id)
    if not details:
        return jsonify ("Customer not found"), 404
    elif request.method==['PUT']:
        data = request.json
        customer_Details[acc_id]=data
        return f"{data} was updated",204
    elif request.method==['DELETE']:
        del customer_Details[acc_id]
        return f"{acc_id} has been deleted",204
    else:
        return {acc_id:details}

@app.route('/customer-details/<int:acc_id>',methods=['GET','POST'])

def new_cusomers():
    if request.method == 'POST':
        new_customer = request.json
        new_acc_id = max(customer_Details) + 1
        customer_Details[new_acc_id] = new_cusomers
        return customer_Details[new_dev_id], 201
    else: 
        return customer_Details, 200
