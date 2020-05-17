import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from teaapp.models import Tea, TeaPackaging, Packaging
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
            p.name packaging_method,
            p.handmade,
            p.production_location
        FROM teaapp_tea t
        LEFT JOIN teaapp_teapackaging tp ON tea_id = t.id
        LEFT JOIN teaapp_packaging p ON pack_id = tp.packaging_id
        WHERE t.id = ?;
        """, (tea_id,))

        all_teas = db_cursor.fetchall()
        tea_groups = {}
        tea_groups_values = tea_groups.values()

        for (tea, packaging) in all_teas:
            if tea.id not in tea_groups:
                tea_groups[tea.id] = tea
                tea_groups[tea.id].packaging_methods.append(packaging)
            else:
                tea_groups[tea.id].packaging_methods.append(packaging)

        return tea_groups_values

def create_tea(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tea = Tea()
    tea.id = _row['id']
    tea.name = _row['name']
    tea.flavor = _row['flavor']

    tea.packaging_methods = []

    packaging = Packaging()
    packaging.id = _row['packaging_id']
    packaging.name = _row['packaging_method']
    packaging.longevity = _row['longevity_in_months']

    return (tea, packaging)

def tea_details(request, tea_id):
    if request.method == 'GET':
        tea_values = get_tea(tea_id)

        template = 'teas/details.html'
        context = {
            'tea_values': tea_values
        }

        return render(request, template, context)
    
    elif request.method == "POST":
        form_data = request.POST

        if("actual_method" in form_data and form_data["actual_method"] == "DELETE"):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM teaapp_teapackaging
                    WHERE tp.id = ?
                """, (tea_id,))

            return redirect(reverse('teaapp:tea_list'))