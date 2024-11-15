# This program is used to decode base64 strings.
import base64

string = ''          # Input Encoded String Here
output = base64.b64decode(string)

decoded = ''
decoded = decoded.encode('utf-8')
encoded = base64.b64encode(decoded).decode('utf-8')