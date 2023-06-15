import datetime
import folium
from django.shortcuts import render, redirect
from .forms import PlacesForm
from .models import Places
from django.views.generic import DetailView, DeleteView
from folium.plugins import MousePosition
import jinja2
from jinja2 import Template
from folium.map import Marker
import sys,threading

class PlacesDetailView(DetailView):
    model = Places
    template_name = 'places/place_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        lat = self.object.lattitude
        long = self.object.longtitude
        f = folium.Figure(width=680,height=300)
        m = folium.Map(location=[59.916357316816026, 30.315987157004628], zoom_start=16).add_to(f)
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

        folium.Marker((lat, long)).add_to(m)

        m = m._repr_html_()

        data = {
            'm': m,
            'object': self.object
        }
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(data)

class DeleteView(DeleteView):
    model = Places
    success_url = '/places'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        return super(DeleteView, self).delete(request, *args, **kwargs)

def edit(request, pk):
    if request.method == 'POST':
        form = PlacesForm(request.POST)
        error = ''
        if form.is_valid():
            instance = form.save(commit=False)
            Places.objects.filter(id=pk).update(
                title=instance.title,
                text=instance.text,
                lattitude=instance.lattitude,
                longtitude=instance.longtitude,
                date=datetime.date.today(),
                deadline=instance.deadline,
            )
            return redirect('places')
        else:
            error = 'Ошибка заполнения'

    obj = Places.objects.get(id=pk)
    form = PlacesForm(instance=obj)
    tmpldata = """<!-- monkey patched Marker template -->
           {% macro script(this, kwargs) %}
               var {{ this.get_name() }} = L.marker(
                   {{ this.location|tojson }},
                   {{ this.options|tojson }}
               ).addTo({{ this._parent.get_name() }}).on('click', onClick);
           {% endmacro %}
           """

    Marker._template = Template(tmpldata)

    def myMarkerInit(*args, **kwargs):
        Marker.__init_orig__(*args, **kwargs)
        # self._template = self._mytemplate

    Marker.__init_orig__ = myMarkerInit
    # Marker.__init__ = myMarkerInit

    f = folium.Figure(width=900, height=600)
    m = folium.Map(location=[59.91635, 30.31598], zoom_start=16).add_to(f)
    locations = [[59.91635, 30.31598]]
    for location in locations:  # range(locations.shape[0]):
        folium.Marker(
            location=location,
            popup=f'<p id="latlon">{location[0]}, {location[1]}</p>',
            draggable=True
        ).add_to(m)

    el = folium.MacroElement().add_to(m)
    el._template = jinja2.Template("""
               {% macro script(this, kwargs) %}
               function copy(text) {
                   var input = document.createElement('textarea');
                   input.innerHTML = text;
                   document.body.appendChild(input);
                   input.select();
                   var result = document.execCommand('copy');
                   document.body.removeChild(input);
                   return result;
               };

               function onClick(e) {
                  var lat = e.latlng.lat; 
                  var lng = e.latlng.lng;
                  var newContent = '<p id="latlon">' + lat + ', ' + lng + '</p>';
                  e.target.setPopupContent(newContent);
                  copy(lat + ' ' + lng);
               };
               {% endmacro %}
           """)
    m = m._repr_html_()
    context = {
        'form': form,
        'm':m
    }
    return render(request, 'places/editplaces.html', context)


def add(request):
    error = ''

    form = PlacesForm()
    tmpldata = """<!-- monkey patched Marker template -->
       {% macro script(this, kwargs) %}
           var {{ this.get_name() }} = L.marker(
               {{ this.location|tojson }},
               {{ this.options|tojson }}
           ).addTo({{ this._parent.get_name() }}).on('click', onClick);
       {% endmacro %}
       """

    Marker._template = Template(tmpldata)

    def myMarkerInit(*args, **kwargs):
        Marker.__init_orig__(*args, **kwargs)
        # self._template = self._mytemplate

    Marker.__init_orig__ = myMarkerInit
    # Marker.__init__ = myMarkerInit

    f = folium.Figure(width=900, height=600)
    m = folium.Map(location=[59.91635, 30.31598], zoom_start=16).add_to(f)
    locations = [[59.91635, 30.31598]]
    for location in locations:  # range(locations.shape[0]):
        folium.Marker(
            location=location,
            popup=f'<p id="latlon">{location[0]}, {location[1]}</p>',
            draggable=True
        ).add_to(m)

    el = folium.MacroElement().add_to(m)
    el._template = jinja2.Template("""
           {% macro script(this, kwargs) %}
           function copy(text) {
               var input = document.createElement('textarea');
               input.innerHTML = text;
               document.body.appendChild(input);
               input.select();
               var result = document.execCommand('copy');
               document.body.removeChild(input);
               return result;
           };

           function onClick(e) {
              var lat = e.latlng.lat; 
              var lng = e.latlng.lng;
              var newContent = '<p id="latlon">' + lat + ', ' + lng + '</p>';
              e.target.setPopupContent(newContent);
              copy(lat + ' ' + lng);
           };
           {% endmacro %}
       """)
    if request.method == 'POST':
        form = PlacesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.date.today()
            #instance.lattitude = float(point[0])
            #instance.longtitude = float(point[1])
            instance.save()
            return redirect('places')
        else:
            error = 'Форма заполнена неверно'
    m = m._repr_html_()
    data = {
        'form': form,
        'error': error,
        'm':m
    }


    return render(request, 'places/addplace.html', context=data)
