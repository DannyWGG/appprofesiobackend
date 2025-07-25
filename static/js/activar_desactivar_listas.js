function activateMotivoFueraServicio(valor)
{
    let $ = django.jQuery;
    if (valor == 'True')
    {
        $("#motivo_no_operatividad").prop("disabled", true);
        $("#motivo_no_operatividad").val('');
        $("#motivo_no_operatividad").clear();
    }

    else
    {
        $("#motivo_no_operatividad").prop("disabled", false);
    }
}