from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project, Review



@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects/'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):

    projects = Project.objects.all()
    projects = ProjectSerializer(projects, many=True)

    return Response(projects.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    project = ProjectSerializer(project, many=False)

    return Response(project.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    data = request.data
    vote = data['vote']
    body = data.get('body', '')

    review, created = Review.objects.get_or_create(
        owner=request.user.profile,
        project=project)

    review.value = vote
    review.body = body
    review.save()
    project.getVoteCount

    project = ProjectSerializer(project, many=False)

    return Response(project.data)