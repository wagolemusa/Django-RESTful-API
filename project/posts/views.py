# from urllib import quote_plus
from urllib.parse import quote_plus  
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.contrib.auth import authenticate
from django.utils import timezone
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import Comment 
# Create your views here.
from .models import Post
from .forms import PostForms
# from .utils import get_red_time



def post_create(request):
	"""
	Methods creates the Posts
	"""
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
		
	form = PostForms(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_obsolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	# if instance.publish > timezone.now().date() or instance.draft:
		# if not request.user.is_staff or not request.user.is_superuser:
			# raise Http404
	share_string = quote_plus(instance.content)

	# counting words 
	# print(get_red_time(instance.get_markdown()))

	comments = instance.comments
	initial_data = {
			"content_type": instance.get_content_type,
			"object_id": instance.id
	}

	form  = CommentForm(request.POST or None, initial = initial_data)
	if form.is_valid() and request.user.is_authenticated():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model=c_type)
		obj_id = form.cleaned_data.get('object_id')
		content_data  = form.cleaned_data.get("content")
		parent_obj = None
		try:
			parent_id = int(request.POST.get("parent_id"))# added on reply
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id=parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()
	 
		new_comment, created = Comment.objects.get_or_create(
						user = request.user,
						content_type = content_type,
						object_id = obj_id,
						content = content_data,
						parent  = parent_obj,
					)
		return HttpResponseRedirect(new_comment.content_object.get_obsolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
		"comments": comments,
		"comment_form": form,
	}
	return render(request, "post_detail.html", context)


def post_list(request):
	""" list items """
	today = timezone.now().date()
	querySet_list = Post.objects.all()

	if request.user.is_staff or request.user.is_superuser:
		querySet_list = Post.objects.all()

	# Search posts
	query = request.GET.get("q")
	if query:
		querySet_list = querySet_list.filter(
							Q(title__icontains=query)|
							Q(content__icontains=query)|
							Q(user__username__icontains=query)
							).distinct()

	paginator = Paginator(querySet_list, 3)
	page = request.GET.get('page')
	querySet = paginator.get_page(page)

	context = {
		"query_list": querySet,
		"title":"list",
		"today": today
	}
	return render(request, "post_list.html", context)
	

def post_update(request, slug=None):
	"""
	It updates posts
	"""
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForms(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "Successfuly updated")
		return HttpResponseRedirect(instance.get_obsolute_url())
	else:
		messages.error(request, "Not update")
	context = {
	"title": instance.title,
	"instance": instance,
	"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request, slug=None):
	"""
	 delete Details 
	"""
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfuly Deleted")
	return redirect("posts:list")

