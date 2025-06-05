from flask import Blueprint, render_template, request
from requests import JSONDecodeError
from requests.exceptions import Timeout
from .handle_requests import send_request
views = Blueprint("views", __name__)

@views.route("/", methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        url = request.form.get('url')
        response_type = request.form.get('response-type')

        try:
            response = send_request(url, response_type)
        except JSONDecodeError:
            response = f"The endpoint does not contain valid json!"
        except Timeout:
            response = "Endpoint is taking too long to respond!"
        except:
            response = "An error occured! Is this a valid url?"

    return render_template("index.html", response=response)


