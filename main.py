from app import application
import os
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5001))
    application.run(debug=True,use_reloader=True,port=port,host='0.0.0.0',threaded=True)
    # application.run(debug=True,use_reloader=True,port=port)

