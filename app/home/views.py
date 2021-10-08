# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Renderiza o template da página inicial na rota /
    """
    return render_template('home/index.html', title="Bem-vindo")

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Renderiza o template do painel de controle na rota /dashboard
    """
    return render_template('home/painel.html', title="Painel de controle")
