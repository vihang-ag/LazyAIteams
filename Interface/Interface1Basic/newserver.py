import flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import Flask, request, render_template
import pymysql

# Database connection
db = pymysql.connect("localhost", "root", "", "annotationdbname", autocommit=True)

app = flask.Flask(__name__)
CORS(app)
@app.route('/getTextJson/<id>', methods=['GET'])
def create_text(id):
    print(id)
    return new_function(id)

@app.route('/postJson', methods=['POST'])
def save_label_for_text():
    data = {"success": False}
    content = request.get_json(silent=True)
    postContent = request.get_json(silent=True)
    old_id=int(content["Id"])
    #data = content["Data"]
    choice = ''
    timer = ''
    choice = choice+content["Choice"]
    timer = timer+content["Time"]
    cursors = db.cursor()
    #insert_sql="INSERT INTO `annotationdbname`.`textdata` (`id`,`annotation`, `human_effort`) VALUES (%s,%s,%s);"
    insert_sql = "UPDATE `annotationdbname`.`textdata` SET annotation=%s, human_effort=%s WHERE id=%s;"
    cursors.execute(insert_sql, (choice, timer, old_id))


    print(content)
    #sqlnewquery="Insert into textdata ()"

    new_id=int(content["Id"])+1
    print(new_id)
    return new_function(new_id)

def new_function(id):
    cursor = db.cursor()
    new_sql="select count(*) from textdata"
    cursor.execute(new_sql)
    countofvalue = cursor.fetchone()
    print(countofvalue[0])
    if(int(id)>countofvalue[0]):
        return jsonify({'id': 0, 'data':"no data", 'annotation':"no data", 'human_effort':"no data"})
    sql = "SELECT * FROM textdata where id=%s"
    cursor.execute(sql, id)
    results = cursor.fetchone()
    id = results[0]
    data = results[1]
    annotation = results[2]
    human_effort = results[3]
    return jsonify({'id': id, 'data':data, 'annotation':annotation, 'human_effort':human_effort})


if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    app.run(port=5000, debug=False)

# postContent = request.get_json(silent=True)
# old_id=int(content["Id"])
# data = content["Data"]
# choice = content["Choice"]
# timer = content["Time"]
# cursors = db.cursor()
# insert_sql="InsertINTO 'try'.'textdata'('id','data','annotation','human_effort','prediction','model_effort;)VALUES(old_id,data,choice,timer,,);"
# cursors.execute(insert_sql)