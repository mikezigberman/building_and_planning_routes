from django.http import HttpResponse

def home(request):
    html = '''<!DOCTYPE html>
              <html>
              <head>
              <title>Title of the website</title>
              </head>

              <body>
              <h1>The content of the document......</h1>
              </body>
              </html>'''
    return HttpResponse(html)