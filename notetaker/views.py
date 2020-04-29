from django.shortcuts import render
from .models import Todo, Note
from django.views import generic
from django.http import HttpResponseRedirect
from django.utils import timezone

def index(request):
    note_list = Note.objects.order_by('-pub_date')
    todo_list = Todo.objects.order_by('-pub_date')
    context = {
        'note_list':note_list,
        'todo_list':todo_list
    }
    return render(request, 'notetaker/index.html', context)



class NoteView(generic.DetailView):
    model = Note
    template_name = 'notetaker/note_detail.html'
   
class TodoView(generic.DetailView):
    model = Todo
    template_name = 'notetaker/todo_detail.html'


def doneTodo(request, todo_id):
        item_done = Todo.objects.get(id=todo_id)
        item_done['done'] = not item_done['done']
        return HttpResponseRedirect('/')

def addNote(request):
    title = request.POST['title']
    body = request.POST['body']

    new_note = Note(title=title, body=body, pub_date=timezone.now())

    new_note.save()
    return HttpResponseRedirect('/')

def deleteNote(request, note_id):
    note_to_delete = Note.objects.get(id=note_id)
    note_to_delete.delete()
    return HttpResponseRedirect('/')