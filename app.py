from flask import Flask, jsonify,request

app=Flask("__name__")

@app.route("/health")
def heathcheck():
    return jsonify({
        "status":"healthy"
    })

@app.route("/NAME",methods=['POST'])
def dem():
    data=request.form
    name=data.get("name")

    print("Received name",name)

    return jsonify({
        "message":"Name Received",
        "your_name":name
                         })
    

name1={"name":"jeeva_old"}
@app.route("/update",methods=['PUT'])
def change():
    data=request.form
    new_data=data.get("name")

    name1["name"]=new_data

    return jsonify({
        "message":"Received",
        "new_name":new_data
    })

name=["jeeva","vijay","ece"]
@app.route("/delete",methods=['DELETE'])
def delete_data():
    deleted=name.pop(2)
    print("Popped element: ",deleted)

    return jsonify({
        "message":"received",
        "popped_element":deleted
    })
    

@app.route("/academics")
def study():
    return "KONGU ENGINEERING COLLEGE"

if __name__=="__main__":
    app.run(debug=True)


