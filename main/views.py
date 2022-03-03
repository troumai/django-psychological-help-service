from django.shortcuts import render
from django.http import HttpResponse
from therapists_list import views
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contacts(request):
    contact1 = {'title': 'General questions and chat',
                'email': 'help@ok.com'}
    contact2 = {'title': 'Cooperation',
                    'phone': '87770008800',
                    'email': 'cooperation@ok.com'}
    contact3 = {'title': 'Career',
                'phone': '87770007700',
                'email': 'career@ok.com'}
    data = {'chat': contact1, 'cooperation': contact2, 'career': contact3}
    return render(request, 'main/contacts.html', context=data)

def certificates(request):
    tariff1 = {
        'sessions_number': 1,
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras venenatis',
        'cost': 11000
    }
    tariff2 = {
        'sessions_number': 3,
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras venenatis',
        'cost': 30000
    }
    tariff3 = {
        'sessions_number': 5,
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras venenatis',
        'cost': 55000
    }
    tariff4 = {
        'sessions_number': 10,
        'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras venenatis',
        'cost': 90000
    }
    data = {'tariffs': (tariff1, tariff2, tariff3, tariff4)}
    return render(request, 'main/certificates.html', context=data)

# def therapists(request):
#     therapist1= {
#         'firstname': 'Tomiris',
#         'surname': 'Abimoldayeva',
#         'age': 19,
#         'email': 'abimoldayevat@ok.com'
#     }
#     therapist2= {
#         'firstname': 'John',
#         'surname': 'Doe',
#         'age': 65,
#         'email': 'john@ok.com'
#     }
#     therapist3= {
#         'firstname': 'Jane',
#         'surname': 'Doe',
#         'age': 36,
#         'email': 'jane@ok.com'
#     }
#     therapist4 = {
#         'firstname': 'Ivan',
#         'surname': 'Ivanov',
#         'age': 23,
#         'email': 'ivanushkadurak@ok.com'
#     }
#     therapist5= {
#         'firstname': 'Lana',
#         'surname': 'Del Rey',
#         'age': 33,
#         'email': 'lana@ok.com'
#     }
#     therapistlist = (therapist1, therapist2, therapist3, therapist4, therapist5)
#     data = {'therapists1': therapistlist}
#     return render(request, 'main/therapists.html', context=data)
