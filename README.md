## GitHub User API

> A simple API to retrieve GitHub user data in different formats: **JSON, HTML, or XML**.

## Installation

1. Install dependencies:

```pip install Flask requests dicttoxml```

2. Run the API:

`python app.py`

3. Make a GET **request:**

`http://127.0.0.1:5000/github_user?username=octocat&format=json`

## Parameters

## Response Examples

## JSON
``
{
  "login": "octocat",
  "name": "The Octocat",
  "company": "GitHub",
  "location": "San Francisco",
  "public_repos": 8,
  "followers": 4600,
  "html_url": "https://github.com/octocat"
}``

## HTML

**Returns a formatted web page with user data.**

## XML
``
<github_user>
  <login>octocat</login>
  <name>The Octocat</name>
  <company>GitHub</company>
  <location>San Francisco</location>
  <public_repos>8</public_repos>
  <followers>4600</followers>
  <html_url>https://github.com/octocat</html_url>
</github_user>
``
## 

