# -*- coding: utf-8 -*
import mimetypes
import json
from urllib import quote

from boto.s3.connection import S3Connection
from boto.s3.key import Key
from bottle import request, response


from plants_dal import Plant
from plants_libs.threshold import Threshold
from plants_libs.EFD import EFD
from plants_web.libs.templates import render_template


def add_form():
    return render_template('add_plant.html')

def add():
    image = request.POST.get('photo')
    name = request.POST.get('name')
    common_name = request.POST.get('common_name')
    plant = Plant.retrieve(request.db, name)
    if plant: return "This species is already in the DB"
    if image is not None:
        mime = mimetypes.guess_type(image.filename)[0]
        conn = S3Connection('AKIAIMXIHJX3TFDQFVCA', 'Lf7xWpeOB9mnY1zfFzl7WNtxtNhmCZ4ZXOI8Kvrr')
        bucket = conn.get_bucket('db_leaves')
        key = Key(bucket)
        key.key = name
        key.set_metadata("Content-Type", mime)
        key.set_contents_from_string(image.value)
        key.set_acl("public-read")
        
        descriptors,ax,bx,ay,by = EFD(Threshold(image.file).process(), 50, 100).fourier_coefficients()
        return Plant({'name': name,'common_name':common_name, 'wiki': request.POST.get('wiki'), 'photo': 'https://s3.amazonaws.com/db_leaves/%s' % quote(name), 'descriptors':descriptors}).save(request.db)
    return []

def search_form():
    return render_template('search.html')

def search():
    image = request.POST.get('photo')
    descriptors,ax,bx,ay,by = EFD(Threshold(image.file).process(), 50, 100).fourier_coefficients()
    plants = Plant.search(request.db, descriptors)
    response.headers['Content-type'] = 'application/json'
    return json.dumps(plants)

