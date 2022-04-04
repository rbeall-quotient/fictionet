$(function() {
    $("#profile_pic").change(function()
    {
        const file = this.files[0];
        if (file)
        {
            let reader = new FileReader();
            reader.onload = function(event)
            {
                $('#image-preview').attr('src', event.target.result);
                $('#image-preview').parent().removeClass("d-none");
            }

            reader.readAsDataURL(file);
        }
    });
});