from flask import Flask, request
import os
from webApp.utils.validate_input import validate_input
from webApp.core.predict import predict

webapp_root = "app"
params_path = "params.yaml"
# css and static assets and js files
static_dir = os.path.join(webapp_root, "static")
# layout and html pages
template_dir = os.path.join(webapp_root, "templates")

application  = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

@application.route('/')
def helloworld():
    return 'Hello World'

@application.route('/predict',methods=['GET','POST'])
def init_application():
    if request.method=='POST':

        req = request.get_json()

        try:
            test_input = validate_input(req)

            if test_input:
                data = req.values()
                data = [list(map(float, data))]
                response = predict(data,params_path)
                return {'result':str(response)}
        except Exception as e:
            return {'error 1':str(e)}
    else:
        return {'error 2':'Request should be POST'}

   
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5001))
    application.run(debug=True,use_reloader=True,port=port,host='0.0.0.0')



