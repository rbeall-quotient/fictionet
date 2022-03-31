$(function() {
    $("#profile_pic").change(function()
    {
        const file = this.files[0];
        console.log(file);
        if (file)
        {
            let reader = new FileReader();
            reader.onload = function(event)
            {
                $('#image-preview').attr('src', event.target.result);
            }

            reader.readAsDataURL(file);
        }
    });
});