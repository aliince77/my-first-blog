from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post 

def post_list(request):
	posts = Post.objects.filter(yayinlanma_tarihi__lte=timezone.now()).order_by('-yayinlanma_tarihi')
	return render(request, 'blog/post_list.html',{'posts':posts})

def yazi_detay(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/yazi_detay.html', {'post':post})


	
