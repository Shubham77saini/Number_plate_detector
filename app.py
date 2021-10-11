from flask import Flask, render_template,request
import os
from deeplearning import OCR

# webserver getway interface

app = Flask(__name__)

Base_path = os.getcwd()
Upload_path = os.path.join(Base_path,'static/upload/')

@app.route('/',methods=['POST','GET'])

def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save =  os.path.join(Upload_path,filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)


        return render_template('index.html',upload=True, upload_image = filename, text = text)

    return render_template ('index.html',upload=False)



if __name__ == "__main__":
    app.run(debug=True)



