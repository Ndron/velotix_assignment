from flask import Flask, request , jsonify
import pickle

from cornac.models import Recommender
model = Recommender.load('trained_model/VAECF/vaecf_model.pkl')
with open('trained_model/VAECF/train_set.pkl', 'rb') as train_set_file:
    train_set = pickle.load(train_set_file)

app = Flask(__name__)

RECOMENDATION_URL = '/predict'
@app.route(RECOMENDATION_URL, methods=['GET'])
def predict():
    params = request.args
    uid = params.get("uid")
    k = int(params.get("k", -1))
    remove_seen = params.get("remove_seen", "false").lower() == "true"

    if uid is None:
        return "uid is required", 400

    if remove_seen and train_set is None:
        return "Unable to remove seen items. 'train_set' is not provided", 400

    response = model.recommend(
        user_id=uid,
        k=k,
        remove_seen=remove_seen,
        train_set=train_set,
    )

    data = {
        "recommendations": response,
        "query": {"uid": uid, "k": k, "remove_seen": remove_seen},
    }

    return jsonify(data), 200



if __name__ == '__main__':

    print('run')
    app.run(host='127.0.0.1', port=5000)
    #curl -X GET "http://127.0.0.1:5000/predict?uid=A1HP7NVNPFMA4N&k=5&remove_seen=false"

