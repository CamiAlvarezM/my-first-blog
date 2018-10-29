from django.shortcuts import render, redirect, render_to_response

def post_list(request):
    return render(request, 'blog/post_list.html', {})