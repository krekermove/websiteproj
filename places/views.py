import datetime
import folium
from django.shortcuts import render, redirect
from .forms import PlacesForm
from .models import Places
from django.views.generic import DetailView, DeleteView
from folium.plugins import MousePosition

class PlacesDetailView(DetailView):
    model = Places
    template_name = 'places/place_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        lat = self.object.lattitude
        long = self.object.longtitude
        f = folium.Figure(width=680,height=300)
        m = folium.Map(location=[59.916357316816026, 30.315987157004628], zoom_start=17).add_to(f)
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

<<<<<<< HEAD
class DeleteView(DeleteView):
    model = Places
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = self.object.name
        return super(DeleteView, self).delete(request, *args, **kwargs)

def edit(request,object_id):
    context={}

    obj=Places.objects.get(id=object_id)
    form=PlacesForm(instance=obj)

    context={'form':form}
    return render(request,'editpage.html',context)

def add(request):
    error = ''

    form = PlacesForm()

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
=======

def add(request):
    error = ''
    m = folium.Map(location=[59.916357316816026, 30.315987157004628], zoom_start=17)
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

    point = m.location

    m = m._repr_html_()
    form = PlacesForm()
>>>>>>> 4feb583db01deab0642a2f3b123cba07eabc9d72

    if request.method == 'POST':
        form = PlacesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.date = datetime.date.today()
            instance.lattitude = float(point[0])
            instance.longtitude = float(point[1])
            instance.save()
            return redirect('places')
        else:
            error = 'Форма заполнена неверно'

    data = {
        'form': form,
        'error': error
    }


    return render(request, 'places/addplace.html', context=data)