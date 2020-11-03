from flask import Flask,jsonify
app = Flask(__name__)

courses = [{'name':"Python programming",
            'course_id':"1",
            'Description':"python description programming",
            'price':"Data science"},
            
            {'name':"sql programming",
            'course_id':"2",
            'Description':"sql description programming",
            'price':"sql"}

            ]
@app.route('/')
def Welcome():
    return 'Hello Welcome to home page!'

@app.route("/courses",methods=['GET'])
def developer():
    return jsonify ({'courses': courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def developer_id(course_id):
    for x,y in enumerate (courses,1):
        if y['course_id'] == course_id:
            return jsonify({'courses': courses[x]})
  
