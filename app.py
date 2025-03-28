
from flask import Flask, jsonify, request, Response
import requests
import dicttoxml

app = Flask(__name__)

def get_github_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None
    
    return response.json()

@app.route('/github_user', methods=['GET'])
def github_user():
    username = request.args.get('username')
    response_format = request.args.get('format', 'json').lower()
    
    if not username:
        return jsonify({'error': 'The "username" parameter is required.'}), 400
    
    user_data = get_github_user_data(username)
    
    if user_data is None:
        return jsonify({'error': 'User not found or error fetching data.'}), 404
    
    if response_format == 'json':
        return jsonify(user_data)
    
    elif response_format == 'html':
        html_content = f"""
        <html>
        <head><title>{user_data.get('login', 'User')}</title></head>
        <body>
            <h1>{user_data.get('name', 'No Name')}</h1>
            <p><strong>Username:</strong> {user_data.get('login')}</p>
            <p><strong>Company:</strong> {user_data.get('company', 'N/A')}</p>
            <p><strong>Location:</strong> {user_data.get('location', 'N/A')}</p>
            <p><strong>Public Repos:</strong> {user_data.get('public_repos', 0)}</p>
            <p><strong>Followers:</strong> {user_data.get('followers', 0)}</p>
            <p><a href="{user_data.get('html_url')}" target="_blank">GitHub Profile</a></p>
        </body>
        </html>
        """
        return Response(html_content, mimetype='text/html')

    elif response_format == 'xml':
        xml_content = dicttoxml.dicttoxml(user_data, custom_root="github_user", attr_type=False)
        return Response(xml_content, mimetype='application/xml')

    return jsonify({'error': 'Invalid format. Use "json", "html", or "xml".'}), 400

if __name__ == '__main__':
    app.run(debug=True)