from flask import Flask,jsonify,request

app=Flask("__name__")

@app.route("/post",methods=['POST'])
def create_data():
    data=request.form
    name=data.get("name")

    print("Created: ",name)

    return({
        "Received":"SUCCESS",
        "Name":name
    })

@app.route("/get",methods=["GET"])
def read_data():
    print("Data read")
    return jsonify({
        "Received":"SUCCESS",
        "Name":"READ"
    })

name1={"name":"jeeva"}
@app.route("/put",methods=["PUT"])
def update():
    data=request.json
    new_data=data.get("name")
    name1["name"]=new_data

    print("New data",new_data)

    return jsonify({
        "Received":"SUCCESS",
        "Name":new_data
    })

users=["first","second","third"]
@app.route("/delete",methods=["DELETE"])
def delete():
    deleted=users.pop(1)
    print("Popped_element: ",deleted)

    return jsonify({
        "Received":"SUCCESS",
        "Popped":deleted
    })
if __name__=="__main__":
    app.run(debug=True)