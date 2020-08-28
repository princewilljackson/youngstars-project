from django.shortcuts import render

# Create your views here.
def home(request):
    """Renders the index page."""
    return render(request, 'index.html')

def test(request):
    """Renders the test page."""
    return render(request, 'test_page.html')