class search_user(webapp.RequestHandler):
            q = (self.request.GET['q']).lower()         #INSERT AJAX CALL TO GOOGLE CLOUDSQL ENDPOINT
            results=models.user.all().fetch(100)
            for records in result:
                print records+"|"+records+"\n"

application = webapp.WSGIApplication([
                                      (r'/user_auth/search_manager',search_user)]

def main():
  run_wsgi_app(application)

if __name__ == '__main__':
  main()

simple:
