function getModelos(marca)
{
    let $ = django.jQuery;
    $.ajax({
                type: "GET",
                url: '/auxiliares/modelos/'+marca+'/',
                dataType: "json",
                success: function(data)
                {
                    let lista = '<option value="" selected="">SELECCIONE</option>'

                    $.each(data, function(key, val)
                    {
                        lista += '<option value="'+ val.id +'">'+ val.descripcion +'</option>'
                    });
                    $('#modelo').html(lista);
                    $('#modelo').prop('disabled', false);                     
                }
            });
}