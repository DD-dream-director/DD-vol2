#!/bin/bash
# The way to tidy environmet.

PROJECT_ROOT="$(pwd)"

IP="127.0.0.1"
PORT=8000

# 開発時に有用なコード達

function open-browser() {
    # Wsl2 only                           # ubuntu 22.04 LTS
    explorer.exe http://"$IP":"$PORT"/ # || xdg-open http://"$IP":"$PORT"/
}

function run() {
    open-browser
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function admin() {
    explorer.exe http://"$IP":"$PORT"/admin # || xdg-open http://"$IP":"$PORT"/
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function dj-test() {
    python3 "$PROJECT_ROOT"/manage.py test testapp
}

function migrate() {
    python3 "$PROJECT_ROOT"/manage.py makemigrations
    python3 "$PROJECT_ROOT"/manage.py migrate
}

function va() {
    # activate python venv
    if [ ! -f ./venv ]; then
        python3 -m venv venv
    fi
    source ./venv/bin/activate
}

function update-model-graph() {
    # deactivate python venv
    python3 manage.py graph_models -a -o "$PROJECT_ROOT"/docs/UML_Graphs/ErGraph_all.png
    python3 manage.py graph_models -o "$PROJECT_ROOT"/docs/UML_Graphs/ErGraph_dd_appOnly.png dd_app
}

alias mig="migrate"
