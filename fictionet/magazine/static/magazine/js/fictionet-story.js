$(function() {
    $("#favorites-icon").click(function(){
        let post_url = "";

        if($(this).data("clicked"))
        {
            $(this).addClass("fa-regular");
            $(this).removeClass("fa-solid");

            $(this).removeData("clicked");
            $(this).removeAttr("data-clicked");

            post_url = $(this).data('remove');
        }
        else
        {
            $(this).removeClass("fa-regular");
            $(this).addClass("fa-solid");

            $(this).data("clicked", "True");

            post_url = $(this).data('add');
        }

        $.ajax({
            url: post_url ,
            type: "POST",
            data:{
                csrfmiddlewaretoken: $(this).data("csrf")
            },
            success: function(data){
                $("#favorites-count").text(data.count)
            },
            error: function(error)
            {
                console.error(error)
            }
        });
    });

    $("#favorites-icon").hover(
            function()
            {
                if(!$(this).data("clicked"))
                {
                    $(this).removeClass("fa-regular");
                    $(this).addClass("fa-solid");
                }
            },
            function()
            {
                if(!$(this).data("clicked"))
                {
                    $(this).removeClass("fa-solid");
                    $(this).addClass("fa-regular");
                }
            }
    );
})