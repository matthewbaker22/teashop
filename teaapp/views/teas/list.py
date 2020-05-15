import sqlite3
from django.shortcuts import render, redirect, reverse
from teaapp.models import Tea
from ..connection import Connection

def tea_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                id, 
                name, 
                flavor   
            FROM teaapp_tea;
            """)

            all_teas = db_cursor.fetchall()
            all_teas = Tea.objects.all().order_by('name')

        template = 'teas/list.html'
        context = {
            'all_teas': all_teas
        }

        return render(request, template, context)