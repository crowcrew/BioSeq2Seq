import os
from os import listdir
from os.path import isfile, join
from bottle import route, template, redirect, run, error, get, post, request, response, static_file
from interface import *


@route('/')
def get_index():
    links = []
    alignment_user_input_files = []
    protein_production_user_input_files = []
    size = 0
    for f in listdir('database'):
        if isfile(join('database', f)):
            links.append(f)
    for f in listdir('user_input/alignment'):
        if isfile(join('user_input/alignment', f)):
            alignment_user_input_files.append(f'user_input/alignment/{f}')
    for f in listdir('user_input/protein_production'):
        if isfile(join('user_input/protein_production', f)):
            protein_production_user_input_files.append(f'user_input/protein_production/{f}')
    return template(
        'index',
        alignment_user_input_files=alignment_user_input_files,
        protein_production_user_input_files=protein_production_user_input_files,
        links=links)

@route('/user_input/alignment/<filename>')
def alignment_sample_files(filename):
    return static_file(filename, root='user_input/alignment')

@route('/user_input/protein_production/<filename>')
def protein_production_sample_files(filename):
    return static_file(filename, root='user_input/protein_production')

@route('/database')
def database_files(filename):
    return static_file(filename, root='database')

@route('/static/css/<filename>')
def css(filename):
    return static_file(filename, root='static/css')


@route('/static/image/<filename>')
def image(filename):
    return static_file(filename, root='static/image')


@route('/static/js/<filename>')
def js(filename):
    return static_file(filename, root='static/js')


@route('/static/json/<filename>')
def json(filename):
    return static_file(filename, root='static/json')


@route('/getalignment', method='POST')
def getalignment():
    selected_database_files = request.POST['selected_database_files'].split(
        ',')
    selected_database_files = [
        "database/" + selected_file
        for selected_file in selected_database_files
    ]
    user_file = request.POST['user_file'].file.read()
    user_file = user_file.decode("utf8")
    selected_algorithm = request.POST['selected_algorithm']
    result = findalignments(user_file, selected_database_files,
                            selected_algorithm)
    import json
    result = json.dumps(result)
    if len(selected_database_files) == 1 and os.path.isdir(
            selected_database_files[0]):
        selected_database_files = [
            selected_database_files[0] + f
            for f in listdir(selected_database_files[0])
            if isfile(join(selected_database_files[0], f))
        ]
    selected_database_files = json.dumps(selected_database_files)
    user_file = json.dumps(user_file)
    return template(
        'result',
        alignment=result,
        sequenceNames=selected_database_files,
        userFile=user_file)


@route('/getProtein', method='POST')
def getProtein():
    user_file = request.POST['user_file_to_protein'].file.read()
    user_file = user_file.decode("utf8")
    protein_sequence = findprotein(user_file)
    import json
    user_file = json.dumps(user_file)
    return template(
        'protein', protein_sequence=protein_sequence, userFile=user_file)


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
