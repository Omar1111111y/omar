from flask import *
m_my = Flask(__name__)
bb= '{"name":"Omar","id":10027,"pp":"wwww.google.com"}'

@m_my.route('/')
def ih():
	return jsonify(bb)
m_my.run()
