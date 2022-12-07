from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    """The Home page for learning log"""
    return render(request, 'Main_app/index.html')


def topics(request):
    topics = Topic.objects.order_by('-data_added')

    context = {'t':topics}

    return render(request, 'Main_app/topics.html',context)
    '''the key t is the variable you will use on the html page '''
    ''' the value is the variable you are using in the view'''

def topic(request,topic_id):
    t = Topic.objects.get(id=topic_id)
    entries = Entry.objects.filter(topic=t)

    context = {'topic':t, 'entries':entries}

    return render(request, 'Main_app/topic.html',context)

''' A get request is getting data from the database'''
''' A post request is asking to write something to the database'''

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        print(request.POST)
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main_app:topics')

    context = {'form':form}
    return render(request, 'Main_app/new_topic.html',context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        print(request.POST)
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Main_app:topic', topic_id=topic_id)

    context = {'form':form,'topic':topic}
    return render(request, 'Main_app/new_entry.html',context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id) # use this variable to reference the model
    topic = entry.topic #same variable

    if request.method != 'POST':
        form = EntryForm(instance=entry) 
    else:
        form = EntryForm(instance=entry,data=request.POST) 
        if form.is_valid():
            form.save()
            return redirect('Main_app:topic', topic_id=topic.id) 
            # topic_id is a variable name / topic.idd is an attribute

    context = {'form':form,'topic':topic, 'entry':entry}
    return render(request, 'Main_app/edit_entry.html',context)

    



            

