from django.shortcuts import render

from .models import Board, List

kanban = Board(name="Kanban Board")

backlog = List(name="Backlog", board=kanban, position=0, color="red")
doing = List(name="Doing", board=kanban, position=1, color="yellow")
review = List(name="Review", board=kanban, position=2, color="violet")
done = List(name="Done", board=kanban, position=3, color="green")
lists = [backlog, doing, review, done]


# Create your views here.
def index(request):
    context = {
        "board": kanban,
        "lists": sorted(lists, key=lambda x: x.position),
    }
    return render(
        request=request, template_name="kanban/index.html", context=context
    )


def base(request):
    return render(request=request, template_name="kanban/materials.html")
