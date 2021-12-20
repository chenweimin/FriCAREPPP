$('.upload-file').change(function () {
    var file = new FormData()
    file.append('file', $('.upload-file')[0].files[0])
    console.log(file)
    $.ajax({
        url: "/upload/",
        type: "POST",
        data: file,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart/form-data',
        success: function () {
        }
    })
})