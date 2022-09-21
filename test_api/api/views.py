from unicodedata import name
from rest_framework.views import APIView
from django.http import Http404
from api.models import Student
from .seriliazers import StudentSerializers
from rest_framework.response import Response

# Create your views here.
class student_details(APIView):

    def get(self,request):
        try:
            id = request.query_params['id']
            if id != None:
                queryset= Student.objects.get(id=id)
                seriliazer_class = StudentSerializers(queryset)
        except:
            queryset = Student.objects.all()
            seriliazer_class = StudentSerializers(queryset,many=True)
        return Response(seriliazer_class.data)
    
    def post(self,request, *args,**kwargs):
        stu_data = request.data
        new_student = Student.objects.create(name=stu_data["name"],roll=stu_data["roll"],city=stu_data["city"])
        new_student.save()
        seriliazer=StudentSerializers(new_student)
        return Response(seriliazer.data)

    def put(self,request, *args,**kwargs):
        data = request.data
        stu_object = Student.objects.all()
        stu_object.name = data["name"]
        stu_object.roll = data["roll"]
        stu_object.city = data["city"]

        stu_object.save()
        serilaizer = StudentSerializers(stu_object)
        return Response(serilaizer.data)
    
    def destory(self,request):
        student = self.get_object()
        student.delete()

        return Response({"message":"Sucessfully delete"})



