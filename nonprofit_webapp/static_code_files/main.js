$(document).ready(function(){
    $('#modal-btn-profile').click(function(){
        console.log('working for profile form')
        $('.ui.modal.myprofile-modal')
        .modal('show')
        ;
    })

    $('.ui.dropdown').dropdown()
})