from flask import Flask, render_template, request
import os

#gtihub_test demo

os.environ['config_env'] = "localhost"
app = Flask(__name__)
print(app)

@app.route("/")
def index():
    flask_data = 'infra-数据接口,运行环境:%s' % (os.environ.get('config_env'))
    return render_template('index.html', flask_data=flask_data)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8090,
        debug=True
    )
