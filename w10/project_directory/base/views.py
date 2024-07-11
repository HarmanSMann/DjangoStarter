from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def base(request):
    return (render(request, "base.html"))

# View function for render contact us template 
# Add this here*****
def contact(request):
    return (render(request, "contact.html"))

# Create courses
courses_array = [
    {"id": 1, "name": "Python"},
    {"id": 2, "name": "JavaScript"},
    {"id": 3, "name": "C"},
]

def courses(request):
    print(courses_array)
    return (render(
        request, "courses.html",
        {"courses": courses_array}))

# View function for render generate image template
def generate_image(request):
    # Check form method is POST
    if request.method == "POST":
        print(request.POST)
        # Get data from form and set defaults if not sent
        width = request.POST.get("width")
        height = request.POST.get("height")
        # Set to 0 if none
        blur = request.POST.get("blur") or 0
        grayscale = request.POST.get("grayscale")

        # String to pass blur and greyscale as get params
        param_string = ""

        # Ternary operator to set blur between 1-10
        blur = blur if int(blur) >=1 and int(blur) <=10 else None

        # If both blur and grayscale, send both as params
        if blur and grayscale:
            param_string += f"?blur={blur}&grayscale"
        # If only blur, pass blur as param
        elif blur:
            param_string += f"?blur={blur}"
        # If no blur but grayscale, set grayscale as param
        elif grayscale:
            param_string += "?grayscale"

        # Generate image url using params in form 
        picsum_url = f"https://picsum.photos/{width}/{height}{param_string}"

        # Print generated url
        print(picsum_url)

        # Render page and pass url for image
        return (render(request, "generate_image.html",
            {"picsum_url": picsum_url}))

    return (render(request, "generate_image.html"))
