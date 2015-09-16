from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Comment
from .forms import CommentForm
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def post(self,request):
    	request.session['nombre']= request.POST['nombre']
    	return redirect ('/home/')


class HomeView(TemplateView):
    
    def get(self,request):
    	if request.session.get('nombre'):
    		comments = Comment.objects.all()
    		diccionario={
    			'user':request.session['nombre'],
    			'comments':comments,
    			'commentForm':CommentForm(),
    		}
    		return render(request,'home.html',diccionario)
    	else:
    		return redirect('/')

    def post(self,request):
    	Comment.objects.create(
    		comment=request.POST['comment'],
    		user=request.session['nombre'])
    	return redirect('/home/')


@csrf_exempt
def create_comment(request):
    Comment.objects.create(
            user= request.POST['user'],
            comment= request.POST['comment'])
    response= JsonResponse({'user': request.POST['user'], 
        'comment':request.POST['comment'] })
    print response
    return HttpResponse(response)
