from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from upload.sharepoint import SharePoint

# Create your views here.
def upload(request):
    if request.method == 'GET':
        return render(request, 'upload.html')

    if request.method == 'POST':
        file = request.FILES.get('file')
        fs = FileSystemStorage()
        fs.save('upload/files/' + file.name, file)

        #i.e - file_dir_path = r'C:\project\report.pdf'
        file_dir_path = r'D:\readdocx\upload\files\%s' %file.name
        # this will be the file name that it will be saved in SharePoint as 
        file_name = file.name
        # The folder in SharePoint that it will be saved under
        folder_name = '2020'
        # upload file
        SharePoint().upload_file(file_dir_path, file_name, folder_name)

        return HttpResponse('ok')