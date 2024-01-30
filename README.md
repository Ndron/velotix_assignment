# How to install and run project 
Load data from  https://jmcauley.ucsd.edu/data/amazon_v2/categoryFilesSmall/Video_Games_5.json.gz
 
pip install -r requirements.txt  
python python flask_api.py  

# sample request
curl -X GET "http://127.0.0.1:5000/predict?uid=A1HP7NVNPFMA4N&k=5&remove_seen=false"



