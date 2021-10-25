
$(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

            
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function(e){

        e.prevenDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este cliente?');

        if(result) {
            window.location.href = delLink;
        }
        
    });    

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });

});