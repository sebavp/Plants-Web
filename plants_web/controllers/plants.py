# -*- coding: utf-8 -*
import mimetypes

from bottle import request
from dropbox import client, rest, session

# XXX Fill in your consumer key and secret below
# You can find these at http://www.dropbox.com/developers/apps
APP_KEY = 'fmnxrettvhzlh69'
APP_SECRET = '9qvf2vhtpxkotfv'
ACCESS_TYPE = 'app_folder'  # should be 'dropbox' or 'app_folder' as configured for your app

from plants_dal import Plant
from plants_libs.threshold import Threshold
from plants_libs.EFD import EFD
from plants_web.libs.templates import render_template

# def command(login_required=True):
#     """a decorator for handling authentication and exceptions"""
#     def decorate(f):
#         def wrapper(self, args):
#             if login_required and not self.sess.is_linked():
#                 print "Please 'login' to execute this command\n"
#                 # self.stdout.write("Please 'login' to execute this command\n")
#                 return

#             try:
#                 return f(self, *args)
#             except TypeError, e:
#                 print str(e) + '\n'
#                 # self.stdout.write(str(e) + '\n')
#             except rest.ErrorResponse, e:
#                 msg = e.user_error_msg or str(e)
#                 print 'Error: %s\n' % msg
#                 # self.stdout.write('Error: %s\n' % msg)

#         wrapper.__doc__ = f.__doc__
#         return wrapper
#     return decorate

def dropbox_session(app_key, app_secret):
    sess = StoredSession(app_key, app_secret, access_type=ACCESS_TYPE)
    api_client = client.DropboxClient(sess)
    sess.load_creds()
    # sess.link()
    return api_client

def add_form():
    return render_template('add_plant.html')

def add():
    image = request.POST.get('photo')
    name = request.POST.get('name')
    plant = Plant.retrieve(request.db, name)
    if plant: return "This species is already in the DB"
    if image is not None:
        mime = mimetypes.guess_type(image.filename)[0]
        descriptors,ax,bx,ay,by = EFD(Threshold(image.file).process(), 50, 100).fourier_coefficients()
        photo = dropbox_session(APP_KEY, APP_SECRET).put_file("/%s.jpg" % (name,), image.value)
        print photo
        return Plant({'name': name, 'wiki': request.POST.get('wiki'), 'photo': photo.get('path'), 'descriptors':descriptors}).save(request.db)
    return []

def search_form():
    return render_template('search.html')

def search():
    image = request.POST.get('photo')
    descriptors,ax,bx,ay,by = EFD(Threshold(image.file).process(), 50, 100).fourier_coefficients()
    plant = Plant.search(request.db, descriptors)
    return plant

class StoredSession(session.DropboxSession):
    """a wrapper around DropboxSession that stores a token to a file on disk"""
    TOKEN_FILE = "token_store.txt"

    def load_creds(self):
        try:
            stored_creds = open(self.TOKEN_FILE).read()
            self.set_token(*stored_creds.split('|'))
            print "[loaded access token]"
        except IOError:
            pass # don't worry if it's not there

    def write_creds(self, token):
        f = open(self.TOKEN_FILE, 'w')
        f.write("|".join([token.key, token.secret]))
        f.close()

    def delete_creds(self):
        os.unlink(self.TOKEN_FILE)

    def link(self):
        request_token = self.obtain_request_token()
        url = self.build_authorize_url(request_token)
        print "url:", url
        print "Please authorize in the browser. After you're done, press enter."
        raw_input()

        self.obtain_access_token(request_token)
        self.write_creds(self.token)

    def unlink(self):
        self.delete_creds()
        session.DropboxSession.unlink(self)