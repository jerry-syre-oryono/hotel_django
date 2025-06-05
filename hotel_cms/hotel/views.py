from django.shortcuts import render, redirect
from .models import Room, Booking
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'hotel/book_room.html', {'form': form, 'room': room})
