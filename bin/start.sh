export FLASK_APP=../hello.py
# for notebooks.ai
export FLASK_RUN_HOST=0.0.0.0
export FLASK_DEBUG=1
export FLASK_RUN_PORT=8080
# for MITRE ECE lab
#export FLASK_RUN_HOST=das10.mitre.org
#export FLASK_RUN_PORT=5000
# for pythonanywhere.com
#export FLASK_RUN_HOST=das10.mitre.org
#export FLASK_RUN_PORT=5000
flask run
