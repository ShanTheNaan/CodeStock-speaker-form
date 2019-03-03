function formSubmit()
{
    var completed = true;
    if(!anyRadioBtnSelected('user-ratings'))
    {
        completed = false;
    }
    else if(document.getElementById('right-stuff').value == "")
    {
        completed = false;
    }
    else if(document.getElementById('improvement').value == "")
    {
        completed = false;
    }

    if(!completed)
    {
        window.alert('Please provide the required fields.');
    }

    return completed;
}

function anyRadioBtnSelected(radioBtnName)
{
    var btns = document.getElementsByName(radioBtnName);
    for(var i = 0; i < btns.length; i++)
    {
        if(btns[i].type == 'radio' && btns[i].checked)
        {
            return true;
        }
    }

    return false;
}