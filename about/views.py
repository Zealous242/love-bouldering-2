from django.contrib import messages
from django.shortcuts import render

from .forms import CollaborateForm
from .models import About


def about_me(request):
    """Render the About page and process collaboration requests."""
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request received! I endeavour to respond "
                "within 2 working days.",
            )

    about = About.objects.order_by("-updated_on").first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
