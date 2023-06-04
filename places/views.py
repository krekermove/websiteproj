import datetime
import folium
from django.shortcuts import render, redirect
from .forms import PlacesForm
from .models import Places
from django.views.generic import DetailView
from folium.plugins import MousePosition

class PlacesDetailView(DetailView):
    model = Places
    template_name = 'places/place_detail.html'


def add(request):
    error = ''
    if request.method == 'POST':
        form = PlacesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.date.today()
            instance.save()
            return redirect('places')
        else:
            error = 'Форма заполнена неверно'
    m = folium.Map(location=[59.916357316816026,30.315987157004628],zoom_start=17)
    formatter = "function(num) {return L.Util.formatNum(num, 5);};"
    mouse_position = MousePosition(
        position='topright',
        separator=' | ',
        empty_string='NaN',
        lng_first=False,
        num_digits=20,
        prefix='Coordinates:',
        lat_formatter=formatter,
        lng_formatter=formatter,
    )
    m.add_child(mouse_position)
    m.add_child(folium.ClickForMarker(popup=m.add_child(folium.LatLngPopup())))
    #m.add_child(folium.ClickForMarker(popup=m.add_child(mouse_position)))

    m = m._repr_html_()
    form = PlacesForm()

    data = {
        'm': m,
        'form': form,
        'error': error
    }

    return render(request, 'places/addplace.html', context=data)