function getPlantel(codigo_plantel)
{
    let $ = django.jQuery;
    $.ajax({
                type: "GET",
                url: '/planteles/ver/'+codigo_plantel+'/',
                dataType: "json",
                success: function(data)
                {
                    $("#eponimo_plantel").val(data[0].nombre_plantel);
                    $("#dependencia_plantel").val(data[0].tipo_dependencia);
                    $("#direccion_plantel").val(data[0].direccion);
                    $("#origen_director_plantel").val(data[0].tipo_documento);
                    $("#cedula_director_plantel").val(data[0].documento_identidad);
                    $("#id_telefono_director_plantel").val(data[0].telefono_movil_director);
                    $("#estado").val(data[0].estado);
                    $("#municipio").val(data[0].municipio);
                    $("#parroquia").val(data[0].parroquia);
                }
            });
}