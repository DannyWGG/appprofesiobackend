function getMunicipio(estado)
{
    let $ = django.jQuery;
    $.ajax({
                type: "GET",
                url: '/geo/municipios/'+estado+'/',
                dataType: "json",
                success: function(data)
                {
                    let lista = '<option value="" selected="">SELECCIONE</option>'

                    $.each(data, function(key, val)
                    {
                        lista += '<option value="'+ val.id +'">'+ val.nombre +'</option>'
                    });
                    $('#municipio').html(lista);
                    $('#municipio').prop('disabled', false);                     
                }
            });
}

function getParroquia(municipio)
{
    console.log(municipio);
    let $ = django.jQuery;
    $.ajax({
            type: "GET",
            url: '/geo/parroquias/'+municipio+'/',
            dataType: "json",
            success: function(data)
            {
                let lista = '<option value="" selected="">SELECCIONE</option>'

                $.each(data, function(key, val)
                {
                    lista += '<option value="'+ val.id +'">'+ val.nombre +'</option>'
                });
                $('#parroquia').html(lista);
                $('#parroquia').prop('disabled', false); 
            }
        });
}

function getComunidad(parroquia)
{
    let $ = django.jQuery;
    $.get('/geo/comunidad/filtro/'+parroquia+'/', function (resp)
    {
        let lista = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item)
        {
           lista += '<option value="'+ item.id +'">'+ item.descripcion +'</option>'
        });
        $('#comunidad').html(lista);
    });
}
