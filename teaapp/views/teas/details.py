import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from teaapp.models import Tea
from ..connection import Connection

def get_tea(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_tea
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            t.id, 
            t.name, 
            t.flavor, 
            tp.id teapackjt_id,
            tp.longevity_in_months,
            tp.packaging_id,
            tp.tea_id,
            p.id pack_id,
            p.name,
            p.handmade,
            p.production_location
        FROM teaapp_tea t
        LEFT JOIN teaapp_teapackaging tp ON tea_id = t.id
        LEFT JOIN teaapp_packaging p ON pack_id = tp.packaging_id
        WHERE t.id = ?;
        """, (tea_id,))

        return db_cursor.fetchone()

def create_tea(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tea = Tea()
    tea.id = _row['id']
    tea.name = _row['name']
    tea.flavor = _row['flavor']

    return tea

def tea_details(request, tea_id):
    if request.method == 'GET':
        tea = get_tea(tea_id)

        template = 'teas/details.html'
        context = {
            'tea': tea
        }

        return render(request, template, context)