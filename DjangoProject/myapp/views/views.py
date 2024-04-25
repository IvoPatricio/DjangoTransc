from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from myapp.models import Users
from myapp.models import Tournaments

def home(request):
	return render(request, "home.html")

#USER MANAGEMENT

def create_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('nickname')  # Assuming 'nickname' corresponds to 'username'
        avatar = request.FILES.get('avatar')

        user = Users.objects.create(email=email, password=password, username=username, avatar=avatar)

        return HttpResponse('User created successfully', status=201)
    else:
        return HttpResponse('Method not allowed', status=405)

def update_user(request, userid):
    user = get_object_or_404(Users, pk=userid)

    if request.method == 'PATCH':
        username = request.POST.get('nickname')
        avatar = request.FILES.get('avatar')

        user.username = username if username is not None else user.username
        user.avatar = avatar if avatar is not None else user.avatar
        user.save()

        return HttpResponse('User updated successfully', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)

def user_sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Logic
        return HttpResponse('Sign in successful', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)

def refresh_token(request):
    if request.method == 'POST':
        # Logic
        return HttpResponse('Token refreshed', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)

def get_users(request):
    if request.method == 'GET':
        users = Users.objects.all()
        user_data = [{'id': user.id, 'email': user.email, 'username': user.username, 'avatar': user.avatar} for user in users]
        return HttpResponse(user_data, content_type='application/json', status=200)
    else:
        return HttpResponse('Method not allowed', status=405)

def get_user_statistics(request, userid):
    if request.method == 'GET':
        user = get_object_or_404(Users, pk=userid)
        statistics = {
            'num_games_won': user.num_games_won,
            'num_tournaments': user.num_tournaments,
            'num_tournaments_won': user.num_tournaments_won
        }
        return JsonResponse(statistics, status=200)
    else:
        return HttpResponse('Method not allowed', status=405)

def get_all_users_statistics(request):
    if request.method == 'GET':
        users = Users.objects.all()
        statistics = [{'userid': user.id, 'num_games_won': user.num_games_won, 'num_tournaments': user.num_tournaments, 'num_tournaments_won': user.num_tournaments_won} for user in users]
        return JsonResponse(statistics, safe=False, status=200)
    else:
        return HttpResponse('Method not allowed', status=405)


#FRIENDS MANAGEMENT

#MATCHES MANAGEMENT

#TOURNAMENTS MANAGEMENT

def create_tournament(request):
    if request.method == 'POST':
        creator_id = request.POST.get('creator_id')

        tournament = Tournaments.objects.create(creator_id=creator_id)

        return JsonResponse({'message': 'Tournament created successfully', 'tournament_id': tournament.id}, status=201)
    else:
        return HttpResponse('Method not allowed', status=405)

def start_tournament(request, tournamentId):
    tournament = get_object_or_404(Tournaments, pk=tournamentId)

    if request.method == 'PATCH':
        tournament.has_started = True
        tournament.save()

        return HttpResponse('Tournament started successfully')
    else:
        return HttpResponse('Method not allowed', status=405)

def finish_tournament(request, tournamentId):
    tournament = get_object_or_404(Tournaments, pk=tournamentId)

    if request.method == 'PATCH':
        tournament.has_finished = True
        tournament.save()

        return HttpResponse('Tournament finished successfully')
    else:
        return HttpResponse('Method not allowed', status=405)

def get_tournament(request, tournamentId):
    tournament = get_object_or_404(Tournaments, pk=tournamentId)

    if request.method == 'GET':
        data = {
            'id': tournament.id,
            'creator_id': tournament.creator_id,
            'has_started': tournament.has_started,
            'has_finished': tournament.has_finished
        }
        return JsonResponse(data)
    else:
        return HttpResponse('Method not allowed', status=405)

def get_user_tournaments(request, userId):
    if request.method == 'GET':
        tournaments = Tournaments.objects.filter(creator_id=userId)
        tournament_data = [{'id': tournament.id, 'has_started': tournament.has_started, 'has_finished': tournament.has_finished} for tournament in tournaments]
        return JsonResponse({'tournaments': tournament_data}, safe=False)
    else:
        return HttpResponse('Method not allowed', status=405)

#CHAT MANAGEMENT