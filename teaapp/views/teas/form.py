import sqlite3
from django.shortcuts import render
from ..connection import Connection
from teaapp.models import Tea

def get_teas():
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            id, 
            name, 
            flavor   
        FROM teaapp_tea
        """)
        
        tea = db_cursor.fetchone()
        return tea

def tea_form(request):
    if request.method == 'GET':
        tea = get_teas()

        template = 'teas/form.html'
        context = {
            'tea': tea
        }
        
        return render(request, template, context)